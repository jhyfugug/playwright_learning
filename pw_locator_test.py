#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/25 7:49 PM
# @Author  : jhyfugug
# @File    : pw_locator_test.py


from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto("/demo/dialog", wait_until="networkidle")
    page.get_by_text("点我开启一个dialog").click()
    expect(page.get_by_role(role="dialog")).to_be_visible()

    page.goto("/demo/checkbox", wait_until="networkidle")
    page.get_by_role(role="checkbox", name="开发", checked=False).set_checked(True)
    page.get_by_role(role="checkbox", name="开发", checked=True).set_checked(False)

    page.goto("demo/table", wait_until="networkidle")
    page.get_by_role(role="table").count()
    expect(page.get_by_role(role="cell")).to_have_count(13)
    expect(page.get_by_role(role="img", include_hidden=True)).to_have_count(4)

    page.goto("demo/grid", wait_until="networkidle")
    expect(page.get_by_role(role="treegrid")).to_be_visible()
    expect(page.get_by_role(role="row").filter(has_text="溜达王").locator("div").nth(1)).to_have_text("44")


def test_get_by_test(page: Page):
    page.goto("/demo/getbytext", wait_until="networkidle")
    expect(page.get_by_text("确定", exact=True)).to_have_count(2)
    expect(page.get_by_text("确定")).to_have_count(3)


def test_get_by_label(page: Page):
    page.goto("/demo/input", wait_until="networkidle")
    page.get_by_label("输入你想输入的任何文字").fill("123456")


def test_get_by_placeholder(page: Page):
    page.goto("/demo/input", wait_until="networkidle")
    page.get_by_placeholder("不用管我,我是placeholder").fill("123456")


def test_get_by_title(page: Page):
    page.goto("/demo/image", wait_until="networkidle")
    expect(page.get_by_title("这是一个title")).to_be_visible()


def test_pw_new_page(page: Page):
    page.goto("/demo/link", wait_until="networkidle")
    page.get_by_text("本页跳转到百度").click()
    expect(page.get_by_text("百度一下", exact=True)).to_be_visible()

    # 跳转到新页面，使用 with 来定义操作的起始和截止。是固定用法
    page.goto("/demo/link", wait_until="networkidle")
    with page.expect_popup() as new_page:
        page.get_by_text("新页面跳转到淘宝").click()

    page_new = new_page.value
    expect(page_new.locator(".search-button").is_visible())

