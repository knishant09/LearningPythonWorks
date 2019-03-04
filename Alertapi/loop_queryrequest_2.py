import requests, json, ssl




def loop_query():

    while True:
            requests.packages.urllib3.disable_warnings()

            body = {
         "query":"raidLdev[@totalIOPS rx b .*]", "startTime":"20181010_000100", "endTime":"20181016_230100"
            }
            payload = json.dumps(body)

            print(payload)


            url = "https://192.168.20.162:8443/dbapi.do?action=query&dataset=defaultDs"

            headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46Q3VtdWx1c0Ax"
            }
            response = requests.post(url, data=json.dumps(body), headers=headers, verify=False)
            json_data = response.json()



            print(json_data)



loop_query()


