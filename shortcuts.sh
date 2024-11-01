# copy POSCAR to Table remove all lines until 2 are on top of actual information

#clean of nonsense info
sed "s/O/O /g" Table |  sed "s/Co/Co /g"  | sed "s/H/H /g" | sed -E "s/C[1-9]/C /g" > tmp

# harvest charges
paste ACF.dat tmp | awk '$14=="H"{print $14, $2, $3, $4 ,1.0-$5}$14=="O"{print $14, $2, $3, $4 ,6.0-$5}$14=="C"{print $14, $2, $3, $4 ,4.0-$5}$14=="Co"{print $14, $2, $3, $4 ,9-$5} 14=="O"{print $14, $2, $3, $4 ,6-$5}'  > Charge_Table

# gnuplot 
 splot 'Charge_Table' u 2:3:4:5 w points palette pt 7

# calculate charge deficite in molecule
 tail -n 28 Charge_Table  | awk '{a+=$5}END{print a}'

