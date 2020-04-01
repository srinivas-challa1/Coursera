import requests
import json


def get_relatedWords(word, input):
    baseurl = "https://api.datamuse.com/words"
    params_dict = {}
    params_dict['ml'] = word
    params_dict['max'] = input
    response = requests.get(baseurl, params_dict)
    wordList = response.json()
    return([wordDict['word'] for wordDict in wordList])


if __name__ == "__main__":
    print(get_relatedWords(input(), input()))
