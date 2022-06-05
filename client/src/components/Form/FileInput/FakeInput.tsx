import React from 'react';
import { Paper, Typography } from '@mui/material';

interface DropZoneProps {
  onFileDrop: (file: File) => void;
}

export const FakeInput: React.FC<DropZoneProps> = ({ onFileDrop }) => {
  const [isDrag, setIsDrag] = React.useState<boolean>(false);

  const dragStartHandler = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDrag(true);
  };
  const dragLeaveHandler = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDrag(false);
  };

  const onDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (e.dataTransfer.files && e.dataTransfer.files.length) {
      onFileDrop(e.dataTransfer.files[0]);
    }
    setIsDrag(false);
  };

  return (
    <Paper
      variant="outlined"
      sx={{ padding: 1, borderWidth: 3, borderStyle: isDrag ? 'dashed' : 'solid' }}
      onDrop={onDrop}
      onDragStart={dragStartHandler}
      onDragLeave={dragLeaveHandler}
      onDragOver={dragStartHandler}
    >
      <Typography textAlign="center" variant="subtitle1">
        Выберите файл или перетащите его сюда
      </Typography>
    </Paper>
  );
};
