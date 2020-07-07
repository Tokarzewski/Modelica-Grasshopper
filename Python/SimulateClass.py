from OMPython import ModelicaSystem

#Input Model
mod=ModelicaSystem(ModelPath,ClassName) #2 arguments
#mod=ModelicaSystem(ModelPath, ClassName, ["Modelica"]) #3 arguments 
#mod=ModelicaSystem(ModelPath, ClassName, commandLineOptions="-d=newInst") #4 arguments

#Outputs
Quantities = mod.getQuantities()
SimOptions = mod.getSimulationOptions()
if RunSimulation == True:
    mod.simulate()
    Solutions = list(mod.getSolutions())
else:
    Solutions = mod.getSolutions()