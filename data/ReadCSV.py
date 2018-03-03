import datetime
import csv
from icalendar import Calendar, Event
import tempfile, os
import json

input_file = csv.reader(open('C:/Users/Jonas/Documents/OpenDataDay/OpenParl/ris-scraper/data/sitzungsplan.csv'))

results ={}



for row_number, row  in enumerate(input_file):
    if row_number > 0:
        key = row[0].strip()
        results[key] = []
        for i in range(1,13):
           # print(row[i])
            row[i] = row[i].split('\n')
            date_list = [elem.strip() for elem in row[i]]
            for date in date_list:
                if len(date)>0:
                    results[key].append(date)

now = datetime.datetime.now()
for key in results.keys():
    results[key] = [datetime.datetime.strptime(elem+ str(now.year),'%d.%m.%Y') for elem in results[key]]

print(results)


directory = os.path.dirname(os.path.realpath(__file__))
for key in results.keys():
    cal = Calendar()
    cal['summary'] = results[key]

    for value in results[key]:
        event = Event()
        event.add('dtstart', value)
        cal.add_component(event)
    f = open(os.path.join(directory, str(key)[:15]+'.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()


for key in results.keys():
    results[key] = [elem.timestamp() for elem in results[key]]

with open('data.json', 'w') as outfile:
    json.dump(results, outfile)

