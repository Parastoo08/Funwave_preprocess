function [] = nc2grd(name_nc,name_grd)
ele = ncread(name_nc,'elevation');
lat = ncread(name_nc,'lat');
lon = ncread(name_nc,'lon');

xmin=min(lon);
xmax=max(lon);
ymin=min(lat);
ymax=max(lat);
aux=size(ele);

nx=aux(2);ny=aux(1);
grdfile=fopen(name_grd,'w');                % Open file
fprintf(grdfile,'%c','DSAA');               % Header code
fprintf(grdfile,'\n %i %i',[nx ny]);        % Grid size
fprintf(grdfile,'\n %f %f',[xmin xmax]);    % X limits
fprintf(grdfile,'\n %f %f',[ymin ymax]);    % Y limits
fprintf(grdfile,'\n %f %f',[min(min(ele)) max(max(ele))]); % Z limits
fprintf(grdfile,'\n');
for jj=1:ny                                 % Write matrix
    for ii=1:nx
        fprintf(grdfile,'%g %c',ele(jj,ii),' ');
    end
    fprintf(grdfile,'\n');
end
fclose(grdfile);

end

