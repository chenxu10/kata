import pandas as pd

def change_detection(df):
    def clean_word(word):
        """Remove punctuation from word ends for comparison"""
        return word.strip(".,!?;:'\"()[]{}") if word else None

    def compare_words(user_word, gpt_word):
        """Compare cleaned words and return appropriate styles"""
        clean_uw = clean_word(user_word)
        clean_gw = clean_word(gpt_word)
        
        if clean_uw == clean_gw:
            return (
                f'<span style="color: #4CAF50">{user_word}</span>' if user_word else None,
                f'<span style="color: #4CAF50">{gpt_word}</span>' if gpt_word else None
            )
        return (
            f'<span style="color: #FF0000">{user_word}</span>' if user_word else None,
            f'<span style="color: #FFD700">{gpt_word}</span>' if gpt_word else None
        )

    def process_sentence_pair(user_sentence, gpt_sentence):
        """Split and compare sentences word-by-word"""
        user_words = user_sentence.split()
        gpt_words = gpt_sentence.split()
        max_length = max(len(user_words), len(gpt_words))
        
        user_line, gpt_line = [], []
        for i in range(max_length):
            uw = user_words[i] if i < len(user_words) else None
            gw = gpt_words[i] if i < len(gpt_words) else None
            
            user_span, gpt_span = compare_words(uw, gw)
            if user_span: user_line.append(user_span)
            if gpt_span: gpt_line.append(gpt_span)
            
        return ' '.join(user_line), ' '.join(gpt_line)

    def create_output_row(user_processed, gpt_processed):
        """Create final pandas Series output row"""
        return pd.Series({
            'user_short': user_processed,
            'gpt_short': gpt_processed
        })

    def process_row(row):
        """Main row processing orchestrator"""
        user_processed, gpt_processed = process_sentence_pair(
            row['user_short'],
            row['gpt_short']
        )
        return create_output_row(user_processed, gpt_processed)

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