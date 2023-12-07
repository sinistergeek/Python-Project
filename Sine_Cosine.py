import numpy as np
import matplotlib.pyplot as plot

time = np.linspace(-2*np.pi,2*np.pi,256,endpooint=True)
amplitude_sin = np.sin(time)
amplitude_cos = np.cos(time)
plot.plot(time,amplitude_sin)
plot.plot(time,amplitude_cos)

plot.title('Sine&Cos wave')
plot.xlabel("Time")
plot.ylabel('Amplitude')
plot.grid(True,which='both')
plot.axhline(y=0,color='k')
plot.show()
plot.show()
