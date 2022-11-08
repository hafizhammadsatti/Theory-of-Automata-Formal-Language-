#!/usr/bin/env python
# coding: utf-8

# In[1]:


class DA:
    
 def start(input_String,current_state):
    def q0(input_String):

      if input_String=="0":
        active_state="q3"
      elif input_String=="1":
        active_state="q1"

      return active_state

    def q1(input_String):

      if input_String=="0":
        active_state="q1"
      elif input_String=="1":
        active_state="q2"
      return active_state

    def q2(input_String):

      if input_String=="0":
        active_state="q2"

      elif input_String=="1":
        active_state="q2"
      return active_state



    def q3(input_String):

      if input_String=="0":
        active_state="q4"
      elif input_String=="1":
        active_state="q3"
      return active_state

    def q4(input_String):
      if input_String=="0":
        active_state="q4"
      elif input_String=="1":
        active_state="q4"
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

      elif active_state=="q4":
        active_state=q4(input_String[i])

    return active_state  




dfa=DA
input_String=input("Enter a string ")
current_state="q0"
valid_string=["0","1"]

for k in range (len(input_String)):
   if input_String[k] not in ['0','1']:
    print("Invalid String Restart Programe")
    exit()

current_state= dfa.start(input_String, current_state)

if(current_state=='q2' or current_state=='q4'):
      print("String Passed")
else:
      print("String Rejected")


# In[ ]:




