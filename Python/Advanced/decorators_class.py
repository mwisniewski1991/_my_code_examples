from datetime import datetime, timedelta
import time
print('-------------------------------------------------')

def check_time(func):
    def wrapper(*args, **kwargs):
        print('STH IS HAPPEN ---------------------')
        current_time = datetime.now()
        class_attributes = args[0]

        if class_attributes.last_download is not None:
            time_diffrence_seconds = (current_time - args[0].last_download).total_seconds()
            
            if time_diffrence_seconds <= 6:
                print('SMALL TIME. ADDING EXTRA SECONDS')
                time.sleep(5)

        func(*args, **kwargs)
    return wrapper

class Data_manager:
    def __init__(self) -> None:
        self.last_download = None
        
    @check_time
    def upload_data(self):
        print('DOWNLOAD DATA')
        self.last_download = datetime.now()

data_manager = Data_manager()
data_manager.upload_data()

time.sleep(5)
data_manager.upload_data()