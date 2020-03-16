import logging

from fastapi import FastAPI

from rcsb.utils.chem.ChemCompSearchWrapper import ChemCompSearchWrapper

from . import descriptorMatch
from . import formulaMatch

# ---
logger = logging.getLogger("app_chem")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s:     %(asctime)s-%(module)s.%(funcName)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
# ---

app = FastAPI()


@app.on_event("startup")
async def startupEvent():
    logger.info("Startup - loading dependencies")
    ccsw = ChemCompSearchWrapper()
    ok1 = ccsw.readConfig()
    ok2 = ccsw.updateChemCompIndex(useCache=True)
    ok3 = ccsw.reloadSearchDatabase()
    logger.info("Completed - loading dependcies status %r", ok1 and ok2 and ok3)


@app.on_event("shutdown")
def shutdownEvent():
    logger.info("Shutdown - application ended")


@app.get("/")
def readRoot():
    return {"msg": "Sevice is up!"}


app.include_router(
    formulaMatch.router, prefix="/chem-match-v1",
)

app.include_router(
    descriptorMatch.router, prefix="/chem-match-v1",
)
