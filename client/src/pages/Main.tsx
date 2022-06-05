import React from 'react';
import { Container } from '@mui/material';
import { Form } from '../components/Form';
import { FormContextProvider } from '../contexts/form.context';

export const Main: React.FC = () => (
  <Container component="main" maxWidth="sm">
    <FormContextProvider>
      <Form />
    </FormContextProvider>
  </Container>
);
