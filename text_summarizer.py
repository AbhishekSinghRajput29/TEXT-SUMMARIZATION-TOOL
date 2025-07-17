from transformers import pipeline
import textwrap

def load_model():
    print("⏳ Loading summarization model...")
    summarizer = pipeline(
        "summarization",
        model="t5-small",
        tokenizer="t5-small",
        device=-1  # Force CPU
    )
    print("✅ Model loaded.\n")
    return summarizer

def get_user_input():
    print("📥 Enter your text (paste or type below).")
    print("👉 Press Enter twice to end input.\n")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return " ".join(lines)

def summarize_text(summarizer, text):
    if len(text.strip()) == 0:
        return "[!] No input provided."

    print("\n✂️ Summarizing... Please wait...\n")
    
    # Dynamically adjust length based on input
    num_words = len(text.split())
    max_len = min(150, int(num_words * 0.6))  # Summary ~60% of original
    min_len = min(30, max(10, int(num_words * 0.3)))  # At least 30 or 30%

    summary = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    return summary[0]['summary_text']

def main():
    summarizer = load_model()
    text = get_user_input()
    summary = summarize_text(summarizer, text)

    print("\n📄 Original Text:\n")
    print(textwrap.fill(text, width=80))
    
    print("\n📝 Summary:\n")
    print(textwrap.fill(summary, width=80))

if __name__ == "__main__":
    main()
