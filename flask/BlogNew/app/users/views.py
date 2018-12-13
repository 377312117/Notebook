"""
Users中的视图以及路由函数
"""


import os
from datetime import datetime
import json

from flask import Flask, redirect, render_template, request,make_response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, or_


import sys
sys.path.append("..")
from config import *
from models import *