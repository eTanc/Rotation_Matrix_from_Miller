#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#h=-1.0
#k=5.0
#l=9.0

h=1.
k=2.
l=3.


norm_miller=np.linalg.norm([h,k,l])

h_2=h/norm_miller
k_2=k/norm_miller
l_2=l/norm_miller


print '\n******************************************************'
print '\n**   COMPUTE ROTATION MATRIX FROM MILLER INDICES    **'
print '\n******************************************************'
print '\n\nh,k,l=',h,k,l
print '\n normalized h,k,l=',h_2,k_2,l_2

phi1= 0.

phi = np.arccos(l / np.sqrt( h*h + k*k + l*l))

phi2= np.arctan2(h / np.sqrt( h*h + k*k), k / np.sqrt(h*h + k*k))

print '\nphi1,phi,phi2=',phi1*180/np.pi,phi*180/np.pi,phi2*180/np.pi

c1=np.cos(phi1) # Psi, precession
s1=np.sin(phi1)
c2=np.cos(phi)  # theta, Nutation
s2=np.sin(phi)
c3=np.cos(phi2) #Phi, rotation propre
s3=np.sin(phi2)

#print c1,s1,c2,s2,c3,s3

M1 = np.matrix([[c1,s1,0.],
                [-s1,c1,0.],
                [0.,0.,1.]])

M2 = np.matrix([[1.,0.,0.],
                [0.,c2,s2],
                [0.,-s2,c2]])

M3 = np.matrix([[c3,s3,0.],
                [-s3,c3,0.],
                [0.,0.,1.]])

M=M3*M2*M1

#print M1,M2,M3


orthM=M*M.T

M = M.transpose()

print M

print '\nsum(M[:,0]**2)=',M[0,0]**2+M[1,0]**2+M[2,0]**2
print '\nsum(M[:,1]**2)=',M[0,1]**2+M[1,1]**2+M[2,1]**2
print '\nsum(M[:,2]**2)=',M[0,2]**2+M[1,2]**2+M[2,2]**2

print '\nM^t*M=',orthM

detM=np.linalg.det(M)

print '\ndet(M)=',detM

print '\nrotation_matrix=',M
#code M-Front
print '\n\n@RotationMatrix {{%6.15f,%6.15f,%6.15f},' % (M[0,0],M[0,1],M[0,2])
print '{%6.15f,%6.15f,%6.15f},' % (M[1,0],M[1,1],M[1,2])
print '{%6.15f,%6.15f,%6.15f}};' % (M[2,0],M[2,1],M[2,2])






