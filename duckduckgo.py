import pytest
import requests

def test_presidents_in_response():
    url_ddg = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'
    response = requests.get(url_ddg)
    ddg_data = response.json()
    related_topics = ddg_data['RelatedTopics']
    presidents = [
        'Washington',
        'Adams',
        'Jefferson',
        'Madison',
        'Monroe',
        'Jackson',
        'Van Buren',
        'Harrison',
        'Tyler',
        'Polk',
        'Taylor',
        'Fillmore',
        'Pierce',
        'Buchanan',
        'Lincoln',
        'Johnson',
        'Grant',
        'Hayes',
        'Garfield',
        'Arthur',
        'Cleveland',
        'Harrison',
        'McKinley',
        'Roosevelt',
        'Taft',
        'Wilson',
        'Harding',
        'Coolidge',
        'Hoover',
        'Roosevelt',
        'Truman',
        'Eisenhower',
        'Kennedy',
        'Johnson',
        'Nixon',
        'Ford',
        'Carter',
        'Reagan',
        'Bush',
        'Clinton',
        'Bush',
        'Obama',
        'Trump'
    ]
    for topic in related_topics:
        if topic['Text'] in presidents:
            presidents.remove(topic['Text'])

