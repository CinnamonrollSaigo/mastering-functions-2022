from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    """search"""
    print(f"searching for name:{name}")
    return wikipedia.search(name)


def summary_wikipedia(name):
    """summary"""
    print(f"summary for name:{name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """get text blob"""
    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """wikipedia"""
    # text = summary_wikipedia(name)
    # blob = get_text_blob(text)
    # phrases = blob.noun_phrases
    return name