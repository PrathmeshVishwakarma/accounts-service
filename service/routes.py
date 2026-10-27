"""
RESTful routes for the Accounts service.
"""
from flask import Blueprint, abort, jsonify, request

from service.models import Account

api = Blueprint("api", __name__)

REQUIRED_FIELDS = ("name", "email")


@api.route("/accounts", methods=["GET"])
def list_accounts():
    """List all accounts."""
    accounts = Account.query.order_by(Account.id).all()
    return jsonify([account.to_dict() for account in accounts]), 200


@api.route("/accounts", methods=["POST"])
def create_account():
    """Create a new account."""
    data = request.get_json(silent=True) or {}
    missing = [field for field in REQUIRED_FIELDS if not data.get(field)]
    if missing:
        abort(400, description=f"Missing required field(s): {', '.join(missing)}")

    account = Account()
    account.from_dict(data)
    account.create()
    return jsonify(account.to_dict()), 201


@api.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    """Read a single account."""
    account = Account.query.get(account_id)
    if not account:
        abort(404, description=f"Account {account_id} not found")
    return jsonify(account.to_dict()), 200


@api.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update an existing account."""
    account = Account.query.get(account_id)
    if not account:
        abort(404, description=f"Account {account_id} not found")

    account.from_dict(request.get_json(silent=True) or {})
    account.update()
    return jsonify(account.to_dict()), 200


@api.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete an account."""
    account = Account.query.get(account_id)
    if not account:
        abort(404, description=f"Account {account_id} not found")

    account.delete()
    return "", 204
