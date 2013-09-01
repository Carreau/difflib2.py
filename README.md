[![Build Status](https://travis-ci.org/Carreau/difflib2.py.png?branch=master)](https://travis-ci.org/Carreau/difflib2.py)

# Difflib2

> A surpriseless alternative to difflib.

Even if python difflib does a lot of great things, in the few cases I
encounterd it didn't behave in a sensible way (not giving the correct edit
length between 2 sequences and/or a weird api)

I also came across the fact that to build more sophisticated diff program I
woudl need to access lower level methods. 

So was born difflib2, might not be as fast (for now) as difflib, but hopefully
more reliable and surprise less.

Hopefully in the long term it could be a drop-in replacement for difflib, but
with more availlables methods.
