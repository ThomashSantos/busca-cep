from datetime import datetime
import logging
import os


date_now = datetime.today()
date_log = date_now.strftime("%Y_%m_%d")
os.makedirs('buscacep/data/log', exist_ok=True)
log_format = '%(asctime)s - %(levelname)s: %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO, filename=f'buscacep/data/log/Log_{date_log}.log', datefmt="%H:%M:%S")
logging.debug('Start proccess...')
