#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Package libraries
try:
    import import_notebook
except ModuleNotFoundError:
    pass

from code_demo import (demo, demo_datasets, demo_pdbs, demo_fasta) 


# In[ ]:


def _test_output_demo(argument):
    '''
    Aux function for test_demo.
    Will try to run a demo function, will return True if there is an error.
    '''
    error = False
    try:
        demo(argument, show=False)
    except:
        error = True
    return error


# In[ ]:


def test_demo():
    '''
    This function will test that demo is capable of generating the 
    types of figures ('heatmap', 'miniheatmap', 'mean', 'kernel', 'pca',
    'position', 'secondary_mean', 'correlation', 'individual_correlation') that demo()
    is supposed to. Will raise an error if at least one of the plots does not work.
    '''
    
    arguments = ['heatmap', 'miniheatmap', 'mean', 'kernel', 'pca',
                'position', 'secondary_mean', 'correlation', 'individual_correlation']
    solutions = [_test_output_demo(argument) for argument in arguments]
    assert any(solutions)==False, 'error when running the demo figures'

