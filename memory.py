
# Connect to Hindsight
client = Hindsight(
    base_url="http://localhost:8888"
)

# Memory bank name
BANK_ID = "recall-desk"


def save_memory(content):
    """Save information into memory."""
    client.retain(
        bank_id=BANK_ID,
        content=content
    )
    print("Memory saved successfully!")


def search_memory(question):
    """Search stored memories."""
    results = client.recall( bank_id=BANK_ID,
        query=question
    )

    for memory in results.results:
        print(memory.text)


def generate_insight(question):
    """Generate an answer using stored memories."""
    answer = client.reflect(
        bank_id=BANK_ID,
        query=question
    )

    return answer.text
