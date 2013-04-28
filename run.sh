#!/bin/bash
#This program runs the models developed in the manuscript
#
#"Modeling of bovine spongiform encephalopathy in a two-species feedback loop"
#By: Richard Barnes and Clarence Lehman
#doi: 10.1016/j.epidem.2013.04.001
#
#The output of these models is then plotted and converted to PDF format to
#produce the figures used in the manuscript.
#
#This code was written by Richard Barnes (rbarnes@umn.edu)

#Show a single species loop with lifespan held at 5 years
./one_species_model.py -k 10 -r 3 -n 5 -c 0.01 > fig_one5years.dat

#Show a single species loop with lifespan held at 4 years
./one_species_model.py -k 10 -r 3 -n 4 -c 0.01 > fig_one4years.dat

#Show a two-species loop with lifespans held at 8 years and 3 years
#Material is fed back to a single age class in both species
./two_species_model.py -k 10 -r 3 -s 0.8 -n 8 -m 3 -c 0.02,0,0,0,0,0,0,0,0.02 -y 40 > fig_two_species.dat

#Show a two-species loop with lifespans held at 8 years and 3 years
#Material is fed back to multiple age classes in both species
./two_species_model.py -k 10 -r 4 -s 0.7 -n 8 -m 3 -c 0.005,0.005,0.005,0,0,0,0,0,0.005,0.005,0 -y 40 > fig_two_species_multiple_feedback.dat

#Plot output of the models
./plot

#Convert EPS output to PDF
epspdf fig_one_species.eps fig_one_species.pdf
epspdf fig_two_species.eps fig_two_species.pdf
epspdf fig_two_species_multiple_feedback.eps fig_two_species_multiple_feedback.pdf

#Crop PDFs
pdfcrop fig_one_species.pdf fig_one_species.pdf
pdfcrop fig_two_species.pdf fig_two_species.pdf
pdfcrop fig_two_species_multiple_feedback.pdf fig_two_species_multiple_feedback.pdf
