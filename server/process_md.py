import io

# pipenv install -q langchain-text-splitters
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter




# needs to take UploadFile
# turn it into string
# pass string to header_splitter
# return chunks in an array

async def chunk_md(file):
    file_string = await md_string(file)
    md_header_splits = string_to_seperate_documents(file_string)
    content_array = extract_document_contents(md_header_splits)
    return content_array

async def md_string(file):
    file_string = str(await file.read())
    # for some reason you need to replace \n's to work w/the splitter
    file_string = file_string.replace(r'\n', '\n')
    return file_string

# turns md file into a list of 'langchain documents' split by header
def string_to_seperate_documents(file_string):
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    # return markdown_splitter.split_text(file_string)


    # -----------------------------

    # MD splits
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on, strip_headers=False
    )
    md_header_splits = markdown_splitter.split_text(file_string)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=250, chunk_overlap=30
    )

    # Split
    splits = text_splitter.split_documents(md_header_splits)
    print('splits are', splits)
    return splits

    # -----------------------------

# gets content as string from langchain documents -> returns as list
def extract_document_contents(langchain_documents):
    content_list = []
    for doc in langchain_documents:
        content_list.append(doc.page_content)
    
    return content_list




