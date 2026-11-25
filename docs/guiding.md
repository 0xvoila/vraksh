# Work Items 

1. Identifying pos in the sentence 🟢
   1. It can be identified by scapy
2. Identifying the dependencies between each word 🟢
   1. It can be identified by scapy
3. Understand scapy graph in details 🟢
   1. Understand the meanings of `relations` 🟢
   2. Understand the meaning of `pos` 🟢
   3. This will help to understand how scapy create the graph tree from a sentence. 🟢
4. Lets call them scene on onwards and able to parse following characterstics of the scene
   1. A scene can have following things 🟢
      1. Action 🟢
         1. Main verbs are the actions 
      2. Doer of the action 🟢
         1. nsubj is the doer of the action
      3. Receiver of the action 🟢
         1. dobj or pobj could be potential receiver of the action
      4. Place of the action 🟢
         1. prep is the place of the action
      5. Time of the action 🟢
         1. prep with at or npadvmod of th action
      6. Location of the object 🟠
      7. Location of the doer 🟠
      8. Additional Information 🟠
         1. Intrument of the action 🟠
         2. Reason of the action 🟠
         3. Conditions of the actions 🟠
      9. Tense of the action 🟢
5. Create a library to summarize when list of scenes are provided 🟠

6. Implement a library when we asked about the elements of a scene then retuns those elements 🟡
   1. Implement a library which parse a question and return 
         1. ID - VR-ABM
      1. Actions in the scene
         1. ID - VR-ABM123 
7. Given a information corpus in the form of a DAG and a question in the from of a DAG  🟡
   1. If two spacy scenes are given 🟡
      1. Can we identify some relationship between them ?
         1. How equal they are ? 
            1. When all actions in the scene are equal 🟢
            2. When all actions doer are same 🟢
            3. When time of action is same
            4. When reason of the action is same 
            5. When location of all objects in the scene is same
            6. When state of all objects in the scene are same
            7. When reference events in the scene are same
         2. How diff they are ?
         3. Is one part of the another 
            1. Does one tells anything about other
            2. Does one contains the other ?
   2. Determine what needs to be identify in the question DAG 🟠
      1.  Determine which pos is being questioned in the question dag? 
   3. Then determine which dag from information corpus is closest to question DAG 🟠