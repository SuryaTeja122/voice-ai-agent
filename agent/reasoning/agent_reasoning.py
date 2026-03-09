import openai
import json
from agent.tools.appointment_tools import book_appointment

openai.api_key = "YOUR_OPENAI_API_KEY"

SYSTEM_PROMPT = """
You are a healthcare appointment assistant.

Available tools:
1. book_appointment
2. cancel_appointment
3. reschedule_appointment
4. check_availability

Return response in JSON format.

Example:
{
 "intent": "book",
 "doctor": "cardiologist",
 "date": "tomorrow"
}
"""

def agent_response(user_input):

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":user_input}
        ]
    )

    content = response.choices[0].message.content

    data = json.loads(content)

    if data["intent"] == "book":
        return book_appointment("patient1", data["doctor"], data["date"])

    if data["intent"] == "cancel":
        return "Your appointment has been cancelled."

    if data["intent"] == "reschedule":
        return "Your appointment has been rescheduled."

    return "I did not understand your request."