导入随机
从时间导入本地时间
从请求导入获取，发布
从日期时间导入日期时间，  日期 
从 zhdate import ZhDate
导入系统
导入操作系统


def get_color（）：
    # 获取随机颜色
    get_colors = lambda n： list（map（lambda i： “#” + “%06x” %  random.兰丁（0， 0xFFFFFF）， 范围（n)))
    color_list = get_colors（100)
    返回随机。选择（color_list)


def get_access_token（）：
    # 应用标识
    app_id = 配置[“app_id”]
    # 应用密钥
    app_secret = 配置[“app_secret”]
    post_url  = （“https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}”
.格式（app_id、app_secret))
    尝试：
        access_token = get（post_url）。json（）['access_token']
    除了键错误：
        print（“获取access_token失败，请检查app_id和app_secret是否正确”)
        操作系统。系统（“暂停”)
        系统。退出（1)
    # 打印（access_token）
    返回access_token


def get_weather（地区）：
    头 = {
        “User-Agent”： “Mozilla/5.0 （Windows NT 10.0;赢64;x64） '
                      'AppleWebKit/537.36 （KHTML， like Gecko） Chrome/103.0.0.0 Safari/537.36'
    }
    键 = 配置[“weather_key”]
    region_url  = “https://geoapi.qweather.com/v2/city/lookup?location={}&key={}”。格式（区域，键)
    响应 = get（region_url，标头=标头）。 杰森()
    如果响应[“代码”] == “404”：
        print（“推送消息失败，请检查地区名是否有误！”)
        操作系统。系统（“暂停”)
        系统。退出（1)
    ELIF 响应[“代码”] == “401”：
        print（“推送消息失败，请检查和风天气key是否正确！”)
        操作系统。系统（“暂停”)
        系统。退出（1)
    其他：
        # 获取地区的位置--id
        location_id = 响应[“位置”][0][“id”]
    weather_url  = “https://devapi.qweather.com/v7/weather/now?location={}&key={}”。格式（location_id，键)
    响应 = get（weather_url，标头=标头）。 杰森()
    # 天气
    天气 = 响应[“现在”][“文本”]
    # 当前温度
    temp = response[“now”][“temp”] + u“\N{DEGREE SIGN}” + “C”
    # 风向
    wind_dir = 响应[“现在”][“风Dir”]
    返回天气、温度、wind_dir


def get_birthday（生日，年份，今天）：
    birthday_year = 生日。分裂（“-”）[0]
    # 判断是否为农历生日
    如果 birthday_year[0] == “r”：
        r_mouth = int（生日。分裂（“-”）[1])
        r_day = int（生日。分裂（“-”）[2])
        # 获取农历生日的今年对应的月和日
        尝试：
            生日 = ZhDate（年、r_mouth、r_day）。to_datetime（）。日期()
        除了类型错误：
            print（“请检查生日的日子是否在今年存在”)
            操作系统。系统（“暂停”)
            系统。退出（1)
        birthday_month = 生日。月
        birthday_day = 生日。日
        # 今年生日
        year_date = 日期（年、birthday_month、birthday_day)

    其他：
        # 获取国历生日的今年对应月和日
        birthday_month = int（生日。分裂（“-”）[1])
        birthday_day = int（生日。分裂（“-”）[2])
        # 今年生日
        year_date = 日期（年、birthday_month、birthday_day)
    # 计算生日年份，如果还没过，按当年减，如果过了需要+1
    if today > year_date:
        if birthday_year[0] == "r":
            # 获取农历明年生日的月和日
            r_last_birthday = ZhDate（（year + 1）， r_mouth， r_day）。to_datetime（）。日期()
            birth_date = 日期（（年份 + 1），r_last_birthday。月，r_last_birthday。日)
        其他：
            birth_date = 日期（（年份 + 1）、birthday_month、birthday_day)
        birth_day = str（birth_date.__sub__（今天））。分裂（“ ”）[0]
    今天的埃利夫  == year_date：
        birth_day = 0
    其他：
        birth_date = year_date
        birth_day = str（birth_date.__sub__（今天））。分裂（“ ”）[0]
    返回birth_day


def get_ciba（）：
    网址 = “http://open.iciba.com/dsapi/”
    头 = {
        “内容类型”： “应用程序/json”，
        “User-Agent”： “Mozilla/5.0 （Windows NT 10.0;赢64;x64） '
                      'AppleWebKit/537.36 （KHTML， like Gecko） Chrome/103.0.0.0 Safari/537.36'
    }
    r = get（url， headers=headers)
    note_en = r。json（）[“content”]
    note_ch = r。json（）[“note”]
    返回note_ch， note_en


def send_message（to_user， access_token， region_name， 天气， 温度， wind_dir， note_ch， note_en）：
    URL  = “https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}”。格式（access_token)
    week_list = [“星期日”， “星期一”， “星期二”， “星期三”， “星期四”， “星期五”， “星期六”]
    年份 = 本地时间（）。tm_year
    月 = 本地时间（）。tm_mon
    日 = 本地时间（）。tm_mday
    今天 = 日期时间。日期（日期时间（年=年，月=月，日=日 ))
    周 = week_list[今天。等周日（） % 7]
    # 获取在一起的日子的日期格式
    love_year = int（config[“love_date”]。分裂（“-”）[0])
    love_month = int（config[“love_date”]。分裂（“-”）[1])
    love_day = int（config[“love_date”]。分裂（“-”）[2])
    love_date = 日期（love_year、love_month love_day)
    # 获取在一起的日期差
    love_days = str（今天。__sub__（love_date））.分裂（“ ”）[0]
    # 获取所有生日数据
    生日 = {}
    对于配置中的 k、v。项目（）：
        如果 k[0：5] == “出生”：
            生日[k] = v
    数据 = {
        “touser”：to_user，
        “template_id”： 配置[“template_id”]，
        “网址”： “http://weixin.qq.com/download”，
        “topcolor”： “#FF0000”，
        “数据”：{
            “日期”：{
                “值”： “{} {}”。格式（今天，周），
                “颜色”：get_color()
},
            “区域”：{
                “值”：region_name，
                “颜色”：get_color()
},
            “天气”：{
                “价值”：天气，
                “颜色”：get_color()
},
            “温度”：{
                “值”：温度，
                “颜色”：get_color()
},
            “wind_dir”：{
                “值”：wind_dir，
                “颜色”：get_color()
},
            “love_day”：{
                “值”：love_days，
                “颜色”：get_color()
},
            “note_en”：{
                “值”：note_en，
                “颜色”：get_color()
},
            “note_ch”：{
                “值”：note_ch，
                “颜色”：get_color()
            }
        }
    }
    对于键，生日中的值。项目（）：
        # 获取距离下次生日的时间
        birth_day = get_birthday（值[“生日”]，年份，今天)
        如果birth_day == 0：
            birthday_data = “今天{}生日哦，祝{}生日快乐！”。格式（值[“名称”]， 值[“名称”])
        其他：
            birthday_data = “距离{}的生日还有{}天”。format（value[“name”]， birth_day)
        # 将生日数据插入数据
        data[“data”][key] = {“value”： birthday_data， “color”： get_color()}
    头 = {
        “内容类型”： “应用程序/json”，
        “User-Agent”： “Mozilla/5.0 （Windows NT 10.0;赢64;x64） '
                      'AppleWebKit/537.36 （KHTML， like Gecko） Chrome/103.0.0.0 Safari/537.36'
    }
    response = post（url， headers=headers， json=data）.杰森()
    如果响应[“错误代码”] == 40037：
        print（“推送消息失败，请检查模板id是否正确”)
    ELIF 响应[“错误代码”] == 40036：
        print（“推送消息失败，请检查模板ID是否为空”)
    ELIF 响应[“错误代码”] == 40003：
        print（“推送消息失败，请检查微信号是否正确”)
    ELIF 响应[“错误代码”] == 0：
        print（“推送消息成功”)
    其他：
        打印（响应)


如果__name__ == “__main__”：
    尝试：
        使用 open（“config.txt”， encoding=“utf-8”） 作为 f：
            config = eval（f.读())
    除了 FileNotFoundError：
        print（“推送消息失败，请检查config.txt文件是否与程序位于同一路径”)
        操作系统。系统（“暂停”)
        系统。退出（1)
    除了语法错误：
        print（“推送消息失败，请检查配置文件格式是否正确”)
        操作系统。系统（“暂停”)
        系统。退出（1)

    # 获取访问令牌
    访问令牌 = get_access_token()
    # 接收的用户
    用户 = 配置 [“用户”]
    # 传入地区获取天气信息
    区域 = 配置[“区域”]
    天气、温度、wind_dir = get_weather（区域）)
    note_ch = 配置[“note_ch”]
    note_en = 配置[“note_en”]
    如果note_ch == “” 和 note_en == “”：
        # 获取词霸每日金句
        note_ch，note_en = get_ciba()
    # 公众号推送消息
    对于用户中的用户：
        send_message（用户、访问令牌、地区、天气、温度、wind_dir、note_ch、note_en)
    操作系统。系统（“暂停”)
