import json
from pathlib import Path
import openpyxl
import mimetypes

class _FileService:

  def __init__(self):
    self.__DIR = Path('.')
    self.__STATIC_RESULT = Path(self.__DIR, 'result')

  @property
  def dir(self):
    return self.__DIR

  @property
  def static_result(self):
    return self.__STATIC_RESULT

  def generate_xlsx(self, path, data):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.create_sheet()
    excel_sheet.append((
      '№',
      'Name',
      'CVE',
      'CWE',
      'Capec High',
      'Capec Medium',
      'Capec Low',
      'No Chance'
    ))

    for i, row in enumerate(data, 1):
      values = list(row.values())
      values.insert(0, i)
      excel_sheet.append(values)

    excel_file.save(path)

  def get_json(self, path):
    with open(path, encoding='utf-8') as file:
      content = json.load(file)
      file.close()
    return content

  def remove_file(self, path) -> bool:
    try:
      Path(self.__STATIC_RESULT, path).unlink()
      return True
    except:
      return False

  def define_mime_type(self, path):
    return mimetypes.guess_type(path)[0]

file_service = _FileService()
