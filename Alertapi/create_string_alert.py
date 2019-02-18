import time, json, os, random

class Create_String_config:
    def __init__(self):
        self.loc = "D:\\MARS_WORK\\python work\\Alertapi\\confAlertDefaultThresholdValues.json"

        with open(self.loc) as f:
            self.data = json.load(f)



    def create_body(self):
        print(self.data)
        print("*********************")

        self.create_config_alert = []
        self.config_alert = {}

        for i in range(len(self.data)):

            sev = ["critical", "warning"]
            severity = random.choice(sev)

            damp = ["no_damping", "state_change", "hourly_gist", "daily_gist"]
            damping = random.choice(damp)

            subcrption_dict = {}

            email = {"email": {"id": ["nishant@domain1.com"], "damping": damping}}
            syslog = {"syslog": {"server": ["192.168.34.144:514:TCP"]}}
            snmp = {"snmp": {"manager": ["192.168.33.250"]}}

            subcrption_dict.update(email)
            subcrption_dict.update(syslog)
            subcrption_dict.update(snmp)

            resource_type = self.data[i].get('resType')
            attr_id = self.data[i].get('attrList')
           # print(resource_type)

            for i in range(len(attr_id)):
               # print(attr_id[i])
               # print(type(attr_id[i]))
                conf_attr_id = attr_id[i].get('attrId')
                resource_mql = resource_type + "[=" + conf_attr_id + " " + "rx" + " " + ".*]"

                for threshold in attr_id[i].get('preDefinedValues'):

                    name = resource_type + '_' + conf_attr_id + '_' + threshold + '_' + str(i)




                    self.config_alert.update({
                                      "name" : name.replace(' ', '_'),
                                      "metric": conf_attr_id,
                                      "resource_type": resource_type,
                                      "resource_mql": resource_mql,
                                      "severity": severity,
                                      "condition": "having",
                                      "default_threshold": [threshold],
                                      "subscription": subcrption_dict
                                      })

                    r = json.dumps(self.config_alert)

                    rl = json.loads(r)
                    self.create_config_alert.append(rl)

        config_alert_json = json.dumps(self.create_config_alert, indent=4)

        print(config_alert_json)

        open("config_alert_out.json", "a").write(config_alert_json)










def main():

    obj = Create_String_config()
    obj.create_body()


if __name__ == "__main__":
    main()
