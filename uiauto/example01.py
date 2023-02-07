import time

import uiautomator2 as u2

def sleep():
    time.sleep(2)
d = u2.connect() # connect to device
# d = u2.connect_usb('4aabc1e0')
# print(d.device_info)


# 获取窗口大小
# print(d.window_size())
# # 设备垂直输出示例: (1080, 1920)
# # 设备水平输出示例: (1920, 1080)
#
# # 获取当前应用程序信息。对于某些android设备，输出可以为空
# # print(d.current_app())
#
# # 获取设备序列号
# print(d.serial)
#
# # 获取WIFI IP
# print(d.wlan_ip)
#
# # 获取详细的设备信息
# print(d.device_info)
# print()


# 下载应用
# d.app_install('https://dl.hdslb.com/mobile/latest/android64/iBiliPlayer-bili.apk?t=20220731')

# 获取正在运行的app
# print(d.app_current())
# print(d.app_list_running())


# 设备操作
# print(d.window_size()) # 获取窗口大小
# print(d.screenshot('test.jpg')) # 获取屏幕截图
# d.push('test.jpg','/sdcard/test.jpg') # 将文件上传到设备
# d.pull('/sdcard/test.jpg','test2.jpg') # 从设备下载文件

# 按键操作
# sleep()
# d.press("home") # 点击home键
# sleep()
# d.press("back") # 点击back键
# sleep()
# d.press("left") # 点击左键
# sleep()
# d.press("right") # 点击右键
# sleep()
# d.press("up") # 点击上键
# d.press("down") # 点击下键
# d.press("center") # 点击选中
# d.press("menu") # 点击menu按键
# d.press("search") # 点击搜索按键
# d.press("enter") # 点击enter键
# d.press("delete") # 点击删除按键
# d.press("recent") # 点击近期活动按键
# d.press("volume_up") # 音量+
# d.press("volume_down") # 音量-
# d.press("volume_mute") # 静音
# d.press("camera") # 相机
# d.press("power") #电源键
# d.unlock() # 解锁设备
# 相当于
# 1. 发射活动:com.github.uiautomator.ACTION_IDENTIFY
# 2. 按home键

# 启动操作
# d.app_start('tv.danmaku.bili')# 启动指定的app
# # 停止应用
# # 相当于'am force-stop'强制停止应用
# import time
# time.sleep(5)
# d.app_stop('tv.danmaku.bili')
#
# # 相当于'pm clear' 清空App数据
# d.app_clear('com.eg.android.AlipayGphone')

# 手势与设备的交互
# 单击屏幕
# d.click(x, y)  # x,y为点击坐标
#
# # 双击屏幕
# d.double_click(x, y)
# d.double_click(x, y, 0.1)  # 默认两个单击之间间隔时间为0.1秒
#
# # 长按
# d.long_click(x, y)
# d.long_click(x, y, 0.5)  # 长按0.5秒（默认）
#
# # 滑动
# d.swipe(sx, sy, ex, ey)
# d.swipe(sx, sy, ex, ey, 0.5)  # 滑动0.5s(default)
#
# # 拖动
# d.drag(sx, sy, ex, ey)
# d.drag(sx, sy, ex, ey, 0.5)  # 拖动0.5s(default)
# # 滑动点 多用于九宫格解锁，提前获取到每个点的相对坐标（这里支持百分比）
#
# # 从点(x0, y0)滑到点(x1, y1)再滑到点(x2, y2)
# # 两点之间的滑动速度是0.2秒
# d.swipe((x0, y0), (x1, y1), (x2, y2), 0.2)

# 注意：单击，滑动，拖动操作支持百分比位置值。例：
# d.long_click(0.5, 0.5)表示长按屏幕中心
# d.swipe(0.5, 0.5, 0.5, 0.5)#表示从屏幕中心滑动到屏幕中心

# XPath：
# 检索方向
# d.orientation
# # 检索方向。输出可以是 "natural" or "left" or "right" or "upsidedown"
#
# # 设置方向
# d.set_orientation("l")  # or "left"
# d.set_orientation("r")  # or "right"
# d.set_orientation("n")  # or "natural"
#
# # 冻结/ 开启旋转
# d.freeze_rotation()  # 冻结旋转
# d.freeze_rotation(False)  # 开启旋转
#
# ########## 截图 ############
# # 截图并保存到电脑上的一个文件中，需要Android>=4.2。
# d.screenshot("home.jpg")
#
# # 得到PIL.Image格式的图像. 但你必须先安装pillow
# image = d.screenshot()  # default format="pillow"
# image.save("home.jpg")  # 或'home.png'，目前只支持png 和 jpg格式的图像
#
# # 得到OpenCV的格式图像。当然，你需要numpy和cv2安装第一个
# import cv2
#
# image = d.screenshot(format='opencv')
# cv2.imwrite('home.jpg', image)
#
# # 获取原始JPEG数据
# imagebin = d.screenshot(format='raw')
# open("some.jpg", "wb").write(imagebin)

#############################
# 转储UI层次结构
# get the UI hierarchy dump content (unicoded).（获取UI层次结构转储内容）
# d.dump_hierarchy()
#
# # 打开通知或快速设置
# d.open_notification()  # 下拉打开通知栏
# sleep()
# d.open_quick_settings()  # 下拉打开快速设置栏
#
# # 检查特定的UI对象是否存在
# d(text="Settings").exists  # 返回布尔值，如果存在则为True，否则为False
# d.exists(text="Settings")  # 另一种写法
#
# # 高级用法
# d(text="哔哩哔哩").exists(timeout=3)  # 等待'Settings'在3秒钟出现
#
# # 获取特定UI对象的信息
# d(text="Settings").info
#
# # 获取/设置/清除可编辑字段的文本(例如EditText小部件)
# d(text="Settings").get_text()  # 得到文本小部件
# d(text="Settings").set_text("My text...")  # 设置文本
# d(text="Settings").clear_text()  # 清除文本
#
# # 获取Widget中心点
# d(text="Settings").center()
# d(text="Settings").center(offset=(0, 0)) # 基准位置左前

# UI对象有五种定位方式：
# text、resourceId、description、className、xpath、坐标
# 执行单击UI对象

# text定位单击
# d(text="设置").click()
# d(text="Settings", className="android.widget.TextView").click()
#
# # resourceId定位单击
# d(resourceId="com.ruguoapp.jike:id/tv_title", className="android.widget.TextView").click()
#
# # description定位单击
# d(description="设置").click()
# d(description="设置", className="android.widget.TextView").click()
#
# # className定位单击
# d(className="android.widget.TextView").click()
#
# # xpath定位单击
# d.xpath("//android.widget.FrameLayout[@index='0']/android.widget.LinearLayout[@index='0']").click()
#
# # 坐标单击
# d.click(182, 1264)
#
# # 等待元素出现(最多10秒），出现后单击
# d(text="Settings").click(timeout=10)
#
# # 在10秒时点击，默认的超时0
# d(text='Skip').click_exists(timeout=10.0)
#
# # 单击直到元素消失，返回布尔
# d(text="Skip").click_gone(maxretry=10, interval=1.0)  # maxretry默认值10,interval默认值1.0
#
# # 点击基准位置偏移
# d(text="Settings").click(offset=(0.5, 0.5))  # 点击中心位置，同d(text="Settings").click()
# d(text="Settings").click(offset=(0, 0))  # 点击左前位置
# d(text="Settings").click(offset=(1, 1))  # 点击右下
#
# # 执行双击UI对象
# d(text="设置").double_click()  # 双击特定ui对象的中心
# d.double_click(x, y, 0.1)  # 两次单击之间的默认持续时间为0.1秒
#
# # 执行长按UI对象
# # 长按特定UI对象的中心
# d(text="Settings").long_click()
# d.long_click(x, y, 0.5)  # 长按坐标位置0.5s默认
#
# # 将UI对象拖向另一个点或另一个UI对象
# # Android<4.3不能使用drag.
# # 在0.5秒内将UI对象拖到屏幕点(x, y)
# d(text="Settings").drag_to(x, y, duration=0.5)
#
# # 将UI对象拖到另一个UI对象的中心位置，时间为0.25秒
# d(text="Settings").drag_to(text="Clock", duration=0.25)

# 常见用法：
# 等待10s
# d.xpath("//android.widget.TextView").wait(10.0)
#
# # 找到并单击
# d.xpath("//*[@content-desc='分享']").click()
#
# # 检查是否存在
# if d.xpath("//android.widget.TextView[contains(@text, 'Se')]").exists:
#     print("exists")
#
# # 获取所有文本视图文本、属性和中心点
# for elem in d.xpath("//android.widget.TextView").all():
#     print("Text:", elem.text)
#
# # 获取视图文本
# for elem in d.xpath("//android.widget.TextView").all():
#     print("Attrib:", elem.attrib)
#
# # 获取属性和中心点
# # 返回: (100, 200)
# for elem in d.xpath("//android.widget.TextView").all():
#     print("Position:", elem.center())

# xpath常见用法：
# 所有元素
# // *
# # resource-id包含login字符
# // *[contains( @ resource - id, 'login')]
#
# # 按钮包含账号或帐号
# // android.widget.Button[contains( @ text, '账号') or contains( @ text, '帐号')]
#
# # 所有ImageView中的第二个
# (// android.widget.ImageView)[2]
#
# # 所有ImageView中的最后一个
# (// android.widget.ImageView)[last()]
#
# # className包含ImageView
# // *[contains(name(), "ImageView")]

# d(resourceId="com.lianjia.beike:id/a7r").click()     # 输入之前对输入框进行click（）操作，用来获取焦点
# d.set_fastinput_ime(True)                            # 切换成FastInputIME输入法
# d.send_keys("保利学府里")                              # adb广播输入
# d.set_fastinput_ime(False)                           # 切换成正常的输入法