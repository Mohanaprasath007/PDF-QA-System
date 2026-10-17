from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_text_chunks(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000
    )

    chunks = text_splitter.split_text(text)

    return chunks