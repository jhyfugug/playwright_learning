#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/19 12:27 AM
# @Author  : jhyfugug
# @File    : my_search_baidu.py


from playwright.sync_api import Page, expect

'''
Page 是类，一般首字母大写的都是类
expect 是方法或者函数
'''


def test_baidu(page: Page):
    """
    使用page 对象实例化 Page 类
    :param page:
    :return:
    """
    page.goto(url="https://www.baidu.com")  # 通过 page 使用相应的 goto 方法指向网页地址
    page.wait_for_timeout(5_000)  # 用于在特定操作完成后，加载时间的设定
    page.locator('//input[@name="wd"]').fill("playwright")  # 定位方法之一： locator ； fill方法是用于填充
    # page.get_by_text("百度一下").click()          # 定位方法之一： get_by_text
    page.locator('#su').click()
    expect(page.get_by_text(
        "https://github.com/microsoft/playwright")).to_be_visible()  # 使用 expect 断言功能； to_be_visible是作为一个显示查询
