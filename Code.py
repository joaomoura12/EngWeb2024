import os

##TODO
##Criar 8 Pastas TPC (TPC1, TPC2, ...)
##Criar Pasta "Projeto"
##Criar Pasta "Teste"
##Em cada pasta criar um ficheiro .gitkeep
for i in range(8):
    os.mkdir(f"TPC{i+1}")
    open(f"TPC{i+1}/.gitkeep", "w")

os.mkdir("Projeto")
open(f"Projeto/.gitkeep", "w")

os.mkdir("Teste")
open(f"Teste/.gitkeep", "w")