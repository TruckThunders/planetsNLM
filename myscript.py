# PYTHON CODE TO DO STUFF FOR SOFTWARE CARPENTRY
# THINGS TO DO GO HERE

import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.nan)

try:

    print "Beginning script."

    coolArray = np.zeros(20)+np.random.rand(20)
    
    print coolArray

except Exception, e:
    print 'You broke it. Good job. Now try again, but this time with feeling.'
