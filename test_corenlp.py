from nlplogic.corenlp import search_wikipedia,summary_wikepedia,get_text_blob,get_phrases

def test_get_phrases():
    assert 'golden state' in get_phrases("golden state warriors")