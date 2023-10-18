import json

from flask import Flask,request
from flask_cors import CORS,cross_origin

import time
app=Flask(__name__)
CORS(app, origins=["http://localhost:3000","http://localhost:8000",'http://10.80.40.145:8000'])
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/ybc/rm/ybcStart/',methods=['GET'])
def ybc_start():
    time.sleep(5)
    all_ready_started=True
    if not all_ready_started:
        return {"success": True,"message": " YBC started successfully ","data": {}}
    else:
        return {"success": False,"message": " YBC is already running ","error_code": 1001,"data": {}}

@app.route('/ybc/rm/ybcStop/',methods=['GET'])
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
                        "message": "Unable to stop the ybc since the stream is streaming state ",
                        "error_code": 1002,
                        "data": {}
                        }
            else:
                return {"success": False,
                    "message": "Unable to stop the ybc since the stream is processing ",
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

@app.route('/ybc/rm/ybcRestart/',methods=['GET'])
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
                "message": "Unable to stop the ybc since the stream is processing ",
                "error_code": 1002,
                "data": {}
                }

    """if streams_are_in_streaming:
        return {
            "success": False,
            "message": "Unable to stop the ybc since the stream is streaming state ",
            "error_code": 1002,
            "data": {}
            }
"""
"""
        ybc restart error
        return {
    "success": False,
    "message": " Unable to restart the YBC ",
    "error_code": 1004,
    "data": {}
    }
    """

@app.route("/ybc/rm/ybcStatus/",methods=['GET'])
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
@app.route('/ybc/rm/getCurrentSchedulerConfig/',methods=['GET'])
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

@app.route('/ybc/rm/getAvailableSchedulerConfig/',methods=['GET'])
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
@app.route('/ybc/rm/switchSchedulerConfig/',methods=['POST'])
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

@app.route('/ybc/rm/getStreamInfo/',methods=['GET'])
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
sm=[
                {
                "stream_id": "60c858a5555f247857000032",
                "stream_start_time": 1658644800,
                "stream_end_time": 1658646600,
                "stream_schedule_duration": 1800,
                "stream_name": "DDNewsLive",
                "service_streaming_status": "STREAMING",
                "stream_is_offload": True
                },{
                "stream_id": "60c858a5555f237857000032",
                "stream_start_time": 1658644800,
                "stream_end_time": 1658646600,
                "stream_schedule_duration": 1800,
                "stream_name": "DDNewsLive",
                "service_streaming_status": "STREAMING",
                "stream_is_offload": True
                },
    {"stream_id": "100c858a5555f237857000032",
                "stream_start_time": 1658644800,
                "stream_end_time": 1658646600,
                "stream_schedule_duration": 1800,
                "stream_name": "DDNewsLive",
                "service_streaming_status": "STREAMING",
                "stream_is_offload": True
                }]
@app.route('/ybc/rm/getPrePositionStreamInfo/',methods=['GET'])
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
@app.route('/ybc/rm/getAllStreamInfo/',methods=['GET'])
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


@app.route("/ybc/rm/getAllOffloadStreamInfo/",methods=['GET'])
def getAllOffloadStreamInfo():
    return {
"success": True,
"message": " Successfully obtained all the offload stream information ",
"data": [
{
"stream_id": "60c858a5555f247857000032",
"stream_start_time": 1658644800,
"stream_end_time": 1658646600,
"stream_schedule_duration": 0,
"stream_name": "DDNewsLive",
"service_streaming_status": "STREAMING",
"stream_is_offload": True
} ]
}
@app.route('/ybc/rm/getRecommendationList/',methods=['GET'])
def getRecommendationList():
    return {"success": True,
"message": " Successfully obtained the recommendation list ",
"data": {
"count" : 2,
"data" : [
{"content_id": "6171516a555f2413e4000041",
"start_time": 1638281167 },{"content_id": "6171518ac55f2413e4000041",
"start_time": 1638281167 }],
"date" : "2021-11-30 09:11:55.450168",
"name" : "Recommended List for offload",
"ver" : " v1.0 "
}
}

@app.route('/ybc/rm/descheduleStream/',methods=['GET'])
def deleteStream():
    sm.pop(-1)

    return {
"success": True,
"message": " Successfully deleted the stream ",
"data": {}
}

@app.route('/ybc/rm/deleteAllSchedules/',methods=['GET'])
def delete_all_streams():
    sm.clear()
    return {
"success": True,
"message": " Successfully deleted all the streams ",
"data": {}
}

@app.route("/ybc/rm/scheduleStream/",methods=['POST'])
def scheduleStream():
    return {
"success" : True,
"message" : " Successfully registered the stream ",
"data" : {}
}
@app.route("/ybc/rm/scheduleOffloadStream/",methods=['POST'])
def scheduleOffloadStream():
    return {
                "success" : True,
                "message" : " Successfully registered the stream ",
                "data" : {}
                }
@app.route("/ybc/rm/updateStreamInfo/",methods=['POST'])
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
@app.route('/ybc/rm/schedulePrePositionStream/',methods=['POST'])
def schedulePrePositionStream():
    print(request.json)
    return {
                "success" : True,
                "message" : " Successfully registered the pre-position stream ",
                "data" : {}
                }

@app.route('/ybc/rm/updatePrePositionStream/',methods=['POST'])
def updatePrePositionStream():
    print(request.json)
    return {
            "success" : True,
            "message" : " Successfully updated the stream ",
            "data" : {}
            }

@app.route('/ybc/rm/getAllPrePositionStreamInfo/',methods=['GET'])
def getAllPrePositionStreamInfo():

    return {
                "success": True,
                "message": " Successfully obtained all pre-position streams information ",
                "data":pp
                }
@app.route('/ybc/rm/deschedulePrePositionStream/',methods=['GET'])
def deschedulePrePositionStream():
    #print(request.data)
    return {
            "success": True,
            "message": " Successfully deleted the stream ",
            "data": {}
            }
#audio
@app.route("/ybc/rm/getAudioStreamInfo/",methods=['GET'])
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
@app.route('/ybc/rm/getAllAudioStreamInfo/',methods=["GET"])
def getAllAudioStreamInfo():
    return {
                "success": True,
                "message": " Successfully obtained all the stream information ",
                "data": [
                {
                "stream_id": "cff4e254c330360abe43f0895c29d350",
                "stream_start_time": 1658644800,
                "stream_end_time": 1682315104,
                "stream_schedule_duration": 600,
                "stream_name": "RAAGAM",
                "service_streaming_status": "STREAMING"
                }
                ]
                }
@app.route('/ybc/rm/descheduleAudioStream',methods=['GET'])
def descheduleAudioStream():
    return {
            "success": True,
            "message": " Successfully deleted the stream ",
            "data": {}
            }
@app.route('/ybc/rm/scheduleAudioStream/',methods=['POST'])
def scheduleAudioStream():
    #print(request.json)
    return {
            "success" : True,
            "message" : " Successfully registered the stream ",
            "data" : {}
}
