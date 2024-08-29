# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
import rasa_sdk
from rasa_sdk import Action, Tracker
from rasa_sdk import forms
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction, SlotSet

from loguru import logger

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


class GetInfoWinLossRecord(Action):

    def name(self) -> Text:
        return "action_win_loss_record"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot('team')
        ret_text = f"{name} is ok"
        
        dispatcher.utter_message(text=ret_text)

        return []
    
class ActionConsult(Action):
    def name(self) -> Text:
        return "action_consult"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        citem = tracker.get_slot('citem')
        logger.info(f'citem is {citem}')
        ret_msg = ''
        if citem != '经销商':
            ret_msg = '暂不支持本领域的咨询，敬请期待'
            dispatcher.utter_message(ret_msg)
            return [FollowupAction("action_listen")]
        
        ret_msg = '请问您想咨询哪个城市的经销商呢？'
        dispatcher.utter_message(ret_msg)
        return []
    
class ActionReturnAgency(Action):
    def name(self) -> Text:
        return "action_return_agency"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        citem = tracker.get_slot('citem')
        city = tracker.get_slot('city')
        
        logger.info(f'citem is {citem}, city is {city}')
                
        if citem == '经销商' and city == '深圳':
            ret_msg = '【红旗贵宾专线】您好，为您查询到深圳市有5家经销商：1、经销商位于广东省深圳市光明区马田街道石围油麻岗工业区33号D栋101，名称为通利华（深圳）汽车销售服务有限公司，电话：29009666；2、经销商位于深圳市宝安区航城街道三围社区航空路西湾智园A1栋101，名称为深圳锦红汽车销售服务有限公司，电话：0755-26688988；3、经销商位于深圳市宝安区新桥街道沙企社区中心路 18号高盛大厦A座一层，名称为深圳奥吉通汽车销售服务有限公司，电话：0755-27272929；4、经销商位于广东省深圳市福田区莲花街道景华社区商报路2号深圳晚报印务楼1层东侧，名称为深圳市鸿钧汽车有限公司，电话：0755-83130868；'
            # dispatcher.utter_message(ret_msg)
            # return [FollowupAction("action_ask_more_service"), SlotSet('citem', None), SlotSet('city', None)]
        
        else:
            ret_msg = '【红旗贵宾专线】您好，感谢您的使用，祝您生活愉快。'
            
        dispatcher.utter_message(ret_msg)
        return [SlotSet('citem', None), SlotSet('city', None)]

class ActionAskMoreService(Action):
    def name(self) -> Text:
        return "action_ask_more_service"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        
        ret_msg = '请问还有什么可以帮您？'
        dispatcher.utter_message(template='utter_ask_more_service')
        return [FollowupAction("action_listen")]
    
class FormActionConsulting(forms.Action):
    def name(self) -> Text:
        return "action_consulting_form_action"

    def required_slots(tracer: Tracker) -> List[Text]:
        return ['citem', 'city']
