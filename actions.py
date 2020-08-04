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


class ActionCalculateGrade(Action):

    def name(self) -> Text:
        return "action_calculate_grade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: Add calc grade response (happy path)
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionHomeworkDetails(Action):

    def name(self) -> Text:
        return "action_hw_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: Add hw details response (happy path)
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

class ActionShowAssignments(Action):

    def name(self) -> Text:
        return "action_show_assignments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: complete show assignments (Happy Path)
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionGetAssignmentGrades(Action):

    def name(self) -> Text:
        return "action_get_assignment_grades"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # TODO: complete action get assignment grades
        dispatcher.utter_message(text="Hello World!")

        return []
