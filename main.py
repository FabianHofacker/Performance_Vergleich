from __future__ import division
import numpy
import numpy as np
from numpy import *
import random
from numpy import savetxt
from numpy import loadtxt
import gurobipy as gp
from gurobipy import GRB
from itertools import combinations

n=100 #Knoten
t=30 #Beobachtungen pro Instanzengröße
w=900 #Breite Rechteck
h=600 #Höhe Rechteck
c=52 #Anzahl Cluster
r=29 #Nummer Frozenset

ratio = loadtxt('ratio.csv', delimiter=',')
#ratio = [0 for m in range(t)] #Liste aller Performance-Ratios

"""---------------------------------------------------------------------------------------------------------------"""
#Nearest-Neighbor-Algorithmus

# Cities are represented as Points, which are represented as complex numbers
Point = complex
City = Point

def X(point):
    "The x coordinate of a point."
    return point.real

def Y(point):
    "The y coordinate of a point."
    return point.imag

def distance(A, B):
    "The distance between two points, inc. clusters"
    return abs(A - B)

def Cities(n, width=w, height=h, seed=t):
    "Make a set of n cities, each with random coordinates within a (width x height) rectangle."
    random.seed(seed * n)
    return frozenset(City(random.randrange(width), random.randrange(height))
                     for c in range(n))

#build a set of cities
städte = Cities(n, width=w, height=h, seed=r)
sets = [städte]
liste = [list(x) for x in sets]

#Liste mit Clustern
L =  [[liste[0][2], liste[0][3]],
     [liste[0][6], liste[0][7]],
     [liste[0][8], liste[0][9]],
     [liste[0][7], liste[0][8]],
     [liste[0][9], liste[0][10]],
     [liste[0][10], liste[0][11]],
     [liste[0][11], liste[0][12]],
     [liste[0][15], liste[0][16]],
     [liste[0][17], liste[0][20]],
     [liste[0][18], liste[0][19]],
     [liste[0][21], liste[0][22]],
     [liste[0][22], liste[0][23]],
     [liste[0][24], liste[0][25]],
     [liste[0][25], liste[0][26]],
     [liste[0][26], liste[0][27]],
     [liste[0][27], liste[0][28]],
     [liste[0][28], liste[0][29]],
     [liste[0][42], liste[0][43]],
     [liste[0][43], liste[0][44]],
     [liste[0][44], liste[0][45]],
     [liste[0][45], liste[0][46]],
     [liste[0][46], liste[0][47]],
     [liste[0][47], liste[0][48]],
     [liste[0][49], liste[0][50]],
     [liste[0][50], liste[0][51]],
     [liste[0][51], liste[0][52]],
     [liste[0][52], liste[0][53]],
     [liste[0][53], liste[0][54]],
     [liste[0][54], liste[0][55]],
     [liste[0][55], liste[0][56]],
     [liste[0][56], liste[0][57]],
     [liste[0][58], liste[0][59]],
     [liste[0][59], liste[0][60]],
     [liste[0][60], liste[0][61]],
     [liste[0][61], liste[0][62]],
     [liste[0][62], liste[0][63]],
     [liste[0][63], liste[0][64]],
     [liste[0][65], liste[0][66]],
     [liste[0][66], liste[0][67]],
     [liste[0][67], liste[0][68]],
     [liste[0][68], liste[0][69]],
     [liste[0][69], liste[0][70]],
     [liste[0][70], liste[0][71]],
     [liste[0][72], liste[0][73]],
     [liste[0][73], liste[0][74]],
     [liste[0][74], liste[0][75]],
     [liste[0][75], liste[0][76]],
     [liste[0][76], liste[0][77]],
     [liste[0][78], liste[0][79]],
     [liste[0][79], liste[0][80]],
     [liste[0][81], liste[0][82]],
     [liste[0][82], liste[0][83]],
     [liste[0][83], liste[0][84]],
     [liste[0][85], liste[0][86]],
     [liste[0][86], liste[0][87]],
     [liste[0][87], liste[0][88]],
     [liste[0][88], liste[0][89]],
     [liste[0][89], liste[0][90]],
     [liste[0][90], liste[0][91]],
     [liste[0][91], liste[0][92]],
     [liste[0][92], liste[0][81]],
     [liste[0][93], liste[0][94]],
     [liste[0][94], liste[0][95]],
     [liste[0][95], liste[0][96]],
     [liste[0][96], liste[0][97]],
     [liste[0][97], liste[0][98]],
     [liste[0][98], liste[0][99]],
     [liste[0][100], liste[0][101]],
     [liste[0][101], liste[0][102]],
     [liste[0][102], liste[0][103]],
     [liste[0][103], liste[0][104]],
     [liste[0][104], liste[0][105]],
     [liste[0][106], liste[0][107]],
     [liste[0][107], liste[0][108]],
     [liste[0][108], liste[0][109]],
     [liste[0][109], liste[0][110]],
     [liste[0][110], liste[0][111]],
     [liste[0][111], liste[0][112]],
     [liste[0][112], liste[0][113]],
     [liste[0][113], liste[0][114]],
     [liste[0][114], liste[0][115]],
     [liste[0][116], liste[0][119]],
     [liste[0][119], liste[0][121]],
     [liste[0][117], liste[0][118]],
     [liste[0][121], liste[0][122]],
     [liste[0][122], liste[0][123]],
     [liste[0][123], liste[0][124]],
     [liste[0][124], liste[0][125]],
     [liste[0][125], liste[0][126]],
     [liste[0][126], liste[0][127]],
     [liste[0][127], liste[0][128]],
     [liste[0][37], liste[0][131]],
     [liste[0][131], liste[0][132]],
     [liste[0][132], liste[0][133]],
     [liste[0][137], liste[0][138]],
     [liste[0][139], liste[0][140]],
     [liste[0][140], liste[0][141]],
     [liste[0][141], liste[0][142]],
     [liste[0][143], liste[0][169]],
     [liste[0][144], liste[0][145]],
     [liste[0][146], liste[0][147]],
     [liste[0][152], liste[0][153]],
     [liste[0][154], liste[0][155]],
     [liste[0][156], liste[0][157]],
     [liste[0][161], liste[0][162]],
     [liste[0][166], liste[0][167]],
     [liste[0][172], liste[0][173]],
     [liste[0][147], liste[0][148]],
     [liste[0][148], liste[0][149]],
     [liste[0][149], liste[0][150]],
     [liste[0][150], liste[0][151]],
     [liste[0][151], liste[0][152]],
     [liste[0][133], liste[0][135]],
     [liste[0][142], liste[0][143]],
     [liste[0][163], liste[0][164]],
     [liste[0][164], liste[0][165]],
     [liste[0][125], liste[0][126]],
     [liste[0][126], liste[0][127]],
     [liste[0][158], liste[0][176]],
     [liste[0][84], liste[0][171]],
     [liste[0][128], liste[0][129]],
     [liste[0][129], liste[0][130]],
     [liste[0][115], liste[0][85]],
     [liste[0][174], liste[0][175]],
     [liste[0][180], liste[0][181]],
     [liste[0][181], liste[0][182]],
     [liste[0][182], liste[0][183]],
     [liste[0][185], liste[0][186]],
     [liste[0][187], liste[0][188]],
     [liste[0][191], liste[0][192]],
     [liste[0][192], liste[0][193]],
     [liste[0][193], liste[0][194]],
     [liste[0][196], liste[0][197]],
     [liste[0][199], liste[0][200]],
     [liste[0][201], liste[0][203]],
     [liste[0][203], liste[0][204]],
     [liste[0][205], liste[0][206]],
     [liste[0][207], liste[0][208]],
     [liste[0][210], liste[0][211]],
     [liste[0][213], liste[0][214]]]

def first(collection):
    "Start iterating over collection, and return the first element."
    return next(iter(collection))

def tour_length(tour):
    "The total of distances between each pair of consecutive cities in the tour."
    return sum(distance(tour[i], tour[i-1])
               for i in range(len(tour)))

Tour = list  # Tours are implemented as lists of cities

def nn_tsp(cities):
    start = first(cities)
    tour = [start]
    unvisited = set(cities - {start})
    while unvisited:
            C = nearest_neighbor(tour[-1], unvisited)
            tour.append(C)
            unvisited.remove(C)
            if len(tour) == n:
                return tour

def nearest_neighbor(A, cities):
    "A in Cluster: Gehe zum nächsten Element im Cluster"
    unvisTemp= set(cities)
    while c==c:
        if nearest_neighbor.counter <= c:
            for f in range(c):
                if A ==L[f][0] and L[f][1] in unvisTemp:
                    nearest_neighbor.counter +=1
                    return L[f][1]
                elif A == L[f][1] and L[f][0] in unvisTemp:
                    nearest_neighbor.counter +=1
                    return L[f][0]

            "A nicht in Cluster: Gehe zum nächsten Nachbarn, der nicht in 2 Clustern ist"
            d=0
            for f in range(c): #zählen, in wie vielen Clustern der NN ist
                if min(unvisTemp, key=lambda c: distance(c, A)) == L[f][0]:
                    d += 1
                if min(unvisTemp, key=lambda c: distance(c, A)) == L[f][1]:
                    d += 1
            if d==2:  #ist der NN in 2 Clustern, wird er übersprungen
                unvisTemp.remove(min(unvisTemp, key=lambda c: distance(c, A)))
            else: #NN wird ausgewählt
                return min(unvisTemp, key=lambda c: distance(c, A))

nearest_neighbor.counter = 0
NN = tour_length(nn_tsp(städte))
assert nearest_neighbor.counter == c, "Zu wenige Cluster!"


"""---------------------------------------------------------------------------------------------------------"""


#GUROBI ALGORITHM

# Es wird eine Liste erstellt, mit der später geprüft wird, ob alle Cluster korrekt erstellt werden
L2 = [[0 for l in range(2)] for k in range(c)]
z=0
for i in range(c):
    for j in range(n):
        for k in range(j):
            if (L[i][0], L[i][1]) == (liste[0][j], liste[0][k]):
                L2[z][0] = j
                L2[z][1] = k
                z += 1
            elif (L[i][0], L[i][1]) == (liste[0][k], liste[0][j]):
                L2[z][0] = j
                L2[z][1] = k
                z += 1

# Kostenmatrix TSP
kosten= [[0 for l in range(n)] for k in range(n)]
for i in range (n):
    for j in range(n):
        kosten[i][j] = distance(liste[0][i], liste[0][j])

# Erweiterung zum CTSP
K = np.amax(kosten) * 0.96
Ksubtr=0
for i in range(n):#Anzahl erzeugter Cluster
    for j in range(n):
        for k in range(c):
            if liste[0][i]==L[k][0] and liste[0][j]==L[k][1]: #prüfen, ob 2 Knoten zu einem Cluster gehören
                kosten[i][j] = kosten[i][j] - K #K von intra-cluster Kanten subtrahieren
                Ksubtr +=1
            elif liste[0][i]==L[k][1] and liste[0][j]==L[k][0]:
                kosten[i][j] = kosten[i][j] - K
                Ksubtr +=1
assert Ksubtr/2 == c, "Es wurden nicht genug Cluster in der Kostenmatrix erzeugt!"

# Callback - use lazy constraints to eliminate sub-tours
def subtourelim(model, where):
    if where == GRB.Callback.MIPSOL:
        vals = model.cbGetSolution(model._vars)
        # find the shortest cycle in the selected edge list
        tour = subtour(vals)
        if len(tour) < n:
            # add subtour elimination constr. for every pair of cities in tour
            model.cbLazy(gp.quicksum(model._vars[i, j] for i, j in combinations(tour, 2))
                         <= len(tour)-1)

# Given a tuplelist of edges, find the shortest subtour
def subtour(vals):
    # make a list of edges selected in the solution
    edges = gp.tuplelist((i, j) for i, j in vals.keys()
                         if vals[i, j] > 0.5)
    unvisited = list(range(n))
    cycle = range(n + 1)
    while unvisited:
        thiscycle = []
        neighbors = unvisited
        while neighbors:# true if list is non-empty
            current = neighbors[0]
            thiscycle.append(current)
            unvisited.remove(current)
            neighbors = [j for i, j in edges.select(current, '*')
                         if j in unvisited]
        if len(thiscycle) <= len(cycle):
            cycle = thiscycle
    return cycle

# Umwandlung Kostenmatrix in Tupelliste
dist = {(i, j): kosten[i][j]
        for i in range(n)
        for j in range(i)}

m = gp.Model()

# Create variables
vars = m.addVars(dist.keys(), obj=dist, vtype=GRB.BINARY, name='x')

for i, j in vars.keys():
    vars[j, i] = vars[i, j]  # edge in opposite direction

# Add degree-2 constraint
m.addConstrs(vars.sum(i, '*') == 2 for i in range(n))

#SOLVE
m._vars = vars
m.Params.lazyConstraints = 1
m.optimize(subtourelim)

vals = m.getAttr('x', vars)
tour = subtour(vals)
assert len(tour) == n

optCost = m.ObjVal + c*K #optimale reale Kosten

#prüfen, ob alle Cluster existieren
selected = gp.tuplelist((i, j) for i, j in m._vars.keys()
      if vals[i, j] > 0.5)
clusterCounter=0
for i in range(n):
    for j in range(c):
        #um die Cluster zu zählen, werden alle Kanten der Lösung in der Clusterliste gesucht
        if selected[i]==(L2[j][0], L2[j][1]) or selected[i]==(L2[j][1], L2[j][0]):
            clusterCounter +=1
assert clusterCounter==c, print("nicht genug Cluster!")

"""--------------------------------------------------------------------------------------------------------------"""


#Vergleich der Performances
p= (NN/optCost)-1 # Wie viel Prozent länger ist die Lösung des NN?
ratio[r]=p
savetxt('ratio.csv', ratio, delimiter=',')

print('')
print('')
print("Mindestwert: ", np.amin(ratio))
print("Maximalwert: ", np.amax(ratio))
print("Mittelwert: ", np.mean(ratio))
print("Standardabweichung: ", np.std(ratio))
print('')










