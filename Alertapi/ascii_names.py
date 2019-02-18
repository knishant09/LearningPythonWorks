import os
import json

def create_ascii():


       config_alert = {}
       create_config_alert = []

       list_val = [chr(i) for i in range(32, 127)]
       print(list_val)

       for i in list_val:
           config_alert.update({"name": i,
                                 "metric": "migrationStatus",
                                 "resource_type": "raidLdev",
                                 "severity": "critical",
                                 "condition": "having",
                                 "default_threshold": [ "Suspend"],
                                 })
           r = json.dumps(config_alert)

           rl = json.loads(r)
           create_config_alert.append(rl)

       config_alert_json = json.dumps(create_config_alert, indent=4)

       print(config_alert_json)

       open("conf_ascii_alert.json", "a").write(config_alert_json)







create_ascii()