% script for plotting
%%
clear all;clc;
text = fopen('earth_50y', 'r');
earth = [];
line = fgets(text);
while ~feof(text)
    if line(1) == 'M'
        line(regexp(line,'[Maaxkmyz,:]'))=[];
        line = strip(line);
        line = deblank(line);
        line = strsplit(line);
        vec = str2double(line);
        earth = [earth; vec];
    end
    line = fgets(text);
end
%%
plot(earth(:,1), earth(:,2))

%%
plot(earth(1:2*365,1), earth(1:2*365,2))
hold on
plot(earth(2*365:4*365,1), earth(2*365:4*365,2))
hold on
plot(earth(4*365:6*365,1), earth(4*365:6*365,2))
hold on
plot(earth(6*365:8*365,1), earth(6*365:8*365,2))
hold on
plot(earth(8*365:10*365,1), earth(8*365:10*365,2))
