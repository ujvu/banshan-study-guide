#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 template.html 里的 {{IMG_xxxx}} 占位符替换成 build/IMG_xxxx.jpg 的 base64 内嵌数据，
生成单文件网页：半山国家森林公园-中班研学提示.html

用法：
  python3 -B build.py

改内容时直接编辑 template.html，然后重新运行本脚本即可。
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "template.html")
OUT = os.path.join(HERE, "半山国家森林公园-中班研学提示.html")
PHOTOS = ["IMG_2844", "IMG_2851", "IMG_2849", "IMG_2848",
          "IMG_2847", "IMG_2846", "IMG_2845"]  # 顺序对应页面点位 ①—⑦

html = open(TPL, encoding="utf-8").read()
for name in PHOTOS:
    src = os.path.join(HERE, "build", name + ".jpg")
    token = "{{%s}}" % name
    if token not in html:
        raise SystemExit(f"模板里找不到占位符 {token}")
    html = html.replace(token, "data:image/jpeg;base64," +
                        base64.b64encode(open(src, "rb").read()).decode())

open(OUT, "w", encoding="utf-8").write(html)
print(f"已生成 {OUT}  ({os.path.getsize(OUT)/1024/1024:.2f} MB)")
