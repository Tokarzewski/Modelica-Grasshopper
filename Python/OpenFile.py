from subprocess import call

Exe = "C:/OpenModelica/bin/OMEdit.exe"
#Mo = "C:/OpenModelica/share/doc/omc/testmodels/SimpleIntegrator.mo"
#Open = True

if Open == True:
    call([Exe, Mo])