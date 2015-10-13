import pickle
import json

### 1. Generate the department links
def department_list():
    with open('departments.json') as data_file:
        data = json.load(data_file)
    links = []
    for dep in data:
        for x in xrange(0, len(dep["title"])):
            val = "http://www.iitkgp.ac.in/commdir3/"+str(dep["title"][x])
            links.append(val)
    deplinks = open('deplinks.pkl', 'wb')
    pickle.dump(links, deplinks)

### 2. Generate the professor links
def professor_list():
    with open('professor.json') as data_file:
        data = json.load(data_file)
    links = []
    for dep in data:
        for x in xrange(0, len(dep["title"])):
            val = "http://www.iitkgp.ac.in"+str(dep["title"][x])
            links.append(val)
    proflinks = open('proflinks.pkl', 'wb')
    pickle.dump(links, proflinks)

### 3. Generate the research area links
def query_list():
    with open('prof_details.json') as data_file:
        data = json.load(data_file)
    finallist = []
    for prof in data:
        for field in prof["field"]:
            d = {}
            d["field"] = field
            d["link"] = prof["title"]
            d["name"] = prof["name"]
            finallist.append(d)

    with open('finallist.json', 'w') as outfile:
        json.dump(finallist, outfile)


def main():
    department_list()
    professor_list()
    query_list()

if __name__ == '__main__':
    main()
