#!/usr/bin/env python

import nbformat, fire
from nbconvert.preprocessors import ExecutePreprocessor

# This file is adapted from https://github.com/fastai/course-v3/blob/master/nbs/dl2/run_notebook.py

def run_notebook(path):
	nb = nbformat.read(open(path), as_version=nbformat.NO_CONVERT)
	ExecutePreprocessor(timeout=600).preprocess(nb, {})
	print('done')

if __name__ == '__main__':
	fire.Fire(run_notebook)
