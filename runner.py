import logging
import csv

from dotenv import dotenv_values

from mongo_helper import MongoConnection, create_selection_in_mongo

logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

entityTypeCounter = {}

config = dotenv_values(".env")
connection_string = config["ATLAS_URI"]
mongo_connection = MongoConnection(connection_string)


# name: String!
# group: String
# category: String
# reason: String
# dataSource: String
# minAgeCondition: Float
# maxAgeCondition: Float
# chiefComplaintCondition: String
# presentInTranscript: String
# absentInTranscript: String
# timing:String
# timingAlternative: String
# alert: String
# providerAction: String
# actionType: String
# outcome: String
# appendedBlended: String
# nudgeSource: String
# example: String
# exclusionCriteria: String
# section:String
# placement: String


if __name__ == '__main__':
    print("here")
    mongo_connection.ping()

    reminders = []

    with open(config['CSV_PATH']) as csvfile:
        spamreader = csv.reader(csvfile, dialect='excel')

        for idx, row in enumerate(spamreader):
            if idx == 0:
                continue
            reminder = {
                "group": row[0],
                "name": row[1],
                "category": row[2],
                "reason": row[3],
                "dataSource": row[4],
                "presentInTranscript": row[7],
                "absentInTranscript": row[8],
                "timing": row[10],
                "timingAlternative": row[11],
                "alert": row[12],
                "providerAction": row[13],
                "actionType": row[14],
                "outcome": row[15],
                "appendedBlended": row[16],
                "nudgeSource": row[17],
                "example": row[18],
                "exclusionCriteria": row[20],
                "section": row[21],
                "placement": row[22],
                "__typename": "Reminder",
                "status": "ACTIVE",
                "createdAt": "2024-07-26T04:03:58.618Z"
            }
            # logging.info(row)
            savedReminder = create_selection_in_mongo(mongo_connection.reminders_collection, reminder)

            logging.info(savedReminder)



