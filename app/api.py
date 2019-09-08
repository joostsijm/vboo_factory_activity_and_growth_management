"""API module"""

import re
from datetime import datetime, date, timedelta

import requests
from bs4 import BeautifulSoup

from app import BASE_URL, HEADERS


TYPES = {
    'yellow': 1,
    'oil': 2,
    'ore': 5,
    'uranium': 11,
    'diamond': 15,
}

def get_factories(state_id):
    """Get factories from state"""
    return read_factories()
    # return download_factories(state_id)

def read_factories():
    """Read factories file"""
    with open('factories.html') as file:
        factories, more = parse_factories(file)
        return factories

def download_factories(state_id):
    """Download the factories"""
    factories = []
    more = True
    page = 0
    while more:
        response = requests.get(
            '{}factory/state/{}/0/0/{}'.format(BASE_URL, state_id, page*25),
            headers=HEADERS
        )
        tmp_factories, more = parse_factories(response.text)
        factories = factories + tmp_factories
        page += 1
    return factories

def parse_factories(html):
    """Parse html return factories"""
    soup = BeautifulSoup(html, 'html.parser')
    factories_tree = soup.find_all(class_='list_link')
    factories = []
    for factory_tree in factories_tree:
        columns = factory_tree.find_all('td')
        factories.append({
            'id': factory_tree['user'],
            'name': columns[1].contents[0].strip(),
            'resource_type': TYPES[columns[1].contents[4]['class'][0]],
            'region_name': columns[1].contents[2],
            'level': columns[2].string,
            'workers': re.sub(r'\/[0-9]*$', '', columns[3].string),
            'wage': int(columns[4].string.replace('%', '')),
            'experience': int(columns[5].string),
        })
    return factories, bool(len(factories_tree) >= 25)

def parse_date(date_string):
    """Parse date to object"""
    if 'Today' in date_string:
        return date.today()
    if 'Yesterday' in date_string:
        return date.today() - timedelta(1)
    return datetime.strptime(date_string, '%d %B %Y').date()
