from playground.browniemotion import generate_oneasset_rw

def test_generate_oneasset_rw():
    oneasset_rw = generate_oneasset_rw(startingprice=100)
    assert max(oneasset_rw) <= 200
    assert min(oneasset_rw) >= 10