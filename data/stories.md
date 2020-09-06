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
  
## inquire english hw
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
  
*****TODO: DOCUMENTS*****

* Notate all training paths in mindmap viz
* Add anything_else workflow examples
  - say no --> goodbye (add to end of each example)
  - say yes --> another document cycle --> anything else 
*****TODO: END*****


## inquire spanish syllabus + nothing else
* inquire_spanish_syllabus
  - utter_spanish_document_syllabus
  - utter_anything_else
* Deny
  - utter_goodbye
  
## inquire history syllabus + nothing else
* inquire_history_syllabus
  - utter_history_document_syllabus
  - utter_anything_else
* Deny
  - utter_goodbye
  
## inquire english syllabus + nothing else
* inquire_english_syllabus
  - utter_english_document_syllabus
  - utter_anything_else
* Deny
  - utter_goodbye

## inquire geometry syllabus + nothing else
* inquire_geometry_syllabus
  - utter_geometry_document_syllabus
  - utter_anything_else
* Deny
  - utter_goodbye

## inquire spanish syllabus + affirm anything else
* inquire_spanish_syllabus
  - utter_spanish_document_syllabus
  - utter_anything_else
* affirm
  - utter_explain_functionality
  
## inquire history syllabus + nothing else
* inquire_history_syllabus
  - utter_history_document_syllabus
  - utter_anything_else
* Deny
  - utter_goodbye

## inquire english syllabus + nothing else
* inquire_english_syllabus
  - utter_english_document_syllabus
  - utter_anything_else
* Deny
  - utter_goodbye

## inquire geometry syllabus + nothing else
* inquire_geometry_syllabus
  - utter_geometry_document_syllabus
  - utter_anything_else
* Deny
  - utter_goodbye


  
## inform syllabus + which syllabus + inform history + give history syllabus
* inquire_syllabus
  - utter_which_class
* inform_history
  - utter_history_document_syllabus

## inquire syllabus + which syllabus + inform english + give english syllabus
* inquire_syllabus
  - utter_which_class
* inform_english
  - utter_english_document_syllabus

## inquire syllabus + which syllabus + inform geometry + give geometry syllabus
* inquire_syllabus
  - utter_which_class
* inform_geometry
  - utter_geometry_document_syllabus  
  
## inquire syllabus + which syllabus + inform spanish + give spanish syllabus
* inquire_syllabus
  - utter_which_class
* inform_spanish
  - utter_spanish_document_syllabus

## inquire documents + class choices + inform class history + history document choices + inform study guide
* inquire_documents
  - utter_which_class
* inform_history
  - utter_history_document_choices
* inform_study_guide
  - utter_history_document_study_guide
  
## inquire documents + class choices + inform class history + history document choices + inform syllabus
* inquire_documents
  - utter_which_class
* inform_history
  - utter_history_document_choices
* inform_syllabus
  - utter_history_document_syllabus
  
## inquire documents + class choices + inform class history + history document choices + inform hw + anything else + deny + goodbye
* inquire_documents
  - utter_which_class
* inform_history
  - utter_history_document_choices
* inform_hw
  - utter_history_document_hw
  - utter_anything_else
* Deny
  - utter_goodbye
  
 ## inquire documents + class choices + inform class spanish + spanish document choices + inform + anything else + deny + goodbye
* inquire_documents
  - utter_which_class
* inform_history
  - utter_spanish_document_choices
* inform_syllabus
  - utter_spanish_document_syllabus
  - utter_anything_else
* Deny
  - utter_goodbye
  
## inquire documents + class choices + inform spanish + spanish document choices + inform vocab sheet
* inquire_documents
  - utter_which_class
* inform_spanish
  - utter_spanish_document_choices
* inform_vocab_sheet
  - utter_spanish_document_vocab_sheet
  
## inquire documents + class choices + inform spanish + spanish document choices + inform hw
* inquire_documents
  - utter_which_class
* inform_spanish
  - utter_spanish_document_choices
* inform_hw
  - utter_spanish_document_hw
  
## inquire documents + class choices + inform class geometry + geometry document choices + inform_syllabus
* inquire_documents
  - utter_which_class
* inform_geometry
  - utter_geometry_document_choices
* inform_syllabus
  - utter_geometry_document_syllabus

## inquire documents + class choices + inform class geometry + geometry document choices + due dates sheet
* inquire_documents
  - utter_which_class
* inform_geometry
  - utter_geometry_document_choices
* inform_due_dates_sheet
  - utter_geometry_document_assignments_due_dates_sheet
  
## inquire documents + class choices + inform class english + english document choices + syllabus 
* inquire_documents
  - utter_which_class
* inform_english
  - utter_english_document_choices
* inform_syllabus
  - utter_english_document_syllabus
 
## inquire documents + class choices + inform class english + english document choices + readings 
* inquire_documents
  - utter_which_class
* inform_english
  - utter_english_document_choices
* inform_inform_readings_sheet
  - utter_english_document_readings_sheet
  
*****TODO: Finish Assignments stories*****


* inquire_assignments
  - utter_assignments_class_choice
* 


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
  
