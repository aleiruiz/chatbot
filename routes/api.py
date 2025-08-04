from flask import Blueprint, request
from implementation.chatbot import inbound_chat_impl
from flasgger import swag_from
from specs.api_specs import inbound_chat_specs

api = Blueprint("api", __name__)


@api.route("/twilio/inbound", methods=["POST"])
@swag_from(inbound_chat_specs)
def inbound_chat():
    return inbound_chat_impl(
        from_id=request.form.get("From"), message=request.form.get("Body")
    )
