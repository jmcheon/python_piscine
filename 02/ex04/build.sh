# !/bin/zsh

# Remove old build and distribution folders
rm -rf build/
rm -rf dist/

# Create a source distribution and a wheel distribution
pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel
$(which python) setup.py sdist bdist_wheel
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl --force-reinstall
