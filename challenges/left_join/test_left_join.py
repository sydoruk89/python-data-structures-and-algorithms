from left_join import left_join
import pytest

@pytest.fixture
def sample_dict():
    t1 = {
        'fond':'enamored',
        'wrath':'anger',
        'diligent':'employed',
        'outfit':'garb',
        'guide':'usher'
        }

    return t1

def test_class_example(sample_dict):

    t1 = sample_dict
    t2 = {
        'fond':'averse',
        'wrath':'delight',
        'diligent':'idle',
        'guide':'follow',
        'flow':'jam'
        }

    assert left_join(t1,t2) == {"fond": ["enamored","averse"], "wrath": ["anger","delight"], "diligent": ["employed","idle"], "outfit": ["garb",None], "guide": ["usher","follow"]}

def test_different_keys(sample_dict):
    t1 = sample_dict
    t2 = {
        'kind':'averse',
        'anger':'delight',
        'studious':'idle',
        'manual':'follow',
        'leak':'jam'
        }
    assert left_join(t1,t2) == {"fond": ["enamored",None], "wrath": ["anger",None], "diligent": ["employed",None], "outfit": ["garb",None], "guide": ["usher",None]}

def test_first_dict_is_empty():
    t1 = {}
    t2 = {
        'kind':'averse',
        'anger':'delight',
        'studious':'idle',
        'manual':'follow',
        'leak':'jam'
        }
    assert left_join(t1, t2) == {}

def test_2_dict_is_empty(sample_dict):
    t1 = sample_dict
    t2 = {}
    assert left_join(t1, t2) == {"fond": ["enamored",None], "wrath": ["anger",None], "diligent": ["employed",None], "outfit": ["garb",None], "guide": ["usher",None]}
    