import numpy as np
import pytest

RNG = np.random.default_rng(seed=1000)
SMALL_ARRAY_SIZE = 1000

@pytest.fixture
def small_array() -> np.ndarray:
    """Small (10x10) image array for testing"""
    return RNG.random(SMALL_ARRAY_SIZE)

@pytest.fixture
def check1(small_array) -> float:
    """Print the sum of the array"""
    return np.sum(small_array)


@pytest.fixture
def another_small_array() -> np.ndarray:
    return RNG.random(SMALL_ARRAY_SIZE)

@pytest.fixture
def check2(another_small_array) -> float:
    """Print the sum of the array"""
    return np.sum(another_small_array)
