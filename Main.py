"""
AI Study Assistant
An open-source study tool for students.

Current features:
- Summarize notes
- Generate study questions
- Create flashcards
"""

def summarize_notes(notes):
    """Create a simple summary from study notes."""
    sentences = [s.strip() for s in notes.split(".") if s.strip()]

    if not sentences:
        return "No notes provided."

    # Keep the first few key sentences as a basic local summary.
    summary = sentences[:3]
    return ". ".join(summary) + "."


def generate_questions(notes):
    """Generate basic study questions from the notes."""
    sentences = [s.strip() for s in notes.split(".") if s.strip()]

    questions = []
    for sentence in sentences[:5]:
        words = sentence.split()
        if len(words) >= 4:
            topic = " ".join(words[:4])
            questions.append(f"What is the significance of {topic}?")

    return questions


def create_flashcards(notes):
    """Create simple flashcards from sentences."""
    sentences = [s.strip() for s in notes.split(".") if s.strip()]

    flashcards = []

    for i, sentence in enumerate(sentences[:5], start=1):
        flashcards.append({
            "card": i,
            "front": f"Explain: {sentence[:60]}...",
            "back": sentence
        })

    return flashcards


def main():
    print("=== AI Study Assistant ===")
    print("1. Summarize notes")
    print("2. Generate questions")
    print("3. Create flashcards")

    notes = input("\nPaste your study notes:\n")

    choice = input("\nChoose an option (1/2/3): ")

    if choice == "1":
        print("\n--- Summary ---")
        print(summarize_notes(notes))

    elif choice == "2":
        print("\n--- Study Questions ---")
        for question in generate_questions(notes):
            print("-", question)

    elif choice == "3":
        print("\n--- Flashcards ---")
        for card in create_flashcards(notes):
            print(f"\nCard {card['card']}")
            print("Q:", card["front"])
            print("A:", card["back"])

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
