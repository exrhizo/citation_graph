#! /usr/bin/env python
"""
This module uses and extends scholar.py to scrape results
from google scholar to determine the authors, citations,
and title of a paper given a list of possible titles.
"""


#from difflib import get_close_matches
#get_close_matches(word, possibilities[, n][, cutoff])
from scholar import ScholarQuerier
from user_agents import USER_AGENTS
from jellyfish import levenshtein_distance as str_metric
from time import sleep
import random


def find_article(canidates):
    """
    A function that attempts to find a good match
    from scholar.py for a set of canidate paper
    titles, it returns the best result.
    """
    canidate_scores = [5000 for dummy in canidates]
    canidate_best_match = ['' for dummy in canidates]
    querier = ScholarQuerier()
    delay = 0
    for ii, canidate in enumerate(canidates):
        sleep(delay)
        querier.UA = random.choice(USER_AGENTS)
        querier.query(canidate)
        for art in querier.articles:
            title = art['title'].encode('ascii', 'ignore')
            score = str_metric(canidate, 
                title)/max(len(title),len(canidate))
            if score < canidate_scores[ii]:
                canidate_scores[ii] = score
                canidate_best_match[ii] = art
        print '----------------------'
        print 'Canidate: '+canidate
        print 'Match:    '+ \
                   canidate_best_match[ii]['title'].encode('ascii', 'ignore')
        print 'Score     '+str(canidate_scores[ii])
        querier.clear_articles()
        delay = max(random.gauss(30, 30), 5)

def main():
    """
    Main function, used to test module.
    """
    test_canidates = ['Polymer 45 (2004) 573579',
        'www.elsevier.com/locate/polymer',
        'Thermal denaturation and folding rates of single domain proteins:',
        'size matters']
    find_article(test_canidates)

if __name__ == "__main__":
    main()
