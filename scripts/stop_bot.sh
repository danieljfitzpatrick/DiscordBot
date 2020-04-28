#!/bin/bash

kill -9 $(ps aux | grep 'bot.py' | awk '{print $2}')