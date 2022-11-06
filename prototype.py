# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pityna
    
def prompt(obj):
    return obj.get_name() + ':' + obj.get_responder_name() + '>'

print('Pityna System prototype : Pityna')
pityna = pityna.Pityna('Pityna')

while True:
    inputs = input(' > ')
    if not inputs:
        print('バイバイ')
        break
    response = pityna.dialogue(inputs)
    print(prompt(pityna), response)