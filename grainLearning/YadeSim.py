# encoding: utf-8
from os.path import expanduser
import sys

# yadeimport.py is generated by `ln yade-versionNo yadeimport.py`
# add the directory where Yade is install
sys.path.append('/usr/bin/')

# import external dependencies
from yadeimport import *

# default parameters
readParamsFromTable(
    # Density
    rho=2450,
    # Young's modulus
    E=70e+9,
    # Poisson's ratio
    nu=0.2,
    # final friction coefficient
    mu=0.4,
    # timestepSafetyCoefficient
    safe=0.1,
    # no. of your simulation
    key=0
)

# glass bead parameters (units: ug->1e-9kg; mm->1e-3m; ms->1e-3s)
lenScale = 1e3  # length in mm <- 1e-3 m
sigScale = 1  # Stress in ug/(mm*ms^2) <- Pa
rhoScale = 1  # Density in ug/mm^3 <- kg/m^3

from yade.params import table
import numpy as np


# function to save simulation data and stop simulation
def addSimData():
    inter = O.interactions[0, 1]
    u = inter.geom.penetrationDepth
    if u > obsCtrlData[-1]:
        simData['u'].append(u)
        simData['f'].append(inter.phys.normalForce.norm())
        obsCtrlData.pop()
    if not obsCtrlData: O.pause()


# define material parameters
def setParams():
    # create materials
    O.materials.append(FrictMat(young=table.E, poisson=table.nu, frictionAngle=atan(table.mu), density=table.rho))


# add particles to simulation
def addParticles():
    # create two particles
    O.bodies.append(sphere(Vector3(0, 0, 0), 1, material=0, fixed=True))
    O.bodies.append(sphere(Vector3(0, 0, 2), 1, material=0, fixed=True))


# set initial condition
def setInitialCondition():
    # set initial timestep
    O.dt = table.safe * PWaveTimeStep()
    # move particle 1
    O.bodies[1].state.vel = Vector3(0, 0, -0.01)


# define engines (TODO: wrap everything within a class)
def createScene(ID=-1):
    O.engines = [
        ForceResetter(),
        InsertionSortCollider([Bo1_Sphere_Aabb()]),
        InteractionLoop(
            [Ig2_Sphere_Sphere_ScGeom()],
            [Ip2_FrictMat_FrictMat_MindlinPhys()],
            [Law2_ScGeom_MindlinPhys_Mindlin()]
        ),
        NewtonIntegrator(damping=0.0, label='newton'),
        # needs to add module collision before function name
        PyRunner(command='addSimData()', iterPeriod=100)
    ]
    O.tags['id'] = str(ID)
    return O.sceneToString()


def runDEM(kwargs):
    # get simulation object
    simObj = kwargs[0]
    # get parameter list
    params = kwargs[1]
    # get data for simulation control
    global obsCtrlData, simData
    obsCtrlData = list(kwargs[2])
    obsCtrlData.reverse()

    print('\nModel evaluation NO. %i' % params['key'])
    # read in things need to be randomized
    if 'rho' not in params.keys():
        print("use default density...")
    if 'E' not in params.keys():
        print("use default Young's modulus...")
    else:
        table.E = abs(params['E'] * sigScale)
    if 'nu' not in params.keys():
        print("use default Poisson's ratio...")
    else:
        table.nu = abs(params['nu'])
    if 'mu' not in params.keys():
        print("use default friction coefficient...")
    else:
        table.mu = abs(params['mu'])
    if 'safe' not in params.keys():
        print("use default Time-stepping safety coefficient...")
    else:
        table.safe = abs(params['safe'])
    print('E: %s; nu: %s; mu: %s; safe: %s' % (table.E, table.nu, table.mu, table.safe))

    # run DEM simulation
    O.stringToScene(simObj)
    setParams()
    addParticles()
    setInitialCondition()
    simData = {'u': [], 'f': []}
    O.run(int(1e10), True)

    # return simulation data
    return simData
