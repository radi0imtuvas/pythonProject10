import math
import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('uzduotis.log')
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# logging.basicConfig(filemode='uzduotis.log', level= logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


def sumavimas(*args):
    ats = sum(*args)
    logger.info(f"Skaiciu {args} suma lygi: {ats}")
    return ats


def saknis(a):
    try:
        rezas = math.sqrt(a)
    except TypeError:
        logger.exception("Ivestas tekstas")
    else:
        logger.info(f"Skaiciaus {a} saknis: {rezas}")
        return rezas

def sakinio_ilgis(sakinys):
    logger.info(f"Sakinio {sakinys} ilgis: {len(sakinys)}")
    return len(sakinys)

def dalyba(x, y):
    try:
        rezultatas = x / y
    except ZeroDivisionError:
        logger.exception("Dalyba is nulio")
    else:
        logger.info(f"Dalyba: {x} / {y} = {padalinom}")
        return rezultatas

skaiciai = (1, 2, 6)
sumavimas(skaiciai)


a = "namas"
saknis(a)


sakinys = "batai buvo du"
sakinio_ilgis(sakinys)


x=10
y=5
padalinom = dalyba(x, y)
