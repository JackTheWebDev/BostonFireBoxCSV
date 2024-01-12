"""
    JackTheWebDev
    January 12, 2024
    Dataset last updated  	September 14, 2023
    https://data.boston.gov/dataset/fire-alarm-boxes
"""

import json

with open("Fire_Alarm_Boxes.geojson", "r+") as file:
    jsonData = json.loads(file.read())

    outputFile = open("boxLists.csv", "w")
    outputFile.write("BOX, DISTRICT, LAT, LONG\n")


    for x in jsonData["features"]:
        print("Writing BOX " + x["properties"]["BOX"] + " is at: " + str(x["geometry"]["coordinates"]) + " in District: " +
              x["properties"]["DISTRICT"])
        outputFile.write(x["properties"]["BOX"]+","+x["properties"]["DISTRICT"]+","+str(x["geometry"]["coordinates"][0])+","+str(x["geometry"]["coordinates"][1])+"\n")