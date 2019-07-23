#!/bin/bash
sysctl -w kernel.shmmax=67108864
sysctl -w kernel.shmmni=8192
sysctl -w kernel.sem="250 32000 32 9216"
