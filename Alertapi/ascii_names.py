import os
import json, random

def create_ascii():


       config_alert = {}
       create_config_alert = []

       list_val = [chr(i) for i in range(91, 97)]
       print(list_val)






       for i in  list_val:
           name_list = str(i) +  "_" + "1"


           print(name_list)
           config_alert.update({"name":  name_list,
                                 "metric": "speedInGbps",
                                 "resource_type": "fabCiscoPortChannel",
                                 "severity": "critical",
                                 "condition": "lt",
                                 "default_threshold": [ 0.0 ],
                                "resource_mql": "fabCiscoPortChannel[=speedInGbps rx .*]",

                                })
           r = json.dumps(config_alert)

           rl = json.loads(r)
           create_config_alert.append(rl)

       config_alert_json = json.dumps(create_config_alert, indent=4)

       print(config_alert_json)

       open("conf_ascii_alert.json", "a").write(config_alert_json)







create_ascii()