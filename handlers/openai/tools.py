import os
import json
import pandas as pd
from handlers.openai.assistant import submit_tool_outputs_and_poll

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, "assets", "sample_caso_ai_engineer.csv")


def check_address():
    return {"lat": -34.8530369, "lng": -56.2007495}


def verify_client():
    return {"success": True}


def request_trip():
    return {
        "sucess": True,
        "message": "Trip has been scheduled and a notification has been generated",
    }


def request_quote():
    return {"success": True, "message": "Quote has been sent to email"}


def fetch_estimated_fare():
    return {"amount": 530, "km": 6.8, "minutes": 12}


def should_run_tool_calls(run, thread_id):
    """
    Check if tool calls should be run.
    """
    # This function can be expanded to include more complex logic
    if (
        run.required_action
        and run.required_action.submit_tool_outputs
        and run.required_action.submit_tool_outputs.tool_calls
    ):
        tool_outputs = []
        for tool_call in run.required_action.submit_tool_outputs.tool_calls:

            if tool_call.function.name == "check_address":
                tool_outputs.append(
                    {
                        "tool_call_id": tool_call.id,
                        "output": json.dumps(check_address()),
                    }
                )
            if tool_call.function.name == "verify_client":
                tool_outputs.append(
                    {
                        "tool_call_id": tool_call.id,
                        "output": json.dumps(verify_client()),
                    }
                )
            if tool_call.function.name == "request_trip":
                tool_outputs.append(
                    {
                        "tool_call_id": tool_call.id,
                        "output": json.dumps(request_trip()),
                    }
                )
            if tool_call.function.name == "request_quote":
                tool_outputs.append(
                    {
                        "tool_call_id": tool_call.id,
                        "output": json.dumps(request_quote()),
                    }
                )
            if tool_call.function.name == "fetch_estimated_fare":
                tool_outputs.append(
                    {
                        "tool_call_id": tool_call.id,
                        "output": json.dumps(fetch_estimated_fare()),
                    }
                )

        if len(tool_outputs) > 0:
            run = submit_tool_outputs_and_poll(
                thread_id=thread_id, run_id=run.id, tool_outputs=tool_outputs
            )
            return should_run_tool_calls(run, thread_id)
    return False
