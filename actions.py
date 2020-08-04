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
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionGetGrades(Action):

    def name(self) -> Text:
        return "action_get_grades"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: Add calc grade response (happy path)
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionGetHomeworkDetails(Action):

    def name(self) -> Text:
        return "action_get_hw_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: Add hw details response (happy path)
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionGetOutstandingAssignments(Action):

    def name(self) -> Text:
        return "action_get_outstanding_assignments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: complete show assignments (Happy Path)
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionDescribePolicy(Action):

    def name(self) -> Text:
        return "action_describe_policy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: complete describe policy function
        dispatcher.utter_message(text="Hello World!")

        return []
