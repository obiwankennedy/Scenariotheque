#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import re

characterOne = {"name":"Ikoma Kae", "init":"8d10e10k4","attack":"9d10r1e10k4","dommage":"8d10e10k2+7","nd":25,"currentDommage":0,"hp":[15,21,27,33,39,45,51,57],"reduc":10,"void":4,"malus":[0,0,0,0,5,10,30],"currentMalus":0, "attackCount":2}
characterTwo = {"name":"Akodo Eiichi", "init":"9d10e10k4+5","attack":"10d10r1e10k5","dommage":"8d10e10k2","nd":30,"currentDommage":0,"hp":[15,21,27,33,39,45,51,57],"reduc":3,"void":3,"malus":[0,0,2,7,12,17,37],"currentMalus":0, "attackCount":2}


def rollCommand(cmd):
  params = ['dice','-c',cmd]
  diceParser = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  stdout, stderr = diceParser.communicate()
  m = re.search("Result: ([0-9]+) - details:.*",stdout)
  if m:
      return m.group(1)

def printValue(characterName,rollName,rollScore):
    print("{} a obtenu {} à son jet de {}".format(characterName,rollScore,rollName))


def computeMalus(character):
     dmg = character["currentDommage"]
     try:
         pos = list(map(lambda x: x>int(dmg), character["hp"])).index(True)
         character["currentMalus"]=character["malus"][pos]
     except:
         pass




init1 = rollCommand(characterOne["init"])
init2 = rollCommand(characterTwo["init"])

printValue(characterOne["name"],"initiative",init1)
printValue(characterTwo["name"],"initiative",init2)

if init2 > init1:
    tree = characterOne
    characterOne = characterTwo
    characterTwo = tree

tour = 1
while ( characterOne["currentDommage"] < max(characterOne["hp"]) and characterTwo["currentDommage"] < max(characterTwo["hp"])):
    print("\n\n\nTour: "+str(tour))
    tour+=1
    usedVoid=False
    for i in range(0,characterOne["attackCount"]):
        finalOutput = "{} Attaque {} : {}"
        attack1 = rollCommand(characterOne["attack"])
        #printValue(characterOne["name"],"attaque",attack1)
        finalOutput = finalOutput.format(characterOne["name"],i+1, attack1)
        if ( int(attack1)-int(characterOne["currentMalus"]) >= characterTwo["nd"]):
           dom1 = rollCommand(characterOne["dommage"])
           #printValue(characterOne["name"],"dommage",dom1)
           finalOutput+=" => Dommage: {}".format(dom1)
           dom1 = int(dom1) - int(characterTwo["reduc"])
           if (characterTwo["void"] > 0 and dom1 >= 10 and not usedVoid):
               characterTwo["void"] -= 1
               dom1 = dom1 - 10
               usedVoid = True
           finalOutput+=", après reduction: {}".format(dom1)
           if (dom1 > 0):
               characterTwo["currentDommage"] += dom1
               computeMalus(characterTwo)
        print(finalOutput)


    usedVoid=False
    for i in range(0,characterTwo["attackCount"]):
        finalOutput = "{} Attaque {} : {}"
        attack1 = rollCommand(characterTwo["attack"])
        #printValue(characterTwo["name"],"attaque",attack1)
        finalOutput = finalOutput.format(characterTwo["name"],i+1, attack1)
        if ( int(attack1)-int(characterTwo["currentMalus"]) >= characterOne["nd"]):
           dom1 = rollCommand(characterTwo["dommage"])
           #printValue(characterTwo["name"],"dommage",dom1)
           finalOutput+=" => Dommage: {}".format(dom1)
           dom1 = int(dom1) - int(characterOne["reduc"])
           if (characterOne["void"] > 0 and dom1 >= 10 and not usedVoid):
               characterOne["void"] -= 1
               dom1 = dom1 - 10
               usedVoid = True
           finalOutput+=", après reduction: {}".format(dom1)
           if (dom1 > 0):
               characterOne["currentDommage"] += dom1
               computeMalus(characterOne)
        print(finalOutput)

    #print(characterOne)
    #print(characterTwo)

if(characterOne["currentDommage"]>= max(characterOne["hp"])):
    print("Le gagnant est: {}".format(characterTwo["name"]))

else:
    print("Le gagnant est: {}".format(characterOne["name"]))


print("\n\n\n\n\n\n\n")
print(characterTwo)
print(characterOne)
