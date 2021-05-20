#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import streamlit as st


# In[2]:


# loading in the model to predict on the data
pickle_in = open('saved_models/bert_model.pkl', 'rb')
bert_model = pickle.load(pickle_in)


# In[3]:


def welcome():
    return 'welcome all'


# In[4]:


def SummarizeText(inp):  
   
    summary_generated = bert_model(inp)
    print(summary_generated)
    return summary_generated


# In[5]:


def main():
      # giving the webpage a title
    st.title("Abstract auto summarization")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:tomato;padding:13px">
    <h1 style ="color:black;text-align:center;">Auto Summarization and key word extraction App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    abstract_text = st.text_input("Abstract", "Type Here") 
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Submit"):
        result = SummarizeText(abstract_text)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()

