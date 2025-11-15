
# Single Page Application in Python
Copyright 2025 Stefan Meisner Larsen<br/>
Licensed under the MIT License.
## Introduction
This is the source for the first post on dev.to about single page web applications in python and javascript
## Create a virtual environment
In the project root (or whereever you want) create a virtual environment
<code>
python3 -m venv .venv
</code>
Activate the the environment by sourcing activate script:
<code>
. .venv/bin/activate

## Install dependencies
Install dependencies including the optional from the "dev" section:

<code>
python -m pip install -e '.[dev]'
</code>

## Run code
<code>

python src/single_page_python.py
