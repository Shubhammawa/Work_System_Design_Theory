clc;
clear all;

x = [1:30];
y = [44,42,41,40,38,37,37,36,34,34,35,33,31,29,29,27,26,24,23,23,22,23,22,22,23,22,21,21,22,21];

X = log(x);
Y = log(y);
plot(X,Y,'r+:')
sum = 0;
for i =  1:29
    sum = sum + log(y(i+1)/y(i))/log(x(i+1)/x(i));
end
m = sum/30;
fprintf('%f\n',m)
    