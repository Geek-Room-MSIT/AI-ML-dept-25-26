#importing modules
import random as r

#intro kinda message
print("This is a random story generator. It generates some random funny stories")
print("------------------------------------------------------------------------")

#list of characters , objects , places and actions
char=["A curious dragon","A brave knight","A mischievous raccoon","A wise owl","A tired astronaut","A dancing robot","A lost cat","A grumpy giant","A singing mermaid","A cheerful wizard"]

obj=["a glowing crystal","an ancient map","a golden key","a rusty sword","a mysterious book","a magical flower","a shiny gemstone","a broken compass","a mysterious pocket watch","a basket of apples"]

place=["in a haunted castle","at the top of a snowy mountain","deep in the forest","on a distant planet","in an enchanted library","inside a secret cave","on a sandy beach","in a magical city","by a sparkling lake","on a pirate ship"]

actions=["jumped over a mountain","whispered a secret spell","found a hidden treasure","chased a butterfly","wrote a letter to a friend","played a haunting melody","stumbled upon an old door","built a sandcastle","sang a beautiful song","got lost in the woods"]

#now to ask how many stories they want

while True:
    a=int(input("Enter the number of stories you want:"))
    for i in range(a):
        print("Here is story",i+1)
        story_char=r.choice(char)
        story_object=r.choice(obj)
        story_place=r.choice(place)
        story_action=r.choice(actions)

        story=story_char+(" "+story_place)+(" "+story_action)+(" "+story_object)
        print(story)
        print()
    rep=input("Do you want to generate again?(y/n)").lower()
    if rep=='n' or rep=="no":
        break
print("bye")
