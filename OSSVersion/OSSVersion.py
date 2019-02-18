import os, requests


class Ossversion():
    def __init__(self):
        self.remoteapi = "http://192.168.1.93:8000/api/remoteCommand"
        self.headers = {'content-type': 'application/json'}
        self.cmd = []


        pass

    def extract_war(self):
        pass

    def app_version(self):
        pass

    def base_version_list(self):
        pass

    def call_remoteapi(self, cmd):
        inputJSON = {}
        inputJSON['ip'] = self.ip
        inputJSON['userName'] = "root"
        inputJSON['password'] = "megha.jeos"
        inputJSON['port'] = 22
        inputJSON['command'] = cmd

        response = requests.post(url=self.remoteapi, data=json.dumps(inputJSON), headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return data["commandsOutputs"]





def main():
    obj = Ossversion("192.168.33.249")

    obj.extract_war()



if __name__ == "__main__":
    main()
