import json
from pathlib import Path


def load_documents():

    docs_path = Path("docs.json")

    if not docs_path.exists():
        raise FileNotFoundError(
            "docs.json file not found"
        )

    with open(docs_path, "r", encoding="utf-8") as file:
        documents = json.load(file)

    return documents