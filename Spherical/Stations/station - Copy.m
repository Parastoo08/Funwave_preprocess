% Clearing Matlab workspace
close all
clear

% Directory of output data files
fdir=[pwd '\'];
p1=[35.35,25.15;36.89,27.30;36.89,27.28;36.84,28.38;40.23,25.89;37.44,24.94]
fid = fopen('stations_spherical1.txt', 'wt');
  fprintf(fid, ['%4.3f   ','%4.3f', '\n'], p1');
  fclose(fid);