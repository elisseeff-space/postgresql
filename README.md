# postgresql

https://computingforgeeks.com/how-to-install-dbeaver-on-debian/

/home/pavel/.postgresql/root.crt   100%[================================================================>]   3.50K  --.-KB/s    in 0s      

2023-12-30 18:59:07 (68.4 MB/s) - ‘/home/pavel/.postgresql/root.crt’ saved [3579/3579]


psql "host=rc1b-xce87o99p8kvstxo.mdb.yandexcloud.net \
      port=6432 \
      sslmode=verify-full \
      dbname=db1 \
      user=elisseeff \
      target_session_attrs=read-write"

pip install asyncpg
