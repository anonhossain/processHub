# file: app/backend/src/services/doc_to_pdf.py
import os
import zipfile
import tempfile
import io
from typing import List
from docx2pdf import convert
from fastapi import UploadFile

class DocToPDFConverter:
    async def convert_and_zip(self, files: List[UploadFile]) -> io.BytesIO:
        # Business logic: Create a sandbox that deletes itself after use
        with tempfile.TemporaryDirectory() as tmp_dir:
            pdf_paths = []

            for file in files:
                if not file.filename: continue
                
                # Save original docx
                input_path = os.path.join(tmp_dir, file.filename)
                with open(input_path, "wb") as f:
                    f.write(await file.read())

                # Convert to PDF
                base_name = os.path.splitext(file.filename)[0]
                output_path = os.path.join(tmp_dir, f"{base_name}.pdf")
                convert(input_path, output_path)
                pdf_paths.append(output_path)

            # Zip the results in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                for pdf in pdf_paths:
                    zip_file.write(pdf, os.path.basename(pdf))
            
            zip_buffer.seek(0)
            return zip_buffer