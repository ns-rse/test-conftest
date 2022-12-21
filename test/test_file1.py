import numpy as np

def test_what_is_the_rng1(small_array, check1, another_small_array, check2):
    print(f"What is our array sum in conftest.check1()? : {check1}")
    print(f"What is our small_array?                    : {np.sum(small_array)}")
    print(f"What is our array sum in conftest.check2()? : {check2}")
    print(f"What is our another_small_array?            : {np.sum(another_small_array)}")
    assert False

def test_again(small_array, another_small_array):
    print(f"If we use the fixtures again what value do we get?")
    print(f"small_array                : {np.sum(small_array)}")
    print(f"another_small_array        : {np.sum(another_small_array)}")
    assert False

def test_yet_again(small_array, another_small_array):
    print(f"If we use the fixtures again what value do we get?")
    print(f"small_array                : {np.sum(small_array)}")
    print(f"another_small_array        : {np.sum(another_small_array)}")
    assert False
