from selenium.webdriver.common.action_chains import ActionChains
from optparse import OptionParser
from selenium import webdriver
import pandas as pd
import time
import sys
import re

pattern_name = "\\n(.+)\\n"
pattern_headline = 'occupation\\n(.+)\\n'
usage="""
<Script> [Options]
[Options]
-h,--help show this help message and exit.
-e,--email Enter login email
-p,--password Enter login password
-s,--skills Flag to scrap each profile, and look at its skill set

operation Modes:
    >Basic mode
    This will scrap all LinkedIn connections list with threre corresponding Name,Headline,and Profile link.
    >Skills scrapper mode(-s/--skills)
    (Time Consuming mode)
    This will do the same job of basic mode but along with visiting each profile and extacting the skills of each.
"""
