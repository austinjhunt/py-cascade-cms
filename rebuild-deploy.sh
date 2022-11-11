#!/bin/bash
# rebuild and redeploy to pypi
rm -rf dist build
rm -rf src/py_cascade_cms_api*egg-info

python setup.py sdist bdist_wheel
#twine upload --repository testpypi --verbose dist/*
# prod
twine upload --verbose dist/*