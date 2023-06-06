from nlplogic.corenlp import get_phrases


def test_get_phrases():
    """test"""
    assert 'golden state' in get_phrases("golden state warriors")