import os
from strgen import StringGenerator
import strgen

class createAlert_scenario:
    def __init__(self):
        self.name = ""
        self.metric = ""
        self.resType = ""
        self.resMql = ""
        self.severity = ["critical","warning", " ", "NULL", "@#$SD"]
        self.condition = ["gt", "lt", "bt", " ", "NULL", "$@#$D"]
        self.thresh = []


    def createalert(self):
        createalert= []
        alert = {}

        self.name = strgen.StringGenerator("[\d\w\p]{30}").render()
        print(self.name)

        alert.update("")
        pass





def main():

    obj = createAlert_scenario()
    obj.createalert()

if __name__ == "__main__":
    main()

