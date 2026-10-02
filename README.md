\# Vision-Guided Robotic Arm

A vision-guided robotic arm simulation that uses computer vision to detect objects and autonomously perform pick-and-place operations in a simulated environment.

\## 📌 Project Overview

This project demonstrates the integration of computer vision, Python programming, and robotic simulation for autonomous object handling.
A webcam is used to capture the workspace, while OpenCV processes the visual information to identify the target object based on its color. The detected information is communicated to a UR5 robotic arm simulated in CoppeliaSim.
The robotic arm then moves to the target location, performs the pick operation, and places the object at the designated location.

\## 🎯 Objectives

\- Detect objects using computer vision.
\- Identify the target object based on color.
\- Establish communication between Python and CoppeliaSim.
\- Control a UR5 robotic arm in simulation.
\- Perform autonomous pick-and-place operations.
\- Demonstrate the application of computer vision in robotic automation.

\## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming and robot control |
| OpenCV | Computer vision and color detection |
| CoppeliaSim | Robotic simulation environment |
| UR5 | Simulated robotic arm |
| Lua | Robot-side simulation control |
| ZeroMQ Remote API | Python–CoppeliaSim communication |

## System Workflow

Webcam
|
v
Image Acquisition
|
v
OpenCV Processing
|
v
Color / Object Detection
|
v
Python Robot Control
|
v
ZeroMQ Remote API
|
v
CoppeliaSim
|
v
UR5 Robotic Arm
|
v
Pick and Place

