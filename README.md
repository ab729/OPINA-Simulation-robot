# Technical Report: Autonomous Robot Car with Camera and Web Interface

## Table of Contents
1. [Introduction](#introduction)
2. [Project Objectives](#project-objectives)
3. [System Architecture](#system-architecture)
4. [Hardware Components](#hardware-components)
5. [Software Components](#software-components)
    - [Video Streaming](#video-streaming)
    - [Line Following Algorithm](#line-following-algorithm)
    - [Web Interface](#web-interface)
6. [Implementation Details](#implementation-details)
    - [Camera Integration](#camera-integration)
    - [Autonomous Driving](#autonomous-driving)
    - [Web Interface Development](#web-interface-development)
7. [Challenges and Solutions](#challenges-and-solutions)
8. [Testing and Results](#testing-and-results)
9. [Conclusion](#conclusion)
10. [Future Work](#future-work)
11. [References](#references)
12. [Approval and Signatures](#approval-and-signatures)

## Introduction
This report documents the development of an autonomous robot car equipped with a camera and a web interface for real-time video monitoring and control. The robot car is designed to follow a white line on the ground, making it suitable for applications in autonomous driving and robotics education. The project integrates both hardware and software components, leveraging computer vision and web technologies.

## Project Objectives
- Develop an autonomous robot car that can follow a white line using computer vision.
- Integrate a camera to capture live video feed from the robot's perspective.
- Develop a web interface for real-time monitoring and control of the robot car.
- Implement basic movement commands (left, right, forward, stop) based on visual input.
- Provide an option to toggle between manual control and autonomous driving.

## System Architecture
The system consists of three main components:
1. **Hardware**: Includes the Raspberry Pi, camera, motors, and sensors.
2. **Software**: Consists of the Python scripts for video processing, autonomous control algorithms, and the Flask web application.
3. **Communication**: The web interface communicates with the robot via HTTP requests, allowing for real-time control and monitoring.

## Hardware Components
- **Raspberry Pi**: The main computing unit that runs the software components.
- **Camera**: Used to capture live video feed and detect the white line on the ground.
- **Motors and Motor Driver**: Control the movement of the robot car.
- **Sensors (Optional)**: Additional sensors for obstacle detection and environmental feedback.

## Software Components

### Video Streaming
The robot car captures live video using the Raspberry Pi camera. The video feed is processed using OpenCV, a powerful library for computer vision tasks. The processed frames are streamed to a web interface where users can monitor the robot's surroundings.

### Line Following Algorithm
The line following algorithm processes each video frame to detect a white line on the ground. The algorithm converts the frame to grayscale, applies Gaussian blur, and thresholds the image to create a binary mask. Contours are detected, and the centroid of the largest contour is used to determine the robot's direction.

### Web Interface
The web interface is built using Flask, a lightweight web framework in Python. It provides a real-time video feed from the robot's camera and control buttons to move the robot manually. An additional button allows the user to toggle the autonomous driving mode.

## Implementation Details

### Camera Integration
The Raspberry Pi camera is interfaced with OpenCV to capture and process video frames. The `VideoCamera` class manages the video capture, processing, and encoding of frames for web streaming.

### Autonomous Driving
The autonomous driving mode is implemented using a simple line following algorithm. The robot's movements (left, right, forward) are controlled based on the position of the detected line in the camera's field of view.

### Web Interface Development
The web interface uses Flask to serve the video feed and control buttons. The interface allows users to monitor the live feed and send movement commands. Autonomous mode can be toggled through a POST request that alters the robot's behavior.

## Challenges and Solutions
- **Camera Calibration**: Initial challenges with camera calibration were resolved by tuning the Gaussian blur and thresholding parameters.
- **Frame Processing Speed**: Optimized the processing pipeline to ensure real-time performance by reducing the resolution and complexity of image processing tasks.
- **Circular Imports**: Refactored the code to eliminate circular imports by decoupling the Flask application logic from the camera control logic.

## Testing and Results
The robot car was tested in various environments to assess its ability to follow a white line. The system was able to consistently detect and follow the line under controlled lighting conditions. The web interface provided smooth video streaming and responsive control. The autonomous driving mode was effective in simple, obstacle-free scenarios.

## Conclusion
The project successfully developed an autonomous robot car with real-time video streaming and web-based control. The system demonstrated the ability to follow a white line and switch between manual and autonomous driving modes. This project serves as a foundational platform for further developments in autonomous vehicles and robotic systems.

## Future Work
- Implement obstacle detection and avoidance to enhance autonomous driving capabilities.
- Improve the robustness of the line-following algorithm in varying lighting conditions.
- Add additional sensors for more complex environmental interactions.
- Expand the web interface to include telemetry data and advanced control features.

## References
- OpenCV Documentation: [https://opencv.org/](https://opencv.org/)
- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Raspberry Pi Camera Module: [https://www.raspberrypi.org/documentation/usage/camera/](https://www.raspberrypi.org/documentation/usage/camera/)

## Approval and Signatures

**Project Lead**  
*Name:* Ahmed Barazenji 
*Signature:* a.b 
*Date:* 11.08.2024

**Reviewer**  
*Name:* Dr. Öğr. Üyesi Can Gökçe  
*Signature:* ___________________________  
*Date:* 12.08.2024

**Project Supervisor**  
*Name:* Dr. Öğr. Üyesi Can Gökçe 
*Signature:* ___________________________  
*Date:* 12.08.2024

---

