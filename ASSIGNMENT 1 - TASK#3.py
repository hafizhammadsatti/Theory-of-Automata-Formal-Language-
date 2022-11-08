#!/usr/bin/env python
# coding: utf-8

# In[1]:


class DA:
    
 def begin(input_String,current_state):
    def q0(input_String):

      if input_String=="a":
        active_state="q2"
      elif input_String=="b":
        active_state="q2"
      elif input_String=="c":
        active_state="q1"

      return active_state

    def q1(input_String):

      if input_String=="a":
        active_state="q3"
      elif input_String=="b":
        active_state="q2"
      elif input_String=="c":
        active_state="q2"

      return active_state

    def q2(input_String):

      if input_String=="a":
        active_state="q3"
      elif input_String=="b":
        active_state="q3"
      elif input_String=="c":
        active_state="q3"

      return active_state


    def q3(input_String):

      if input_String=="a":
        active_state="q3"
      elif input_String=="b":
        active_state="q3"
      elif input_String=="c":
        active_state="q3"

      return active_state
    
    size=len(input_String)
    active_state=current_state

    for i in range(size):
      if active_state=="q0":
        active_state=q0(input_String[i])

      elif active_state=="q1":
        active_state=q1(input_String[i])


      elif active_state=="q2":
        active_state=q2(input_String[i])

      elif active_state=="q3":
        active_state=q3(input_String[i])

    return active_state  






dfa=DA
final_state=["q2"]
input_String=input("Enter a string ")
current_state="q0"


for k in range (len(input_String)):
   if input_String[k] not in ['a','b',"c"]:
    print("Invalid String Restart Programe")
    exit()

current_state= dfa.begin(input_String, current_state)
for k in final_state:
   if(current_state==k):
      print("String Passed")
   else:
      print("String Rejected")


# In[ ]:





# In[ ]:





# In[ ]:




