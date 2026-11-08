def research_topic(topic):
    print(f"Researching: {topic}")
    return f"Research notes for {topic}"


if _name_ == "_main_":
    topic = input("Enter a research topic: ")
    notes = research_topic(topic)
    print(notes)
