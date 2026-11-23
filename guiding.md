# Work Items 

1. Identifying pos in the sentence 🟢
   1. It can be identified by scapy
2. Identifying the dependencies between each word 🟢
   1. It can be identified by scapy
3. Understand scapy graph in details 🟢
   1. Understand the meanings of `relations` 🟢
   2. Understand the meaning of `pos` 🟢
   3. This will help to understand how scapy create the graph tree from a sentence. 🟢
4. Lets call them scene no onwards
   1. A scene can have following things 🟢
      1. Action 🟢
      2. Doer of the action 🟢
      3. Receiver of the action 🟢
      4. Place of the action 🟢
      5. Time of the action 🟢
      6. Reason of the action 🟢
      7. Changes in the state of the object during scene 🟢
      8. Changes in the location of the objects during scene 🟢
      9. Past or future reference of the events 🟢
      10. Order of the actions / state changes etc 🔴    
5. Implement a library, which consumes a scene and parse  🟢
   1. Implement a library which parse following items from the scene 🟢
      1. Actions in the scene 🟢 
      2. Doers of each action 🟢
      3. Receiver of the each action 🟢
      4. Place of the action 🟢
      5. Time of the action 🟢
      6. Reason of the action 🟢
      7. Changes in the state of the object during scene 🟢
      8. Changes in the location of the objects during scene 🟢
      9.  Past or future reference of the events 🟢
      10. Above all are implemented by scapy in the form of the graph 🟢
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