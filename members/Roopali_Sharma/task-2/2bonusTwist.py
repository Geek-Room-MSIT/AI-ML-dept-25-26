#Random Story Generator Bonus Twist
import random 
characters = ["a sleepy panda", "an alien", "a pirate", "a robot"] 
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"] 
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"] 
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"] 
activity = ["ate pizza","drank coffee","played ludo","did some gossips"]
fun=["became ghosts","became zombies","scared people","did party"]
num=int(input("tell how many stories you want to listen?"))
for i in range(num):
    RandomChar=random.choice(characters)
    RandomPlace=random.choice(places)
    RandomObj=random.choice(objects)
    RandomAction=random.choice(actions)
    RandomActivity=random.choice(activity)
    RandomFun=random.choice(fun)
    print(f"Once {RandomPlace} i met {RandomChar} which had {RandomObj} so we together {RandomActivity} and then we {RandomAction} so at night we {RandomFun}")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
