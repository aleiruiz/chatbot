import openai
import time
from handlers.assistant_profiles.Mowi import (
    tools as Mowi_tools,
    prompt as Mowi_prompt,
)


def get_existing_assistant(name):
    assistants = openai.beta.assistants.list(limit=100)
    for assistant in assistants.data:
        if assistant.name == name:
            return assistant
    return None


def get_or_create_assistant(name):
    assistant = get_existing_assistant(name)
    if assistant:
        return assistant
    else:
        new_assistant = openai.beta.assistants.create(
            name=name,
            instructions=Mowi_prompt,
            model="gpt-4o",
            tools=Mowi_tools,
        )
        return new_assistant


def create_thread():
    return openai.beta.threads.create()


def create_user_message(thread_id, message):
    return openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message,
    )


def create_and_poll(thread_id, assistant_id):
    return openai.beta.threads.runs.create_and_poll(
        thread_id=thread_id, assistant_id=assistant_id
    )


def get_last_assistant_message(thread_id):
    messages = openai.beta.threads.messages.list(thread_id=thread_id)
    for message in messages.data:
        if message.role == "assistant":
            return message.content[0].text.value if message.content else None
    return None

def submit_tool_outputs_and_poll(thread_id, run_id, tool_outputs):
    return openai.beta.threads.runs.submit_tool_outputs_and_poll(
        thread_id=thread_id, run_id=run_id, tool_outputs=tool_outputs
    )