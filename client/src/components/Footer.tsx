import React from 'react';
import { Box, Container, Link, Stack, Typography } from '@mui/material';

export const Footer = () => (
  <Box component="footer" sx={{ marginTop: 'auto', padding: 1, backgroundColor: 'primary.main' }}>
    <Container maxWidth="sm">
      <Stack direction="row" justifyContent="space-between" alignItems="center">
        <Stack direction="row" spacing={0.5}>
          <Typography component="span" variant="subtitle1" color="primary.contrastText">
            by
          </Typography>
          <Link
            href="https://vk.com/leendrew"
            color="primary.contrastText"
            target="_blank"
            variant="subtitle1"
          >
            LeenDrew
          </Link>
        </Stack>
        <Link
          href="https://github.com/LeenDrew/si-parser"
          color="primary.contrastText"
          target="_blank"
          variant="subtitle1"
        >
          Repository
        </Link>
      </Stack>
    </Container>
  </Box>
);
