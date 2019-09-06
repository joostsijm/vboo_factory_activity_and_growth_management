"""API module"""

import re
from datetime import datetime, date, timedelta

import requests
from bs4 import BeautifulSoup

from app import BASE_URL, HEADERS


def get_factories(state_id):
    """Get factories from state"""
    return download_factories(state_id)

def download_factories(state_id):
    """Download the players"""
    return []

def parse_factories(html):
    """Parse html return factories"""
    soup = BeautifulSoup(html, 'html.parser')
    factories_tree = soup.find_all(class_='list_link')
    factories = []
    return factories

def parse_date(date_string):
    """Parse date to object"""
    if 'Today' in date_string:
        return date.today()
    if 'Yesterday' in date_string:
        return date.today() - timedelta(1)
    return datetime.strptime(date_string, '%d %B %Y').date()
