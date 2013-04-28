#!/usr/bin/python
#This program simulates the spread of BSE in a one-species loop.
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
  #Initialize prion levels to 
  prions=scipy.zeros(ops.lifespan)
  prions[0]=ops.initial_infect

  R=scipy.exp(scipy.log(ops.R)/ops.timestep)

  c=scipy.zeros(ops.lifespan)
  feedback=ops.feedback.split(',')
  for n in range(len(feedback)):
      c[n]=float(feedback[n])

  times=[]
  plevels=[]
  for y in range(ops.years):
    for t in range(ops.timestep):
      times.append(y+t/float(ops.timestep))
      plevels.append(prions.sum())
      print "%f\t%f" % (y+t/float(ops.timestep),prions.sum())
      prions*=R
    prions=scipy.roll(prions,1)
    ly=prions[0]
    prions[0]=0
    prions+=ly*c

  return times,plevels

def main():
  parser = OptionParser(usage="%prog [options]", version="%prog 1.0")
  parser.add_option("-n", dest="lifespan", type="int", help="Lifespan of Animal\t\t(def: 5)", default=5)
  parser.add_option("-k", dest="timestep", type="int", help="Number of timesteps per year\t(def: 1)", default=1)
  parser.add_option("-r", dest="R", type="float", help="Replication rate\t\t(def: 5.0)", default=5.0)
  parser.add_option("-i", dest="initial_infect", type="float", help="Initial infection amount\t(def: 1.0)", default=1.0)
  parser.add_option("-c", dest="feedback", type="string", help="Feedback amount, a string separated by commas\t(def: 0.01)", default="0.01")
  parser.add_option("-y", dest="years", type="int", help="Number of years to run simulation\t(def: 25)", default="25")
  parser.add_option("-g", dest="graph", action="store_true", help="Graph results")

  (ops, args) = parser.parse_args()
  xvals,yvals=calc(ops)

  if ops.graph:
    import matplotlib.pyplot as plt
    plt.plot(xvals,yvals)
    plt.axis([0,25,0,10000])
    plt.show()


main()
