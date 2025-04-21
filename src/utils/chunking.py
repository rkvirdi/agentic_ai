import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text,chunk_size: int = 200, chunk_overlap : int=30):
    text_chunks=[]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )
    for t in text:
        text_chunk = text_splitter.create_documents([t])
        text_chunks.append(text_chunk)
    new_text=[t for t in text_chunks]
    all_chunks=[x for x in new_text]
    return all_chunks
    

def read_files(folder_path: str) -> list:
    all_file = os.listdir(folder_path)
    texts=[]
    for file in all_file:
        if file.endswith('.txt'):
            with open(os.path.join(folder_path,file) ,mode='r',encoding='utf-8') as file:
                text = file.read()
                texts.append(text)
    return(texts)

