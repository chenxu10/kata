import pandas as pd
from collections import Counter

def change_detection(df):
    def clean_word(word):
        """Remove punctuation while preserving original word"""
        return word.strip(".,!?;:'\"()[]{}") if word else None

    def process_sentence_pair(user_sent, gpt_sent):
        """Compare sentences and highlight matches across positions"""
        # Split and clean both sentences
        user_words = user_sent.split()
        gpt_words = gpt_sent.split()
        
        # Create counters for cleaned words
        user_cleaned = [clean_word(w) for w in user_words]
        gpt_cleaned = [clean_word(w) for w in gpt_words]
        
        # Track remaining matches using counters
        user_counter = Counter(user_cleaned)
        gpt_counter = Counter(gpt_cleaned)

        # Process user's words
        user_output = []
        for word, cleaned in zip(user_words, user_cleaned):
            if gpt_counter.get(cleaned, 0) > 0:
                user_output.append(f'<span style="color: #4CAF50">{word}</span>')
                gpt_counter[cleaned] -= 1
            else:
                user_output.append(f'<span style="color: #FF0000">{word}</span>')

        # Process GPT's words
        gpt_output = []
        for word, cleaned in zip(gpt_words, gpt_cleaned):
            if user_counter.get(cleaned, 0) > 0:
                gpt_output.append(f'<span style="color: #4CAF50">{word}</span>')
                user_counter[cleaned] -= 1
            else:
                gpt_output.append(f'<span style="color: #FFD700">{word}</span>')

        return ' '.join(user_output), ' '.join(gpt_output)

    def create_output_row(user_processed, gpt_processed):
        """Create final pandas Series output row"""
        return pd.Series({
            'user_short': user_processed,
            'gpt_short': gpt_processed
        })

    def process_row(row):
        """Main row processing orchestrator"""
        user, gpt = process_sentence_pair(row['user_short'], row['gpt_short'])
        return create_output_row(user, gpt)

    # Process rows and convert to styled HTML
    styled_df = df.apply(process_row, axis=1)
    return styled_df.style.set_properties(**{'white-space': 'pre-wrap'}).format(escape=None)

def test_change_detection():
    input_df = pd.DataFrame({
        "user_short": ["this is an apple. that is an apple.", "legal billing is fun!"],
        "gpt_short": ["this is an orange. that is an apple.", "legal billing is serious."]
    })
    
    result = change_detection(input_df)
    
    # Verify we get a Styler object
    assert isinstance(result, pd.io.formats.style.Styler), "Should return a Styler object"
    # Add more checks here if needed

if __name__ == "__main__":
    input_df = pd.DataFrame({
        "user_short": ["this is an apple. that is an apple.", "legal billing is fun!"],
        "gpt_short": ["this is an orange. that is an apple.", "legal billing is serious."]
    })
    result = change_detection(input_df)
    with open("example_cd.html", "w") as f:
        f.write(result.to_html())