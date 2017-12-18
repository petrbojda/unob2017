% script to plot dBm levels

db = -100:100;
semilogx (dbm2volts(db,50),db);
grid on;