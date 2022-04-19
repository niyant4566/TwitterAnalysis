# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:49:18 2021

@author: niyan
"""

import re

tweets = open("10000 tweets.json", "r", encoding="utf-8")
newtweets = open("fixedjson.json", "w",encoding="utf-8")

for l in tweets.readlines():
    if re.match(r'\s+[\{\}\[\]\,]\s*',l):
        newtweets.write(l)
    elif l.startswith("    \"_id\"") or l.startswith("/*"):
        pass
    elif l.strip().startswith("\"verified\""):
        newtweets.write(l)
    elif re.match(r'.*\:\s*[A-Za-z]+.*', l) is not None:
        pass
    else:
        newtweets.write(l)
        
newtweets.close()
tweets.close()