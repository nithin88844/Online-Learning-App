import json

def register(filename,name,mobile_no,email_ID,password):

    details = {
        "Name":name,
        "Mobile No.":mobile_no,
        "Email ID":email_ID,
        "Password":password
    }
    file = open(filename,"r+")
   
    try:
        data = json.load(file)
        if data:
            if details not in data:
                data.append(details)
                file.seek(0)
                file.truncate()
                json.dump(data,file)
                file.close()
                return True
        else:
            return False

    except json.decoder.JSONDecodeError:
        lst = []
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    
    except Exception as ex:
        print("Exception in register function : ",ex)
        return False
    
    finally:
        file.close()

    return False

def login(filename,username,password):
    try:
        file = open(filename,"r+")
        data = json.load(file)
        for i in data:
            if i["Email ID"] == username and i["Password"] == password:
                return True
            
    except Exception as ex:
        print("Exception in login function : ",ex)
    return False

def create_module(filename,module_ID,module_name,start_date,end_date):
    details = {
        "Module ID": module_ID,
        "Module Name":module_name,
        "Start Date" : start_date,
        "End date" : end_date
        }
        
    file = open(filename,"r+")
   
    try:
        data = json.load(file)
        if data:
            if details not in data:
                data.append(details)
                file.seek(0)
                file.truncate()
                json.dump(data,file)
                file.close()
                return True
        else:
            return False

    except json.decoder.JSONDecodeError:
        lst = []
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    
    except Exception as ex:
        print("Exception in register function : ",ex)
        return False
    
    finally:
        file.close()

    return False

def view_module(filename):
    file = open(filename,"r+")
    data = json.load(file)
    return data

def delete_module(filename,module_ID):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["Module id"] == module_ID:
            data.pop(i)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    else:
        return False

