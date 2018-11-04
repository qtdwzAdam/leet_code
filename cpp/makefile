all: program


program: 832.o function.o
		g++ -v -g -Wall -std=c++11 function.o 832.o -o program


832.o: 832.cpp
		g++ -c -std=c++11 832.cpp -o  832.o


function.o: function.cpp
		g++ -c function.cpp -o function.o


clean: 
		rm *.o
		rm program

