# from plyer import notification  import time

# title = 'Desktop Notifier'
# message = 'This is a notification from your python desktop notifier!'

# notification.notify(title=title,
#                     message=message,
#                     timeout=10) #Notification will stay for 10 seconds

# time.sleep(15)#Wait for 15 seconds before closing the notification

From plyer import notification 
import time

def desktop_notifier(title,message):
    notification.notify(
        title=title,
        message=message,
        app_name="Desktop Notifier",
        timeout=10
    )
    
if _name_=="_main_":
    title="Notification Title"
    message="This is a desktop notification message."
    desktop_notifier(title,message)
       