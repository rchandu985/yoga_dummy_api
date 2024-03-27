import json

from flask import Flask,request
from flask_cors import CORS,cross_origin
from flask_httpauth import HTTPBasicAuth
import mysql.connector

import time
app=Flask(__name__)
CORS(app, origins=["http://localhost:3000","http://localhost:8000",'http://10.80.40.145:8000'],supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'


# MySQL configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '01000011'
MYSQL_DB = 'yoga_broadcast_core'

# Connect to MySQL
db_connection = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

# Create a cursor
cursor = db_connection.cursor(dictionary=True)

auth = HTTPBasicAuth()
@auth.verify_password
def verify_password(username, password):
    """Verify the username and password."""
    
    return username

@app.route('/Auth/GetUserInformation/')
@auth.login_required
def GetUserInformation():
    
    """Protected view."""
    # Get the username from the request
    username = request.authorization.username
    q=f"SELECT first_name,last_name,email,is_superuser FROM auth_user where (username=dev)"
    #print(q)
    cursor.execute("SELECT first_name, last_name, email, is_superuser FROM auth_user WHERE username = %s", (username,))

    users = cursor.fetchone()

    # Convert the result into a list of dictionaries
    users.update({"full_name":users.get("first_name")+" "+users.get("last_name"),"username":username})
    return    {"message": "Successfully Obtained The User User Details","profile":users}



@app.route("/Auth/Login/",methods=['POST'])
def Login():
    return {
    "message": "Successfully Login",
    "login_status": True,
    "user_action_permissions": [
        {
            "permission_name": "DeleteAllSchedules",
            "related": "YBC"
        },
        {
            "permission_name": "DescheduleAudioStream",
            "related": "YBC"
        },
        {
            "permission_name": "DeschedulePrePositionStream",
            "related": "YBC"
        },
        {
            "permission_name": "DescheduleStream",
            "related": "YBC"
        },
        {
            "permission_name": "GetAllAudioStreamInfo",
            "related": "YBC"
        },
        {
            "permission_name": "GetAllOffloadStreamInfo",
            "related": "YBC"
        },
        {
            "permission_name": "GetAllPrePositionStreamInfo",
            "related": "YBC"
        },
        {
            "permission_name": "GetAllStreamInfo",
            "related": "YBC"
        },
        {
            "permission_name": "GetAudioStreamInfo",
            "related": "YBC"
        },
        {
            "permission_name": "GetAvailableSchedulerConfig",
            "related": "YBC"
        },
        {
            "permission_name": "GetCurrentSchedulerConfig",
            "related": "YBC"
        },
        {
            "permission_name": "GetPrePositionStreamInfo",
            "related": "YBC"
        },
        {
            "permission_name": "GetRecommendationList",
            "related": "YBC"
        },
        {
            "permission_name": "GetStreamInfo",
            "related": "YBC"
        },
        {
            "permission_name": "ScheduleAudioStream",
            "related": "YBC"
        },
        {
            "permission_name": "ScheduleOffloadStream",
            "related": "YBC"
        },
        {
            "permission_name": "SchedulePrePositionStream",
            "related": "YBC"
        },
        {
            "permission_name": "ScheduleStream",
            "related": "YBC"
        },
        {
            "permission_name": "SwitchSchedulerConfig",
            "related": "YBC"
        },
        {
            "permission_name": "UpdatePrePositionStream",
            "related": "YBC"
        },
        {
            "permission_name": "UpdateStreamInfo",
            "related": "YBC"
        },
        {
            "permission_name": "YbcRestart",
            "related": "YBC"
        },
        {
            "permission_name": "YbcStart",
            "related": "YBC"
        },
        {
            "permission_name": "YbcStatus",
            "related": "YBC"
        },
        {
            "permission_name": "YbcStop",
            "related": "YBC"
        },
        {
            "permission_name": "PushToDigicaster",
            "related": "Emergency Alerts"
        },
        {
            "permission_name": "AeCheckThreshold",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbCheckOffloadStream",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbCheckThreshold",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbContentUserMapLive",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbContentUsers",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbDelAllOffloadStreams",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbDelAllRecommendations",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbDelAllUeData",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbGetOffloadInfo",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbGetRecommendations",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbGetUeInfo",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbGetVodUeInfo",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbLiveStreamUsers",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbLiveUsers",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbLiveUsersCount",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbPutRecommendations",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbRestart",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbStart",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbStatus",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbStop",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbUeWithinBrh",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeDbUniqueUe",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeGetContentDetails",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeGetDefaultTime",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeGetThreshold",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeOffloadReset",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeOffloadStatus",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeRestart",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeSetThreshold",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeSetTriggerTime",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeStart",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeStatus",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeStop",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "AeTriggerEngine",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "GetEmergencyAlertsConfigurationData",
            "related": "Emergency Alerts"
        },
        {
            "permission_name": "GetEmergencyAlertsData",
            "related": "Emergency Alerts"
        },
        {
            "permission_name": "test",
            "related": "AnalyticsEngine"
        },
        {
            "permission_name": "DeleteAllAlerts",
            "related": "Emergency Alerts"
        },
        {
            "permission_name": "ReadDeviceRfAllInputSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "GetAboutDevice",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "GetDeviceAllInputSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "GetDeviceAllOutputParameetersData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadAsi1OutputConfigurationData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadAsi2OutputConfigurationData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadAsiAllInputSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadAllInputMoipSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadMoip1OutputConfigurationData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadMoip1OutputStreamConfigurationData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadMoip2OutputConfigurationData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadMoip2OutputStreamConfigurationData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadMoipSrcfiltersAllInputSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadMoipSourceSelectionAllInputSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadAbrAllInputSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadZixiAllInputSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadSrtAllInputSettingsData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "GetAllPeInformation",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ReadControlDeBissConditionalAccessodersAllConigurationData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "module_name",
            "related": "YBC"
        },
        {
            "permission_name": "ConfigureRFPorts",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigureAsi",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigureMoip",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigureMoipSrcFilter",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigureMoipSourceSelection",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigureAbr",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigureZixi",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigureSrt",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigurePe",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "AccessAllDecodersConfigurationData",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "ConfigureDecoders",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "Backup",
            "related": "IRD-Synamedia"
        },
        {
            "permission_name": "BrhStastics",
            "related": "Brh"
        }
    ],
    "user_navbar_permissions": [
        "IRD-Synamedia",
        "Brh",
        "AnalyticsEngine",
        "Emergency Alerts",
        "YBC"
    ],
    "is_superuser": True
}

@app.route('/Ybc/Start/',methods=['GET'])
def ybc_start():
    time.sleep(5)
    all_ready_started=True
    if not all_ready_started:
        return {"success": True,"message": " YBC started successfully ","data": {}}
    else:
        return {"success": False,"message": " YBC is already running ","error_code": 1001,"data": {}}

@app.route('/Ybc/Stop/',methods=['GET'])
def ybc_stop():
    processing=True
    streaming=True
    ybc_status=True
    if ybc_status:
        if processing:
            return {
                        "success": True,
                        "message": "YBC stopped successfully ",
                        "data": {}
                        }
        else:
            if streaming:
                return {
                        "success": False,
                        "message": "Unable to stop the Ybc since the stream is streaming state ",
                        "error_code": 1002,
                        "data": {}
                        }
            else:
                return {"success": False,
                    "message": "Unable to stop the Ybc since the stream is processing ",
                    "error_code": 1002,
                    "data": {}
                    }
    else:
        return {
                "success": False,
                "message": " YBC has not started yet ",
                "error_code": 1000,
                "data": {}
                }

@app.route('/Ybc/YbcRestart/',methods=['GET'])
def ybc_restart():

    streams_processing=False
    streams_are_in_streaming=False

    if not streams_processing:
        return {
                    "success": True,
                    "message": " YBC restarted successfully ",
                    "data": {}
                    }
    else:
        return {
                "success": False,
                "message": "Unable to stop the Ybc since the stream is processing ",
                "error_code": 1002,
                "data": {}
                }

    """if streams_are_in_streaming:
        return {
            "success": False,
            "message": "Unable to stop the Ybc since the stream is streaming state ",
            "error_code": 1002,
            "data": {}
            }
"""
"""
        Ybc restart error
        return {
    "success": False,
    "message": " Unable to restart the YBC ",
    "error_code": 1004,
    "data": {}
    }
    """

@app.route("/Ybc/Status/",methods=['GET'])
def ybc_instance_active():
    status=True
    if status:
        return {
"success": True,
"message": " YBC is running ",
"data": {"version": "1.0.0"}
}
    else:
        return {
"success": False,
"message": " YBC is not running ",
"data": {}
}

#Get Current Scheduler Configuration
s=['abc']
@app.route('/Ybc/GetCurrentSchedulerConfig/',methods=['GET'])
def getCurrentSchedulerConfig():
    status=True
    if status:
        return {
                "success": True,
                "message": " Successfully obtained the current scheduler configuration ",
                "data":{
                "channel_bandwidth" : s[0],
                "mod_type" : "QPSK",
                "code_rate" : "9_15",
                "maximum_bandwidth" : 5397964 ,
                "current_bw_usage" : 3416520 ,
                "digicaster_ip" : " 192.168.22.238 ",
                }}
    else:
        return {
            "success": False,
            "message": " YBC has not started yet ",
            "error_code": 1000,
            "data": {}
            }

#Get Available Scheduler Configuration

@app.route('/Ybc/GetAvailableSchedulerConfig/',methods=['GET'])
def Get_Available_Scheduler_Configuration():
    success=True

    if success:
        return {
                    "success": True,
                    "message": " Successfully obtained the available scheduler configurations ",
                    "data": ["DIGI_CONFIG_8MHz_5Mbps",
                    "DIGI_CONFIG_8MHz_10Mbps",
                    "DIGI_CONFIG_8MHz_13Mbps"]*5
                    }
    else:
        return {
                "success": False,
                "message": " Cannot update the configuration when a service is either scheduled or soon to be scheduled. ",
                "error_code": 1500,
                "data": {}
                }
@app.route('/Ybc/SwitchSchedulerConfig/',methods=['POST'])
def Switch_Scheduler_Configuration():
    data=request.json
    #print(data)
    resp=True
    time.sleep(5)
    if resp:
        s.pop()
        s.append(data['scheduler_config'])
        return {
"success": True,
"message": " Successfully updated the scheduler configuration ",
"data": {}
}
    else:
        #Invalid Scheduler Configuration
        return {
"success": False,
"message": " Invalid Scheduler Configuration ",
"error_code": 1101,
"data": {}}
"""Scheduler Configuration update failure
{
"success": False,
"message": " Unable to Update Scheduler Configuration ",
"error_code": 1500,
"data": {}
}
"""

@app.route('/Ybc/GetStreamInfo/',methods=['POST'])
def GetStreamInfo():
    return {
"success": True,
"message": " Successfully obtained the stream information by id ",
"data": {
"stream_id": "60c858a5555f247857000032",
"stream_start_time": 1658644800,
" stream_end_time ": 1658646600,
"stream_schedule_duration": 1800,
"stream_name": "DDNewsLive",
"stream_url": "sample_reference_stream_url" ,
"is_stream_live": False ,
"stream_priority": 1,
"stream_video_bitrate": 200000,
"stream_audio_bitrate": "AUDIO_BITRATE_96",
"stream_protocol_type": "mmt",
"service_streaming_status": "STREAMING",
"stream_is_offload": False,
"stream_video_resolution":"VIDEO_FRAME_SIZE_720",
"stream_video_frame_rate": "VIDEO_FRAME_RATE_60"
}
}
sm=[{"stream_id": f"{x}0c858a5555f247857000032","stream_start_time": 1658644800-x,"stream_end_time": 1658646600+x,"stream_schedule_duration": 1800+x,"stream_name": f"DDNewsLive{x}","service_streaming_status": "STREAMING","stream_is_offload": True} for x in range(15)]
@app.route('/Ybc/GetPrePositionStreamInfo/',methods=['GET'])
def getPrePositionStreamInfo():
    return {
            "success": True,
            "message": " Successfully obtained the pre-position stream information by id ",
            "data": {
            "stream_id" : "60c858a5555f2478570000db",
            "stream_start_time" : 1658644800,
            "stream_name" : "Laptop",
            "stream_url" : "sample_reference_stream_url" ,
            "stream_priority" : 4,
            "service_streaming_status" : "STREAMING",
            "content_length" : 35987887,
            "content_bitrate " : 1107319 ,
            "current_transmission_count " : 1 ,
            "total_transmission_count " : 12,
            "current_transmission_percentage " : 48
            }
            }
@app.route('/Ybc/GetAllStreamInfo/',methods=['GET'])
def getAllStreamInfo():

    success=True
    if success:
        return  {
                "success": True,
                "message": " Successfully obtained all the stream information ",
                "data": sm
                }
    else:
        return {
                "success": False,
                    "message": " YBC has not started yet ",
                    "error_code": 1000,
                    "data": {}
                    }


@app.route("/Ybc/GetAllOffloadStreamInfo/",methods=['GET'])
def getAllOffloadStreamInfo():
    return {
"success": True,
"message": " Successfully obtained all the offload stream information ",
"data": [{
"stream_id": f"{x}0c858a5555f247857000032",
"stream_start_time": 1658644800-x,
"stream_end_time": 1658646600+x,
"stream_schedule_duration": 0,
"stream_name": "DDNewsLive",
"service_streaming_status": "STREAMING",
"stream_is_offload": True
} for x in range(15)]}
@app.route('/Ybc/GetRecommendationList/',methods=['GET'])
def getRecommendationList():
    return {"success": True,
"message": " Successfully obtained the recommendation list ",
"data": {
"count" : 2,
"data" : [
{"content_id": f"{x}6171516a555f2413e4000041","start_time": 1638281167+x} for x in range(10)],
"date" : "2021-11-30 09:11:55.450168",
"name" : "Recommended List for offload",
"ver" : " v1.0 "
}
}

@app.route('/Ybc/DescheduleStream/',methods=['GET'])
def deleteStream():
    sm.pop(-1)

    return {
"success": True,
"message": " Successfully deleted the stream ",
"data": {}
}

@app.route('/Ybc/DeleteAllSchedules/',methods=['GET'])
def delete_all_streams():
    sm.clear()
    return {
"success": True,
"message": " Successfully deleted all the streams ",
"data": {}
}

@app.route("/Ybc/ScheduleStream/",methods=['POST'])
def scheduleStream():
    return {
"success" : True,
"message" : " Successfully registered the stream ",
"data" : {}
}
@app.route("/Ybc/ScheduleOffloadStream/",methods=['POST'])
def scheduleOffloadStream():
    return {
                "success" : True,
                "message" : " Successfully registered the stream ",
                "data" : {}
                }
@app.route("/Ybc/UpdateStreamInfo/",methods=['POST'])
def updateStreamInfo():
    #print(request.json)
    return {
            "success" : True,
            "message" : " Successfully updated the stream ",
            "data" : {}}
pp= [
                {
                "stream_id": "60c858a5555f247857000032",
                "stream_start_time": 1658644800,
                "stream_name": "Laptop",
                "current_transmission_count": 1,
                "total_transmission_count": 12 ,
                "current_transmission_percentage": 48,
                "service_streaming_status": "STREAMING"
                }
                ]
@app.route('/Ybc/SchedulePrePositionStream/',methods=['POST'])
def schedulePrePositionStream():
    print(request.json)
    return {
                "success" : True,
                "message" : " Successfully registered the pre-position stream ",
                "data" : {}
                }

@app.route('/Ybc/UpdatePrePositionStream/',methods=['POST'])
def updatePrePositionStream():
    print(request.json)
    return {
            "success" : True,
            "message" : " Successfully updated the stream ",
            "data" : {}
            }

@app.route('/Ybc/GetAllPrePositionStreamInfo/',methods=['GET'])
def getAllPrePositionStreamInfo():

    return {
                "success": True,
                "message": " Successfully obtained all pre-position streams information ",
                "data":pp
                }
@app.route('/Ybc/DeschedulePrePositionStream/',methods=['GET'])
def deschedulePrePositionStream():
    #print(request.data)
    return {
            "success": True,
            "message": " Successfully deleted the stream ",
            "data": {}
            }
#audio
@app.route("/Ybc/GetAudioStreamInfo/",methods=['GET'])
def getAudioStreamInfo():
    return {
                "success": True,
                "message": "Successfully obtained the audio stream information by id" ,
                "data": {
                "stream_id": "cff4e254c330360abe43f0895c29d350",
                "stream_start_time": 1682314504,
                "stream_end_time": 1682315104,
                "stream_schedule_duration": 600,
                "stream_name": "RAAGAM",
                "stream_url":" Reference Stream Url ",
                "stream_priority": 3,
                "stream_audio_bitrate": "AUDIO_BITRATE_96",
                "stream_protocol_type": "mmt",
                "service_streaming_status": "STREAMING"
                }
                }
@app.route('/Ybc/GetAllAudioStreamInfo/',methods=["GET"])
def getAllAudioStreamInfo():
    return {
                "success": True,
                "message": " Successfully obtained all the stream information ",
                "data": [
                {
                "stream_id": f"{x}cff4e254c330360abe43f0895c29d350",
                "stream_start_time": 1658644800-x,
                "stream_end_time": 1682315104+x,
                "stream_schedule_duration": 600+x,
                "stream_name": "RAAGAM",
                "service_streaming_status": "STREAMING"
                }
                for x in range(15)]
                }
@app.route('/Ybc/DescheduleAudioStream',methods=['GET'])
def descheduleAudioStream():
    return {
            "success": True,
            "message": " Successfully deleted the stream ",
            "data": {}
            }
@app.route('/Ybc/ScheduleAudioStream/',methods=['POST'])
def scheduleAudioStream():
    #print(request.json)
    return {
            "success" : True,
            "message" : " Successfully registered the stream ",
            "data" : {}
}
    
#analytics engine
@app.route("/Ybc/Ae/OffloadStatus/",methods=['POST'])
def AeOffloadStatus():
    return { "success": True, "message": "Successfully set the state of offload stream", "data": {} }

@app.route("/Ybc/Ae/OffloadReset/",methods=['GET'])
def AeOffloadReset():
    return{ "success": True, "message": "YBC has been restarted", "data": {} }

@app.route("/Ybc/Ae/SetTriggerTime/",methods=['POST'])
def AeSetTriggerTime():
    return { "data": {}, "message": "Default time has been successfully updated", "success": True }

@app.route("/Ybc/Ae/TriggerEngine/",methods=['GET'])
def AeTriggerEngine():
    return { "data": {}, "message": "Successfully triggered analytic engine", "success": True }

@app.route("/Ybc/Ae/GetDefaultTime/",methods=['GET'])
def AeGetDefaultTime():
    return { "data": { "Default AE Trigger Time": "12:00" }, "message": "Successfully fetched default triggering time of the analytic engine", "success": True }

@app.route("/Ybc/Ae/GetThreshold/",methods=['GET'])
def AeGetThreshold():
    return { "data": { "Offload threshold": 2 }, "message": "Successfully fetched offload threshold of the analytic engine", "success": True }

@app.route("/Ybc/Ae/DbDelAllOffloadStreams/",methods=['GET'])
def AeDbDelAllOffloadStreams():
    return { "data": {}, "message": "Successfully cleared offload queue", "success": True }
    
@app.route("/Ybc/Ae/DbGetOffloadInfo/",methods=['GET'])
def AeDbGetOffloadInfo():
    return { "data": {}, "message": "No Data Found", "success": True }
    
@app.route("/Ybc/Ae/DbDelAllUeData/",methods=['GET'])
def AeDbDelAllUeData():
    return { "data": True, "message": "Users deleted successfully", "success": True }
    
@app.route("/Ybc/Ae/DbUeWithinBrh/",methods=['GET'])
def AeDbUeWithinBrh():
    return { "success": True, "message": "Data Found", "data": { "Number of Users": 6, "User Details": [ { "yogaLocationDataItem": { "yogaUserAltitude": 850.759951171875, "yogaUserLatitude": 12.9840704, "yogaUserLocationAccuracy": 11.613, "yogaUserLongitude": 77.5959881 }, "yogaMediaDataItem": { "yogaMediaContentId": "601d3a5d555f2414d8000000", "yogaMediaContentPlaybackCh annel": 7000, "yogaMediaContentPlaybackSt atus": 6002 }, "yogaTimestamp": "1614774865", "yogaUserDataItem": { "yogaUserDataId": "8b1805dc-a9b0-4fe4-abe5-b4 9780b528d6", "yogaUserDataSDKVersion": "0.1.1(2)" } } ]*3 } }


@app.route("/Ybc/Ae/GetContentDetails/",methods=['POST'])
def AeGetContentDetails():
    return { "success": True, "message": "Successfully fetched content details", "data": { } }

@app.route("/Ybc/Ae/DbUniqueUe/",methods=['GET'])
def AeDbUniqueUe():
    return { "success": True, "message": "Data Found", "data": { "Number of Users": 6, "User Details": [ { "yogaLocationDataItem": { "yogaUserAltitude": 850.759951171875, "yogaUserLatitude": 12.9840704, "yogaUserLocationAccuracy": 11.613, "yogaUserLongitude": 77.5959881 }, "yogaMediaDataItem": { "yogaMediaContentId": "601d3a5d555f2414d8000000", "yogaMediaContentPlaybackCh annel": 7000, "yogaMediaContentPlaybackSt atus": 6002 }, "yogaTimestamp": "1614774865", "yogaUserDataItem": { "yogaUserDataId": "8b1805dc-a9b0-4fe4-abe5-b4 9780b528d6", "yogaUserDataSDKVersion": "0.1.1(2)" } } ]*3 } }


@app.route("/Ybc/Ae/DbGetUeInfo/",methods=['GET'])
def AeDbGetUeInfo():
    return { "success": True, "message": "Data Found", "data": { "Number of Users": 6, "User Details": [ { "yogaLocationDataItem": { "yogaUserAltitude": 850.759951171875, "yogaUserLatitude": 12.9840704, "yogaUserLocationAccuracy": 11.613, "yogaUserLongitude": 77.5959881 }, "yogaMediaDataItem": { "yogaMediaContentId": "601d3a5d555f2414d8000000", "yogaMediaContentPlaybackCh annel": 7000, "yogaMediaContentPlaybackSt atus": 6002 }, "yogaTimestamp": "1614774865", "yogaUserDataItem": { "yogaUserDataId": "8b1805dc-a9b0-4fe4-abe5-b4 9780b528d6", "yogaUserDataSDKVersion": "0.1.1(2)" } } ]*3 } }

@app.route("/Ybc/Ae/DbGetVodUeInfo/",methods=['GET'])
def AeDbGetVodUeInfo():
    return { "success": True, "message": "Data Found", "data": { "Number of Users": 6, "User Details": [ { "yogaLocationDataItem": { "yogaUserAltitude": 850.759951171875, "yogaUserLatitude": 12.9840704, "yogaUserLocationAccuracy": 11.613, "yogaUserLongitude": 77.5959881 }, "yogaMediaDataItem": { "yogaMediaContentId": "601d3a5d555f2414d8000000", "yogaMediaContentPlaybackCh annel": 7000, "yogaMediaContentPlaybackSt atus": 6002 }, "yogaTimestamp": "1614774865", "yogaUserDataItem": { "yogaUserDataId": "8b1805dc-a9b0-4fe4-abe5-b4 9780b528d6", "yogaUserDataSDKVersion": "0.1.1(2)" } } ]*3 } }

@app.route("/Ybc/Ae/DbDelAllRecommendations/",methods=['GET'])
def AeDbDelAllRecommendations():
    return { "success": True, "message": "All Recommendations have been deleted", "data": {} }

@app.route("/Ybc/Ae/DbPutRecommendations/",methods=['POST'])
def AeDbPutRecommendations():
    return { "data": {}, "message": "Stored the recommendations into the database", "success": True }

@app.route("/Ybc/Ae/SetThreshold/",methods=['POST'])
def AeSetThreshold():
    return { "data": {}, "message": "Offload threshold has been succesfully updated", "success": True }


@app.route("/Ybc/Ae/DbGetRecommendations/",methods=['GET'])
def AeDbGetRecommendations():
    return {
            "success": True,
            "message": "Data Found",
            "data": {
            "name": "Recommended List for offload",
            "date": "2021-03-03 10:13:17.935418",
            "ver": "v1.0",
            "data": 
            [
            {
            "content_id":
            "601d3ac2555f2414d8000006",
            "start_time": 1614765600
            },
            {
            "content_id":
            "601d3a5d555f2414d8000000",
            "start_time": 1614776400
            }
            ]*5,
            "count": 10
            }
            }

@app.route("/Ybc/Ae/DbContentUsers/",methods=['GET'])
def AeDbContentUsers():
    return { "success": True, "message": "Content and it’s users", "data": { "60c858a5555f247857000030":1,"60c858a5555f347857000030":2,"70c858a5555f247857000030":7,"60y858a5555f247857000030":1,"63c858a5555f247857000030":10,"60r858a5555f247857000030":76 ,"60c858a5555f247957000030":11,"60c858a5755f247857000030":26,"60c658a5555f247857000030":9,"60c858a5555f247857000036":12,"68c858a5555f247857000030":8}, }

@app.route("/Ybc/Ae/DbContentUserMapLive/",methods=['GET'])
def AeDbContentUserMapLive():
    return { "success": True, "message": "Content and it’s users", "data": { "60c858a5555f247857000030":1,"60c858a5555f347857000030":2,"70c858a5555f247857000030":7,"60y858a5555f247857000030":1,"63c858a5555f247857000030":10,"60r858a5555f247857000030":76 ,"60c858a5555f247957000030":11,"60c858a5755f247857000030":26,"60c658a5555f247857000030":9,"60c858a5555f247857000036":12,"68c858a5555f247857000030":8}, }


@app.route("/Ybc/Ae/DbLiveStreamUsers/",methods=['GET'])
def AeDbLiveStreamUsers():
    return { "success": True, "message": "Data Found", "data": { "Number of Users": 6, "User Details": [ { "yogaLocationDataItem": { "yogaUserAltitude": 850.759951171875, "yogaUserLatitude": 12.9840704, "yogaUserLocationAccuracy": 11.613, "yogaUserLongitude": 77.5959881 }, "yogaMediaDataItem": { "yogaMediaContentId": "601d3a5d555f2414d8000000", "yogaMediaContentPlaybackCh annel": 7000, "yogaMediaContentPlaybackSt atus": 6002 }, "yogaTimestamp": "1614774865", "yogaUserDataItem": { "yogaUserDataId": "8b1805dc-a9b0-4fe4-abe5-b4 9780b528d6", "yogaUserDataSDKVersion": "0.1.1(2)" } } ]*3 } }


@app.route("/Ybc/Ae/DbLiveUsers/",methods=['GET'])
def AeDbLiveUsers():
    return { "success": True, "message": "Data Found", "data": { "Number of Users": 6, "User Details": [ { "yogaLocationDataItem": { "yogaUserAltitude": 850.759951171875, "yogaUserLatitude": 12.9840704, "yogaUserLocationAccuracy": 11.613, "yogaUserLongitude": 77.5959881 }, "yogaMediaDataItem": { "yogaMediaContentId": "601d3a5d555f2414d8000000", "yogaMediaContentPlaybackCh annel": 7000, "yogaMediaContentPlaybackSt atus": 6002 }, "yogaTimestamp": "1614774865", "yogaUserDataItem": { "yogaUserDataId": "8b1805dc-a9b0-4fe4-abe5-b4 9780b528d6", "yogaUserDataSDKVersion": "0.1.1(2)" } } ]*3 } }

@app.route("/Ybc/Ae/DbLiveUsersCount/",methods=['GET'])
def AeDbLiveUsersCount():
    return { "data": { "Number of Live Users": 0, "Number of Users in Broadband": 0, "Number of Users in Broadcast": 0 }, "message": "Live Users count", "success": True }


@app.route("/Ybc/Ae/DbStart/",methods=['GET'])
def AeDbStart():
    return { "success": True, "message": "AE started successfully", "data": {} }

@app.route("/Ybc/Ae/DbStop/",methods=['GET'])
def AeDbStop():
    return { "success": True, "message": "AE stopped successfully", "data": {} }

@app.route("/Ybc/Ae/DbStatus/",methods=['GET'])
def AeDbStatus():
    return { "data": { "Status": "Running", "Version": "v0.1.7" }, "message": "Status of the System", "success": True }


@app.route("/Ybc/Ae/DbRestart/",methods=['GET'])
def AeDbRestart():
    return { "success": True, "message": "AE restarted successfully", "data": {} }


##
@app.route("/Ybc/Ae/Start/",methods=['GET'])
def AeStart():
    return { "success": True, "message": "AE started successfully", "data": {} }

@app.route("/Ybc/Ae/Stop/",methods=['GET'])
def AeStop():
    return { "success": True, "message": "AE stopped successfully", "data": {} }

@app.route("/Ybc/Ae/Status/",methods=['GET'])
def AeStatus():
    return { "data": { "Status": "Running", "Version": "v0.1.7" }, "message": "Status of the System", "success": True }


@app.route("/Ybc/Ae/Restart/",methods=['GET'])
def AeRestart():
    return { "success": True, "message": "AE restarted successfully", "data": {} }




@app.route('/cap_public_website/FetchAllAlertDetails',methods=['GET'])
def ndma():
    #print(request.json)
    return [
    {
        "severity": "ADVISORY",
        "identifier": 1700649879487026,
        "effective_start_time": "Wed Nov 22 16:05:00 IST 2023",
        "effective_end_time": "Thu Nov 23 16:05:00 IST 2023",
        "disaster_type": "Earthquake",
        "area_description": "24 districts of Arunachal Pradesh",
        "severity_level": "Likely",
        "type": 0,
        "actual_lang": "en",
        "warning_message": "MOCK EXERCISE DON'T PANIC:  STATE-LEVEL MOCK EXERCISE on Earthquake is being conducted simultaneously in all distts of Arunachal Pradesh on 23rd Nov 23 from 9:00 am to 2:00 pm. Siren will be blown at 9 am at incident sites across the state, public is advised not to panic. Issued by SDMA Arunachal Pradesh.",
        "disseminated": "true",
        "severity_color": "Red",
        "alert_id_sdma_autoinc": 22229,
        "centroid": "96.85624667238118,28.066616430769745",
        "alert_source": "Arunachal Pradesh SDMA",
        "area_covered": "121789",
        "sender_org_id": "26"
    },{
        "severity": "ADVISORY",
        "identifier": 1700641078135037,
        "effective_start_time": "Wed Nov 22 16:05:00 IST 2023",
        "effective_end_time": "Thu Nov 23 16:05:00 IST 2023",
        "disaster_type": "Earthquake",
        "area_description": "24 districts of Arunachal Pradesh",
        "severity_level": "Likely",
        "type": 0,
        "actual_lang": "en",
        "warning_message": "MOCK EXERCISE DON'T PANIC:  STATE-LEVEL MOCK EXERCISE on Earthquake is being conducted simultaneously in all distts of Arunachal Pradesh on 23rd Nov 23 from 9:00 am to 2:00 pm. Siren will be blown at 9 am at incident sites across the state, public is advised not to panic. Issued by SDMA Arunachal Pradesh.",
        "disseminated": "true",
        "severity_color": "green",
        "alert_id_sdma_autoinc": 22229,
        "centroid": "96.85624667238118,28.066616430769745",
        "alert_source": "Arunachal Pradesh SDMA",
        "area_covered": "121789",
        "sender_org_id": "26"
    },

]



if __name__=='__main__':

    app.run(debug=True,host="10.80.61.19",port=6000)
