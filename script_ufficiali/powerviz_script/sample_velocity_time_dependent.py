# Direct Recorded Script
# PowerVIZ 6-2022-R1 ( PowerVIZ 6.0.5 )
# Date: Tue Jul 11 18:35:19 2023

project6=app.currentProject

#########################
### Creazione grafici 
#########################


project6 = app.newProject(CDIFilename="./ac-NASA_UFSC-V16_2chW-M0.3-NoSlip_NoSlip_run_fine.cdi", fluidFilename="./ac_plane1_stream_inst_avg.snc", exportAnalysisCaseObject="", exportSimulationObject="", name="Project1", variablesToLoad=["Velocity Magnitude","X-Velocity","Y-Velocity","Z-Velocity","Static Pressure","Density","Temperature","Total Pressure","Total Temperature"])




baseAssembly1=project6.baseAssembly
modelView1=baseAssembly1.defaultModelView
part20=project6.getEntityByPath("/plane1_stream")
modelViewObject142=modelView1.getModelViewObject(part20)
modelViewObject142.imageShow="On"
modelViewObject142.streamlineShow="On"
modelViewObject142.contourShow="On"
modelViewObject142.licShow="On"
viewer1=project6.getViewer(0)
camera1=viewer1.camera
coordSystem1=project6.get(name="default_csys", type="CoordSystem")

surfaceImage1=project6.get(name="Surface Image", type="SurfaceImage")
scalarPropertySet2=project6.get(name="X-Velocity", type="ScalarPropertySet")
surfaceImage1.scalarPropertySet=scalarPropertySet2

timeAnimation1=project6.timeAnimation

surfaceGraph1 = project6.new(type="SurfaceGraph")
surfaceGraph1.name = "Sample"
surfaceGraph1.orientationMode = "X-Aligned"
scalarPropertySet51=project6.get(name="X-Velocity", type="ScalarPropertySet")
surfaceGraph1.scalarPropertySet=scalarPropertySet51
surfaceGraph1.rotate90Degrees()
##################################
### Plot ed Export
##################################
t0 = project6.nextTimeFrameSteps
tf = project6.endTimeFrameSteps
n_ts = project6.numberTimeFrames

import numpy as np
ts = int((tf-t0)/n_ts)
project6.timeStep=t0
timeAnimation1.timestep=t0
i = 0 

while project6.currentTimeFrame != n_ts-1:

    x_position = 0.065

    surfaceGraph1.position = ((x_position, -0.02, 0.006223), "m")
    surfaceGraph1.size = ((0.04, 0.04, 1.21543e-05), "m")
    xYGraph = surfaceGraph1.calculate()
    xYGraph.exportToCSV(filename="time_{}.csv".format(i+1), onlyVisible=False)
	
    i += 1
    prev_ts = project6.timeStep
    project6.timeStep=prev_ts+ts
    timeAnimation1.timestep=prev_ts+ts
    
# sign=bXG97hFcoolq3o2fr19/p7fmw5UZERBPtPI+b5MRttm3Wyb6vHKjVkWYLpK8Qi2je8aj7N0Ip5WUWnwXS5Pab02uH2KqTkNkMWisQ0qnZxgtbthj1PJ/3jBraclbxVxRUDpI+yoM7h4OAxTboUuwxRscfDpTnj4MsQTINrQGHhE=
