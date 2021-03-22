import time
from plyer import notification
if __name__ == "__main__":
   while True:
       notification.notify(
         title = " Please Drink Water ",
         message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. ",
         app_icon= "icon/icon.ico",
         timeout=5
    )
  
