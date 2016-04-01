import json

def read_json():
    with open('read.json','r') as f:
        data=json.load(f)
        keylist=data.keys()
        valuelist=data.values()
        for value in valuelist:
            print value
        
def write_json():
    d = {'a': True, 'b': 'hello', 'c': None}
    data=json.dumps(d)
    print data

def main():
    read_json()
    write_json()        



if __name__ == "__main__":
    main()
