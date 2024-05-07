## Virtual environments

In this section, we'll use poetry to create a virtual environment, define the dependencies that we'll need for this project in a `pyproject.toml` file, and install those dependencies. Note: in most cases, we'd want to commit our `pyproject.toml` and `poetry.lock` file to this repository so that other developers will have the same python environment, but we won't here so that everyone can create those files on their own. 

I'll also say that we won't deal here with having multiple versions of python installed on the same system, but you may find yourself wanting to do that. One tool that I find useful for that is [`pyenv`](https://github.com/pyenv/pyenv) an easy-to-use tool for having multiple versions of python installed. If you decide to check it out, let me know if you want to talk through it!

1. Install poetry by running `curl -sSL https://install.python-poetry.org | python3 -` on your terminal. More installation options/instructions can be found [in the poetry documentation](https://python-poetry.org/docs/#installation).
2. We'll use poetry's built-in tool for starting a new project (although you could do all of this by creating a `pyproject.toml` file on your own). Run `poetry init`. For this project, let's add the `requests` package to our dependencies and the `black` package to our development dependencies. 
3. Then run `poetry install` to install this virtual environment. You'll see a warning because poetry is looking to install the package we are building to our environment. Since we're not building a package here, we don't need to worry about it, or we could add the `package-mode = false` configuration to the first block in our `pyproject.toml` file.
4. Now, run `poetry shell`. You're now "inside" your environment. So, you could run `python` and then import one of the packages we just installed. Any command line tool you've installed will also be available, so you can run the command line command `black`. Exit the virtual environment shell with `exit`.
5. We've already defined two dependency groups: the main dependencies and the dev dependencies. Let's say we only want the main dependencies in our environment. You can run `poetry install --sync --without dev` and poetry will synch our environment to remove the dev dependencies. 

The [poetry cli documentation](https://python-poetry.org/docs/cli/) contains good instructions on a number of other very useful commands, some of which we'll  use later in this tutorial.

## Formatting code

We'll use black as our code formatter of choice. We installed black in our dev dependencies in the earlier section. Make sure we've still got our dev dependencies installed by running `poetry install --sync`. 

1. Take a look at the code `formatting_example.py` and notice the weird formatting. You could import and use the function in a python shell to test its functionality.
2. Run `black --check --diff formatting_example.py` to see when black would change about this file. 
3. Run `black formatting_example.py` to see black actually make the formatting changes. 

