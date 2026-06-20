from flask import Flask, render_template, request, jsonify, session
import chess
import chess.polyglot
import random
import time
import os
import uuid
from functools import wraps
from typing import Optional, Dict, Any