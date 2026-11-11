import os
from mysql import connector
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
class BloodDonorManager:
    def __init__(self):
        self.connection = connector.connect(
            user =os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME"),
            host = os.getenv("DB_HOST")
        )
        print("Connected Successfully...!")
        
        
    def get_object(self, id=None):    
        try:
            self.cursor = self.connection.cursor()
            query = "select * from Donor where id=%s"          
            values = (id,)
            self.cursor.execute(query,values) 
            record = self.cursor.fetchone()
            return record         
        except Exception as e:
            print(e)
                                
            
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = """insert into Donor (name, blood_group, phone, city, last_donation) values(%s,%s,%s,%s,%s)"""
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Data inserted successfully...!")
        except Exception as e:
            print(e)
            
            
    def get(self):
        self.cursor = self.connection.cursor()
        query = "select * from Donor"
        self.cursor.execute(query)
        
        records = self.cursor.fetchall()
        return records
                  
         
    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)
            if record==None:
                print("No record found")
            print(record)           
        except Exception as e:
            print(e)
                    
                    
    def delete(self, id=None):
            try:
                record = self.get_object(id=id)
                if record != None:
                    query = "delete from Donor where id=%s"
                    self.cursor.execute(query,(id,))
                    self.connection.commit()
                    
                    return True, "Donor deleted successfully....!"
                else:
                    return False, "No record found...!"
                        
            except Exception as e:
                print(e)
                
                
    def put(self, id= None, **kwargs):
        try:
            record = self.get_object(id=id)
            
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                
                query = f"update Donor set {placeholder} where id=%s"
                
                values = [v for v in kwargs.values()]
                
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                
                return True, "Donor updated successfully....!"
            else:
                return False, "No record found...!"
            
        except Exception as e:
            print(e)

donor_instance = BloodDonorManager()
#donor_instance.post(name="Riya", blood_group="O+", phone="9834567802", city="Kochi", last_donation=datetime.today())
#donor_instance.post(name="Anjal", blood_group="B+", phone="9830000802", city="Kochi", last_donation=datetime.today())
#donor_instance.get()
#donor_instance.retrieve(id=1)
#donor_instance.delete(id=9)
#donor_instance.put(id=1, name="Anjal", blood_group="B+", phone="9830000802", city="Kochi", last_donation=datetime.today())

donor_instance.connection.close()


