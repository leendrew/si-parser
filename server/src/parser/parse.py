from bs4 import BeautifulSoup
import re
from src.helpers.request import get_page

BDU_URL = 'https://bdu.fstec.ru/vul/'
CWE_URL = 'https://cwe.mitre.org/data/definitions/'
CAPEC_URL = 'http://capec.mitre.org/data/definitions/'
BDU_TYPE_DICT = {
  "критический": "critical",
  "высокий": "high",
  "средний": "medium",
  "низкий": "low",
}

# accept array values ex: ['critical', 'high']
def get_bdu_list(file_content, accepted_bdu_types):
  soup = BeautifulSoup(file_content, 'lxml')
  rows =  soup.find('table', 'vulnerabilitiesTbl').find_all(lambda tag: tag.find('td', 'bdu'))

  bdu_list = []

  for row in rows:
    type = row.find('td', 'risk').text.strip().lower()
    bdu_type = BDU_TYPE_DICT[type]

    if not (bdu_type in accepted_bdu_types):
      continue

    bdu_text = row.find('td', 'bdu').text
    bdu_num = re.findall(r'[0-9]+-[0-9]+', bdu_text)[0]
    bdu_list.append(bdu_num)

  return bdu_list

def get_cwe_cve_for_bdu(bdu_num):
  page_content = get_page(BDU_URL + bdu_num)
  soup = BeautifulSoup(page_content, 'lxml')
  table = soup.find('table', class_='table')

  if not table:
    return None

  cwe_list = []
  cve_list = []

  for tr in table.find_all('tr'):
    for link in tr.find_all('a'):
      link_text = link.text.lower()
      cwe_num = re.findall(r'[0-9]+', link_text)
      cve_num = re.findall(r'[0-9]+-[0-9]+', link_text)

      if link_text.startswith('cwe') and cwe_num:
        cwe_list = [*cwe_list, *cwe_num]

      if link_text.startswith('cve') and cve_num:
        cve_list = [*cve_list, *cve_num]

  return cwe_list, cve_list

def get_capec_for_cwe(cwe_num):
  page_content = get_page(CWE_URL + cwe_num)
  soup = BeautifulSoup(page_content, 'lxml')
  searched_div = soup.find('div', id='Related_Attack_Patterns')

  if not searched_div:
    return None

  capec_list = []

  for link in searched_div.find('table').find_all('a'):
    link_text = link.text.lower().strip()

    if link_text.startswith('capec'):
      capec_num = re.findall(r'[0-9]+', link_text)[0]
      capec_list.append(capec_num)

  return capec_list

def get_capec_type(capec_num):
  page_content = get_page(CAPEC_URL + capec_num)
  soup = BeautifulSoup(page_content, 'lxml')
  searched_div = soup.find('div', id='Likelihood_Of_Attack')

  if not searched_div:
    return 'no_chance'

  capec_type = searched_div.find('p').text.lower().strip()
  return capec_type

def parse_file(file_content, accepted_bdu_types):
    bdu_list = get_bdu_list(file_content, accepted_bdu_types)

    final_list = []

    # TODO: Rename to *_diff and do not take from .json
    # set1.difference(set2) || set1 - set2 -> set3 where set3.el already IN set1 and NOT IN set2
    # EX: cwe_set_diff = cwe_set - cwe_set_db
    # cwe_w_capec_dict = get_json('cwe_w_capec_dict.json')
    # capec_w_type_dict = get_json('capec_w_type_dict.json')
    cwe_w_capec_dict = {}
    capec_w_type_dict = {}

    # cwe_w_capec_dict_diff = {}
    # capec_w_type_dict_diff = {}

    # TODO: delete i, enumerate before release
    for i, bdu_num in enumerate(bdu_list, 1):
      res = get_cwe_cve_for_bdu(bdu_num)

      if not res:
        print(f'STEP {i} BDU {bdu_num} IS MISSING')
        continue

      cwe_list, cve_list = res

      capec_high_list = []
      capec_medium_list = []
      capec_low_list = []
      capec_no_chance_list = []

      for cwe in cwe_list:
        # TODO: Check <capec_list> for <cwe> in DB
        # EX: cwe_check = db_request(cwe)
        # if not cwe_check:
        #   cwe_set_diff = {*cwe_set_diff, cwe}
        if cwe not in cwe_w_capec_dict:
          # TODO: Update cwe_set_diff

          capec_list = get_capec_for_cwe(cwe)

          if not capec_list:
            # TODO: Update cwe_w_capec_dict_diff
            cwe_w_capec_dict[cwe] = []
            continue

          # TODO: Update cwe_w_capec_dict_diff
          cwe_w_capec_dict[cwe] = capec_list

          for capec in capec_list:
            # TODO: Check <capec_type> for <capec> in DB
            # EX: capec_check = db_request(capec)
            # if not capec_check:
            #   capec_set_diff = {*capec_set_diff, capec}
            if capec not in capec_w_type_dict:
              capec_type = get_capec_type(capec)
              # TODO: Update capec_w_type_dict_diff
              capec_w_type_dict[capec] = capec_type

        for capec in cwe_w_capec_dict[cwe]:
          capec_type = capec_w_type_dict[capec]
          match capec_type:
            case 'high':
              capec_high_list.append(capec)
            case 'medium':
              capec_medium_list.append(capec)
            case 'low':
              capec_low_list.append(capec)
            case 'no_chance':
              capec_no_chance_list.append(capec)

      cve_str = ', '.join(cve_list)
      cwe_str = ', '.join(cwe_list)
      capec_high_str = ', '.join(capec_high_list or '-')
      capec_medium_str = ', '.join(capec_medium_list or '-')
      capec_low_str = ', '.join(capec_low_list or '-')
      capec_no_chance_str = ', '.join(capec_no_chance_list or '-')

      row = {
        'bdu': bdu_num,
        'cve': cve_str,
        'cwe': cwe_str,
        'capec_high': capec_high_str,
        'capec_medium': capec_medium_str,
        'capec_low': capec_low_str,
        'capec_no_chance': capec_no_chance_str,
      }

      final_list.append(row)
      print(f'FINAL_LIST step {i} of {len(bdu_list)}')

    # return final_list, cwe_w_capec_dict, capec_w_type_dict
    return final_list
