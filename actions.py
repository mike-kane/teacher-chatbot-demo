# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetDueDates(Action):

    def name(self) -> Text:
        return "action_get_due_dates"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: Add due dates response (happy path)
        message = """DUE DATES PLACEHOLDER"""
        dispatcher.utter_message(text=message)

        return []


class ActionGetGrades(Action):

    def name(self) -> Text:
        return "action_get_grades"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Here are your grades for the quarter so far: 
        
        |   Date  |     Assignment     | Grade |
|:-------:|:------------------:|:-----:|
|  9/1/20 |     Homework 1     |   96  |
|  9/3/20 |       Quiz 1       |   85  |
|  9/9/20 |     Homework 2     |  100  |
| 9/10/20 | Unit 1 Study Guide |   0   |
| 9/12/20 |     Homework 3     |   100  |

Your current grade in class for this quarter is: 76.2% 
        """
        dispatcher.utter_message(text=message)

        return []


class ActionGetHomeworkDetails(Action):

    def name(self) -> Text:
        return "action_get_hw_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: Add hw details response (happy path)
        message = """PLACEHOLDER FOR HOMEWORK DETAILS"""
        dispatcher.utter_message(text=message)

        return []


class ActionGetAssignments(Action):

    def name(self) -> Text:
        return "action_get_assignments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: complete show assignments (Happy Path)
        message = """GET ASSIGNMENTS PLACEHOLDER"""
        dispatcher.utter_message(text=message)

        return []


class ActionDescribePolicy(Action):

    def name(self) -> Text:
        return "action_describe_policy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: complete describe policy function
        message = """POLICY PLACEHOLDER"""
        dispatcher.utter_message(text=message)

        return []
