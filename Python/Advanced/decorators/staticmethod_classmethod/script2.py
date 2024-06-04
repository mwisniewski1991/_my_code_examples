import datetime

class Calendar:
    def __init__(self):
        self.events = []
        
    def add_event(self,event):
        self.events.append(event)
	
    @staticmethod
    def is_weekend(date):
        return date.weekday() > 4
    
    @classmethod
    def from_json(cls, filename):
        c = cls()
        #code to parse json to Calendar Class
        return c

def main():
    c = Calendar()
    c.add_event('party')

    today = datetime.date.today()
    print(c.is_weekend(today)) #with out staticmethod this does not work
    print(Calendar.is_weekend(today)) 

main()