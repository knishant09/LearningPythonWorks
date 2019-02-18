import xlrd, json, re
import random

class CreateAlertDef:
    def __init__(self, probe_name):
        self.loc = "D:\\MARS_WORK\\python work\\Alertapi\\ConfigurationAlertMetrics_v1.1_Final.xlsx"
        self.wb = xlrd.open_workbook(self.loc)
        self.sheet = self.wb.sheet_by_index(0)
        self.probe_name = probe_name

    def createAlertDef(self):

        self.create_config_alert = []
        self.config_alert = {}
        for row in range(self.sheet.nrows):
            for column in range(self.sheet.ncols):
                if self.probe_name == self.sheet.cell(row, column).value:
                    self.row_list = []
                    self.row_list.append(row)
                    for i in self.row_list:
                        if self.sheet.cell_value(i, 9) != "String":

                            resource_type = self.sheet.cell_value(i, 1)
                            attr_id = self.sheet.cell_value(i, 3)
                            name = re.sub('[^A-Za-z0-9]+', '_', self.probe_name) + "_" + attr_id + "_" + str(i)
                            resource_mql = resource_type + "[=" + attr_id + " " + "rx" + " " + ".*]"
                            sev = ["critical","warning"]
                            severity = random.choice(sev)

                            condn_list = ["gt", "lt", "bt"]
                            condition = random.choice(condn_list)

                            damp = ["no_damping", "state_change", "hourly_gist", "daily_gist"]
                            damping = random.choice(damp)

                            subcrption_dict = {}

                            email = {"email": {"id": ["rohidas@domain1.com"],"damping": damping}}
                            syslog = {"syslog" : { "server": ["192.168.20.65:514:TCP"]}}
                            snmp = {"snmp" : {"manager": ["192.168.33.250"]}}

                            subcrption_dict.update(email)
                            subcrption_dict.update(syslog)
                            subcrption_dict.update(snmp)
                           # print(subcrption_dict)


                            if condition == "gt" or condition == "lt":
                                threshold = (round(random.uniform(0, 10), 4))
                                threshold = [threshold]

                            else:
                                threshold = (round(random.uniform(1,10), 4), (round(random.uniform(10,100), 4)))

                            self.config_alert.update({"name": name,
                                    "metric": attr_id,
                                     "resource_type": resource_type,
                                     "resource_mql" : resource_mql,
                                     "severity" : severity,
                                     "condition": condition,
                                     "default_threshold": threshold,
                                     "subscription" : subcrption_dict

                                             })

                            r = json.dumps(self.config_alert)

                            rl = json.loads(r)
                            self.create_config_alert.append(rl)

        config_alert_json = json.dumps(self.create_config_alert)

        print(config_alert_json)

        


def main():
    probe_name = input("Enter the Probe name as in the excel sheet:")
    obj = CreateAlertDef(probe_name)
    obj.createAlertDef()

if __name__ == "__main__":
    main()