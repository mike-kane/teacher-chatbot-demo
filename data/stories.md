## greet
* greet
  - utter_greet
  
## greet + bot challenge
* greet
  - utter_greet
* bot_challenge
  - utter_explain_bot
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## greet + inquire functionality
* greet
  - utter_greet
* inquire_functionality
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

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
  - utter_hw_hear_projects
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
  - utter_hw_hear_projects
* deny
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
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
  - utter_hw_hear_projects
* affirm
  - utter_project_choices
* affirm_many
  - utter_project_history
  -utter_project_spanish

## inquire project
* inquire_project
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
* inquire_project
  - utter_project_choices
* inform_history
  - utter_project_history

## inquire project + inform spanish
* inquire_project
  - utter_project_choices
* inform_spanish
  - utter_project_spanish
  
## inquire project + inform english
* inquire_project
  - utter_project_choices
* inform_english
  - utter_project_english
  
## inquire project + inform geometry
* inquire_project
  - utter_project_choices
* inform_geometry
  - utter_project_geometry

## inquire spanish syllabus + nothing else
* inquire_spanish_syllabus
  - utter_spanish_document_syllabus
  - utter_anything_else
* deny
  - utter_goodbye
  
## inquire history syllabus + nothing else
* inquire_history_syllabus
  - utter_history_document_syllabus
  - utter_anything_else
* deny
  - utter_goodbye
  
## inquire english syllabus + nothing else
* inquire_english_syllabus
  - utter_english_document_syllabus
  - utter_anything_else
* deny
  - utter_goodbye

## inquire geometry syllabus + nothing else
* inquire_geometry_syllabus
  - utter_geometry_document_syllabus
  - utter_anything_else
* deny
  - utter_goodbye

## inquire spanish syllabus + affirm anything else
* inquire_spanish_syllabus
  - utter_spanish_document_syllabus
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire history syllabus + nothing else
* inquire_history_syllabus
  - utter_history_document_syllabus
  - utter_anything_else
* deny
  - utter_goodbye

## inquire english syllabus + nothing else
* inquire_english_syllabus
  - utter_english_document_syllabus
  - utter_anything_else
* deny
  - utter_goodbye

## inquire geometry syllabus + nothing else
* inquire_geometry_syllabus
  - utter_geometry_document_syllabus
  - utter_anything_else
* deny
  - utter_goodbye


  
## inform syllabus + which syllabus + inform history + give history syllabus
* inform_syllabus
  - utter_which_class
* inform_history
  - utter_history_document_syllabus

## inform syllabus + which syllabus + inform english + give english syllabus
* inform_syllabus
  - utter_which_class
* inform_english
  - utter_english_document_syllabus

## inform syllabus + which syllabus + inform geometry + give geometry syllabus
* inform_syllabus
  - utter_which_class
* inform_geometry
  - utter_geometry_document_syllabus  
  
## inform syllabus + which syllabus + inform spanish + give spanish syllabus
* inform_syllabus
  - utter_which_class
* inform_spanish
  - utter_spanish_document_syllabus

## inform documents + class choices + inform class history + history document choices + inform study guide
* inform_documents
  - utter_which_class
* inform_history
  - utter_history_document_choices
* inform_study_guide
  - utter_history_document_study_guide
  
## inform documents + class choices + inform class history + history document choices + inform syllabus
* inform_documents
  - utter_which_class
* inform_history
  - utter_history_document_choices
* inform_syllabus
  - utter_history_document_syllabus
  
## inform_documents + class choices + inform class history + history document choices + inform hw + anything else + deny + goodbye
* inform_documents
  - utter_which_class
* inform_history
  - utter_history_document_choices
* inform_hw
  - utter_history_document_hw
  - utter_anything_else
* deny
  - utter_goodbye
  
 ## inform_documents + class choices + inform class spanish + spanish document choices + inform + anything else + deny + goodbye
* inform_documents
  - utter_which_class
* inform_history
  - utter_spanish_document_choices
* inform_syllabus
  - utter_spanish_document_syllabus
  - utter_anything_else
* deny
  - utter_goodbye
  
## inform_documents + class choices + inform spanish + spanish document choices + inform vocab sheet
* inform_documents
  - utter_which_class
* inform_spanish
  - utter_spanish_document_choices
* inform_vocab_sheet
  - utter_spanish_document_vocab_sheet
  
## inform_documents + class choices + inform spanish + spanish document choices + inform hw
* inform_documents
  - utter_which_class
* inform_spanish
  - utter_spanish_document_choices
* inform_hw
  - utter_spanish_document_hw
  
## inform_documents + class choices + inform class geometry + geometry document choices + inform_syllabus
* inform_documents
  - utter_which_class
* inform_geometry
  - utter_geometry_document_choices
* inform_syllabus
  - utter_geometry_document_syllabus

## inform_documents + class choices + inform class geometry + geometry document choices + due dates sheet
* inform_documents
  - utter_which_class
* inform_geometry
  - utter_geometry_document_choices
* inform_due_dates_sheet
  - utter_geometry_document_assignments_due_dates_sheet
  
## inform_documents + class choices + inform class english + english document choices + syllabus 
* inform_documents
  - utter_which_class
* inform_english
  - utter_english_document_choices
* inform_syllabus
  - utter_english_document_syllabus
 
## inform_documents + class choices + inform class english + english document choices + readings 
* inform_documents
  - utter_which_class
* inform_english
  - utter_english_document_choices
* inform_readings_sheet
  - utter_english_document_readings_sheet

## inquire assignments +  assignments class choices + affirm many + assignments all outstanding
* inquire_assignments
  - utter_assignments_class_choice
* affirm_many
  - utter_assignments_all_outstanding
  
## inquire assignments + assignments class choices + spanish + class assignments outstanding + anything else + deny
* inquire_assignments
  - utter_assignments_class_choice
* inform_spanish
  - utter_assignments_spanish_outstanding
  - utter_anything_else
* deny
  -utter_goodbye
  
## inquire assignments + assignments class choices + english + class assignments outstanding + anything else + deny
* inquire_assignments
  - utter_assignments_class_choice
* inform_english
  - utter_assignments_english_outstanding
  - utter_anything_else
* deny
  -utter_goodbye
  
## inquire assignments + assignments class choices + history + class assignments outstanding + anything else + deny
* inquire_assignments
  - utter_assignments_class_choice
* inform_history
  - utter_assignments_history_outstanding
  - utter_anything_else
* deny
  -utter_goodbye
  
## inquire assignments + assignments class choices + geometry + class assignments outstanding + anything else + deny
* inquire_assignments
  - utter_assignments_class_choice
* inform_geometry
  - utter_assignments_geometry_outstanding
  - utter_anything_else
* deny
  -utter_goodbye
  
## inquire assignments + assignments class choices + spanish + class assignments outstanding + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inform_spanish
  - utter_assignments_spanish_outstanding
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire assignments + assignments class choices + english + class assignments outstanding + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inform_english
  - utter_assignments_english_outstanding
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire assignments + assignments class choices + history + class assignments outstanding + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inform_history
  - utter_assignments_history_outstanding
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire assignments + assignments class choices + geometry + class assignments outstanding + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inform_geometry
  - utter_assignments_geometry_outstanding
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire assignments  + assignments class choices + inquire missing assignments + assignments missing 1 + affirm many + assignments missing spanish + note + affirm +  assignments missing spanish note 2a +  + assignments missing geometry + affirm + assignments missing geometry note + anything else + deny + goodbye
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* affirm_many
  - utter_assignments_missing_spanish_2
* affirm
  - utter_assignments_missing_spanish_note_2a
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* deny
  - utter_goodbye
  
## inquire assignments  + assignments class choices + inquire missing assignments + assignments missing 1 + affirm many + assignments missing spanish + note + affirm +  assignments missing spanish note 2a +  + assignments missing geometry + affirm + assignments missing geometry note + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* affirm_many
  - utter_assignments_missing_spanish_2
* affirm
  - utter_assignments_missing_spanish_note_2a
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire assignments  + assignments class choices + inquire missing assignments + assignments missing 1 + inform spanish + assignments missing spanish + note + affirm +  assignments missing spanish note 2a +   + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_spanish
  - utter_assignments_missing_spanish_2
* affirm
  - utter_assignments_missing_spanish_note_2a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire assignments  + assignments class choices + inquire missing assignments + assignments missing 1 + inform geometry + assignments missing geometry + note + affirm +  assignments missing geometry note 3a +   + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_geometry
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire assignments + assignments class choices + inquire missing assignments + assignments missing 1 + inform english + assignments all good
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_english
  - utter_assignments_all_good

## inquire assignments + assignments class choices + inquire missing assignments + assignments missing 1 + inform history + assignments all good
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_history
  - utter_assignments_all_good
  
## inquire assignments  + assignments class choices + inquire missing assignments + assignments missing 1 + inform geometry + assignments missing geometry + note + deny + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_geometry
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire assignments  + assignments class choices + inquire missing assignments + assignments missing 1 + inform geometry + assignments missing geometry + note + affirm +  assignments missing geometry note 3a +   + anything else + deny + goodbye
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_geometry
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire assignments  + assignments class choices + inquire missing assignments + assignments missing 1 + inform spanish + assignments missing spanish + note + deny + anything else + affirm + explain functionality
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_geometry
  - utter_assignments_missing_geometry_3
* deny
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire assignments  + assignments class choices + inquire missing assignments + assignments missing 1 + inform geometry + assignments missing spanish + note + deny + anything else + deny + goodbye
* inquire_assignments
  - utter_assignments_class_choice
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_geometry
  - utter_assignments_missing_geometry_3
* deny
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire missing assignments + assignments missing 1 + both + assignments missing spanish 2 + affirm + assignments missing spanish note 2a + assignments missing geometry 3 + affirm + assignments missing geometry note 3a + anything else + deny + goodbye
* inquire_missing_assignments
  - utter_assignments_missing_1
* affirm_many
  - utter_assignments_missing_spanish_2
* affirm
  - utter_assignments_missing_spanish_note_2a
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  -utter_anything_else
* deny
  - utter_goodbye


## inquire missing assignments + assignments missing 1 + both + assignments missing spanish 2 + deny assignments missing geometry 3 + affirm + assignments missing geometry note 3a + anything else + deny + goodbye
* inquire_missing_assignments
  - utter_assignments_missing_1
* affirm_many
  - utter_assignments_missing_spanish_2
* deny
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  -utter_anything_else
* deny
  - utter_goodbye
  
## inquire missing assignments + assignments missing 1 + inform spanish + assignments missing spanish 2 + affirm + assignments missing spanish note 2a + anything else + affirm + explain functionality
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_spanish
  - utter_assignments_missing_spanish_2
* affirm
  - utter_assignments_missing_spanish_note_2a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire missing assignments + assignments missing 1 + inform geometry + assignments missing geometry 3 + affirm + assignments missing geometry note 3a + anything else + affirm + explain functionality
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_geometry
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire missing assignments + assignments missing 1 + inform english + assignments all good + anything else + affirm + explain functionality
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_english
  - utter_assignments_all_good
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire missing assignments + assignments missing 1 + inform history + assignments all good + anything else + affirm + explain functionality
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_history
  - utter_assignments_all_good
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire spanish missing assignments + assignments missing spanish 2 + affirm + assignments missing spanish note 2a + anything else + deny + goodbye
* inquire_missing_assignments_spanish
  - utter_assignments_missing_spanish_2
* affirm
  - utter_assignments_missing_spanish_note_2a
  - utter_anything_else
* deny
  - utter_goodbye

## inquire spanish missing assignments + assignments missing spanish 2 + deny + anything else + deny + goodbye
* inquire_missing_assignments_spanish
  - utter_assignments_missing_spanish_2
* deny
  - utter_anything_else
* deny
  - utter_goodbye

## inquire geometry missing assignments +  assignments missing geometry 3 + affirm + assignments missing geometry note 3a + anything else + deny + goodbye
* inquire_missing_assignments_geometry
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* deny
  - utter_goodbye

## inquire geometry missing assignments + assignments missing geometry 3 + deny + anything else + deny + goodbye
* inquire_missing_assignments_geometry
  - utter_assignments_missing_geometry_3
* deny
  - utter_anything_else
* deny
  - utter_goodbye

## inquire english missing assignments + all good + anything else + deny + goodbye 
* inquire_missing_assignments_english
  - utter_assignments_all_good
  - utter_anything_else
* deny
  - utter_goodbye

## inquire history missing assignments + all good + anything else  + deny + goodbye 
* inquire_missing_assignments_history
  - utter_assignments_all_good
  - utter_anything_else
* deny
  - utter_goodbye
  
## inquire missing assignments + assignments missing 1 + inform english + assignments all good + anything else + deny + goodbye
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_english
  - utter_assignments_all_good
  - utter_anything_else
* deny
  - utter_goodbye

## inquire missing assignments + assignments missing 1 + inform history + assignments all good + anything else + deny + goodbye
* inquire_missing_assignments
  - utter_assignments_missing_1
* inform_history
  - utter_assignments_all_good
  - utter_anything_else
* deny
  - utter_goodbye
  
## inquire spanish assignments + assignments spanish class outstanding + spanish project + view missing assignment spanish  + affirm + missing assignment spanish note 2a  + anything else + affirm + explain functionality
* inquire_assignments_spanish
  - utter_assignments_spanish_outstanding
  - utter_project_spanish
  - utter_assignments_missing_spanish_2
* affirm
  - utter_assignments_missing_spanish_note_2a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire spanish assignments + assignments spanish class outstanding + spanish project +  view missing assignment spanish note + deny +  anything else + affirm + explain functionality
* inquire_assignments_spanish
  - utter_assignments_spanish_outstanding
  - utter_project_spanish
  - utter_assignments_missing_spanish_2
* deny
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality


## inquire geometry assignments + assignments geometry class outstanding + view missing assignment note geometry + affirm + view missing assignment note geometry 3a +  anything else + affirm + explain functionality
* inquire_assignments_geometry
  - utter_assignments_geometry_outstanding
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire geometry assignments + assignments geometry class outstanding + view missing assignment note + deny +  anything else + affirm + explain functionality
* inquire_assignments_geometry
  - utter_assignments_geometry_outstanding
  - utter_assignments_missing_geometry_3
* deny
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire history functionality + assignments history outstanding + history project +  anything else + affirm + explain_functionality
* inquire_assignments_history
  - utter_assignments_history_outstanding
  - utter_project_history
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire history functionality + assignments history  outstanding + history project + anything else + deny + goodbye
* inquire_assignments_history
  - utter_assignments_history_outstanding
  - utter_project_history
  - utter_anything_else
* deny
  - utter_goodbye
  
## inquire english functionality + assignments english outstanding + anything else + affirm + explain functionality
* inquire_assignments_english
  - utter_assignments_english_outstanding
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire english functionality + assignments english outstanding + anything else + deny + goodbye
* inquire_assignments_english
  - utter_assignments_english_outstanding
  - utter_anything_else
* deny
  - utter_goodbye

## inquire grades + utter grades class more info 2 + affirm + grades class more info which class 3 + inform english + utter_grades_english_more_info_4a + anything else + affirm + explain functionality
* inquire_grades
  - utter_grades_overall_1
  - utter_grades_class_more_info_2
* affirm
  - utter_grades_class_more_info_which_class_3
* inform_english
  - utter_grades_english_more_info_4a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire grades + utter grades class more info 2 + affirm + grades class more info which class 3 + inform geometry + utter_grades_geometry_more_info_4b + anything else + deny + goodbye
* inquire_grades
  - utter_grades_overall_1
  - utter_grades_class_more_info_2
* affirm
  - utter_grades_class_more_info_which_class_3
* inform_geometry
  - utter_grades_geometry_more_info_4b
  - utter_anything_else
* deny
  - utter_goodbye

## inquire grades + utter grades class more info 2 + affirm + grades class more info which class 3 + inform history + utter_grades_history_more_info_4c + anything else + deny + goodbye
* inquire_grades
  - utter_grades_overall_1
  - utter_grades_class_more_info_2
* affirm
  - utter_grades_class_more_info_which_class_3
* inform_history
  - utter_grades_history_more_info_4c
  - utter_anything_else
* deny
  - utter_goodbye

## inquire grades + utter grades class more info 2 + affirm + grades class more info which class 3 + inform spanish + utter_grades_spanish_more_info_4d + anything else + affirm + explain functionality
* inquire_grades
  - utter_grades_overall_1
  - utter_grades_class_more_info_2
* affirm
  - utter_grades_class_more_info_which_class_3
* inform_spanish
  - utter_grades_spanish_more_info_4d
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality

## inquire grades + grades class more info 2 + inform english + utter grades english more info 4a
* inquire_grades
  - utter_grades_overall_1
  - utter_grades_class_more_info_2
* inform_english
  - utter_grades_english_more_info_4a
  
## inquire grades + grades class more info 2 + inform geometry + utter grades english more info 4b
* inquire_grades
  - utter_grades_overall_1
  - utter_grades_class_more_info_2
* inform_geometry
  - utter_grades_geometry_more_info_4b
  
## inquire grades + grades class more info 2 + inform history + utter grades english more info 4c
* inquire_grades
  - utter_grades_overall_1
  - utter_grades_class_more_info_2
* inform_history
  - utter_grades_history_more_info_4c
 
## inquire grades + grades class more info 2 + inform spanish + utter grades english more info 4d
* inquire_grades
  - utter_grades_overall_1
  - utter_grades_class_more_info_2
* inform_spanish
  - utter_grades_spanish_more_info_4d
  
## inquire spanish grade + missing assignment note attached + affirm + view note
* inquire_grade_spanish
  - utter_grades_spanish_more_info_4d
  - utter_assignments_missing_spanish_2
* affirm
  - utter_assignments_missing_spanish_note_2a
  - utter_anything_else
* deny
  - utter_goodbye

## inquire spanish grade + missing assignment note attached + deny + anything else + deny + goodbye
* inquire_grade_spanish
  - utter_grades_spanish_more_info_4d
  - utter_assignments_missing_spanish_2
* deny
  - utter_anything_else
* deny
  - utter_goodbye
  
## inquire geometry grade + missing assignment note attached + affirm + view note + anything else + affirm + explain functionality
* inquire_grade_geometry
  - utter_grades_geometry_more_info_4b
  - utter_assignments_missing_geometry_3
* affirm
  - utter_assignments_missing_geometry_note_3a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire geometry grade + missing assignment note attached + deny + anything else + affirm + explain functionality
* inquire_grade_geometry
  - utter_grades_geometry_more_info_4b
  - utter_assignments_missing_geometry_3
* deny
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire history grade + utter grades class more info 4c + affirm + explain functionality
* inquire_grade_history
  - utter_grades_history_more_info_4c
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire history grade + utter grades class more info 4c + anything else + deny + goodbye
* inquire_grade_history
  - utter_grades_history_more_info_4c
  - utter_anything_else
* deny
  - utter_goodbye

## inquire english grade + utter grades class more info 4a + anything else + affirm + explain functionality
* inquire_grade_english
  - utter_grades_english_more_info_4a
  - utter_anything_else
* affirm
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire english grade + utter grades class more info 4a + anything else + deny + goodbye
* inquire_grade_english
  - utter_grades_english_more_info_4a
  - utter_anything_else
* deny
  - utter_goodbye
  
## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_explain_bot
  - utter_explain_functionality
  - utter_explain_deadlines_functionality
  - utter_explain_assignments_functionality
  - utter_explain_grades_functionality
  
## inquire class info + inform spanish + Deny
* inquire_class_info
  - utter_which_class
* inform_spanish
  - utter_class_info_spanish_overall
* deny

## inquire class info + inform english + Deny + goodbye
* inquire_class_info
  - utter_which_class
* inform_english
  - utter_class_info_english_overall
* deny

## inquire class info + inform history + Deny + goodbye
* inquire_class_info
  - utter_which_class
* inform_history
  - utter_class_info_history_overall
* deny

## inquire class info + inform geometry + Deny + goodbye
  * inquire_class_info
  - utter_which_class
* inform_geometry
  - utter_class_info_geometry_overall
* deny

## inquire class info + inform spanish + affirm + class info details choices
* inquire_class_info
  - utter_which_class
* inform_spanish
  - utter_class_info_spanish_overall
* affirm
  - utter_class_info_details_choices
  
## inquire class info + inform english + affirm + class info details choices
* inquire_class_info
  - utter_which_class
* inform_english
  - utter_class_info_english_overall
* affirm
  - utter_class_info_details_choices
  
## inquire class info + inform history + affirm + class info details choices
* inquire_class_info
  - utter_which_class
* inform_history
  - utter_class_info_history_overall
* affirm
  - utter_class_info_details_choices
  
## inquire class info + inform geometry + affirm + class info details choices
* inquire_class_info
  - utter_which_class
* inform_geometry
  - utter_class_info_geometry_overall
* affirm
  - utter_class_info_details_choices

## inquire class info spanish + utter class info spanish overall + affirm + utter class info details choices
* inquire_class_info_spanish
  - utter_class_info_spanish_overall
* affirm
  - utter_class_info_details_choices

## inquire class info english + utter class info {} overall + affirm + utter class info details choices
* inquire_class_info_english
  - utter_class_info_english_overall
* affirm
  - utter_class_info_details_choices
  
## inquire class info history + utter class info {} overall + affirm + utter class info details choices
* inquire_class_info_history
  - utter_class_info_history_overall
* affirm
  - utter_class_info_details_choices
  
## inquire class info geometry + utter class info {} overall + affirm + utter class info details choices
* inquire_class_info_geometry
  - utter_class_info_geometry_overall
* affirm
  - utter_class_info_details_choices
  
***TODO: COMPLETE MESSAGING WORKFLOW***

## inquire message read 
* inquire_message_read
  - utter_check_messages_summary
  - utter_message_check_message_1
  - utter_message_check_message_2
  - utter_message_check_message_3

## inquire message read + inquire message leave + which recipient + inform_ soccer +
* inquire_message_read
  - utter_check_messages_summary
  - utter_message_check_message_1
  - utter_message_check_message_2
  - utter_message_check_message_3
* inquire_message_leave
  - utter_message_which_recipient
* inform_coach
  - utter_what_message
* inform{"message": "I turned it in"}
  - utter_message_sent


***TODO: COMPLETE CALENDAR WORKFLOW***

## inquire calendar + utter calendar week overview + utter calendar more choices + inform school + utter calendar school 

## inquire calendar + utter calendar week overview + utter calendar more choices + inform extracurriculars + utter calendar soccer

