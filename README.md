# STEERER

## Project Purpose
Develop an AI system to monitor and estimate crowd density in Makkah during Hajj and Umrah pilgrimages to ensure pilgrim safety and optimize crowd management.

## The Challenge
- 2–3 million pilgrims gather in Makkah during Hajj.
- Crowd densities vary dramatically, from 50 to 2000+ people per area.
- Safety critical – overcrowding can lead to stampedes and casualties.
- Complex environment with buildings, structures, and varying crowd patterns.
- Real-time monitoring needed for immediate crowd management decisions.

## Dual Model Solution
### Why Two Models Together
- **CrowdHat** – Detects individual heads clearly in sparse areas.
- **STEERER** – Estimates density in packed, overlapping crowds.

Both run simultaneously on the same image for complete coverage.

### System Architecture
1. Makkah video feed
2. Remove buildings/structures (segmentation)
3. Parallel processing:
    - CrowdHat → Count individual pilgrims
    - STEERER → Estimate dense crowd areas
4. Intelligent fusion → Final crowd count
5. Safety alerts & crowd management

## Technical Goal
Achieve <15 heads/frame accuracy across all crowd densities while excluding buildings and providing real-time analysis for Makkah crowd safety management.

## Installation
```bash
python -m pip install opencv-python-headless numpy ultralytics
```

## Usage
```bash
python steerer.py --input "C:\\Users\\user\\OneDrive\\Desktop\\6min.mp4" --output result.mp4
```
Green dots represent STEERER density estimates, and red dots mark CrowdHat head detections. Press `q` to exit the viewer.
