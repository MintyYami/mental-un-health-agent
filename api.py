import google.generativeai as genai
import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

# configure API key
genai.configure(api_key="")
# configure model version
model = genai.GenerativeModel("gemini-2.5-flash-lite")


# prompting
def check_depressed_state(input):
    response = model.generate_content(f"Analyse this input on a scale of 1 to 10, with 10 being the happiest, and 1 being the saddest. Respond with only a singular number. Input: {input}")
    return response.text

def get_response(input):
    response = model.generate_content(f"Check if input is a simple greeting. If it is, greet back normally. If not, give me one roast about being a CS major, and try to incorporate the input into the response where possible. Do not add explanation. Input: {input}")
    return response.text
