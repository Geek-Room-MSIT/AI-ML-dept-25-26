#Generate a random 2-line funny story by mixing random characters, places, and actions.
import random

character=['a penguin','platamus perry ','a samurai','a vampire','a werewolf','a fox','a alien','trump','a horse']
places=['home','movies','park','mall','cafe','escape room','court']
activity=['dancing','studying','watching TV','singing','walking','running']
object=['pen','gift card','earphones','charger','book','nobel peace prize']

n=int(input("How many sentence do you want -: "))
k=1

for k in range(n):
    print("")
    print(random.choice(character),"was with", random.choice(character),"at",random.choice(places),random.choice(activity),"when they found a ",random.choice(object))
    
