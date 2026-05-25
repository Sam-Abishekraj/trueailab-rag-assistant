from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = []
    chunk_id = 1

    for document in documents:

        full_text = f"""
Title: {document["title"]}

{document["content"]}
        """.strip()

        split_texts = text_splitter.split_text(
            full_text
        )

        for chunk_text in split_texts:

            # avoid useless tiny chunks
            if len(chunk_text.strip()) < 100:
                continue

            chunks.append({
                "chunk_id": chunk_id,
                "title": document["title"],
                "content": chunk_text,
                "source_document": document["title"]
            })

            chunk_id += 1

    return chunks