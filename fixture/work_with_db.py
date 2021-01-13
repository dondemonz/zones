import psycopg2
from psycopg2.extras import DictCursor
from model.input_data import *
import time


class DbHelper:

    def __init__(self, host="localhost", dbname=None, user="postgres", password="postgres", records=None, edge_template=None, action=None):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.records = records
        self.edge_template = edge_template
        self.action = action
        self.connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        self.connection.autocommit = True

    def check_alarm_zone_exists(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_alarm_zone_no_exists(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id,))
                self.records = cursor.fetchall()
                assert self.records == []
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_alarm_exists_in_db(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "md2_macro_alarms" WHERE cam_id =%s', (cam_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_alarm_not_in_db(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "md2_macro_alarms" WHERE cam_id =%s', (cam_id2,))
                self.records = cursor.fetchall()
                assert self.records == None or self.records == []
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_smart_search_alarm_not_in_db(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "md2_alarms"')
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_alarm_zone_type(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #при создании зоны с данным типом там пусто (в ответе отображается как None), но если выставить любой другой тип, а затем вернуть то уже будет 0
                assert self.records[0][10] == [] or self.records[0][11] == 0 or self.records[0][10] == None
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_blackened_zone_type(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #при создании зоны с данным типом там пусто (в ответе отображается как None), но если выставить любой другой тип, а затем вернуть то уже будет 0
                assert self.records[0][10] == 1
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_information_zone_type(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #при создании зоны с данным типом там пусто (в ответе отображается как None), но если выставить любой другой тип, а затем вернуть то уже будет 0
                assert self.records[0][10] == 2
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_armed_always_on(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #при создании зоны с данным типом там пусто (в ответе отображается как None), но если выставить любой другой тип, а затем вернуть то уже будет 0
                assert self.records[0][9] == 1
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_armed_always_off(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #при создании зоны с данным типом там пусто (в ответе отображается как None), но если выставить любой другой тип, а затем вернуть то уже будет 0
                assert self.records[0][9] == 0
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_smart_search_off(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #при создании зоны с данным типом там пусто (в ответе отображается как None), но если выставить любой другой тип, а затем вернуть то уже будет 0
                assert self.records[0][11] == [] or self.records[0][11] == 0 or self.records[0][11] == None
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def check_smart_search_on(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_ZONE" WHERE id =%s', (zone_id2,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #при создании зоны с данным типом там пусто (в ответе отображается как None), но если выставить любой другой тип, а затем вернуть то уже будет 0
                assert self.records[0][11] == 1
                #print("records", self.records)
        cursor.close()
        #чистим переменную для следующего запроса
        self.records.clear()
        return conn

    def clean_fsindex_db(self):
        with self.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM "md2_macro_alarms"')
                conn.commit()
        cursor.close()

    def clean_fsindex_smart_search(self):
        with self.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM "md2_alarms"')
                conn.commit()
        cursor.close()

    def close_connection(self):
        self.connection.close()
        print("close")




