#!/usr/bin/env python
# coding: utf-8

# In[1]:




def addP(x):
    global Pscore
    Pscore += x
    
def addS(x):
    global Sscore
    Sscore += x


# In[2]:


P = ["I like temperate weather with plenty of sun",
    "I love to live by a beach",
    "I like to spend my free time hanging out with friends", 
    "I enjoy afternoon picnic in the park",
    "I hate getting stuck in traffic",
    "I sometimes fear being able to not afford things",
    "I love being a part of a local community",
    "I enjoy driving around town",
    "I love spending time with my extended family",
    "I can't stand long flights",
    "I enjoy going to the zoo",
    "Bali", 
    "Beach",
    "Riverside Park",
    "Jogging",
    "I hate having to find parking"]

P2 = ["Being grateful is the key to happiness",
    "Take life one day at a time...",
    "I would do alot to be able to live in Australia",
    "School is where my children obtain good education and values",
    "Everything is preordained, we just have to learn and enjoy the ride..."]


# In[3]:


S = ["I take the opportunity to dress up during winter",
    "I love the city",
    "I like to spend my free time pampering myself",
    "I enjoy a good coffee and good food",
    "I love shopping",
    "I sometimes fear being lonely",
    "I like to make friends with new people",
    "I would love to be able to have a job I am passionate about",
    "I plan to open an Indo Supermarket or maybe any other business",
    "I hate feeling bored",
    "I enjoy trying new restaurants",
    "Singapore", 
    "Mountain",
    "Kids Playground",
    "Yoga",
    "I don't feel the need to stand out in the crowd"]

S2 = ["Having money enables good life regardless where we live",
    "Always plan ahead!",
    "If things go wrong, we can always go back with no regrets.",
    "Every child is different, we can only guide them and hope for the best!",
    "I don't like looking back and relive the past..."
    ]


# In[ ]:


Pscore = 0
Sscore = 0
for x in range (16):
    print("A : " + P[x])
    print("B : " + S[x])
    Ans = input ("Please input A or B : ")
    Ans = Ans.upper()
    if Ans == "A":
        addP(1)
    else :
        addS(1)
    print("------------------------------------------------------------------------------")
    
for x in range (5):
    print("A : " + P2[x])
    print("B : " + S2[x])
    Ans = input ("Please input A or B : ")
    Ans = Ans.upper()
    if Ans == "A":
        addP(2)
    else :
        addS(2)
    print("------------------------------------------------------------------------------")

print("A : I believe Yonax is very talented and he can achieve big things, he just needed the push")
print("B : I believe Yonax makes a good familyman that puts his family over work")
M = input("Please input A or B : ")
M = M.upper()
if M == "A":
    addS(4)
else:
    addP(4)
print("------------------------------------------------------------------------------")
    
print("A : Yonax is somewhat lazy!")
print("B : Yonax gives up easily!")
N = input("Please input A or B : ")
N = N.upper()
if N == "A":
    addP(4)
else:
    addS(4)
print("------------------------------------------------------------------------------")
    
print("A : I believe good things will happen to us!")
print("B : I am grateful to be in Australia!")    
O = input("Please input A or B : ")
O = O.upper()
if O == "A":
    addS(5)
else:
    addP(5)
print("------------------------------------------------------------------------------")

print("A : Pushing through hardship will earn you success.")
print("B : Expectation is the root of disappointment.")    
Q = input("Please input A or B : ")
Q = Q.upper()
if Q == "A":
    addS(5)
else:
    addP(5)
print("------------------------------------------------------------------------------")
    
print("The score for Perth is : " + str(Pscore))
print("The score for Sydney is : " + str(Sscore))
if Pscore > Sscore :
    print("Let's go to Perth!")
elif Pscore == Sscore:
    print("You gotta get some other opinion to help you...")
else:
    print("Let's go to Sydney!")
print("------------------------------------------------------------------------------")
Z = input("Are you happy with the result? Don't answer... Just take a photo of the result and we will discuss later...")
    
    


# In[ ]:





# In[ ]:





# In[ ]:




