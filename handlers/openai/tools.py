import os
import json
import pandas as pd
from handlers.openai.assistant import submit_tool_outputs_and_poll

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, "assets", "sample_caso_ai_engineer.csv")

def fetch_vehicles_data():
    """
    Function to fetch a csv with information about vehicles, specifically, Mileage, Price, Maker, Model, Year,
    Version, Bluetooth availability, Length, Width, Height, and Car Play availability.
    """
    df = pd.read_csv(csv_file_path)
    return df.to_json(orient="records", indent=2)

def fetch_credit_estimate(args):
    """
    Fetch credit estimate using stock id, and timespan
    """
    args_data = json.loads(args)
    stock_id = args_data.get("stock_id")
    time_span = float(args_data.get("time_span"))
    down_payment = float(args_data.get("down_payment", 0))

    df = pd.read_csv(csv_file_path)

    stock = df[df["stock_id"] == stock_id].head(1)

    if stock.empty:
        return {
            "error": f"No vehicle found with stock_id {stock_id}."
        }
    
    vehicle_info = stock.iloc[0].to_dict()
    price = vehicle_info.get("price", 0)
    financing_amount = price - down_payment
    total_price = down_payment + (financing_amount * (1 + 0.10) ** time_span)
    monthly_payment = total_price / (time_span * 12)

    return {
        "stock_id": stock_id,
        "time_span": time_span,
        "interest_rate": 10,
        "down_payment": down_payment,
        "financing_amount": financing_amount,
        "total_price": total_price,
        "monthly_payment": monthly_payment,
    }

def should_run_tool_calls(run, thread_id):
    """
    Check if tool calls should be run.
    """
    # This function can be expanded to include more complex logic
    if run.required_action and run.required_action.submit_tool_outputs and run.required_action.submit_tool_outputs.tool_calls:
        tool_outputs = []
        for tool_call in run.required_action.submit_tool_outputs.tool_calls:
            if tool_call.function.name == "fetch_vehicles_data":
                tool_outputs.append({
                    "tool_call_id": tool_call.id,
                    "output": json.dumps(fetch_vehicles_data()),
                })
            if tool_call.function.name == "fetch_credit_estimate":
                tool_outputs.append({
                    "tool_call_id": tool_call.id,
                    "output": json.dumps(fetch_credit_estimate(tool_call.function.arguments)),
                })

        if(len(tool_outputs) > 0):
            run = submit_tool_outputs_and_poll(thread_id=thread_id, run_id=run.id, tool_outputs=tool_outputs)
            return should_run_tool_calls(run, thread_id)
    return False    
