from app.services.retrieval_service import (
    search_documents
)

from app.prompts.chat_prompt import (
    build_prompt
)

from app.services.llm_service import (
    generate_response
)

from app.services.memory_service import (
    get_chat_history,
    add_message
)


def ask_rag(
    session_id,
    question
):

    retrieved_docs = (
        search_documents(
            question
        )
    )

    if not retrieved_docs:

        return {
            "reply": (
                "I could not find enough "
                "information in the "
                "university knowledge base."
            ),
            "retrievedChunks": 0
        }

    retrieved_docs = sorted(
        retrieved_docs,
        key=lambda x: x["score"],
        reverse=True
    )

    context = "\n\n".join([
        result["chunk"][
            "content"
        ]
        for result in retrieved_docs
    ])

    chat_history = (
        get_chat_history(
            session_id
        )
    )

    history_text = "\n".join([
        f"{msg['role']}: "
        f"{msg['content']}"
        for msg in chat_history
    ])

    prompt = build_prompt(
        context=context,
        question=question,
        history=history_text
    )

    response = generate_response(
        prompt
    )

    answer = response["text"]

    tokens_used = response[
        "tokens"
    ]

    add_message(
        session_id,
        "user",
        question
    )

    add_message(
        session_id,
        "assistant",
        answer
    )

    return {
        "reply": answer,
        "retrievedChunks": len(retrieved_docs),
        "tokensUsed": tokens_used
    }