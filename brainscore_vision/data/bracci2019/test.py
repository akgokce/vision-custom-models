#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:32:25 2024

@author: costantino_ai
"""
import pytest
from brainscore_vision import load_dataset, load_stimulus_set

@pytest.mark.private_access
def test_existence():
    assert load_dataset('Bracci2019') is not None
    assert load_stimulus_set('Bracci2019') is not None
    
    