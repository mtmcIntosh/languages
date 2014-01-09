
datafile="data/m_0.0"
lines=$(cat $datafile |wc -l)

for file in 0.0 0.1 0.5; do 
	for line in {1..5} ; 
		do echo $file;
	done 
done > col_1

for file in `ls data/m*`; do
	 seq $lines 
done > col_2

cat data/m_0.0 data/m_0.1 data/m_0.5 > col_3

paste -d' ' col_1 col_2 col_3


