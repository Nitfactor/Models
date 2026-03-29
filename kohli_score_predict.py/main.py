from openai import OpenAI
import json


client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

match_history = [
    {"match": 1, "runs": 100, "run_rate": 9.5, "strike_rate": 158.73},
{"match": 2, "runs": 101, "run_rate": 9.9, "strike_rate": 165.57},
{"match": 3, "runs": 21, "run_rate": 6.3, "strike_rate": 105.00},
{"match": 4, "runs": 77, "run_rate": 9.4, "strike_rate": 157.14},
{"match": 5, "runs": 83, "run_rate": 8.4, "strike_rate": 140.68},
{"match": 6, "runs": 22, "run_rate": 8.2, "strike_rate": 137.50},
{"match": 7, "runs": 113, "run_rate": 9.4, "strike_rate": 156.94},
{"match": 8, "runs": 3, "run_rate": 2.0, "strike_rate": 33.33},
{"match": 9, "runs": 42, "run_rate": 12.6, "strike_rate": 210.00},
{"match": 10, "runs": 18, "run_rate": 15.4, "strike_rate": 257.14},
{"match": 11, "runs": 51, "run_rate": 7.1, "strike_rate": 118.60},
{"match": 12, "runs": 70, "run_rate": 9.5, "strike_rate": 159.09},
{"match": 13, "runs": 42, "run_rate": 9.3, "strike_rate": 155.56},
{"match": 14, "runs": 92, "run_rate": 11.7, "strike_rate": 195.74},
{"match": 15, "runs": 27, "run_rate": 12.5, "strike_rate": 207.69},
{"match": 16, "runs": 47, "run_rate": 9.7, "strike_rate": 162.07},
{"match": 17, "runs": 33, "run_rate": 8.2, "strike_rate": 137.50},
{"match": 18, "runs": 59, "run_rate": 9.8, "strike_rate": 163.89},
{"match": 19, "runs": 31, "run_rate": 6.2, "strike_rate": 103.33},
{"match": 20, "runs": 7, "run_rate": 7.0, "strike_rate": 116.67},
{"match": 21, "runs": 67, "run_rate": 9.6, "strike_rate": 159.52},
{"match": 22, "runs": 22, "run_rate": 9.4, "strike_rate": 157.14},
{"match": 23, "runs": 62, "run_rate": 8.3, "strike_rate": 137.78},
{"match": 24, "runs": 1, "run_rate": 2.0, "strike_rate": 33.33},
{"match": 25, "runs": 73, "run_rate": 8.1, "strike_rate": 135.19},
{"match": 26, "runs": 70, "run_rate": 10.0, "strike_rate": 166.67},
{"match": 27, "runs": 51, "run_rate": 6.5, "strike_rate": 108.51},
{"match": 28, "runs": 62, "run_rate": 11.3, "strike_rate": 187.88},
{"match": 29, "runs": 43, "run_rate": 10.3, "strike_rate": 172.00},
{"match": 30, "runs": 54, "run_rate": 10.8, "strike_rate": 180.00},
{"match": 31, "runs": 12, "run_rate": 6.0, "strike_rate": 100.00},
{"match": 32, "runs": 43, "run_rate": 7.4, "strike_rate": 122.86},
{"match": 33, "runs": 69, "run_rate": 10.9, "strike_rate": 181.58},
{"match": "venue_aggregate", "runs": 3270, "run_rate": 8.7, "strike_rate": 144.22},
{"match": "vs_csk_at_venue", "runs": 327, "run_rate": 8.6, "strike_rate": 143.42},
{"match": "recent_home_opener_2026", "runs": 69, "run_rate": 10.9, "strike_rate": 181.58}
]

prompt_text = f"""
Below is the performance data for Virat Kohli's last 33 matches and other data:
{json.dumps(match_history, indent=2)}

Based on this trend, his scoring consistency, and recent run rate, 
predict how many runs he will score in the next match. 
Provide a specific number and a short reason for your prediction.
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "You are an expert cricket statistician and performance predictor."},
        {"role": "user", "content": prompt_text}
    ]
)

print(response.choices[0].message.content)

# Model predicted a score of 54 runs 

