#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/19 12:27 AM
# @Author  : jhyfugug
# @File    : my_search_baidu.py


from playwright.sync_api import Page, expect


def test_pw_action(page: Page):
    page.goto("/demo/button")
    page.wait_for_timeout(20_000)
