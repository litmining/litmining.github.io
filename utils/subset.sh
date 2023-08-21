#! /bin/bash

# subset selection from https://markoskon.com/creating-font-subsets/

pyftsubset \
    "$1" \
    --output-file="$2" \
    --flavor=woff2 \
    --layout-features="kern,liga,clig,calt,ccmp,locl,mark,mkmk,\
  onum,pnum,smcp,c2sc,frac,lnum,tnum,subs,sups,\
  cswh,dlig,ss01,ss03,zero"\
    --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,\
  U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,\
  U+2122,U+2190-21BB,U+2212,U+2215,U+F8FF,U+FEFF,U+FFFD"
