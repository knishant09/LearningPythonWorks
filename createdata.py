import requests, sys, json
import datetime, random



class dataload():

    def __init__(self, *args):
        self.ip = args.__getitem__(0)
        self.auth = args.__getitem__(1)
        self.ts = args.__getitem__(2)
        self.storagelst = args.__getitem__(3)

    def createjson(self, i):
        print(i)
        my_data = {}
        meta = {}
        meta.update({"ts": self.ts, "dataSubsetId": "CumulusSystems_421358_G200"})
        my_data.update({"meta": meta})
        resources = []
        res_sig_values = {}
        self.res_sig = "raidLdev#421358-"+ str(i) +"^"+ str(i) +"^"+ str(i)+""
        print(self.res_sig)
        self.name = "421358-"+ str(i) +":"+ str(i) +":"+ str(i) +""
        print(self.name)
        self.voltype = "OPEN-V-CVS"
        res_sig_values.update({"signature": self.res_sig, "name": self.name, "volumeType": self.voltype})
        totalIOPS = []
        time_duration = {}
        self.data = []
        for i in range(10):
            self.data.append(random.randint(1, 100))
        time_duration.update({"from": self.ts, "interval": 5, "data": self.data})
        self.relationsLst = []
        self.relationsLst.append(self.storagelst)
        totalIOPS.append(time_duration)
        res_sig_values.update({"totalIOPS": totalIOPS})
        res_sig_values.update({"relationsCompleteList": self.relationsLst})
        resources.append(res_sig_values)
        my_data.update({"resources": resources})
        my_data_json = json.dumps(my_data)

        return my_data_json




    def runload(self, testjson):
        print(testjson)
        print("***************************")

        headers = {
            'Authorization': self.auth,
            'Content-Type': 'application/json',
            'x-waitTime': '10',
        }

        params = (
            ('action', 'createOrUpdateResourceData'),
            ('dataset', 'defaultDs')
        )

        data = testjson
        requests.packages.urllib3.disable_warnings()
        post_url = "https://"+ self.ip +":8443/dbapi.do"

        response = requests.post(post_url, headers=headers, params=params, data=data,
                                 verify=False)
        print("-------------------")
        print(response.content)
        print(response.request)
        print(response.headers)
        print(response)


def main():

   #passing IP, Basic Auth, Timestamp,storage
    obj = dataload("192.168.33.21", "Basic YWRtaW46Q3VtdWx1c0Ax", "20180706_000000", "raidStorage#421358")
    for i in range(99, 59000):
        print(i)
        testjson = obj.createjson(i)
        #print(testjson)
        obj.runload(testjson)


if __name__ == "__main__":
    main()


