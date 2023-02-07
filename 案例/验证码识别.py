"""
[课程内容]: 简单实现验证码识别

[授课老师]: 青灯教育-自游

[环境使用]:
    Python 3.8
    Pycharm
[模块使用]:
    ddddocr  ---> pip install ddddocr

"""
import ddddocr

ocr = ddddocr.DdddOcr()

with open('img_3.png', 'rb') as f:
    img_bytes = f.read()

result = ocr.classification(img_bytes)
print(result)



