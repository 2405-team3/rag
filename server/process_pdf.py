import pymupdf as pym
import spacy
import io

nlp = spacy.load("en_core_web_sm")


async def chunk_pdf(file):
    pdf = await open(file)
    return sentences(pdf)

async def open(file):
    file_bytes = await file.read()
    file_buffer = io.BytesIO(file_bytes)

    pdf = pym.open(stream=file_buffer, filetype="pdf")
    return pdf


def sentences(pdf):
    text = ""

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        text += page.get_text()

    doc = nlp(text)
    # array of sentences for embedding
    sentences = [sent.text for sent in doc.sents]
    return sentences



