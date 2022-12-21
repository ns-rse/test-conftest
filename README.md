# pytest, fixtures and Random Number Generation

This small repository provides a [minimal reproducible
example](https://stackoverflow.com/help/minimal-reproducible-example) to investigate the behaviour of
[Numpy](https://numpy.org/) [Random Number Generator](https://numpy.org/doc/stable/reference/random/generator.html) and
its behaviour when using [pytest fixtures](https://docs.pytest.org/en/7.2.x/explanation/fixtures.html) from a
`conftest.py`.

## Motiviation

We observed some strange behaviour with arrays differing in tests. This is meant to investigate the issue.

A RNG is initialised in `test/conftest.py` there are four fixtures

| Fixture                 | Description                            |
|-------------------------|----------------------------------------|
| `small_array()`         | Numpy array of random numbers.         |
| `check1()`              | Sum of small_array()                   |
| `another_small_array()` | Another Numpy array of random numbers. |
| `check2()`              | Sum of `another_small_array()`.        |

In the `test/test_file1.py` has three test functions which prints the values and aims to demonstrate how the value
returned changes with each use of the fixture.

To run the code ensure you have `pytest` and `numpy` installed (ideally under a virtual environment), clone the
repository and run the tests.

``` bash
git clone git@github.com:ns-rse/test-conftest.git
cd test-conftest
pytest
```

The tests all fail (by design) so that the values of summing the arrays are printed. they are...

``` bash
 ❱ pytest
_________________________________________________ test_what_is_the_rng1 __________________________________________________
What is our array sum in conftest.check1()? : 487.95289395579516
What is our small_array?                    : 487.95289395579516
What is our array sum in conftest.check2()? : 491.17291291943263
What is our another_small_array?            : 491.17291291943263
_______________________________________________________ test_again _______________________________________________________

If we use the fixtures again what value do we get?
small_array                : 490.0930281302126
another_small_array        : 503.3995169906159
_____________________________________________________ test_yet_again _____________________________________________________

If we use the fixtures again what value do we get?
small_array                : 510.45647735087
another_small_array        : 508.94587061858283
```

This shows that the fixture `small_array` and `another_small_array` have the same value when they are first used in
`conftest.py` **and** the first time they are used in `test_file1.test_what_is_the_rng1()` function.

Each subsequent call to either fixture that returns a random array gives a new value, this is expected.

If you comment out `test_again()` and re-run the tests then the values returned by `test_yet_again()` are the same as
those returned by `test_again()` because order and the number of times the RNG has been called is important.

``` bash
 ❱ pytest
_________________________________________________ test_what_is_the_rng1 __________________________________________________
What is our array sum in conftest.check1()? : 487.95289395579516
What is our small_array?                    : 487.95289395579516
What is our array sum in conftest.check2()? : 491.17291291943263
What is our another_small_array?            : 491.17291291943263
_____________________________________________________ test_yet_again _____________________________________________________

If we use the fixtures again what value do we get?
small_array                : 490.0930281302126
another_small_array        : 503.3995169906159
```

This demonstrates that the number of times the RNG is called impacts the values it returns.

If you start with `test/test_file1.py` and have tests which use the RNG in the order...

``` bash
test_something()
test_another_thing()
```

...you'll get consistent results. However if you introduce a test _in-between_ (`test_something_in_between()`) these
then `test_another_thing` will generate **different** values the next time it runs and your test will fail.

``` bash
test_something()
test_something_in_between()
test_another_thing()
```
