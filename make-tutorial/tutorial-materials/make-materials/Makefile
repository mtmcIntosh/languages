# pdbprocess.mk - Caroline Gorham
# dependencies, what the make file is doing

include config.mk

#all: PDBAnalysis.tar.gz #topmost dependency
all: $(ARCHIVE) 		

#PDBAnalysis.tar.gz: cubane.pdb.data ethane.pdb.data methane.pdb.data propane.pdb.data
#       tar -czf $PDBAnalysis.tar.gz cubane.pdb.data ethane.pdb.data methane.pdb.data
$(ARCHIVE): $(patsubst %.pdb, %.pdb.data,$(wildcard *.pdb)) $(PROCESSOR) 
	tar -czf $@ $^               #$@ dependant, $^ dependancy

#octane.pdb.data : octane.pdb process_pdb.sh
#	./process_pdb.sh octane.pdb > octane.pdb.data
%.pdb.data : %.pdb $(PROCESSOR)
	./$(PROCESSOR) $< > $@     # $< instead of $^ for only first dependency

# make info, could give help information and text or whatever is useful
info : 
	echo pdbprocess.mk        

# make clean, start fresh
clean : 
	rm *.pdb.data
