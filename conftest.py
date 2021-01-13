from fixture.load_dll import DllHelper
from model.input_data import *
import pytest



@pytest.fixture
def fix_alarm_zone(request):
    fix_alarm = DllHelper()
    fix_alarm.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">,parent_id<" + slave + ">,name<" + grabber_name + ">,type<ISS Video Concentrator>,model<default>").encode("utf-8"))
    fix_alarm.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id + ">,parent_id<" + cam_id + ">,name<" + cam_name + ">").encode("utf-8"))
    fix_alarm.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id2 + ">,parent_id<" + slave + ">,name<" + grabber_name2 + ">,type<Virtual>,model<default>,chan<1>").encode("utf-8"))
    fix_alarm.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id2 + ">,parent_id<" + cam_id2 + ">,name<" + cam_name2 + ">,,mux<0>").encode("utf-8"))
    def fin():
        fix_alarm.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">").encode("utf-8"))
        fix_alarm.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id2 + ">").encode("utf-8"))
        #print('\nSome resource fin')
    request.addfinalizer(fin)
    return fix_alarm

@pytest.fixture
def fix_information_zone(request):
    fix_information_zone = DllHelper()
    fix_information_zone.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id2 + ">,parent_id<" + slave + ">,name<" + grabber_name2 + ">,type<Virtual>,model<default>,chan<1>").encode("utf-8"))
    fix_information_zone.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id2 + ">,parent_id<" + cam_id2 + ">,name<" + cam_name2 + ">,,mux<0>").encode("utf-8"))
    def fin():
        fix_information_zone.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id2 + ">").encode("utf-8"))
        #print('\nSome resource fin')
    request.addfinalizer(fin)
    return fix_information_zone