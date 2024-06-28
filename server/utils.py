import os
import process_pdf as pdf
import process_md as md

def file_type(filename):
    # Split the filename into name and extension
    _, file_extension = os.path.splitext(filename)
    
    # Return the file extension without the leading dot
    return file_extension.lstrip('.')


async def chunk(file):
    match file_type(file.filename):
        case 'pdf':
            return await pdf.chunk_pdf(file)
        case 'md':
            return await md.chunk_md(file)

