"""Database module"""

from datetime import datetime

from app import Session
from app.models import State, Player, Factory, FactoryTrack, FactoryStat


def get_state(state_id):
    """Get regions from state"""
    session = Session()
    state = session.query(State).get(state_id)
    session.close()
    return state

def save_factories(state_id, factories):
    """Save factories to database"""
    session = Session()
    session.close()

    factory_track = FactoryTrack()
    factory_track.state_id = state_id
    factory_track.date_time = datetime.now()
    session.add(factory_track)

    for factory_dict in factories:
        factory = session.query(Factory).get(factory_dict['id'])
        if factory is None:
            factory = save_factory(session, factory_dict)
        factory_stat = FactoryStat()
        factory_stat.level = factory_dict['level']
        factory_stat.experience = factory_dict['experience']
        factory_stat.wage = factory_dict['wage']
        factory_stat.workers = factory_dict['workers']
        factory_stat.factory_id = factory_dict['id']
        factory_stat.factory_track_id = factory_track.id
        session.add(factory_stat)

    session.commit()
    session.close()


def save_factory(session, factory_dict):
    """Save factory to database"""
    factory = Factory()
    factory.id = factory_dict['id']
    factory.name = factory_dict['name']
    factory.resource_type = factory_dict['resource_type']
    session.add(factory)
    return factory
