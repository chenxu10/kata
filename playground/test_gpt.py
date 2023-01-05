from transformers import pipeline

def test_load_pretrained_transformer():
    model = pipeline("sentiment-analysis")
    result = model("I like the way it is and I love it!")
    resultlabel = result[0]['label']
    expected = "POSITIVE"
    assert resultlabel == expected
    
if __name__ == "__main__":
    test_load_pretrained_transformer()