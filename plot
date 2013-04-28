#!/usr/bin/gnuplot
#This program plots the output of the models developed in the manuscript
#
#"Modeling of bovine spongiform encephalopathy in a two-species feedback loop"
#By: Richard Barnes and Clarence Lehman
#doi: 10.1016/j.epidem.2013.04.001
#
#The results are the figures used in the manuscript.
#
#This code was written by Richard Barnes (rbarnes@umn.edu)

set terminal postscript portrait
set output "fig_one_species.eps"

#set size 0.8,0.4
set lmargin 2.8
set multiplot
set size ratio 0.3
set size 0.8,0.4
set origin 0.1,0.1
set xtics 5
set xrange[0:25]
set xlabel "Year"
set ylabel "Prion Level" offset 0,5
plot "fig_single4years.dat" u ($1+1):2 w lines t "4 years"
set xlabel ""
set origin 0.1,0.32
set xtics format ""
set x2tics 5
set ylabel ""
plot "fig_single5years.dat" u ($1+1):2 w lines t "5 years"
unset multiplot

reset
set xrange [0:40]
#set yrange [0:12]
#set y2range [0:120]
set y2tic format "% g"
set ytics nomirror
set xlabel "Year"
set ylabel "Prion Units in Long-Lived Species"
set y2label "Prion Units in Short-Lived Species"
set key left top
set terminal postscript eps
set size ratio 0.5
set size 0.8,0.8
set output "fig_two_species.eps"
plot "fig_two_species.dat" u 1:2 w lines t "Long-Lived" ls 1, "fig_two_species.dat" u 1:3 w lines axes x1y2 t "Short-Lived" ls 2

reset
set xrange [0:40]
#set yrange [0:12]
#set y2range [0:120]
set y2tic format "% g"
set ytics nomirror
set xlabel "Year"
set ylabel "Prion Units in Long-Lived Species"
set y2label "Prion Units in Short-Lived Species"
set key left top
set terminal postscript eps
set size ratio 0.5
set size 0.8,0.8
set output "fig_two_species_multiple_feedback.eps"
plot "fig_two_species_multiple_feedback.dat" u 1:2 w lines t "Long-Lived" ls 1, "fig_two_species_multiple_feedback.dat" u 1:3 w lines axes x1y2 t "Short-Lived" ls 2
