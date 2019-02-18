import xml.etree.ElementTree as ET
import time, json, os, xlrd

class Create_configatt:
    def __init__(self):
        self.tree = ET.parse("D:\\MARS_WORK\\python work\\Alertapi\\ResourceDef.xml")
        self.root = self.tree.getroot()
        self.loc = "D:\\MARS_WORK\\python work\\Alertapi\\ConfigurationAlertMetrics_v1.1_Final.xlsx"
        self.wb = xlrd.open_workbook(self.loc)
        self.sheet = self.wb.sheet_by_index(0)
        self.xl_probe_list = self.sheet.col_values(0)
        self.xl_probe_list = list(dict.fromkeys(self.xl_probe_list))


    def _parsexml(self):
        self.remove_file()
        self.probe_list = []
        self.res_type = {}
        self.conf_attr = []
        self.probe_type = {}
        for ResourceDef in self.root.iter('ResourceDef'):

            self.res_type = {ResourceDef.get('type'): ResourceDef.get('configAttributes')}
            self.probe_type = {ResourceDef.get('requiredProbe'): self.res_type}
            self.probe_list.append(self.probe_type)

        res = json.dumps(self.probe_list, indent=4, sort_keys=True)
        open("config_resource.json", "a").write(res)
        print(res)

    def remove_file(self):
        myfile = "D:\\MARS_WORK\\python work\\Alertapi\\config_resource.json"

        ## If file exists, delete it ##
        if os.path.isfile(myfile):
            os.remove(myfile)
        else:  ## Show an error ##
            print("Error: %s file not found" % myfile)



    def _collectconfig(self):

        self.res_type = {}
        self.conf_type = []
        for ResourceDef in self.root.iter('ResourceDef'):

            for key, value in ResourceDef.items():
                for key in self.probe_list:
                    print()




                    self.probe_list.append(value)
                    self.probe_list = list(dict.fromkeys(self.probe_list))




        pass




def main():

    obj = Create_configatt()

    obj._parsexml()


if __name__ == "__main__":
    main()