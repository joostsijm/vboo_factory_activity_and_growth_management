"""Database module"""

from datetime import datetime

from app import session
from app.models import State, Player


def get_state(state_id):
    """Get regions from state"""
    return session.query(State).get(state_id)

def save_factories(factories):
    """Save factories to database"""
    return
