import xlrd, json, re, os, time
import requests
requests.packages.urllib3.disable_warnings()


class FetchStringValue:
    def __init__(self):
        self.loc = "D:\\MARS_WORK\\python work\\Alertapi\\ConfigurationAlertMetrics_v1.1_Final.xlsx"
        self.wb = xlrd.open_workbook(self.loc)
        self.sheet = self.wb.sheet_by_index(0)
        self.probe_list = self.sheet.col_values(0)
        self.probe_list = list(dict.fromkeys(self.probe_list))


        self.resource_type = self.sheet.col_values(1)
        self.resource_type = list(dict.fromkeys(self.resource_type))


    def remove_file(self):
        myfile = "D:\\MARS_WORK\\python work\\Alertapi\\out.json"

        ## If file exists, delete it ##
        if os.path.isfile(myfile):
            os.remove(myfile)
        else:  ## Show an error ##
            print("Error: %s file not found" % myfile)

    def runload(self):
        self.remove_file()
        resource_list = []

        for row in range(self.sheet.nrows):
            for column in range(self.sheet.ncols):
                for probe in self.probe_list[2:]:
                    if probe == self.sheet.cell(row, column).value:
                        self.row_list = []
                        self.row_list.append(row)
                        for i in self.row_list:

                            #if self.sheet.cell_value(i, 9) == "String":
                             attr_id = self.sheet.cell_value(i, 3)
                             print(attr_id)
                             #res_Type = self.sheet.cell_value(i, 1)
                             res_Type = 'dfLU'
                             print(res_Type)
                             headers = {
                                'Authorization': "Basic YWRtaW46Q3VtdWx1c0Ax",
                                  'x-waitTime': '10',

                                      }

                             url = "https://" + "192.168.20.65" + ":8443/dbapi.do?" + "action=retrieveResourceData" + "&dataset=defaultDs" + "&resType=" + res_Type
                             print(url)

                             response = requests.get(url=url, headers=headers, verify=False)

                             content = response.content.decode('utf8')
                             content = content.replace('\n','')

                                #time.sleep(2)
                               # print(content)
                             content_dict = json.loads(content)


                                #print(type(content_dict))
                             val = []

                             resource_dict = {}
                             attr_dict = {}
                             for key, value in content_dict.items():
                                if isinstance(value, list) is True:
                                    for person in value:
                                        if attr_id in person:
                                              val.append(person[attr_id])
                                              val = list(dict.fromkeys(val))
                               # print(val)
                             attr_dict = {attr_id : val}
                             #print(attr_dict)
                             print(res_Type)
                             resource_dict = {res_Type : attr_dict}
                             resource_list.append(resource_dict)
        res = json.dumps(resource_list, indent=4, sort_keys=True)
        #res1 = json.loads(res)
        open("server_20.65_df.json", "a").write(res)

        print(res)



    def _fetchdata(self):
        self.runload()


        probe_type = []
        

def main():

    obj = FetchStringValue()

    obj._fetchdata()


if __name__ == "__main__":
    main()