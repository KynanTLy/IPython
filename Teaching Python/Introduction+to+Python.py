
# coding: utf-8

# # Welcome to the basic of Python!
# 
# ## Introduction
# 
# ### What is coding?
# 
# You can think of coding as another language just like English. In this case our **language** is called <font color=green> **Python 3** </font>. Just like any language there exist some "*grammer rules*". However we will go into more details on these "*grammer rules*" as they come up. 
# 
# What can coding do for me? Well coding allows us to accomplish a varity different task. You can using coding to display data, do statical analysis, and do other services.
# 
# Before we can really dive into <font color=green> **Python 3** </font> we need to go over some terminology.
# 
# ### Variables (Or what I like to call them: Nicknames)
# 
# <font color=green> **Variables** </font> are in simple terms <font color=blue> **containers of data** </font>. They are used to refer to something else or in this case data. If you think about how we use nickname in real life, it follows a similar idea. Just like how we use nicknames for people to refer to them, variables do the same thing. Hence for purpose of learning if I used <font color=blue> *variable or nicknames interchangeably* </font>
# 
# Lets look at the line below

# In[1]:

x = 13


# What does this do? This means we created a variable or nickname <font color=green>**x**</font> which refers to the number <font color=green>**13** </font>. Now anytime we refer to <font color=green>**x**</font> in our program, what we really mean is the number <font color=green>**13**</font>.
# 
# Therefore we can use <font color=green> **x** in place of using the value **13** </font>
# 
# However there are certain "*grammer rules*" for what is a valid <font color=blue>**nickname**</font> or <font color=blue>**variable**</font>. For example we **cannot** start a variable name with a *space* or "*\_*" or a *number*. Another rule is that we are not allowed to have more than 1 word in our nickname. <font color=blue>**Variables must begin with a letter**. </font>
# ***
# <div class="alert alert-block alert-info">
# **For example:**
# 
# Two Word = 10  
# -  <font color=red>Invalid</font> because we are <font color=red>using 2 *seperate* words</font>
# 
# 4ThereABumberInFront = 10
# -  <font color=red>Invalid</font> because we are using the <font color=red>number *4* at the beginning</font>
# 
# /SpecialCharacterInFront = 10
# -  <font color=red>Invalid</font> because we are using the <font color=red>*'/'* at the beginning</font>
# 
# Two_World = 10
# -  <font color=green>Valid</font>. This is because we can use "\_" to connect to two words. The reason for this is because the <font color=green>*computer reads "Two_World" as one single word*</font>. 
# 
# ThisHasTheNumber4InIt = 10
# -  <font color=green>Valid</font>. This is because again the computer treats it as <font color=green>*one word and the number 4 is not at the beginning.*</font> 
# </div>
# ***
# 
# Now that is strange isn't it? There is the <font color=green>**number 4**</font> in the word. How does the computer know that we mean the word <font color=blue>**character '4'**</font> and not the <font color=blue>**numerical value of '4'**</font>. We will discuss this in the next point <font color=green>**Python Data Type**</font>.
# 

# ### Python Data Type
# 
# Do you remember in Math class where there are different type of numbers? There are <font color=green>**Integer**</font> or <font color=green>**Whole Numbers**</font>, <font color=green>**Real Number**</font>. In Python 3 and other programming language there is are many other data type, for now we will keep it simple and list some of the more common ones. 
# 
# #### Here is a list of some common Data Type 
# <div class="alert alert-block alert-info">
# -  <font color=blue>**Character**</font>
#     -  Think of character as any <font color=green>**single key**</font> on your keyboard. This could be numbers, letters and special characters.
# 
# -  <font color=blue>**String**</font>
#     -  String is any combination of Characters encased between <font color=green>**" "**</font> or <font color=green>**' '**</font>. This can include <font color=green>**numbers**</font>, <font color=green>**letters**</font> and even <font color=green>**special characters**</font>.
#         -  Remember  <font color=green>**"/""**</font> and  <font color=green>**"/'"**</font> can be used interchangably however if you choose to use one over the other, you have to be <font color=blue>**consistent**</font>! So you <font color=red>cannot have **"Hello'** </font>but  <font color=green> **"Hello"** or **'Hello'** </font> are exactly the same
# -  <font color=blue>**Integer**</font>
#     -  Refers to whole numbers like  <font color=green>**3**</font> or  <font color=green>**262361508**</font>.
# -  <font color=blue>**Float**</font> 
#     -  Refers to decimal numbers like  <font color=green>**3.14**</font>.
#     
# </div>
# We can see the difference in the example below:

# In[2]:

This_Refers_To_The_Integer_4 = 4
This_Refers_To_The_String_4 = '4'


# As you can see above the two <font color=blue>**4**</font> are displayed in different colours. One is <font color=green>green for the **Integer**</font> and the other is <font color=red>red for the **String**</font>. This is to indicate that <font color=blue>**they are different**</font>. Depending on what program you are using to write Python code it may be a different colour or have no colour atgreen.
# 
# Now if we do some basic operation on the two variables or nicknames we can see they give us different results

# In[3]:

This_Refers_To_The_Integer_4 = 4

This_Refers_To_The_Integer_4 * 4


# In[4]:

This_Refers_To_The_String_4 = '4'

This_Refers_To_The_String_4 * 4


# As you can see they give us <font color=blue>**different result** because they are **different data type**</font>. One multipled the number <font color=green>**4 x 4**</font> resulting in <font color=green>**16**</font>. In the second case we are saying we want <font color=green>"**4 copies of the character 4**"</font> resulting in <font color=green>"**4444**" </font>
# 
# Now that we have discussed the different data types, we are going to touch on <font color=blue>**Data Structures**</font>
# 
# ### Data Structures
# 
# Imagine you are going to the grocery store, you might bring along a shopping list which list all the things that you might want to purchase. You wouldn't bring 10 different pieces of paper to record all the things you need. You would just bring just the 1 list. 
# 
# #### List 
# 
# List follow the same format as other <font color=blue>**Data Structure**</font> in how it is declared. There is also some <font color=green> *rules* </font> that a list must follow. One of these rules is that a list can <font color=blue> only have 1 **data type** stored inside it</font>. This means that a list <font color=red> cannot contain both an *Integer* and a *String* </font>.

# In[5]:

example_list = []


# This is how we would declare an empty list. List are declared with <font color=green>'**[**'</font> and <font color=green>'**]**'</font>. These <font color=blue>*square brackets*</font> is an indicator that tells Python that you are declaring a list
# 
# But an empty list is not very useful to have, so lets fill it with some data

# In[6]:

example_list = [3, 4, 5]


# Now our example_list contains <font color=blue>**3 integer elements**</font>. That is the <font color=green>numberic value 3, 4, and 5</font>. As you can see, each <font color=blue>**element** (or things insides our list)</font> is seperated with <font color=blue>'**,**'</font>. 
# 
# <div class="alert alert-block alert-info">
# **A String example**  
# 
# example_list_strings = [  
# &nbsp;&nbsp;"Hello this is a list",  
# &nbsp;&nbsp;"of strings. As you can see",   
# &nbsp;&nbsp;"some of these sentences can be longer than other and that is okay."  
# ]
# 
# </div>
# 
# One thing to note with this example that is different from the previous (aside from the fact that this is a list of <font color=green>**strings**</font>) is that not all the <font color=blue>list element is in the same line</font>. This is <font color=green>**perfectly okay**</font> in Python 3. That is because Python 3 is smart and assumes that you mean for all of it to be in the same line. 
# 
# Therefore this means that
# 
# <div class="alert alert-block alert-info">
# example_list_strings = [  
# &nbsp;&nbsp;"Hello this is a list",  
# &nbsp;&nbsp;"of strings. As you can see",   
# &nbsp;&nbsp;"some of these sentences can be longer than other and that is okay."  
# ]  
#   
#   
# is the <font color=green>**SAME**</font> as   
#   
#   
# example_list_strings = ["Hello this is a list", "of strings. As you can see","some of these sentences can be longer than other and that is okay."]
# 
# </div>
# 
# As long as the <font color=green>proper list grammer is followed</font>
# 
# Now that we know how to create a list, how do access an <font color=blue>**element**</font> in a list?
# 
# This can be done with using the <font color=blue> "**[**" and "**]**" </font> and specifing an <font color=blue>**index**</font>. Look at the example below

# In[7]:

example_list = [3, 4, 5]
example_list[1]


# As you can see the output for <font color=green> *example_list[1]* </font> resulted in the number <font color=blue>**4**</font>. Why does this happen? You would expect when ask for the <font color=blue> **element 1** </font> you would expect it to return the 1st item of the list or in this case <font color=green>**3**</font>. However in Python 3 and other programming languages we start the list at <font color=green>**0**</font>. 
# 
# **Using the Previous Example:**
# <div class="alert alert-block alert-info">
# 
# **example_list = [3, 4, 5]**
# 
# To extract the first <font color=blue>**element**</font> or the number <font color=blue> **3** </font>. We would use the line of code:
# 
# **example_list[0]**
# </div>
# 
# Breaking down what the line above. We are telling the computer to go find the <font color=blue>list</font> called **example_list**. Next lets look at the <font color=blue>**0**</font> inside the <font color=green>*square brackets*</font>. The <font color=blue>**0**</font> refering to an <font color=green> **index** </font>. 
# 
# Recall that <font color=green> **index** </font> refers to a <font color=blue> **position** </font> in the list. Since in Python 3 we <font color=red>*do not start counting form 1* </font>, we <font color=blue> *start at 0* </font>. 
# 
# <div class="alert alert-block alert-info">
# **example_list = [3, 4, 5]**  
# 
# To get the <font color=blue> *1st element (3)* </font> you would use: **example_list[0]** for the **0th index/position**  
# 
# To get the <font color=blue> *2nd element (4)* </font> you would use: **example_list[1]** for the **1st index/position**  
# 
# To get the <font color=blue> *3rd element (5)* </font> you would use: **example_list[2]** for the **2nd index/position**  
# 
# </div>
# 
# As you can see, we can now select <font color=blue>**individual elements**</font> from a list. However what happens when we want to select <font color=blue>**more than 1**</font>?
# 
# ### List Slicing
# 
# Think of <font color=green>**slicing**</font> like you are slicing a pie. You can slice yourself any size of slice. You could have a big one or a small one. To <font color=green>**slice**</font> a list you need to learn a <font color=blue>**new grammer rule**</font>.
# 
# **Using the previous example:**
# 

# In[8]:

example_list = [3, 4, 5]
example_list[0:2]


# As you can see with the above example it returned us <font color=blue>**[3, 4]**</font> or more than <font color=green>1 element</font>.
# 
# Now lets look at exactly what happend
# 
# <div class="alert alert-block alert-info">
# **example_list[0:2]**
# </div>
# 
# Normally if we only wanted one element we would have just use <font color=blue>**1 number**</font> to <font color=green>refer to the index/position of the element in the list we wanted</font>
# 
# However in the above example we have <font color=blue> **2 number as well as a ":" seperating the two numbers** </font>
# 
# The <font color=blue>**1st number**</font> refers to where we want to <font color=blue>**start**</font> our <font color=green>*slice*</font>. The <font color=blue>**:**</font> is used to tell the computer we are going to slice. The <font color=blue>**2nd number**</font> refers to where we are going <font color=blue>**end**</font>.
# 
# 
# Note: we <font color=red>**DO NOT include the 2nd number index/position value **</font> (in this example) when we slice.
# 
# Therefore the example:
# <div class="alert alert-block alert-info">
# **example_list[0:2]**
# </div>
# 
# would return us all <font color=blue>elements in the list</font> from the <font color=green>** 0th element -> 1st element**</font>. Or the element  <font color=green>**3**</font> from  <font color=green>**example_list[0]**</font> and  <font color=green>**4**</font> from  <font color=green>**example_list[1]**</font>.
# 
# It is also worth noting that slicing will <font color=blue>always returned</font> the results in a <font color=green>*list*</font>
# 
# Here are a list of few more example:
# <div class="alert alert-block alert-info">
# **example_list[0:4]**  This would return **[3, 4, 5]**  
# 
# **example_list[0:0]**  This would return **[]** Remember this means it is an <font color=green>**empty list**</font>    
# 
# **example_list[2:3]**   This would return **[5]**  
# </div>
# 
# 
# 
