import requests, time, json
from pprint import pprint

class ArDiag():
    def __init__(self, ip):
        self.ip = ip
        self.remoteapi = "http://192.168.1.108:8000/api/remoteCommand"
        self.headers = {'content-type': 'application/json'}
        self.cmd = ["date", "", "cat /etc/hosts | tail -4"]



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

    def fetch_nodedetails(self):

        self.cluster_node_url = "http://{}:8088/ws/v1/cluster/nodes".format(self.ip)
        response = requests.get(url=self.cluster_node_url)

        self.data = response.json()

    def fetch_clustermetrics(self):
        self.clustermetrics_url = "http://{}:8088/ws/v1/cluster/metrics".format(self.ip)
        response = requests.get(url=self.clustermetrics_url)

        self.metricsdata = response.json()

    def cpu_mem_metrics(self):
        try:
            data = self.call_remoteapi([self.cmd[1]])
            str1 ='\n'.join(data)
            return str1
        except Exception as e:
            return False

    def date_time(self):
        try:
            data = self.call_remoteapi([self.cmd[0]])
            str1 ='\n'.join(data)
            return str1
        except Exception as e:
            return False

    def cluster_ips(self):
        try:
            data = self.call_remoteapi([self.cmd[2]])
            str1 = '\n'.join(data)
            return str1
        except Exception as e:
            return False


    def diag_report(self):
        self.fetch_clustermetrics()
        cluster_metricdetail = json.dumps(self.metricsdata)
        cluster_ds = json.loads(cluster_metricdetail)


        self.fetch_nodedetails()
        node_details = json.dumps(self.data)
        datastore = json.loads(node_details)
        worker_list = datastore["nodes"]["node"]




        strnodeTable = "<html><table border =1><tr style='text-align:right;padding:20px;'><b> Worker Node Health Details</b></tr><tr><th> Date</th><th>Worker ID</th><th>PhyicalMem(MB)</th><th>VirtualMem(MB)</th><th>CPU Usage</th><th>Aggr. Containers PhysicalMem(MB)</th><th>Aggr. Containers VirtualMem(MB)</th><th>ContainerCPU Usage</th><th>Worker available Memory(MB)</th><th>Worker Running Containers</th><th>Worker AvailableVirtualcore</th></tr>"

        for i in reversed(range(len(worker_list))):
            print("********{}******".format(i))
            print(worker_list[i]["id"])
            print(type(worker_list[i]["id"]))


            strnodeRW =  "<tr style='text-align:center;padding:15px;'><td>" + self.date_time() + "</td> <td>" + str(worker_list[i]["id"]) + "</td> <td>" + str(worker_list[i]["resourceUtilization"]["nodePhysicalMemoryMB"]) + "</td><td>" + str(worker_list[i]["resourceUtilization"]["nodeVirtualMemoryMB"]) + "</td> <td>" + str(worker_list[i]["resourceUtilization"]["nodeCPUUsage"]) + "</td> <td>" + str(worker_list[i]["resourceUtilization"]["aggregatedContainersPhysicalMemoryMB"]) + "</td> <td>" + str(worker_list[i]["resourceUtilization"]["aggregatedContainersVirtualMemoryMB"]) + "</td> <td>" + str(worker_list[i]["resourceUtilization"]["containersCPUUsage"]) + "</td>  <td>" + str(worker_list[i]["availMemoryMB"]) + "</td><td>" + str(worker_list[i]["numContainers"]) + "</td><td>" + str(worker_list[i]["availableVirtualCores"]) + "</td></tr>"
         #   strnodeRW = "<tr style='text-align:center;padding:15px;'><td>" + self.date_time() + "</td> <td>" + worker_list[i]["id"] + "</td> </tr>"
            strnodeTable = strnodeTable + strnodeRW

        strTable = "<html><table border =1><tr style='text-align:right;padding:20px;'><b>  Cluster Metric Report </b> </tr><tr><th>Apps Submitted</th><th>Apps completed</th><th>Available MB</th><th>Allocated MB</th><th>Total MB</th><th>Total Virtual core</th><th>Available VirtualCore</th><th>Allocated VirtualCore</th><th> MASTER CPU/MEM </th></tr>"
        strRW = "<tr style='text-align:center;padding:15px;'><td>" + str(cluster_ds["clusterMetrics"]["appsSubmitted"]) + "</td> <td>" + str(cluster_ds["clusterMetrics"]["appsCompleted"]) + "</td> <td>" + str(cluster_ds["clusterMetrics"]["availableMB"]) + "</td> <td>" + str(cluster_ds["clusterMetrics"]["allocatedMB"]) + "</td> <td>" + str(cluster_ds["clusterMetrics"]["totalMB"]) + "</td> <td>" + str(cluster_ds["clusterMetrics"]["totalVirtualCores"]) + "</td> <td>" + str(cluster_ds["clusterMetrics"]["availableVirtualCores"]) + "</td> <td>" + str(cluster_ds["clusterMetrics"]["allocatedVirtualCores"])+ "</td> <td style='white-space:pre;text-align:left;'>" + self.cpu_mem_metrics() + "</td> </tr>"

        strhostdetailsTable = "<html><table border =1><tr style='text-align:right;padding:20px;'><b>  Cluster Host Details </b> </tr>"

        strhostdetailsRW = "<tr style='white-space:pre;'><td>" + self.cluster_ips() + "</td> </tr>"

        strhostdetailsTable = strhostdetailsTable + strhostdetailsRW

        strTable = strTable + strRW

        strhostdetailsTable = strhostdetailsTable + "</table></html>"
        strTable = strTable + "</table></html>"
        strnodeTable = strnodeTable + "</table></html>"

        hs = open("AR_diag_report.html", 'w')
        hs.write(strhostdetailsTable)
        hs.write(strTable)
        hs.write(strnodeTable)
        hs.close()


def main():
    obj = ArDiag("192.168.36.120")

    obj.diag_report()


if __name__ == "__main__":
    main()


