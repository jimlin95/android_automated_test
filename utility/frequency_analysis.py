from pylab import plot, show, title, xlabel, ylabel, subplot, savefig , log
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

def plotSpectru(data,Fs):
    n = len(data) # lungime semnal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range
    
    Y = fft(data)/n # fft computing and normalization
    Y = Y[range(n/2)]
    
    plot(frq,abs(Y),'r') # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')
def plotAmplitudeSpectru(filename,outfile):

    rate,data=read(filename)
    lungime=len(data)
    timp=len(data)/float(rate)
    t=linspace(0,timp,len(data))
    subplot(2,1,1) 
    plot(t,data,'b')
    xlabel('Time')
    ylabel('Amplitude')
    subplot(2,1,2) 
    plotSpectru(data,float(rate))
    savefig(outfile) 
