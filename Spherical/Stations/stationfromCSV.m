% Clearing Matlab workspace
close all
clear

% Directory of output data files
fdir=[pwd '\'];
a=readtable('stationsall.csv');
b=a{:,:};
fid = fopen('stationsall.txt', 'wt');
  fprintf(fid, ['%4.3f   ','%4.3f', '\n'], b');
  fclose(fid);