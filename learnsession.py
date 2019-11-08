import json
from lschallenge import DuolingoLearnSessionChallenge
from web_request import DuolingoReadData
from collections import namedtuple

class DuolingoLearnSession(object):
    def __init__(self, jsonResponseData):
        self.learnSessionData = jsonResponseData
        self.learnSessionMetaData = self.learnSessionData["metadata"]
        self.learnSessionChallengeList = self.learnSessionData["challenges"]

        self.currentLanguage = self.learnSessionMetaData["language_string"]

    def getChallenge(self, index):
        challenge = DuolingoLearnSessionChallenge(self.learnSessionChallengeList[0])
        return challenge


if __name__ == '__main__':
    from pprint import pprint

    data = DuolingoReadData()
    ls = DuolingoLearnSession(json.loads(data.getData()))
    print("Frage 1:")
    pprint(ls.getChallenge(0).getSourcePrompt())
    print("Antwortmoeglichkeiten:")
    pprint(ls.getChallenge(0).getCorrectSolutions())