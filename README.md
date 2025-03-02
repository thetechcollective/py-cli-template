## This template has a devcontainer designed to run python using uv

- Supports inherited gh login from host (co-routine btw `.devcontainer/initializeCommand.sh` and `.devcontainer/postCreateCommand.sh` utilizing `.devcontainer/gh-login.sh`)
- gh-extensions `gh-semver` and `gh-tt` pre-installed (`.devcontainer/postCreateCommand.sh`)
- Some neat gh aliases preinstalled (`.devcontainer/postCreateComand.sh` and `.gh-alias.yml`)
- support for `gh workon|wrapup|deliver` and integration to our GitHub Downstream Project (`'gitconfig`)
- Support for `pytest`, `pytest-cov`, `debugpy` and other python standard features (`.devcontainer/devcontainer.json`, `.vscode/settings.json`, `pytest.ini`)
- Support for a Python environment using uv (`pyprojeect.toml`, `uv.lock`, `.devcontainer/postCreateCommand.sh`) 
- Support for a repo scoped `.gitconfig` (`.devcontainer/postCreateCommand.sh`)
- A useful `.gitignore`
- A debug laucher (`.vscode/launch.json`) 
- A GitHub workflow that just runs your unit tests with coverage.
- It has a coverage threshold (see `.coveragerc`)
- The `Gitter` class, and it's unit tests are left behind, as an example - but it may prove useful!

### You need to:
- Rename the two scripts in the root: `gh-sample` and `gh-sample.py`
- Search for 'TODO' and make the necessary corrections
- In the command pallette choose `Python: Select Interpreter` and pick the interpreter that is defined by `defaultInterpreterPath`.
- Visit [`thetechcollective/gh-tt`](https://github.com/thetechcollective/gh-tt) to get more inspiration.

### You may also want to:
- Update the `uv.lock` by running `uv lock`
- Try to run the unit tests and seem them run smoothly
- Set a break point and start the debugger


