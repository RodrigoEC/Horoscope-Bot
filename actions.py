from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class getTodayHoroscope(Action):

    def name(self):
        return "get_todays_horoscope"


    def run(self, dispatcher, tracker, domain):
        #Taking the horoscope sign stored on the slot "horoscope_sign"
        user_horoscope_sign = tracker.get_slot("horoscope_sign")
        base_url = "http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}"
        url = base_url.format(**{'day' : "today", 'sign' : user_horoscope_sign} )

        res = requests.get(url)
        todays_horoscope = res.json["horoscope"]

        response = "Your today's horoscope: \n{}".format(todays_horoscope)

        #Method that send the response back to the user
        dispatcher.utter_message(response)

        #Stored data that can be used in the future
        return (SlotSet("horoscope_sign", user_horoscope_sign)) 

class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"   
    
    def run(self, dispatcher, tracker, domain):
        #Taking the information stored in the slot subscribe (True or False)
        subscribe = tracker.get_slot("subscribe")

        if subscribe == "True":
            response = "You1re successfully subscribed"   

        else: 
            response = "You1re sucessfully unsubscribed"

        #Method that send the response back to the user
        dispatcher.utter_message(response)

        #Stored data that can be used in the future
        return [SlotSet("subscribe", subscribe)]
    