"""
[课程内容]: 实现抖音APP自动点赞操作

[授课老师]: 青灯教育-自游

[环境使用]:
    Python 3.8
    Pycharm
    雷电模拟器
    adb

[模块使用]:
    uiautomator2 ---> pip install pbr
    weditor   python -m weditor

"""
import uiautomator2 as u2
d = u2.connect()
print(d.info)
d(text='抖音').click()
d(resourceId='com.ss.android.ugc.aweme:id/g=b').click()
d.send_keys('蜘蛛膜')
d(resourceId='com.ss.android.ugc.aweme:id/op0').click()
d(className='com.lynx.tasm.behavior.ui.view.UIView').click()
d.swipe_ext("up")
d(resourceId='com.ss.android.ugc.aweme:id/container').click()
while True:
    d(resourceId='com.ss.android.ugc.aweme:id/djf').click()
    d.swipe_ext("up")