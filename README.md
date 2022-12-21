# pytest, fixtures and Random Number Generation

This small repository provides a [minimal reproducible
example](https://stackoverflow.com/help/minimal-reproducible-example) to investigate the behaviour of
[Numpy](https://numpy.org/) [Random Number Generator](https://numpy.org/doc/stable/reference/random/generator.html) and
its behaviour when using [pytest fixtures](https://docs.pytest.org/en/7.2.x/explanation/fixtures.html) from a
`conftest.py`.

## Motiviation

We observed some strange behaviour with arrays differing in tests. This is meant to investigate the issue.
