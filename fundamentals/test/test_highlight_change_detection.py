import pandas as pd

def change_detection(df):
    def compare_words(user_word, gpt_word):
        """Compare individual word pair and return styled spans"""
        if user_word == gpt_word:
            return (
                f'<span style="color: #4CAF50">{user_word}</span>',
                f'<span style="color: #4CAF50">{gpt_word}</span>'
            )
        else:
            user_style = f'<span style="color: #FF0000; text-decoration: underline">{user_word}</span>' if user_word else None
            gpt_style = f'<span style="color: #FFA500; text-decoration: underline">{gpt_word}</span>' if gpt_word else None
            return (user_style, gpt_style)

    def process_sentence_pair(user_sentence, gpt_sentence):
        """Process a pair of sentences and return styled components"""
        user_words = user_sentence.split()
        gpt_words = gpt_sentence.split()
        max_len = max(len(user_words), len(gpt_words))
        
        user_output, gpt_output = [], []
        
        for i in range(max_len):
            uw = user_words[i] if i < len(user_words) else None
            gw = gpt_words[i] if i < len(gpt_words) else None
            
            user_span, gpt_span = compare_words(uw, gw)
            if user_span: user_output.append(user_span)
            if gpt_span: gpt_output.append(gpt_span)
            
        return ' '.join(user_output), ' '.join(gpt_output)

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
        "user_short": ["this is an apple", "legal billing is fun!"],
        "gpt_short": ["this is an orange", "legal billing is serious."]
    })
    
    result = change_detection(input_df)
    
    # Verify we get a Styler object
    assert isinstance(result, pd.io.formats.style.Styler), "Should return a Styler object"
    # Add more checks here if needed

if __name__ == "__main__":
    input_df = pd.DataFrame({
        "user_short": ["this is an apple", "legal billing is fun!"],
        "gpt_short": ["this is an orange", "legal billing is serious."]
    })
    result = change_detection(input_df)
    with open("example_cd.html", "w") as f:
        f.write(result.to_html())