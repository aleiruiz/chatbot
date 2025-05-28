from handlers.openai.tools import should_run_tool_calls
from handlers.twilio.client import send_message
from db.redis import get_session, set_session
from handlers.openai.assistant import get_or_create_assistant, create_thread, create_and_poll, create_user_message, get_last_assistant_message

def inbound_chat_impl(from_id, message):
    """
    This function handles inbound chat messages from Twilio. It retrieves or creates an assistant,
    manages the session, and processes the user's message to generate a response.
    """
    if not from_id or not message:
        return 'Missing from_id or message', 400
        
    assistant = get_or_create_assistant("Karlos")
    thread_id = get_session(from_id)

    if(thread_id is None):
        thread = create_thread()
        # Create a new session for the user
        set_session(from_id, thread.id)
        thread_id = thread.id
    
    create_user_message(thread_id=thread_id, message=message)

    run = create_and_poll(thread_id=thread_id, assistant_id=assistant.id)

    should_run_tool_calls(run, thread_id)

    response = get_last_assistant_message(thread_id=thread_id)

    send_message(to=from_id, body=response)

    return {"message": "ok"}, 200