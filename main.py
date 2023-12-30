import asyncio
import asyncpg
from config_postgre import ConfigBox

async def run():
    ConfigBox.set_logger_name('postgre')
    
    conn = await asyncpg.connect(user='elisseeff', password='elisseeff',
                                 database='db1', host='rc1b-xce87o99p8kvstxo.mdb.yandexcloud.net', port=6432)
    #values = await conn.fetch(
    #    'SELECT * FROM films;'
    #)
    #print(values)

    
    # Check if Table catalogs_control exists
    select_query = "SELECT * from tblDict_497;"
    ConfigBox.cur.execute(select_query)
    res = ConfigBox.cur.fetchall()

    for _ in res:
        insert_query = f"insert into tbldict_497 values ({_[0]}, '{_[2]}', '{_[3]}', {_[1]});"
        #print(insert_query)
        #input()
        try :
            await conn.execute(insert_query)
        except Exception as e :
            ConfigBox.logger.error(f"{insert_query}: {e}")
        #await conn.commit()
        
    
    await conn.close()

if __name__ == '__main__':
    print("Hello!")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())