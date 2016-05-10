pokedex = []
f = open('pokemon.txt', 'r')
#load pokedex
for line in f:
	substring = line[1:-2]
	temp = substring.split(", ")
	pokedex.append(temp)
#change appropriate string to int
for item in pokedex:
	item[0] = int(item[0])
#print pokedex

f.close()

f = open('strength.txt', 'r')
strengths = []
for line in f:
	substring = line[1:-2]
	temp = substring.split(", ")
	strengths.append(temp)
f.close()
#print strengths
#print 
print
#print pokemon number 1-10
print "SELECT id, name FROM pokedex WHERE id <= 10"
print [[i[0], i[1]] for i in pokedex if i[0]<=10]
print
#print all grass type pokemon
print "SELECT id, name FROM pokedex WHERE type1 or type2 == 'Grass'"
print [[i[0], i[1]] for i in pokedex if i[2]=="Grass" or i[3] == "Grass"]
print
#group by type and sort the pokemon by name
print "SELECT name from pokedex GROUP BY type1 ORDER BY ID"
for type1 in sorted({p[2] for p in pokedex}): print (type1, sorted([p[1] for p in pokedex if p[2]==type1], key = lambda x: x[0]))
print
#print all pokemon who are strong against grass type pokemon, grouped by type
print "print all pokemon who are strong against grass type pokemon, grouped by type, sorted by name within the group"
print 
test = 'Grass'
for strongtype in sorted({s[0] for s in strengths if s[1] == test or s[2] == test or s[3] == test or s[4] == test}): print(strongtype, sorted([p[1] for p in pokedex if p[2]==strongtype or p[3]== strongtype]))

#Don't use exec for Option A, #5
#instead, change the env in lis.py
#WHAT DOES THIS MEAAAANNNNN?!?!!
