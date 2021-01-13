from model.input_data import *
from fixture.work_with_db import DbHelper
import time

def test_check_zones(fix_alarm_zone):
    # учитывая, что зона хранится только с объектом, таблицу obj_cam_zone в данном случае чистить не надо
    # в конце теста чистится только fs_index, так как OBJ_CAM_ZONE из бд securos чистится после удаления объекта фикстуры
    db = DbHelper(dbname="securos")
    db.check_alarm_zone_exists()
    db.check_alarm_zone_type()
    db.check_alarm_zone_no_exists()
    db1 = DbHelper(dbname="fsindex")
    db1.clean_fsindex_db()
    fix_alarm_zone.send_react(("MEDIA_CLIENT|1|ADD_SEQUENCE|mode<1x1>,seq<|" + cam_id2 + ">").encode("UTF-8"))
    fix_alarm_zone.send_react(("CAM|" + cam_id2 + "|ARM").encode("UTF-8"))
    time.sleep(8)
    fix_alarm_zone.send_react(("CAM|" + cam_id2 + "|DISARM").encode("UTF-8"))
    db1.check_alarm_exists_in_db()
    db.check_armed_always_off()
    fix_alarm_zone.send_event(("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<" + zone_id2 + ">,armed_always<1>").encode("UTF-8"))
    db.check_armed_always_on()
    fix_alarm_zone.send_event(("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<" + zone_id2 + ">,blackened<1>").encode("UTF-8"))
    db.check_blackened_zone_type()
    fix_alarm_zone.send_event(("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<" + zone_id2 + ">,blackened<2>").encode("UTF-8"))
    db.check_information_zone_type()
    db.check_smart_search_off()
    fix_alarm_zone.send_event(("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<" + zone_id2 + ">,blackened<0>").encode("UTF-8"))
    fix_alarm_zone.send_event(("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<" + zone_id2 + ">,smart_search<1>").encode("UTF-8"))
    db.check_smart_search_on()
    db1.clean_fsindex_db()
    time.sleep(1)

def test_check_information_zone_works(fix_information_zone):
    db1 = DbHelper(dbname="fsindex")
    db1.clean_fsindex_db()
    fix_information_zone.send_react(("MEDIA_CLIENT|1|ADD_SEQUENCE|mode<1x1>,seq<|" + cam_id2 + ">").encode("UTF-8"))
    fix_information_zone.send_event(("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<" + zone_id2 + ">,blackened<2>").encode("UTF-8"))
    fix_information_zone.send_react(("CAM|" + cam_id2 + "|ARM").encode("UTF-8"))
    time.sleep(8)
    fix_information_zone.send_react(("CAM|" + cam_id2 + "|DISARM").encode("UTF-8"))
    db1.check_alarm_not_in_db()
    time.sleep(1)

def test_check_blackened_zone_works(fix_information_zone):
    db1 = DbHelper(dbname="fsindex")
    db1.clean_fsindex_db()
    fix_information_zone.send_react(("MEDIA_CLIENT|1|ADD_SEQUENCE|mode<1x1>,seq<|" + cam_id2 + ">").encode("UTF-8"))
    fix_information_zone.send_event(("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<" + zone_id2 + ">,blackened<1>").encode("UTF-8"))
    fix_information_zone.send_react(("CAM|" + cam_id2 + "|ARM").encode("UTF-8"))
    time.sleep(8)
    fix_information_zone.send_react(("CAM|" + cam_id2 + "|DISARM").encode("UTF-8"))
    db1.check_alarm_not_in_db()
    time.sleep(1)

def test_check_smart_search_works(fix_information_zone):
    db1 = DbHelper(dbname="fsindex")
    db1.clean_fsindex_smart_search()
    fix_information_zone.send_react(("MEDIA_CLIENT|1|ADD_SEQUENCE|mode<1x1>,seq<|" + cam_id2 + ">").encode("UTF-8"))
    fix_information_zone.send_event(("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<" + zone_id2 + ">,smart_search<1>").encode("UTF-8"))
    fix_information_zone.send_react(("CAM|" + cam_id2 + "|ARM").encode("UTF-8"))
    time.sleep(8)
    fix_information_zone.send_react(("CAM|" + cam_id2 + "|DISARM").encode("UTF-8"))
    db1.check_smart_search_alarm_not_in_db()
    time.sleep(1)