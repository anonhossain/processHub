#file: app/backend/src/api/v1/routers/file_router.py

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse, StreamingResponse
from services.doc_to_pdf import DocToPDFConverter
from typing import List

api = APIRouter(prefix="/api/v1")

@api.get("/hello", tags=["Hello"], 
         summary="Hello Endpoint", 
         description="Returns a greeting message.", 
         response_description="A greeting message.",
         deprecated=False,
         response_model_exclude={"Password"})
def hello():
    return {"message": "Hello, Anon!"}

# file: app/backend/src/api/v1/routers/file_router.py
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from services.doc_to_pdf import DocToPDFConverter
from typing import List

api = APIRouter(prefix="/api/v1")

# file: app/backend/src/api/v1/routers/file_router.py
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from services.doc_to_pdf import DocToPDFConverter
from typing import List

api = APIRouter(prefix="/api/v1")

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from services.doc_to_pdf import DocToPDFConverter
from typing import List

api = APIRouter(prefix="/api/v1")

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from services.doc_to_pdf import DocToPDFConverter
from typing import List

api = APIRouter(prefix="/api/v1")

@api.post("/doc-to-pdf", tags=["File"])
async def convert_doc_to_pdf(files: List[UploadFile] = File(...)):
    service = DocToPDFConverter()
    
    # 1. Execute business logic
    zip_data = await service.convert_and_zip(files)
    
    # 2. Return the response with headers that trigger the browser download
    return StreamingResponse(
        zip_data,
        media_type="application/zip",
        headers={
            # 'attachment' tells the browser to download to the local PC
            "Content-Disposition": "attachment; filename=converted_files.zip",
            # 'Access-Control-Expose-Headers' is helpful for frontend JS to see the filename
            "Access-Control-Expose-Headers": "Content-Disposition"
        }
    )