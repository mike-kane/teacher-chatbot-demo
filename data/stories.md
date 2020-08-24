## greet
* greet
  - utter_greet
  
## greet + bot challenge
* greet
  - utter_greet
* bot_challenge
  - utter_explain_bot
  - utter_explain_functionality

## greet + inquire functionality
* greet
  - utter_greet
* inquire_functionality
  - utter_explain_functionality
  
## greet + ask hw
* greet
  - utter_greet
* inquire_homework
  - utter_hw
  - action_get_hw_details

## inquire project
* inquire_project
  - utter_project_details

## inquire class policy
* inquire_class_policy
  - utter_policy_choices
  - slot{"policy_choice": "grading"}
  - action_describe_policy

## greet + inquire class policy
* greet
  - utter_greet
  - utter_explain_bot
* inquire_class_policy{"policy_choice":"contact_info"}
  - slot{"policy_choice":"contact_info"}
  -action_describe_policy
  
## inquire grade + inquire class policy
* inquire_grades
  - action_get_grades
* inquire_class_policy{"policy_choice":"grading"}
  - slot{"policy_choice":"grading"}

## greet + inquire project + inquire due dates + inquire class policies
* greet
  - utter_greet
  - utter_explain_bot
* inquire_project
  - utter_project_details
* inquire_due
  - action_get_due_dates
* inquire_class_policy
  - utter_policy_choices
  - slot{"policy_choice":"project"}
  - action_get_due_dates

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_explain_bot
  - utter_explain_functionality
