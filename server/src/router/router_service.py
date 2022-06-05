import uuid
from enum import Enum
from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse
from src.parser.parse import parse_file
from src.helpers.parse_vulnerabilities import get_accepted_types
from src.helpers.file_service import file_service
from pathlib import Path

class MIME_TYPE(Enum):
  HTML = 'text/html'

router = APIRouter()

@router.get('/')
async def greetings():
  return {"message": "Hello"}

@router.post('/parse')
async def parse_form(files: UploadFile = File(...), vulnerability: str = Form(...)):

  if files.content_type != MIME_TYPE.HTML.value:
    return HTTPException(status_code=415, detail="Тип файла не поддерживается")

  file_name = str(uuid.uuid4())
  file_full_name = file_name + '.xlsx'
  file_path = Path(file_service.static_result, file_full_name)
  file_mime_type = file_service.define_mime_type(file_path)

  file_content = files.file.read()
  accepted_types = get_accepted_types(vulnerability)
  final_list = parse_file(file_content, accepted_types)
  file_service.generate_xlsx(file_path, final_list)

  custom_headers = {"X-File-Name": file_full_name}

  return FileResponse(file_path, filename=file_full_name, media_type=file_mime_type, headers=custom_headers)

@router.get('/delete/{file_path}')
async def download_file(file_path: str):
  if not file_service.remove_file(file_path):
    return HTTPException(status_code=404, detail="Файл не найден")
  return {}
