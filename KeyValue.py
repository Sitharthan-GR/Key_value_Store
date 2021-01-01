import os
import json
import sys
from datetime import datetime,timedelta
from json.decoder import JSONDecodeError
class DataBase:
    def __init__(self,file_loc=None,fname=None):
        if file_loc is None:
            self.file_loc="./DB"
        else:
            self.file_loc=file_loc
        if fname is None:
            self.fname=os.path.basename(sys.argv[0][:-3])
        else:
            self.fname=fname
        
        os.makedirs(self.file_loc,exist_ok=True)
        self.path=self.file_loc+"/{}.json".format(self.fname)
    
    def create(self,key,value,t2l=None):
        
            
        
        
            timestamp=datetime.now().time()
            if len(key)>32:
                print("ERROR:length of key should be less than 32")
                return False
            if sys.getsizeof(value)>16000:
                print("ERROR: file size should be less than 16 kb")
                return False
            if os.path.exists(self.path):
                self.data=json.load(open(self.path,'r'))
            else:
                self.data={}
            try:
                if key in self.data:
                    print("ERROR: key already exists")
                else:
                    dicto={"value":value,"timestamp":str(timestamp),"t2l":t2l}
                    self.data[str(key)]=dicto
                try:
                    json.dump(self.data,open(self.path,'w+'))
                    file_size=os.path.getsize(self.path)
                    if(file_size<=1073741824):
                        return True
                    else:
                        print("File Size exceeds 1 GB(limit)")
                        return False
                except:
                    return False
            except Exception as e:
                print("[X] Error Saving Values to Database : " + str(e))
                return False
                   
    
    def Read(self,key):
        path=self.file_loc+"/{}.json".format(self.fname)
        if len(key)>32:
            print("ERROR:length of key should be less than 32")
            return False
        if os.path.exists(path):
            self.data=json.load(open(path,'r'))
            if key in self.data:
                ts=self.data[key]['timestamp']
                t2l=self.data[key]['t2l']
                if t2l:
                    expiry=self.Key_expiry_checking(key,ts,t2l)
                    if expiry:
                        print("ERROR:Key expired")
                        return False
                    else:
                        print(self.data[key]['value'])
                else:
                    print(self.data[key]['value'])
            else:
                print("ERROR: no key found")
        else:
            print("ERROR:no database found")
            
        
    def Delete(self,key):
        if len(key)>32:
            print("ERROR:length of key should be less than 32")
            return False
        if os.path.exists(self.path):
            self.data=json.load(open(self.path,'r'))
        else:
            print("ERROR:no database found")
            return False
        try:
            if key in self.data:
                ts=self.data[key]['timestamp']
                t2l=self.data[key]['t2l']
                if t2l:
                    expiry=self.Key_expiry_checking(key,ts,t2l)
                    if expiry:
                        print("ERROR:Key expired")
                        return False
                    else:
                        del self.data[key]
                else:
                    del self.data[key]
            else:
                return print("ERROR:no key found")
            try:
                json.dump(self.data,open(self.path,'w+'))
                return True
            except:
                return False
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def Key_expiry_checking(self,key,timestamp,t2l):


        cur_time=datetime.now().time()
        ts1=datetime.strptime(timestamp,'%H:%M:%S.%f').time()
        time_diff=(timedelta(hours=cur_time.hour,minutes=cur_time.minute,seconds=cur_time.second)-timedelta(hours=ts1.hour,minutes=ts1.minute,seconds=ts1.second)).total_seconds()                
        if(time_diff>=t2l):
            del self.data[key]
            json.dump(self.data,open(self.path,'w+'))
            return True
        else:
            return False
    

      




        

                    
        
        
                

            
        