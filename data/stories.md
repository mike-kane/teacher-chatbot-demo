## greet
* greet
  - utter_greet
  
## greet + bot challenge
* greet
  - utter_greet
* bot_challenge
  - utter_explain_bot
  - utter_explain_functionality
  - utter_deadlines_functionality
  - utter_assignments_functionality
  - utter_grades_functionality
  - utter_policies_functionality

## greet + inquire functionality
* greet
  - utter_greet
* inquire_functionality
  - utter_explain_functionality
  - utter_deadlines_functionality
  - utter_assignments_functionality
  - utter_grades_functionality
  - utter_policies_functionality

*****TODO: Finish Hw stories*****

## inquire spanish hw
* inquire_spanish_hw
  - utter_hw_spanish
  
## inquire hw
* inquire_english_hw
  - utter_hw_english_1
  - utter_hw_english_2
  
## inquire geometry hw
* inquire_geometry_hw
  - utter_hw_geometry
  
## inquire history hw
* inquire_history_hw
  - utter_hw_history
  
## greet + ask hw + deny projects + deny_anything_else
* greet
  - utter_greet
* inquire_hw
  - utter_hw_1
  - utter_hw_spanish
  - utter_hw_geometry
  - utter_hw_english_1
  - utter_hw_english_2
  - utter_hw_history
  _utter_hw_hear_projects
* deny
  - utter_anything_else
* deny
  - utter_goodbye
  
## greet + bot challenge + ask hw + deny projects + affirm + inquire functionality
* greet
  - utter_greet
* inquire_hw
  - utter_hw_1
  - utter_hw_spanish
  - utter_hw_geometry
  - utter_hw_english_1
  - utter_hw_english_2
  - utter_hw_history
  _utter_hw_hear_projects
* deny
  - utter_anything_else
* affirm
  - utter_explain_functionality
  
## greet + bot challenge + ask hw + affirm projects 
* greet
  - utter_greet
* inquire_hw
  - utter_hw_1
  - utter_hw_spanish
  - utter_hw_geometry
  - utter_hw_english_1
  - utter_hw_english_2
  - utter_hw_history
  _utter_hw_hear_projects
* affirm
  - utter_project_choices
* affirm_many
  - utter_project_history
  -utter_project_spanish
  
  *****TODO: Finish Project stories*****

## inquire project
* inquire_projects
  - utter_project_choices
* affirm_many
  - utter_project_spanish
  - utter_project_history
  
## inquire history project
* inquire_history_project
  - utter_project_history

## inquire spanish project
* inquire_spanish_project
  - utter_project_spanish

## inquire english project
* inquire_english_project
  - utter_project_english
  
## inquire geometry project
* inquire_geometry_project
  - utter_project_geometry
  
## inquire project + inform history
* inquire_projects
  - utter_project_choices
* inform_history
  - utter_history_project

## inquire project + inform spanish
* inquire_projects
  - utter_project_choices
* inform_spanish
  - utter_spanish_project
  
## inquire project + inform english
* inquire_projects
  - utter_project_choices
* inform_english
  - utter_english_project
  
## inquire project + inform geometry
* inquire_projects
  - utter_project_choices
* inform_geometry
  - utter_geometry_project
  
*****TODO: Finish Documents stories*****

## inquire spanish syllabus

## inquire history syllabus

## inquire english syllabus

## inquire geometry syllabus

## inquire syllabus + which syllabus + inform history + give history syllabus

## inquire syllabus + which syllabus + inform english + give english syllabus

## inquire syllabus + which syllabus + inform geometry + give geometry syllabus

## inquire syllabus + which syllabus + inform spanish + give spanish syllabus

## inquire documents + class choices + inform class history + history document choices + {document choice}

## inquire documents + class choices + inform class spanish + spanish document choices + {document choice}

## inquire documents + class choices + inform class english + english document choices + {document choice}

## inquire documents + class choices + inform class geometry + geometry document choices + {document choice} 

*****TODO: Finish Assignments stories*****

*****TODO: Finish Grades stories*****



## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_explain_bot
  - utter_explain_functionality
  - utter_deadlines_functionality
  - utter_assignments_functionality
  - utter_grades_functionality
  - utter_policies_functionality
  
