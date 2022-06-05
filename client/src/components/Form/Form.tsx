import React from 'react';
import axios from 'axios';
import { Button, Link } from '@mui/material';
import styles from './_form.module.scss';
import { FormContext, actions } from '../../contexts/form.context';
import { FileInput } from './FileInput';
import { Vulnerabilities } from './Vulnerabilities';

const SUPPORTED_FORMATS = ['text/html'];
const REGEXP = /(?<=критический|средний|высокий|низкий).+\n.+(?=<td>(\d+)<\/td>)/gi;

export const Form = () => {
  const [state, dispatch] = React.useContext(FormContext);
  const { file, vulnerabilities } = state;
  const isFileValid = !!state.file.value && !state.file.error;
  const isVulnerabilitiesValid = Object.values(vulnerabilities).some((el) => el);
  const isReady = isFileValid && isVulnerabilitiesValid;

  const [receivedFile, setReceivedFile] = React.useState<{ name: string; url: string } | null>(
    null,
  );
  const downloadFile = () => {
    axios
      .get(`/delete/${receivedFile?.name as string}`)
      // eslint-disable-next-line
      .catch((e) => console.log(e.toJSON()));
    // ! Clear()
    setReceivedFile(null);
  };
  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('files', state.file.value as File);
    formData.append('vulnerability', JSON.stringify(state.vulnerabilities));

    const res = await axios.post('/parse', formData, {
      responseType: 'blob',
    });
    const fileName = res.headers['x-file-name'];
    const fileURL = URL.createObjectURL(res.data as Blob);
    setReceivedFile({ name: fileName, url: fileURL });
  };

  const [array, setArray] = React.useState<number[]>([]);
  const validate = React.useCallback(async (): Promise<void> => {
    if (!file.value) return;
    if (!SUPPORTED_FORMATS.includes(file.value.type)) {
      dispatch(actions.setFileErrorAction('Поддерживается только .html формат'));
      return;
    }
    const res = await file.value.text();
    const arr = Array.from(res.matchAll(REGEXP)).map((el) => parseInt(el[1], 10));
    setArray(arr);
    if (!arr.length) {
      dispatch(actions.setFileErrorAction('Загрузите отчет ScanOval'));
      return;
    }
    dispatch(actions.setFileErrorAction(''));
    // eslint-disable-next-line
  }, [file.value]);
  React.useEffect(() => {
    // eslint-disable-next-line
    validate().catch(console.error);
    // eslint-disable-next-line
  }, [file.value]);

  return (
    <form className={styles.form} onSubmit={onSubmit} noValidate>
      <FileInput />
      {!!array.length && <Vulnerabilities values={array} />}
      <Button type="submit" variant="contained" sx={{ marginTop: 1 }} disabled={!isReady}>
        Сгенерировать таблицу
      </Button>
      {receivedFile && (
        <Link
          sx={{ marginTop: 1 }}
          href={receivedFile.url}
          download={receivedFile.name}
          onClick={downloadFile}
        >
          <Button type="button" variant="contained" fullWidth>
            Загрузить файл
          </Button>
        </Link>
      )}
    </form>
  );
};
