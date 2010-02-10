import os
from simplersa import rsa

from __PROJECT_NAME__.settings import PROJECT_ROOT

DEBUG = False

DATABASE_ENGINE = 'mysql'
DATABASE_HOST = 'mysqlhacloudmastervip.pbs.org'
DATABASE_NAME = '__PROJECT_NAME__'
DATABASE_USER = '__PROJECT_NAME__'
DATABASE_PASSWORD = rsa.decrypt('UCYGq9FkxE0JL9v9D7peaOMzmBmqkyfUjBy6rENB/01FT8XP20mWw2R9uOQUcvwc2xHmz8zDbFYtZ/e2ZkHgEg5N2yXpYUaxZ+tsRgIvrIJw1CjatMozNopZsu/HrGkb1FX0At4gOVn4rr89UbHoI0qbHOyzP9C07mfZeeyExhDZJiIm00pj54WJ/ABbR/gz8w724gnM0x6820HdLZsujaC1/IpcuIuQxNqWXOKz1ZdngyQU35Iblnt2A22cw7FD4T8mdSrm6DeG96Vv1/FGaT04eaMsQNaFl7cLc/5BwtW1QeXeYvsXxr9JjBLt92w1oDjFrxP6xLmWWWF21RltRg==', key='www')
