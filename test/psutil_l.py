#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil

print(psutil.cpu_times())
print(psutil.pids())
print(psutil.Process(37845))