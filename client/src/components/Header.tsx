import React from 'react';
import { AppBar, Typography } from '@mui/material';

export const Header: React.FC = () => (
  <AppBar sx={{ padding: 1 }} position="static">
    <Typography component="h1" variant="h4" textAlign="center">
      Table Generator
    </Typography>
  </AppBar>
);
