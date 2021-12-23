REQUEST_TIMEOUT = 20
SYSTEM_ID = '100080'
TEST_CONSTANT = 1
# url control
BUSINESS_BUBBLE_NUMBER_APP_ADDR = '/HxoaApi/App/msgCount'
BUSINESS_BUBBLE_NUMBER_OA_ADDR = '/HxoaApi/App/auditUserNum'
BUSINESS_BUBBLE_NUMBER_CRM_ADDR = '/CrmCommon/getInformNum'
BUSINESS_BUBBLE_NUMBER_ERP_ADAPTER_NO = '100095'
BUSINESS_SSO_ADAPTER_NO = '100012'
BUSINESS_ERP_ADAPTER_NO = '100074'

# userInfo 请求 urlControl
BUSINESS_AUTH_ADDR = '/user/info'
BUSINESS_OA_ADDR = '/hi/psn/mobileTree'
BUSINESS_ERP_ADDR = '/user/getUserInfoDetailByToken'
BUSINESS_NC_ADDR = '/app/log/userInfo'
BUSINESS_CAR_ADDR = '/usedcar/v1/app_auth/get_shop_url'
BUSINESS_CHAT_ADDR = '/OaChat/getLoginInfo'
BUSINESS_CRM_ADDR = '/User/getUserInfo'

CHANNEL_PC_CHAT = 'pc_chat'

# 聊天 权限 10 default
CHAT_PERMISSION = 10

AVATAR_PATH = '/avatar/'  # 上传头像路径
AVATAR_PREVIEW_PREFIX = 'preview_'  # 缩略图前缀

WXQRPATH = '/wxqr/'  # 微信二维码保存路径

# 车牌识别 地址
DRIVER_LICENSE_PATH = '/static/upload/recognize/driverLicense/'  # 驾驶证识别图片存放路径
GENERAL_PATH = '/static/upload/recognize/general/'  # vin识别图片存放路径
LICENSE_PATH = '/static/upload/recognize/license/'  # 车牌识别图片存放路径
VEHICLE_PATH = '/static/upload/recognize/vehicle/'  # 行驶证识别图片存放路径
ID_CARD_PATH = '/static/upload/recognize/idCard/'  # 身份证识别图片存放路径
COMMON_PATH = '/static/upload/recognize/common/'  # 通用文字识别图片存放路径
MEETING_EXCEL_PATH = '/static/upload/meeting/'  # 会议签到表路径

#  urlControl OA 跳转 看板
OA_CHECK_KANBAN = '/bpm/wfs/bill/notice'

# auth token url

# k8s内网域名访问 本地调试 与 服务器访问 时
# K8S_DOMAIN_DEBUGTEST = 'https://dms.t.hxqcgf.com'
# K8S_DOMAIN_PRERELEASE = 'https://dms.hxqcgf.com'
# K8S_DOMAIN_RELEASE = 'https://pacss.hxqcgf.com'
K8S_DOMAIN_DEBUGTEST = 'http://dms-gateway.kubernetes-plugin'
K8S_DOMAIN_PRERELEASE = 'http://dms-gateway.dms-staging'
K8S_DOMAIN_RELEASE = 'http://dms-gateway.dms-prod'

# 地址
REQUEST_ADDRESS = {
    'debug': {  # 开发线
        'ERP_FileServer': 'http://10.0.15.134:9999/apigateway/hxfile/api/fileUpload',
        'ERP_message_adapter_server': 'http://10.0.15.134:9999/apigateway/erp-api/messageAdapter/fileUpload',
        'ERP_File_Host': 'http://10.0.15.134:8080',
        'dms_host': 'http://10.0.15.134:9999/apigateway',
        "app_wings_url": 'http://10.0.15.134:9999/apigateway/dms-appwings',
        "vue_business_host": 'http://10.0.15.77:8111',
        'statisticsPermission': 'AutoShowFlow',  # 车展统计权限code
        'face_contrast_host': '',
        "teleconferencing_host": 'http://10.0.15.216:5000',
        "chat_params": {  # 测试线
            # workers: 4,
            'port': 5000,  # 端口号
            'environmentHost': 'http://10.0.15.134:9999/dms-appwings',  # 接口中心地址
            'chatUrl': 'http://10.0.15.134:9999/dms-app-chat/Chat/V1',  # 聊天服务器地址
            'environment': 'debug',  # 环境参数
            'showMobileNum': False,  # 是否显示电话号码
            'mongoDB': {  # mongoDB配置
                'host': '10.0.14.224',
                'port': '27017',
                'user': 'app',
                'pswd': 'app',
                'database': 'app_cache'
            },
            'productionMode': "false",  # 推送是否开启产品模式，正式线为"true"，其他环境为"false",

            '/recognize/general': '412fa2b7e53c47709d3b7fd8f62ab464',  # 识别接口AppCode参数,
            '/recognize/vehicle': '412fa2b7e53c47709d3b7fd8f62ab464',  # 行驶证识别接口AppCode参数,
            '/recognize/license': '412fa2b7e53c47709d3b7fd8f62ab464',  # 车牌识别接口AppCode参数,
            '/recognize/idCard': '412fa2b7e53c47709d3b7fd8f62ab464',  # 身份证识别接口AppCode参数,
            '/recognize/driverLicense': 'e1ac66c2b25944b38e27de686157df7a',  # 驾驶证识别接口AppCode,
            '/recognize/common': 'e1ac66c2b25944b38e27de686157df7a',  # 通用文字识别AppCode参数

            'dms-app-mobil-push-host': 'http://10.0.15.134:9999/dms-app-push'  # dms-app-mobil-push微服务地址
        },
        'commonInfo': {
            "androidWebPDFShellHost": 'http://10.0.15.134:9999/car-mobile-api/pdfjs/web/viewer.html',
            # "auctionHost": 'http://dms-shop.tm.hxqc.com/car.html#/auction/activities',
            # "chatServiceHost": 'http://124.202.158.252:23000',
            # "geekShareHost": 'http://dms-shop.tm.hxqc.mobi/netShare/index',
            "insuranceHost": '',  # 保险查询
            "assessmentHost": 'http://10.0.15.134:9999/usedCar.html#/assessment',
            # "liveChatHost": 'ws://10.0.15.216:3014',
            # "liveRTMPHost": 'rtmp://124.202.158.252:11935/live',
            # "usedCarHost": 'http://10.0.15.130:31094/car.html#/',
        }

    },
    'debugTest': {  # 测试线
        'ERP_FileServer': 'https://dms.t.hxqcgf.com/apigateway/hxfile/api/fileUpload',
        'ERP_message_adapter_server': 'https://dms.t.hxqcgf.com/apigateway/erp-api/messageAdapter/fileUpload',
        'ERP_File_Host': 'https://dms.t.hxqcgf.com/erpfileserver',
        'dms_host': f'{K8S_DOMAIN_DEBUGTEST}/apigateway',
        "app_wings_url": f'{K8S_DOMAIN_DEBUGTEST}/apigateway/dms-appwings',
        "vue_business_host": 'http://10.0.15.77:8111',
        'statisticsPermission': 'AutoShowFlow',  # 车展统计权限code
        'face_contrast_host': 'http://10.0.15.77:8101',
        "teleconferencing_host": '',
        "chat_params": {  # 测试线
            # workers: 4,
            'port': 5000,  # 端口号
            'environmentHost': f'{K8S_DOMAIN_DEBUGTEST}/apigateway/dms-appwings',  # 接口中心地址
            'chatUrl': f'{K8S_DOMAIN_DEBUGTEST}/apigateway/dms-app-chat/Chat/V1',  # 聊天服务器地址
            'environment': 'debugTest',  # 环境参数
            'showMobileNum': False,  # 是否显示电话号码
            'mongoDB': {  # mongoDB配置
                'host': '10.0.14.224',
                'port': '27017',
                'user': 'app',
                'pswd': 'app',
                'database': 'app_cache'
            },
            'productionMode': "false",  # 推送是否开启产品模式，正式线为"true"，其他环境为"false",

            '/recognize/general': '412fa2b7e53c47709d3b7fd8f62ab464',  # 识别接口AppCode参数,
            '/recognize/vehicle': '412fa2b7e53c47709d3b7fd8f62ab464',  # 行驶证识别接口AppCode参数,
            '/recognize/license': '412fa2b7e53c47709d3b7fd8f62ab464',  # 车牌识别接口AppCode参数,
            '/recognize/idCard': '412fa2b7e53c47709d3b7fd8f62ab464',  # 身份证识别接口AppCode参数,
            '/recognize/driverLicense': 'e1ac66c2b25944b38e27de686157df7a',  # 驾驶证识别接口AppCode,
            '/recognize/common': 'e1ac66c2b25944b38e27de686157df7a',  # 通用文字识别AppCode参数

            'dms-app-mobil-push-host': f'{K8S_DOMAIN_DEBUGTEST}/apigateway/dms-app-push'  # dms-app-mobil-push微服务地址
        },
        'commonInfo': {
            "androidWebPDFShellHost": 'https://dms.t.hxqcgf.com/apigateway/car-mobile-api/pdfjs/web/viewer.html',
            # "auctionHost":  'http://10.0.15.130:31094/car.html#/auction/activities',
            # "auctionHost": 'https://dms.t.hxqcgf.com/interalapp/car.html#/auction/activities',
            # "geekShareHost": 'https://dms-shop.tm.hxqc.mobi/netShare/index',
            "insuranceHost": 'https://dms.t.hxqcgf.com/interalapp/usedCar.html#/insuranceQueryPage',  # 保险查询
            "assessmentHost": 'https://dms.t.hxqcgf.com/interalapp/usedCar.html#/assessment',  # 评估详情
            # "liveChatHost": 'ws://10.0.15.216:3014',
            # "liveChatHost": 'ws://10.0.15.216:3014',
            # "liveRTMPHost": 'rtmp://124.202.158.252:11935/live',
        }

    },
    'preRelease': {  # 预上线
        'ERP_FileServer': 'https://dms.hxqcgf.com/apigateway/hxfile/api/fileUpload',
        'ERP_message_adapter_server': 'https://dms.hxqcgf.com/apigateway/erp-api/messageAdapter/fileUpload',
        'ERP_File_Host': 'https://file.dms.hxqcgf.com',
        'dms_host': f'{K8S_DOMAIN_PRERELEASE}/apigateway',
        "app_wings_url": 'https://appwings.dms.hxqcgf.com',
        "vue_business_host": 'http://10.0.15.77:8112',
        'statisticsPermission': 'AutoShowFlow',  # 车展统计权限code
        'face_contrast_host': 'http://10.0.15.77:8101',
        "chat_params": {  # 测试线
            # workers: 4,
            'port': 5000,  # 端口号
            'environmentHost': f'{K8S_DOMAIN_PRERELEASE}/apigateway/dms-appwings',  # 接口中心地址
            'chatUrl': f'{K8S_DOMAIN_PRERELEASE}/apigateway/dms-app-chat/Chat/V1',  # 聊天服务器地址
            'environment': 'preRelease',  # 环境参数
            'showMobileNum': False,  # 是否显示电话号码
            'mongoDB': {  # mongoDB配置
                'host': '10.0.14.224',
                'port': '27017',
                'user': 'app',
                'pswd': 'app',
                'database': 'app_cache'
            },
            'productionMode': "false",  # 推送是否开启产品模式，正式线为"true"，其他环境为"false",
            '/recognize/general': 'fcaa27df6e344ea5980818fe0cdf44b8',  # 识别接口AppCode参数,
            '/recognize/vehicle': 'fcaa27df6e344ea5980818fe0cdf44b8',  # 行驶证识别接口AppCode参数,
            '/recognize/license': 'fcaa27df6e344ea5980818fe0cdf44b8',  # 车牌识别接口AppCode参数,
            '/recognize/idCard': 'fcaa27df6e344ea5980818fe0cdf44b8',  # 身份证识别接口AppCode参数,
            '/recognize/driverLicense': 'e1ac66c2b25944b38e27de686157df7a',  # 驾驶证识别接口AppCode,
            '/recognize/common': 'e1ac66c2b25944b38e27de686157df7a',  # 通用文字识别AppCode参数
            'dms-app-mobil-push-host': f'{K8S_DOMAIN_PRERELEASE}/apigateway/dms-app-push'  # dms-app-mobil-push微服务地址
        },
        'commonInfo': {
            "androidWebPDFShellHost": 'https://app.pre.hxqc.com/pdfjs/web/viewer.html',
            "insuranceHost": 'https://app.dms.hxqcgf.com/usedCar.html#/insuranceQueryPage',  # 保险查询
            "assessmentHost": 'https://app.dms.hxqcgf.com/usedCar.html#/assessment',
        }
    },
    'release': {  # 正式线
        'ERP_FileServer': 'https://pacss.hxqcgf.com/apigateway/hxfile/api/fileUpload',
        'ERP_message_adapter_server': 'https://pacss.hxqcgf.com/apigateway/erp-api/messageAdapter/fileUpload',
        'ERP_File_Host': 'https://file.pacss.hxqcgf.com',
        'dms_host': f'{K8S_DOMAIN_RELEASE}/apigateway',
        "app_wings_url": 'https://appwings.pacss.hxqcgf.com',
        "vue_business_host": 'https://appwings.hxqc.mobi',
        'statisticsPermission': 'AutoShowFlow',  # 车展统计权限code
        'face_contrast_host': 'http://10.0.15.115',
        "chat_params": {  # 正式线
            # workers: 4,
            'port': 5000,  # 端口号
            'environmentHost': f'{K8S_DOMAIN_RELEASE}/apigateway/dms-appwings',  # 接口中心地址
            'chatUrl': f'{K8S_DOMAIN_RELEASE}/apigateway/dms-app-chat/Chat/V1',  # 聊天服务器地址
            'environment': 'release',  # 环境参数
            'showMobileNum': False,  # 是否显示电话号码
            'mongoDB': {  # mongoDB配置
                'host': '10.0.14.224',
                'port': '27017',
                'user': 'app',
                'pswd': 'app',
                'database': 'app_cache'
            },
            'productionMode': "false",  # 推送是否开启产品模式，正式线为"true"，其他环境为"false",
            '/recognize/general': 'fcaa27df6e344ea5980818fe0cdf44b8',  # 识别接口AppCode参数,
            '/recognize/vehicle': 'fcaa27df6e344ea5980818fe0cdf44b8',  # 行驶证识别接口AppCode参数,
            '/recognize/license': 'fcaa27df6e344ea5980818fe0cdf44b8',  # 车牌识别接口AppCode参数,
            '/recognize/idCard': 'fcaa27df6e344ea5980818fe0cdf44b8',  # 身份证识别接口AppCode参数,
            '/recognize/driverLicense': 'e1ac66c2b25944b38e27de686157df7a',  # 驾驶证识别接口AppCode,
            '/recognize/common': 'e1ac66c2b25944b38e27de686157df7a',  # 通用文字识别AppCode参数
            'dms-app-mobil-push-host': f'{K8S_DOMAIN_RELEASE}/apigateway/dms-app-push'  # dms-app-mobil-push微服务地址
        },
        'commonInfo': {
            "androidWebPDFShellHost": 'https://app.hxqc.com/pdfjs/web/viewer.html',
            "insuranceHost": 'https://app.pacss.hxqcgf.com/usedCar.html#/insuranceQueryPage',  # 保险查询
            "assessmentHost": 'https://app.pacss.hxqcgf.com/usedCar.html#/assessment',
        }
    }
}

# 服务名
SYSTEM_MODULE = {
    'S1': '/auth',
    'S2': '/erp-api/messageAdapter',  # erp 通用地址
    'S2_1': '/admin',  # erp admin 微服务名
    'S2_file': '/hxfile',  # erp 文件上传 微服务名
    'S3': '/crm-interface/App/V1',
    'S4': '/biapi',
    'S5': '/dms-hr-basic',
    'S5_1': '/dms-hr',
    'S6': '/car-mobile-api',  # 车管家
    'S7': '/dms-appwings',
    'S8': '/dms-app-chat/Chat/V1',
    'S9': '/car-main',
    'S10': '/dms-hr',
    'S11': '/dms-app-push',
}

# 多服务名 定义


CONF_SYSTEM = {  # confSystem参数配置
    'SSO': 'S1',
    'ERP': 'S2',
    'CRM': 'S3',
    'NC': 'S4',
    'OA': 'S5',
    'MALL': 'S6',
    'AppWings': 'S7',
    'Chat': 'S8',
    'UsedCar': 'S9',
    'EHR': 'S10'
}

SYSTEM_SECRET = {
    'S1': 'SSO',
    'S2': 'ERP',
    'S3': 'CRM',
    'S4': 'NC',
    'S5': 'OA',
    'S6': 'Mall',
    'S7': 'App',
    'S8': 'Chat',
    'S9': 'UsedCar',
    'S10': 'EHR',
}
# des3 加解密参数
DES_KEY = {  # 加密参数配置
    'SSO': {
        'alg': 'des-ede3-cbc',
        'key': 'a$%$^#w12341@#@1-03@ffs3',
        'secretKey': 'my.oschina.net/penngo?#@',
        'iv': '01234567'
    },

    'ERP': {
        'alg': 'des-ede3-cbc',
        'key': 'a$%$^#w12341@#@1-03@ffs3',
        'secretKey': 'hxqc.com/owkx.kew#kpdh32',
        'iv': '08183625'
    },

    'CRM': {
        'alg': 'des-ede3-cbc',
        'key': 'kj@fr#bgxt41@#@1-03@ffs3',
        'secretKey': '52%HF9U*lQADmir!p#FW0HHg',
        'iv': '01234567'
    },

    'OA': {
        'alg': 'des-ede3-cbc',
        'key': 'oa@12@w62t41n#b1-0fssfs0',
        'secretKey': 'hxqc.com/oadsckew#kpdhaa',
        'iv': '76543210'
    },

    'NC': {

        'alg': 'des-ede3-cbc',
        'key': 'diap$@ds%&^erwc@$^*fsvs4',
        'secretKey': 'oalx@052vos,xpedc;xo1@$6',
        'iv': '52681239'
    },

    'NSCode': {
        'alg': 'des-ede3-cbc',
        'key': '',
        'secretKey': '^0f0wo@!m6s*89^n0#&nh;d$',
        'iv': '01234567'
    },
    'Mall': {
        'alg': 'des-ede3-cbc',
        'key': '',
        'secretKey': '^0f0wo@!m6s*89^n0#&nh;d$',
        'iv': '01234567'
    },
    'App': {
    "type": "des3",
    'alg': 'des-ede3-cbc',
    'key': '2zke1@$%kaocmalzomzlajqo',
    'secretKey': 'jshyui890kxiq*9snbxhau@!',
    'iv': '01234567'
},
    'Chat': {
        'alg': 'des-ede3-cbc',
        'key': 'a$%$^#w12341@#@1-03@ffs3',
        'secretKey': '9$1D7p5SFfC9FHwdVUE#-zi0',
        'iv': '01234567'
    },
    'UsedCar': {
        'alg': 'des-ede3-cbc',
        'key': 'a$%$^#w12341@#@1-03@ffs3',
        'secretKey': '9$1D7p5SFfC9FHwdVUE#-zi0',
        'iv': '01234567'
    },
    'EHR': {
        'alg': 'des-ede3-cbc',
        'key': 'cb%6^*w45@41@#@1-03@ffs3',
        'secretKey': 'hxqc.com/oadsckew#kpdhaa',
        'iv': '76543210'
    }
}

AES_KEY = {  # 加密参数配置
    'alg': 'des-ede3-cbc',
    'key': '2zke1@$%kaocmalzomzlajqo',
    'secretKey': 'hxqc!@#scodms001',
    'iv': 'hxqc!@#scodms001'
}

U_PUSH_CONFIG = {
    'url': 'http://msg.umeng.com/api/send',
    'type': 'customizedcast',
    'aliasTypeID': "ID_NUMBER",
    'aliasTypeShopID': "SHOP_ID_NUMBER",
    'title': '掌上神器',
    'dialogRouter': 'hxbusiness://PushMissionDialog',
    'Android': {
        'appKey': '58c89f1f04e2050199001db0',
        'appMasterSecret': 'qqzqkt1dflnwir9kvvde7cmyjssossli',
        'miActivity': 'com.hxqc.business.push.MiPushActivity'
    },
    'iOS': {
        'appKey': '58c89f9b677baa4c9500150f',
        'appMasterSecret': 'oi5yh0mjib3p2jxoqgnheeqmvnjp1eiu'
    }
}

SYSTEM = {
    'android': 'Android',
    'ios': 'iOS'
}

AMAPKEY = '9bc96a5f3e3ec887d158e31876770a40'  # 高德地图key
BAI_DU_CONFIG = [  # 百度参数设置
    {
        'grant_type': 'client_credentials',
        'app_id': '16421272',
        'client_id': 'Rx1hGq067hOj0WGHOkCD6TR6',
        'client_secret': '1zz6zNbeCL2NcuqGNy19WYbGqFa8Ri4L'
    }, {
        'app_id': '16384040',
        'grant_type': 'client_credentials',
        'client_id': 'QZ4CLcuBLaBhf2j00eIqgp3l',
        'client_secret': 'ruf9WSi0wGgug3pogciULreYwgsDMfKw'
    }]
PROVINCE_CODE = ['京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪', '苏', '浙', '皖', '闽', '赣', '鲁', '豫', '鄂', '湘', '粤', '桂',
                 '琼',
                 '渝', '川', '黔', '滇', '藏', '陕', '甘', '青', '宁', '新', '台', '港', '澳']  # 省市简称

FEEDBACK_TYPE = {  # 反馈意见类型
    10: {
        'title': '意见反馈',
        'subtitle': '用着不爽，我有话说'
    },

    30: {
        'title': '高能故事',
        'subtitle': '明明可以靠脸，非要靠才华'
    },
    40: {
        'title': '我宣你',
        'subtitle': 'CP官宣，必须安排'
    },
    50: {
        'title': '吐槽拆台',
        'subtitle': '收集吐槽，避开大坏蛋'
    },
    20: {
        'title': '其他问题',
        'subtitle': ''
    }
}
# 规则级别
RULE_LEVELS = {
    'group': 'GROUP',  # 组规则
    'shop': 'SHOP'  # 单店规则
}

# 积分数据级别
SCORE_LEVEL = {
    'monthShop': 'MONTHSHOP',  # 单店月榜
    'yearShop': 'YEARSHOP',  # 单店年榜
    'monthBrand': 'MONTHBRAND',  # 品牌月榜
    'yearBrand': 'YEARBRAND',  # 品牌年榜
}

HFPCBZ = 4  # 回访频次
POST_TYPE = {
    'Mod': 'mod',
    'Add': 'add',
    'Del': 'del'
}
# 识别地址
RECOGIZE_PATH = {
    '/recognize/general': 'http://vin.market.alicloudapi.com/api/predict/ocr_vin',  # VIN识别地址
    '/recognize/license': 'http://ocrcp.market.alicloudapi.com/rest/160601/ocr/ocr_vehicle_plate.json',  # 车牌识别地址
    '/recognize/driverLicense': 'http://dm-52.data.aliyun.com/rest/160601/ocr/ocr_driver_license.json',  # 驾驶证识别地址
    '/recognize/vehicle': 'http://dm-53.data.aliyun.com/rest/160601/ocr/ocr_vehicle.json',  # 行驶证识别地址
    '/recognize/idCard': 'http://dm-51.data.aliyun.com/rest/160601/ocr/ocr_idcard.json',  # 身份证识别地址
    '/recognize/common': 'http://tysbgpu.market.alicloudapi.com/api/predict/ocr_general',  # 通用文字识别地址
}

# 重定向 web url 地址
# WEB_REDIRECT_URL = {
#     'debug': 'http://10.0.15.205:7002',
#     'preRelease': 'http://59.172.37.74:17001',
#     'release': 'http://appwings.hxqc.mobi',
# }

# 待定跳转 web path
REDIRECT_PATH = ['/web/vehicleEvaluation', '/web/violationQuery', '/web/maintenanceQuery', '/web/vehicleInsurance',
                 '/web/getUsedCarPrice', '/web/statisticsCountList', '/answer/index', '/private/feedback/list']
# 直辖市车牌
MUNICIPALITIES = ['京', '津', '沪', '渝']

NODE_TIME = {
    'notRemind': -1,
    'startRemind': 0,
    'fiveMinutes': 5 * 60,
    'fifteenMinutes': 15 * 60,
    'thirtyMinutes': 30 * 60,
    'oneHour': 60 * 60,
    'threeHour': 3 * 60 * 60,
    'oneDay': 24 * 60 * 60,
}

NOTIFY_TYPE = {
    'notify': 10,
    'option': 20
}

SCHEDULE_ROUTER = {
    "calendar": "hxbusiness://SchedulePlanDetail",
    "meeting": "hxbusiness://ScheduleMeetingDetail",
    "task": "hxbusiness://ScheduleTaskDetail",
}

MEETING_STATUS = {
    'normal': 10,  # 正常
    'end': 20,  # 结束
    'cancel': 30  # 取消
}

TASK_ROLE = {
    'creator': 0,  # 创建者
    'administrator': 10,  # 管理者(默认为创建者)
    'participator': 20,  # 参与者
    'reader': 30  # 抄送者
}

MEETING_ROLE = {
    'creator': 0,  # 创建者
    'administrator': 10,  # 管理者
    'participator': 20  # 参与者
}

MEETING_RESPONSE_STATUS = {
    'noResponse': 10,  # 不响应
    'attend': 30,  # 参加
    'notAttend': 40  # 不参加
}

READ_STATUS = {
    'unread': 10,  # 已读
    'read': 20  # 未读
}

COMMENT_TYPE = {
    'system': 10,  # 系统回复
    'person': 20  # 个人回复
}

MEETING_MESSAGE = {
    'mod': '修改了会议',
    'cancel': '取消了会议'
}

MEETING_SIGN_ROUTER = 'hxbusiness://ScheduleMeetingSign'

MEETING_QR_UPDATE_TIME = 30 * 1000  # 动态二维码刷新时间间隔

TASK_STATUS = {
    'normal': 10,  # 正常
    'close': 20,  # 关闭
    'cancel': 30  # 取消
}

# 日程类型
SCHEDULE_TYPE = {
    'meeting': 10,  # 会议
    'calendar': 20,  # 日程
    'task': 30,  # 任务
    'message': 40,  # 任务
    'teleconference': 50  # 远程会议
}

# 远程会议角色
TELECONFERENCE_ROLE = {
    'creator': 0,  # 创建者
    'administrator': 10,  # 管理者
    'participator': 20  # 参与者
}
# 远程会议类型 10 预约会议 20 即时会议
TELECONFERENCE_TYPE = {
    'appointment': 10,
    'immediate': 20
}

# mike 状态
TELECONFERENCE_MIC = {
    'open': 10,
    'close': 20
}

TELECONFERENCE_ROUTER = {
    'meeting_add': 'hxbusiness://TeleconferenceAdd',
    'meeting_detail': 'hxbusiness://RemoteMeetingDetails'
}
# 任务列表筛选条件
TASK_CONDITION = {
    'notDone': 10,  # 未完成
    'doneORClose': 20,  # 已完成/关闭
    'mySend': 30,  # 我发出 即creater为自己,
    'myExec': 40,  # 我执行 participator包含自己
    'myReader': 50,  # 抄送 reader包含自己
    'overdue': 60  # 逾期
}

TASK_MESSAGE = {
    'mod': '修改了任务',
    'done': '将任务标记为已完成',
    'notDone': '将任务标记为未完成',
    'close': '将任务标记为已关闭',
    'open': '将任务标记为未关闭',
    'overdue': '任务已逾期'
}

TASK_CONTROL = {
    'notDone': 0,  # 未完成
    'done': 10,  # 完成
    'close': 30,  # 关闭
    'open': 40  # 打开
}

# 远程会议分享的router
SHARE_ROUTER = "hxbusiness://TeleconferenceAdd?"

# 提醒时间间隔5分钟
URGE_TIME = 5 * 60

# 会议列表筛选条件
MEETING_CONDITION = {
    'notComplete': 10,  # 未结束
    'endORCancelORNotAttend': 20,  # 结束/取消/不参加
    'mySendORAdmin': 30,  # 我发出/我管理
    'isAssociated': 40  # 有关联 即有关联任务
}

REQUEST_DATA = {
    'adapter_no': '',
    'confSystem': 'S1',
    'entityCode': '',
    'data': '',
    'system_id': '100080',
    'identity_code': '',
    'uCode': '',
    'encodeType': '',
    'businessEnvironment': '',
    'time': '',
    'aid': '100080',
}

PUSH_SYSTEM = ['Android', 'iOS']

# 交易类型
TRXCODE = {
    'VSP001': '消费',
    'VSP002': '消费撤销',
    'VSP003': '退货',
    'VSP004': '预授权',
    'VSP005': '预授权撤销',
    'VSP006': '预授权完成',
    'VSP007': '预授权完成撤销',
    'VSP008': '手工退货登记',
    'VSP011': '扫码预消费',
    'VSP012': '扫码预消费回退',
    'VSP013': '扫码预消费完成',
    'VSP014': '扫码预消费完成退货',
    'CMN001': '消费冲正',
    'CMN002': '预授权冲正',
    'CMN003': '预授权完成冲正',
    'VSP501': '微信支付',
    'VSP502': '微信支付撤销',
    'VSP503': '微信支付退款',
    'VSP511': '支付宝支付',
    'VSP512': '支付宝支付撤销',
    'VSP513': '支付宝支付退货',
    'VSP521': '通联钱包消费',
    'VSP522': '通联钱包消费撤销',
    'VSP523': '通联钱包消费退货',
    'VSP505': '手机QQ 支付',
    'VSP506': '手机QQ支付撤销',
    'VSP507': '手机QQ支付退款',
    'VSP541': '扫码支付',
    'VSP542': '扫码支付撤销',
    'VSP543': '扫码支付退货',
    'VSP551': '银联扫码支付',
    'VSP552': '银联扫码撤销',
    'VSP553': '银联扫码退货',
}

# 交易结果状态码  注，其他3开头交易码均为交易失败，
TRXSTATUS = {
    '0000': '成功',
    '1001': '交易不存在',
    '3029': '交易已冲正',
    '3050': '交易已撤销',
    '3999': '交易失败'
}

# 借贷标志
ACCTTYPE = {
    '00': '借记卡',
    '01': '存折',
    '02': '信用卡',
    '03': '准贷记卡',
    '04': '预付费卡',
    '05': '境外卡',
    '99': '其他',
}

WORKBENCH_BANNER_ROUTER = 'hxbusiness://OreoWeb?'

# 看板对应的url 10 30 60
