"""Main app"""

import time

from app import scheduler, LOGGER
from app.api import get_factories
from app.database import get_state, save_factories


def print_factories(factories):
    """Print professors"""
    for factory in factories:
        print('{:30} {:24} {:2} {:3} {:3}'.format(
            factory['name'],
            factory['region_name'],
            factory['resource_type'],
            factory['level'],
            factory['workers'],
        ))

def job_update_factories(state_id):
    """Update factories"""
    LOGGER.info('Run update factories for state "%s"', state_id)
    state = get_state(state_id)
    LOGGER.info('"%s": get factories', state.name)
    factories = get_factories(state.id)
    LOGGER.info('"%s": "%s" factories', state.name, len(factories))
    print_factories(factories)
    save_factories(state.id, factories)
    LOGGER.info('"%s": done saving factories', state.name)


def add_update_factories(state_id):
    """Add jobs"""
    scheduler.add_job(
        job_update_factories,
        'cron',
        args=[state_id],
        id='factories_{}'.format(state_id),
        replace_existing=True,
        hour='2'
    )

if __name__ == '__main__':
    # jobs
    job_update_factories(2788)

    # Verenigde Nederlanden
    add_update_factories(2788)
    # Belgium
    add_update_factories(2604)
    # De Provincien
    add_update_factories(2620)

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        LOGGER.info('Exiting application')
        exit()
