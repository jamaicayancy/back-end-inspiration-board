from flask import Blueprint, request, jsonify, make_response
from app import db

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")