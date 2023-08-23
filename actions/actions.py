# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser
import requests

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_get_url"

     async def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            website = tracker.latest_message.get("text")
            if "google" in website.lower():
                url= "www.google.com"
                dispatcher.utter_message("Opening Google")
            elif "youtube" in website.lower():
                url= "www.youtube.com"
                dispatcher.utter_message("Opening Youtube")
            elif "amazon" in website.lower():
                url="www.amazon.in"
                dispatcher.utter_message("Opening Amazon")
            else:    
                
                dispatcher.utter_message("I didn't get it")

            webbrowser.open(url)
         

            return []
     





class ActionGetWeather(Action):

     def name(self) -> Text:
         return "action_get_weather"

     async def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
             city = tracker.get_slot('location')
             url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9da23ae5fb608cfd713bbf1aa462d8d1"
             response = requests.get(url)     

             data = response.json()

             x =data['main']
             temp = round(x['temp'] - 273.15,2)
             place =data["name"]
             x= data['weather']
             desc = x[0]['main']         

             weather_data = "it's {} *c currently in {}. weather is {} .".format(temp,place,desc)
             dispatcher.utter_message(weather_data)
             return [SlotSet("location", city)]

