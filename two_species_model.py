#!/usr/bin/python
#This program simulates the spread of BSE in a two-species loop.
#It has been used to produce figures in the manuscript
#
#"Modeling of bovine spongiform encephalopathy in a two-species feedback loop"
#By: Richard Barnes and Clarence Lehman
#doi: 10.1016/j.epidem.2013.04.001
#
#This code was written by Richard Barnes (rbarnes@umn.edu)
import scipy
from optparse import OptionParser
import sys

def calc(ops):
  prions=scipy.zeros(ops.lifespans+ops.lifespann)
  prions[0]=ops.initial_infect

  R=scipy.zeros(ops.lifespans+ops.lifespann)
  R[0:ops.lifespans]=scipy.exp(scipy.log(ops.Rs)/ops.timestep)
  R[ops.lifespans:]=scipy.exp(scipy.log(ops.Rn)/ops.timestep)

  c=scipy.zeros(ops.lifespans+ops.lifespann)
  feedback=ops.feedback.split(',')
  for n in range(len(feedback)):
      c[n]=float(feedback[n])

  times=[]
  slevels=[]
  nlevels=[]
  print c
  for y in range(ops.years):
    for t in range(ops.timestep):
      times.append(y+t/float(ops.timestep))
      slevels.append(prions[0:ops.lifespans].sum())
      nlevels.append(prions[ops.lifespans+1:].sum())
      print "%f\t%f\t%f" % (y+t/float(ops.timestep),prions[0:ops.lifespans].sum(),prions[ops.lifespans:].sum())
      prions*=R
    prions=scipy.roll(prions,1)
    feedback_from_n_to_s=prions[0]
    feedback_from_s_to_n=prions[ops.lifespans]
    prions[0]=0
    prions[ops.lifespans]=0
    prions[0:ops.lifespans]+=feedback_from_n_to_s*c[0:ops.lifespans]
    prions[ops.lifespans:]+=feedback_from_s_to_n*c[ops.lifespans:]

  return times,slevels,nlevels

def main():
  parser = OptionParser(usage="%prog [options]", version="%prog 1.0")
  parser.add_option("-n", dest="lifespans", type="int", help="Lifespan of Susceptible Animal\t\t(def: 5)", default=5)
  parser.add_option("-m", dest="lifespann", type="int", help="Lifespan of Non-susceptible Animal\t\t(def: 3)", default=3)
  parser.add_option("-k", dest="timestep", type="int", help="Number of timesteps per year\t(def: 1)", default=1)
  parser.add_option("-r", dest="Rs", type="float", help="Replication rate in susceptible animal\t\t(def: 5.0)", default=5.0)
  parser.add_option("-s", dest="Rn", type="float", help="Replication rate in non-susceptible animal\t\t(def: 1.0)", default=1.0)
  parser.add_option("-i", dest="initial_infect", type="float", help="Initial infection amount\t(def: 1.0)", default=1.0)
  parser.add_option("-c", dest="feedback", type="string", help="Feedback amount, a string separated by commas\t(def: 0.01,0,0,0,0,0.01)", default="0.01,0,0,0,0,0.01")
  parser.add_option("-y", dest="years", type="int", help="Number of years to run simulation\t(def: 25)", default="25")
  parser.add_option("-g", dest="graph", action="store_true", help="Graph results")

  (ops, args) = parser.parse_args()
  times,slevels,nlevels=calc(ops)

  if ops.graph:
    import matplotlib.pyplot as plt
    plt.plot(xvals,yvals)
    plt.axis([0,25,0,10000])
    plt.show()


main()
