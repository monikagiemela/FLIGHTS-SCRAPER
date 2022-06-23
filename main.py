from Flight_Scrapers.LaxJfk import LaxJfk
from Flight_Scrapers.LgaOrd import LgaOrd
from Flight_Scrapers.DfwOrd import DfwOrd
#from AtlMco import AtlMco

from apscheduler.schedulers.blocking import BlockingScheduler
import logging


logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

sched = BlockingScheduler(timezone="Europe/Berlin")
print("Initializing CRON Schedular.... ")

@sched.scheduled_job("cron", day_of_week="sat", hour=20, minute=00)
def scheduled_job():
    lax_jfk = LaxJfk()
    lax_jfk.execute()
    

@sched.scheduled_job("cron", day_of_week="tue", hour=20, minute=00)
def scheduled_job():
    lga_ord = LgaOrd()
    lga_ord.execute()

@sched.scheduled_job("cron", day_of_week="tue", hour=20, minute=15)
def scheduled_job():
    dfw_ord = DfwOrd()
    dfw_ord.execute()

#atl_mco = AtlMco()
#atl_mco.execute()

sched.start()