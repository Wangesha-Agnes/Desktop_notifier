from plyer import notification
import time
def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Desktop Notifier",
        timeout=10
    )
if __name__ == "__main__":
    title = "Notification Title"
    message = "This is a desktop notification message."
    desktop_notifier(title, message)