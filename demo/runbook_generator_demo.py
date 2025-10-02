import json

# Load synthetic alert
with open("synthetic_alert.json") as f:
    alert = json.load(f)

def generate_runbook(alert):
    # Toy demo function – synthetic only
    return f"""
Runbook Steps:
1. Check logs for {alert['service']}.
2. Scale up pod replicas by +2.
3. Monitor CPU usage for 15 mins.
4. If stable, continue monitoring; else escalate.
"""

if __name__ == "__main__":
    print(generate_runbook(alert))
