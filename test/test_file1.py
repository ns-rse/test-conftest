import numpy as np

def test_what_is_the_rng1(small_array, check):
    print(f"What is our array sum in conftest? : {check}")
    print(f"What is our array sum here?        : {np.sum(small_array)}")
    assert False
