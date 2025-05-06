## Virtual environments

In this section, we'll use poetry to create a virtual environment, define the dependencies that we'll need for this project in a `pyproject.toml` file, and install those dependencies. Note: in most cases, we'd want to commit our `pyproject.toml` and `poetry.lock` file to this repository so that other developers will have the same python environment, but we won't here so that everyone can create those files on their own. 

I'll also say that we won't deal here with having multiple versions of python installed on the same system, but you may find yourself wanting to do that. One tool that I find useful for that is [`pyenv`](https://github.com/pyenv/pyenv) an easy-to-use tool for having multiple versions of python installed. If you decide to check it out, let me know if you want to talk through it!

1. Install poetry by running `curl -sSL https://install.python-poetry.org | python3 -` on your terminal. More installation options/instructions can be found [in the poetry documentation](https://python-poetry.org/docs/#installation). The rest of these instructions assume that you are using poetry >= 2. Use `poetry --version` to check your version of poetry.
2. We'll use poetry's built-in tool for starting a new project (although you could do all of this by creating a `pyproject.toml` file on your own). Run `poetry init`. For this project, let's add the `requests` package to our dependencies and the `black` package to our development dependencies. 
3. Then run `poetry install` to install this virtual environment. You'll get an error because poetry is looking to install the package we are building to our environment. Add the `package-mode = false` configuration to the `[tool.poentry]` block in your `pyproject.toml` file, and run `poetry install` again.
4. Now, run `poetry env activate`. This will print a command starting with `source` to your terminal. Copy this command into your terminal prompt and run it. You're now "inside" your environment. So, you could run `python` and then import one of the packages we just installed. Any command line tool you've installed will also be available, so you can run the command line command `black`. You can use `exit` to close the terminal.
5. We've already defined two dependency groups: the main dependencies and the dev dependencies. Let's say we only want the main dependencies in our environment. You can run `poetry install --sync --without dev` and poetry will synch our environment to remove the dev dependencies. 

The [poetry cli documentation](https://python-poetry.org/docs/cli/) contains good instructions on a number of other very useful commands, some of which we'll  use later in this tutorial.

## Formatting code

We'll use black as our code formatter of choice. We installed black in our dev dependencies in the earlier section. Make sure we've still got our dev dependencies installed by running `poetry install --sync`. 

1. Take a look at the code `formatting_example.py` and notice the weird formatting. You could import and use the function in a python shell to test its functionality.
2. Run `black --check --diff formatting_example.py` to see when black would change about this file. 
3. Run `black formatting_example.py` to see black actually make the formatting changes. 

## Linting code

We'll use pylint as our code linter. pylance is another code linter that comes installed with the "Python" extension of VSCode.

1. Add `pylint` to our dev dependencies in poetry: run `poetry add --group dev pylint`. 
2. Write the function described in `sample_functions.py`.
3. Then run `pylint` on your code by running `pylint sample_functions.py`. 
4. Try setting up the `pylint` extension to VSCode. Open `sample_functions.py` and see what alerts you see.

## Type checking

We'll use mypy as our type-checking utility.

1. Add `mypy` to our dev dependencies in poetry. Install and set-up the VSCode extension for mypy.
2. Add some types to the function you wrote in `sample_functions.py` and track the alerts that mypy gives you as you go along.
3. Try adding the `--strict` argument to mypy in the VSCode extension settings. See what new things mypy complains about. Depending on the code base you are working on and your own workflow, you may or may not find the `--strict` setting helpful.

## Unit testing

Python ships with the built-in unittest module.

1. Write some unit tests using the unittest module for the class in function_for_testing.py.
2. Run your tests by running `python -m unittest tests`. Do they pass?
3. Try adding a test for some additional functionality. Run your unittests to verify that your new test does not pass.
4. Add a function to what you have in `sample_functions.py`. Run your tests again. Do they pass?

Note: You don't have to run all of your unit tests every time. To select what test (or section of tests) to run, you can pass in a dot-separated path to the test. For example, to run a test case call "MyTestCase" that is in `tests.py`, you can run `python -m unittest tests.MyTestCase`. 
