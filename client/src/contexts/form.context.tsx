import React, { useReducer, createContext } from 'react';

type ReceivedFile = File | null;

export interface FormState {
  file: {
    value: ReceivedFile;
  };
  vulnerabilities: {
    critical: boolean;
    high: boolean;
    medium: boolean;
    low: boolean;
  };
}

type Schema<T> = {
  [Key in keyof T]: T[Key] & { error: string };
};
type FormSchema = Schema<FormState>;

const initialState: FormSchema = {
  file: {
    value: null,
    error: '',
  },
  vulnerabilities: {
    critical: false,
    high: false,
    medium: false,
    low: false,
    error: '',
  },
};

enum VulnerabilityActionName {
  TOGGLE_CRITICAL = 'TOGGLE_CRITICAL',
  TOGGLE_HIGH = 'TOGGLE_HIGH',
  TOGGLE_MEDIUM = 'TOGGLE_MEDIUM',
  TOGGLE_LOW = 'TOGGLE_LOW',
  SET_VULNARABILITY_ERROR = 'SET_ERROR',
}

enum FileActionName {
  SET_FILE = 'SET_FILE',
  SET_FILE_ERROR = 'SET_FILE_ERROR',
}

export const actions = {
  setFileAction: (file: ReceivedFile) => ({
    type: FileActionName.SET_FILE,
    payload: file,
  }),
  setFileErrorAction: (message: string) => ({
    type: FileActionName.SET_FILE_ERROR,
    payload: message,
  }),

  toggleVulnerabilitiesCriticalAction: () => ({
    type: VulnerabilityActionName.TOGGLE_CRITICAL,
    payload: null,
  }),
  toggleVulnerabilitiesHighAction: () => ({
    type: VulnerabilityActionName.TOGGLE_HIGH,
    payload: null,
  }),
  toggleVulnerabilitiesMediumAction: () => ({
    type: VulnerabilityActionName.TOGGLE_MEDIUM,
    payload: null,
  }),
  toggleVulnerabilitiesLowAction: () => ({
    type: VulnerabilityActionName.TOGGLE_LOW,
    payload: null,
  }),
  setVulnerabilitiesErrorAction: (message: string) => ({
    type: VulnerabilityActionName.SET_VULNARABILITY_ERROR,
    payload: message,
  }),
};

type Infernal<T> = T extends { [key: string]: infer U } ? U : never;
type ActionTypes = ReturnType<Infernal<typeof actions>>;

const reducer = (state: FormSchema, { type, payload }: ActionTypes): FormSchema => {
  switch (type) {
    case FileActionName.SET_FILE: {
      const file = payload as ReceivedFile;
      return {
        ...state,
        file: {
          ...state.file,
          value: file,
        },
      };
    }
    case FileActionName.SET_FILE_ERROR: {
      const message = payload as string;
      return {
        ...state,
        file: {
          ...state.file,
          error: message,
        },
      };
    }

    case VulnerabilityActionName.TOGGLE_CRITICAL: {
      return {
        ...state,
        vulnerabilities: {
          ...state.vulnerabilities,
          critical: !state.vulnerabilities.critical,
        },
      };
    }
    case VulnerabilityActionName.TOGGLE_HIGH: {
      return {
        ...state,
        vulnerabilities: {
          ...state.vulnerabilities,
          high: !state.vulnerabilities.high,
        },
      };
    }
    case VulnerabilityActionName.TOGGLE_MEDIUM: {
      return {
        ...state,
        vulnerabilities: {
          ...state.vulnerabilities,
          medium: !state.vulnerabilities.medium,
        },
      };
    }
    case VulnerabilityActionName.TOGGLE_LOW: {
      return {
        ...state,
        vulnerabilities: {
          ...state.vulnerabilities,
          low: !state.vulnerabilities.low,
        },
      };
    }
    case VulnerabilityActionName.SET_VULNARABILITY_ERROR: {
      const message = payload as string;
      return {
        ...state,
        vulnerabilities: {
          ...state.vulnerabilities,
          error: message,
        },
      };
    }

    default:
      throw new Error();
  }
};

type FormContext = [FormSchema, React.Dispatch<ActionTypes>];

export const FormContext = createContext<FormContext>([initialState, () => null]);

export const FormContextProvider: React.FC = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);
  const memoizedValue = React.useMemo(() => [state, dispatch] as FormContext, [state]);
  return <FormContext.Provider value={memoizedValue}>{children}</FormContext.Provider>;
};
