import requests
import time
last_time_alert={}
bot_token="8904393857:AAE_cBuzmlFWOLFrCiU6KUAaVrloKpeRFIY"

def send_message(message):

    url=(
        f"https://api.telegram.org/bot"
        f"{bot_token}/sendMessage" 
        )
    payLoad={
        "chat_id": 1421002065,
        "text": message
    }
    try:
        requests.post(
            url,
            data=payLoad,
            timeout=10)
        
    except Exception as e :
        print(f"telegram error:{e}")



def can_send_alert(alert_type):

    if alert_type not in last_time_alert:
        last_time_alert[alert_type] = time.time()
        return True
    elapsed_time=time.time() - last_time_alert[alert_type]      

    if elapsed_time > 15*60:
        last_time_alert[alert_type] = time.time()
        return True
    return False




# fire  alert 
def fire_alert_func():
    if can_send_alert("fire_alert"):
         send_message("Fire detected ")


# smoke alert
def smoke_alert_func():
    if can_send_alert("smoke_alert"):
        send_message("Smoke detected")


# crowd alert
def crowd_alert_func():
  if can_send_alert("crowd_alert"):
      send_message("Crowd Alert: more than 12 people detected")

# ppe violation alert
def ppe_violation_alert(violating_ids):
  if can_send_alert("ppe_violation_alert"):
    send_message(f"PPE Violation detected for IDs: {violating_ids}")                   

