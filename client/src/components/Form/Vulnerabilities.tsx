import React from 'react';
import {
  FormControl,
  FormHelperText,
  FormGroup,
  FormControlLabel,
  Checkbox,
  Typography,
} from '@mui/material';
import { FormContext, actions } from '../../contexts/form.context';

interface VulnerabilitiesProps {
  values: number[];
}

export const Vulnerabilities: React.FC<VulnerabilitiesProps> = ({ values }) => {
  const [state, dispatch] = React.useContext(FormContext);
  const { vulnerabilities } = state;
  const [criticalCount, highCount, mediumCount, lowCount] = values;

  const onCriticalChange = () => dispatch(actions.toggleVulnerabilitiesCriticalAction());
  const onHighChange = () => dispatch(actions.toggleVulnerabilitiesHighAction());
  const onMediumChange = () => dispatch(actions.toggleVulnerabilitiesMediumAction());
  const onLowChange = () => dispatch(actions.toggleVulnerabilitiesLowAction());

  return (
    <FormControl sx={{ margin: 1 }}>
      <FormHelperText component="span" sx={{ textAlign: 'center' }}>
        <Typography component="span" variant="h6">
          Выберите нужные ошибки
        </Typography>
      </FormHelperText>
      <FormGroup>
        <FormControlLabel
          control={
            <Checkbox
              name="vulnerabilities"
              checked={vulnerabilities.critical}
              onChange={onCriticalChange}
            />
          }
          label={`${criticalCount} Критические`}
        />
        <FormControlLabel
          control={
            <Checkbox
              name="vulnerabilities"
              checked={vulnerabilities.high}
              onChange={onHighChange}
            />
          }
          label={`${highCount} Высокие`}
        />
        <FormControlLabel
          control={
            <Checkbox
              name="vulnerabilities"
              checked={vulnerabilities.medium}
              onChange={onMediumChange}
            />
          }
          label={`${mediumCount} Средние`}
        />
        <FormControlLabel
          control={
            <Checkbox name="vulnerabilities" checked={vulnerabilities.low} onChange={onLowChange} />
          }
          label={`${lowCount} Низкие`}
        />
      </FormGroup>
    </FormControl>
  );
};
