# ROS 2 Digital Twin & Real-time Telemetry Visualizer

This project demonstrates a professional implementation of a **Digital Twin** visualization system using **ROS 2 Jazzy** and **Rviz2**. It focuses on the communication between a robot's physical model and its live data status.

## 🚀 Overview
The system consists of a custom-designed robot (URDF) and a Python-based telemetry node. Instead of monitoring raw data in the terminal, this project visualizes robot health/status using **Dynamic Markers** in a 3D environment.

## 🛠 Features
- **URDF Modeling:** A clean, organized robot description.
- **Custom Telemetry Node:** A Python node that broadcasts `visualization_msgs/Marker` to reflect real-time status.
- **Rviz2 Integration:** Leverages the power of Rviz for data visualization rather than heavy simulation.
- **VirtualBox Optimized:** Designed to run efficiently in virtualized environments by prioritizing Rviz over Gazebo.

## 📁 Project Structure
- `urdf/robot.urdf`: The physical description of the robot.
- `mini_sentinel/brain_node.py`: The Python node logic for broadcasting telemetry data.
- `setup.py` & `package.xml`: Standard ROS 2 configuration for easy deployment.

## 💻 How to Run
1. **Launch the Visualizer:**
   ```bash
   ros2 launch urdf_tutorial display.launch.py model:=$(pwd)/src/mini_sentinel/urdf/robot.urdf
