import json, os
import logging
import sqlite3 as sq
from enum import Enum

class postgreConfig():
    #activ_catalogs = (3699, 3732, 3733, 4363, 4364, 4365, 4374, 4375, 4376, 4412, 4415, 4416)
    #StepQuantity = 878
    logger = logging.getLogger(__name__)
    # настройка обработчика и форматировщика для logger
    if os.name == 'posix': 
        file_name = "/home/pavel/github/postgresql/log/postgresql.log"
    elif os.name == 'nt':
        file_name = r'C:\Users\Eliseev\GitHub\postgresql\log\postgresql.log'
    else: raise ValueError("Unsupported operating system")

    handler = logging.FileHandler(file_name, mode='w')
    #formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s", datefmt='%Y/%m/%d %I:%M:%S')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s", datefmt='%Y/%m/%d %H:%M:%S')

    def __init__(self) -> None:
        
        # Set up logger
        # self.logging #.info('Verify successfully init!')
        
        self.logger.setLevel(logging.INFO)
        
        # добавление форматировщика к обработчику
        self.handler.setFormatter(self.formatter)
        # добавление обработчика к логгеру
        self.logger.addHandler(self.handler)

        if os.name == 'posix': filename = "/home/pavel/github/postgresql/db/dict.db"
        elif os.name == 'nt': filename = str(r'C:\Users\Eliseev\GitHub\postgresql\db\dict.db')
        else: raise ValueError("Unsupported operating system")
        self.dbase = sq.connect(filename)
        self.cur = self.dbase.cursor()

        if os.name == 'posix': in_file = "/home/pavel/cfg/config.json"
        elif os.name == 'nt': in_file = str(r'C:\Users\Eliseev\GitHub\cfg\config.json')
        else: raise ValueError("Unsupported operating system")
        file = open(in_file, 'r')
        self.config = json.load(file)

    @classmethod
    def set_logger_name(self, logger_name: str)->bool:
        self.logger.name = logger_name

#CatalogType = T_CatalogType()
ConfigBox = postgreConfig()

if __name__ == '__main__':
    print("Hello!")
    
    ConfigBox.logger.warning('New YaGPTConfig successfully init!')
