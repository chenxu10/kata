import pandas as pd

def to_rope(s):
    return Rope(s)


class Rope:
    def __init__(self, s):
        self.s = s

    def __str__(self) -> str:
        return self.s

assert str(to_rope("abc")) == 'abc'



def generate_tweedie_dataset():
    return pd.DataFrame({
      "net_loss":[1000,1000],  
    })


pd.testing.assert_frame_equal(
    generate_tweedie_dataset(),
    pd.DataFrame({"net_loss":[1000,1000]})
)