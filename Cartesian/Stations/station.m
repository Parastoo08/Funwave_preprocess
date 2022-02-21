% Clearing Matlab workspace
close all
clear

% Directory of output data files
fdir=[pwd '\'];
p1=[3919769.23,877184.59;4101249.29,1061673.37;4101248.29,1061674.37;4100409.61,1158702.62;4461552.08,853103.03;4149868.02,848654.08]
fid = fopen('stations_cartesian.txt', 'wt');
  fprintf(fid, ['%4.3f   ','%4.3f', '\n'], p1');
  fclose(fid);