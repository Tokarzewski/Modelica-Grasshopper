#Python version of batch file "C:\JModelica.org-2.14\setenv.bat"
#SUNDIALS_HOME, IPOPT_HOME AND JPYPE_JVM have to be set mannualy

import sys, os
sys.path.append("C:\JModelica.org-2.14\install\Python_64")
import pyfmi, pymodelica, assimulo

os.environ["JM_BIN_HOME"]="C:\JModelica.org-2.14"
os.environ["JMODELICA_HOME"]=os.environ["JM_BIN_HOME"]+"\install"

os.environ["MINGW_HOME"]=os.environ["JM_BIN_HOME"]+"\MinGW"
os.environ["SUNDIALS_HOME"]=os.environ["JMODELICA_HOME"]+"\ThirdParty\Sundials" #why manually?
os.environ["JAVA_HOME"]=os.environ["JM_BIN_HOME"]+"\Java\jdk-11.0.2"
os.environ["SEPARATE_PROCESS_JVM"]=os.environ["JM_BIN_HOME"]+"\Java\jdk-11.0.2"
os.environ["IPOPT_HOME"]=os.environ["JM_BIN_HOME"]+"\Ipopt\Ipopt64" #why manually?
os.environ["JVMDLL64_HOME"]=os.environ["JM_BIN_HOME"]+"\Java\jdk-11.0.2\\bin\server"
os.environ["PYTHONHOME"]=os.environ["JM_BIN_HOME"]+"\Python27\Python_64"
os.environ["PYTHONPATH"]=os.environ["JMODELICA_HOME"]+"\Python_64"
os.environ["CASADI_LIB_HOME"]=os.environ["JMODELICA_HOME"]+"\ThirdParty\CasADi64\lib"
os.environ["CASADI_INTERFACE_HOME"]=os.environ["JMODELICA_HOME"]+"\lib\casadi_interface64"
os.environ["JPYPE_JVM"]=os.environ["JM_BIN_HOME"]+"\Java\jdk-11.0.2\\bin\server\jvm.dll" #why manually?
os.environ["BOOST_HOME"]=os.environ["JM_BIN_HOME"]+"\BoostSubsetCasADiInterface"

PATH=[]
PATH.append(os.environ["MINGW_HOME"]+"\\bin")
PATH.append(os.environ["PYTHONHOME"])
PATH.append(os.environ["PYTHONHOME"]+"\Scripts")
PATH.append(os.environ["CASADI_LIB_HOME"])
PATH.append(os.environ["JVMDLL64_HOME"])
PATH.append(os.environ["JM_BIN_HOME"]+"\Java\jdk-11.0.2\\bin")
PATH.append(os.environ["IPOPT_HOME"])
PATH.append(os.environ["PATH"])
os.environ["PATH"]=";".join(PATH)

import pyjmi, casadi