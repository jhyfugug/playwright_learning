#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/19 12:27 AM
# @Author  : jhyfugug
# @File    : my_search_baidu.py


from playwright.sync_api import Page


def test_baidu(page: Page):
    page.goto(url="https://www.baidu.com")
    page.wait_for_timeout(5_000)
