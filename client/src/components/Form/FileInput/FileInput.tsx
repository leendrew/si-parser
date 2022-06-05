/* eslint-disable jsx-a11y/label-has-associated-control */
import React from 'react';
import {
  Typography,
  Input,
  FormHelperText,
  FormControl,
  List,
  ListItem,
  ListItemText,
  ListItemAvatar,
  Avatar,
} from '@mui/material';
import { InsertDriveFile } from '@mui/icons-material';
import styles from './_fileInput.module.scss';
import { FakeInput } from './FakeInput';
import { FormContext, actions } from '../../../contexts/form.context';

export const FileInput: React.FC = () => {
  const [state, dispatch] = React.useContext(FormContext);
  const { file } = state;

  const onInputFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    if (e.target.files && e.target.files.length) {
      dispatch(actions.setFileAction(e.target.files[0]));
    }
  };

  // eslint-disable-next-line react-hooks/exhaustive-deps
  const onFileDrop = React.useCallback((f: File) => dispatch(actions.setFileAction(f)), []);

  return (
    <>
      <FormControl error={!!file.error}>
        <label>
          <Input
            className={styles.input}
            type="file"
            name="file"
            inputProps={{ accept: 'text/html' }}
            onChange={onInputFileChange}
          />
          <FakeInput onFileDrop={onFileDrop} />
        </label>
        {!!file.error && (
          <FormHelperText component="span" sx={{ textAlign: 'center' }}>
            <Typography component="span" variant="h6">
              {file.error}
            </Typography>
          </FormHelperText>
        )}
      </FormControl>
      {!!file.value && (
        <List>
          <ListItem>
            <ListItemAvatar>
              <Avatar>
                <InsertDriveFile />
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary={file.value.name} />
          </ListItem>
        </List>
      )}
    </>
  );
};
