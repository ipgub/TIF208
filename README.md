# DSP

Notes on DSP using python.


## Packages

There are two competing packages currently found for DSP using python

- ThinkDSP

    + Written by [Mark Wickert](http://www.eas.uccs.edu/~mwickert/). Modul can be downloaded/cloned from https://github.com/mwickert/scikit-dsp-comm.

    + Web: http://www.eas.uccs.edu/~mwickert/ece5650/

    + Written lecture materials: only partially available, as some of course materials were password protected.

    + Codes: Some available as python jupiter notebook (must be further checked for its availability).

    + Additional plugin for jupyter is also required:
        -   labextension: create table of content. Install by the command

            >>   jupyter labextension install @jupyterlab/toc

            Sources: https://github.com/jupyterlab/jupyterlab-toc

    + Video: Available through the website. However, not all of them have been checked for its availability. The video are longer in duration (like 2 hours).

        - http://www.eas.uccs.edu/~mwickert/ece5650/lectures/5650_Lect2_f19.mp4.mp4

- scikit-dsp-comm

    + Written by: Allen Downey

    + Written materials: Book 'ThinkDSP' where we can also found the codes used in the book.

    + Sources: https://github.com/AllenDowney/ThinkDSP

    + Web: http://greenteapress.com/thinkdsp/thinkdsp.pdf

    + Video:


## Topics

### Systems

Concept to be covered:

- Discrete time systems

- Convolution

- Impulse response of DT system

- System output, given the description of the system in terms of LCCDE equation

- LTI system (filter): taken from Coursera course DSP, week #5


    + LTI systems description (video - coursera): https://d3c33hcgiwev3.cloudfront.net/o1xjAPTKEeWwywqelD7oVQ.processed/full/360p/index.webm?Expires=1586390400&Signature=e4WAtomGO8sPbuLsJKt5S2wK865dKI3jV98qIqN~8okTX2Kpsnp-nxIMo2tOuLTKgGgSU1kzq9-ZHudD~VT56RHXXrAARZWE-rtmErNKNZstvPJh0EGNJLOc67MY45fEVsKMMOQsJTtlru6yjnvqFAzfP-TbuPE-KmcOk4AEBh4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
    
    + Convolution - Impulse response
    
        - Video: https://d3c33hcgiwev3.cloudfront.net/o31_HPTKEeWAQhLLv31W2Q.processed/full/360p/index.webm?Expires=1586390400&Signature=B76mh7nSpxd5T6n9OMuEC2BCkjAfhzKy0npjIaV0HX-~CbNHUgPP9n73NSJJCjfwXWtGWuKxE6sdzy1lwY7P9cMt84KUQYAEfMevnbt1pjyneF5Nhtr7cSjF8L6kC0qQz23m5AjipcDkvbPPKfg24gtKgmxvRV-wIuyzKmgOCsY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
    
        - Question:
    
            ```
                     Let x[n] = u[n]x[n]=u[n],
    
                             h[n]  = 1 for n=0,
                                      1/2 for n=±1
                                      0 otherwise,
    
                              and y[n]=(x⋆h)[n]. Compute y[2]
    
            ```

   + Summary

   In this lesson we have studied a special class of processing devices called linear time-invariant (LTI) filters. As the name indicates, these systems are characterised by two properties:

   linearity: the output of a linear combination of inputs is equal to the linear combination of the outputs

   time-invariance: the system behaves in exactly the same way independently of when it is being switched on.

   These are very reasonable assumptions to make in practice and, as we will see, there is already a large set of processing methods that falls under this category.

   LTI filters are entirely characterised by their impulse response, i.e., their response to the impulse delta function \(\delta[n]\). From the impulse response \( h[n] \), the output of an LTI filter \(y[n]\) can be computed by convolving the input \( x[n]\) with the impulse response,

y[n] = \sum_{k=-\infty}^{\infty} x[k] h[n-k]y[n]=∑
k=−∞
∞
​	 x[k]h[n−k].

We have concluded this lesson by studying concrete examples of how to compute this convolution in practice.


   + Moving average filter

        - Video (8 min): https://d3c33hcgiwev3.cloudfront.net/FSgB4fTLEeWAQhLLv31W2Q.processed/full/360p/index.webm?Expires=1586390400&Signature=h5as6nIYc9H8ryYdiCOFfADmXT9euPBfTINCaan8HHACkydgwJgpuZTGaldHpI12QU3v9he~pAGYNJ4ljNeUeu4crSeAeP66SEc4lVvd-ACK-dSG218wZUttvq3AGp~fizAssm7ZEOPzEhG4J7gLgMvS7vMC3YAsmTQJtc4r9G4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

        - Question:

            ```
                Let x=(1 2 3 4 5 2 3 5 1 2), T h be a MA filter with M=4
                and y the filtered output of x with h. Compute y[2].

            ```

   + Leaky Integrator

        - Video (5 min): https://d3c33hcgiwev3.cloudfront.net/FUCTCfTLEeWHdw4u67-syQ.processed/full/360p/index.webm?Expires=1586390400&Signature=ToWwPzlmr7Wcnu-J2XgQmGcptynX4A6t0z92t2LcfLMVTh6Dt4IY29VxaI-3~EV19O21TmEsm92RoH-9wUyc7xwsIQP3a4cZ4cQhxQ9TXkrMAGV-T7x7RkC4IUPFO8h7omE0j5ZHt9kq0bNbotLnFrR8886Pn4VrVj33FBKTIG4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

        - Question


   + Summary

   In this lesson we have studied two examples of LTI filters, the moving average and the leaky integrator. The moving average is just a local average computed over the last M observations, including the current one. We have seen the formula for its impulse response and derived a simple recursive formula to compute it efficiently.

   The leaky integrator is a special case of the moving average filter when M becomes large. It is also defined by a recursive formula. The basic idea is to add a portion \( \lambda \) of the past accumulated values so far and a fraction \((1 - \lambda)\)  of the current observation. By setting the value of \(\lambda \) less than 1, we ensure the system never blows up.


#### Text materials

- Signals and systems:
    http://pilot.cnxproject.org/content/collection/col10064/latest/module/m34614/latest

[Discrete Time System](http://pilot.cnxproject.org/content/collection/col10064/latest/module/m34614/latest)

[Discrete Time Impulse Response](http://pilot.cnxproject.org/content/collection/col10064/latest/module/m34626/latest)

[Convolution](http://pilot.cnxproject.org/content/collection/col10064/latest/module/m10087/latest)

[Linear Constant Coefficient Difference Equation LCCDE](http://pilot.cnxproject.org/content/collection/col10064/latest/module/m12325/latest)


#### System output

The coefficients of an LCCDE equation is equivalent to the coefficient of a filter.

Example on Matlab (from [Lab Manual][/Users/irwan/Documents/MyLectures/DSP/xref/lab_manual_DSP.pdf]) for linearity's check:

````matlab
 
clear all, close all
n = 0:40;
a = 2; b = -3;
x1 = cos(2*pi*0.1*n);
x2 = cos(2*pi*0.4*n);
x = a*x1 + b*x2;
num = [2.2403 2.4908 2.2403]; den = [1 -0.4 0.75];
ic = [0 0];   % Set zero initial conditions
y1 = filter(num,den,x1,ic);       % Compute the output y1[n]
y2 = filter(num,den,x2,ic); % Compute the output y2[n]
y = filter(num,den,x,ic); % Compute the output y[n]
yt = a*y1 + b*y2;
d = y - yt; % Compute the difference output d[n]
% Plot the outputs and the difference signal
subplot (3,1,1)
stem(n ,y);
ylabel('Amplitude');
title('Output Due to Weighted Input');
subplot(3,1,2)
stem(n,yt);
ylabel('Amplitude');
title('Weighted Output');
subplot(3,1,3)
stem(n,d);
xlabel('Time index n');
ylabel('Amplitude');
title('Difference Signal');

````

Python equivalent for Matlab's filter is scipy's signal module `lfilter` with syntax

```py
scipy.signal.lfilter(b, a, x, axis=-1, zi=None)[source]
```

which can be used for similar purpose to the above Matlab linearity check using the following code:

````python
b=np.array([1,2,2,1])
a=np.array([1])

# define signals
x1 =
x2 =

````

provided that we have checked the similarity/equivalence between Matlab's filter() function and python's lfilter() modul.

The scipy.signal.lfilter is implemented as a direct II transposed structure. This means that the filter implements:

```py
a[0]*y[n] = b[0]*x[n] + b[1]*x[n-1] + ... + b[M]*x[n-M]
                      - a[1]*y[n-1] - ... - a[N]*y[n-N]
```

The rational transfer function describing this filter in the z-transform domain is:

```
                     -1              -M
        b[0] + b[1]z  + ... + b[M] z
Y(z) = -------------------------------- X(z)
                    -1              -N
        a[0] + a[1]z  + ... + a[N] z

```

in which `b[n]` and `a[n]` are the NUMERATOR and DENOMINATOR of the filter, respectively.

#### Impulse response

Matlab for impulse response

```m
% Compute the impulse response y
close all, clear all
N = 40;
num = [2.2403 2.4908 2.2403];
den = [1 -0.4 0.75];
y = impz(num,den,N);
% Plot the impulse response
stem(y);
xlabel('Time index n'); ylabel('Amplitude');
title('Impulse Response'); grid;

```

For python, there's no impz function/module. Following [this page](https://share.cocalc.com/share/2d40fa76b887c790c8326000d30003490133d16e/DSPBasics.ipynb?viewer=share), we have to create an impulse (discrete) and filter it to get the response:

```py

b=np.array([1,2,2,1])
a=np.array([1])

def delta(pos,len):
    x  = np.zeros(len)
    x[pos] = 1.0
    return x

imp = delta(0,100)
plt.stem(imp)
plt.show()
h_ = signal.lfilter(b,a,imp)
plt.stem(h_)
plt.show()
```

However, from [another page](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.dimpulse.html), there is scipy's signal implementation of discrete time system's impulse respons
