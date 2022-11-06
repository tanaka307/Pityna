# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import responder
import random
import dictionary

class Pityna(object):
    def __init__(self, name):
        self.name = name
        self.dictionary = dictionary.Dictionary()
        self.emotion = Emotion(self.dictionary.pattern)
        self.res_random = responder.RandomResponder('Random',self.dictionary.random)
        self.res_repeat = responder.RepeatResponder('Repeat?')
        self.res_pattern = responder.PatternResponder('Pattern', self.dictionary)
        
    def dialogue(self, input):
        self.emotion.update(input)
        x = random.randint(1, 100)
        if x <= 60:
            self.responder = self.res_pattern
        elif 61 <= x <= 90:
            self.responder = self.res_random
        else:
            self.responder = self.res_repeat
            
        resp = self.responder.response(input, self.emotion.mood)
        self.dictionary.study(input)
        return resp
    
    def save(self):
        self.dictionary.save()
    
    def get_responder_name(self):
        return self.responder.name
    
    def get_name(self):
        return self.name
    
class Emotion:
    MOOD_MIN = -15
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5
    
    def __init__(self, pattern):
        self.pattern = pattern
        self.mood = 0
        
    def update(self, input):
        if self.mood < 0:
            self.mood += Emotion.MOOD_RECOVERY
        elif self.mood > 0:
            self.mood -= Emotion.MOOD_RECOVERY
            
        for ptn_item in self.pattern:
            if ptn_item.match(input):
                self.adjust_mood(ptn_item.modify)
                break
        
    def adjust_mood(self, val):
        self.mood += int(val)
        if self.mood > Emotion.MOOD_MAX:
            self.mood = Emotion.MOOD_MAX
        elif self.mood < Emotion.MOOD_MIN:
            self.mood = Emotion.MOOD_MIN
    