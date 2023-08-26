#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: substitute_once
Class: 204111/2023 Sec TA
DATE: 11:17 17/7/2023 AD
"""


def substitute_once(text: str, old: str, new: str) -> str:
    idx_old = text.find(old)
    if idx_old >= 0 and old:
        text = text[:idx_old] + new + text[idx_old + len(old):]
    return text
