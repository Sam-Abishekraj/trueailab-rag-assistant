from collections import defaultdict


# in-memory session storage
chat_memory = defaultdict(list)

MAX_HISTORY = 10
# 5 user + 5 assistant messages


def get_chat_history(
    session_id
):

    return chat_memory[
        session_id
    ]


def add_message(
    session_id,
    role,
    content
):

    chat_memory[
        session_id
    ].append({
        "role": role,
        "content": content
    })

    # keep only latest history
    if len(
        chat_memory[
            session_id
        ]
    ) > MAX_HISTORY:

        chat_memory[
            session_id
        ] = chat_memory[
            session_id
        ][-MAX_HISTORY:]


def get_history_text(
    session_id
):

    history = get_chat_history(
        session_id
    )

    return "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in history
        ]
    )