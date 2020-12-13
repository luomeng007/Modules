# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/12/13 11:57
software: PyCharm

Description:
"""
import psutil

print(psutil.cpu_count())  # get the number of logical CPUs: 8
print(psutil.cpu_freq())  # CPU frequency scpufreq(current=1992.0, min=0.0, max=1992.0)MHz
print(psutil.net_io_counters()[:2])  # get bytes send and bytes received
