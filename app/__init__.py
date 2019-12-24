"""Fabriek Activiteit en Groei Beheer"""

import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

from app.models import Base, State, Region, Player


load_dotenv()

# database
ENGINE = create_engine(os.environ["DATABASE_URI"], client_encoding='utf8')
SESSION = sessionmaker(bind=ENGINE)

# scheduler
SCHEDULER = BackgroundScheduler(
    daemon=True,
    job_defaults={
        'misfire_grace_time': 900
    },
)
SCHEDULER.start()

# logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

# api
BASE_URL = os.environ["API_URL"]
HEADERS = {
    'Authorization': os.environ["AUTHORIZATION"]
}
