#!/bin/bash
set -eu
pylint $(git ls-files '*.py')
flake8 $(git ls-files '*.py')
