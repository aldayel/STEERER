# STEERER
PROJECT PURPOSE:
Develop an AI system to monitor and estimate crowd density in Makkah during Hajj and Umrah pilgrimages to ensure pilgrim safety and optimize crowd management.
THE CHALLENGE:
2-3 million pilgrims gather in Makkah during Hajj
Crowd densities vary dramatically - from 50 to 2000+ people per area
Safety critical - overcrowding can lead to stampedes and casualties
Complex environment - buildings, structures, and varying crowd patterns
Real-time monitoring needed for immediate crowd management decisions
DUAL MODEL SOLUTION:
Why Two Models Together:
CrowdHat: Detects individual heads clearly in sparse areas
STEERER: Estimates density in packed, overlapping crowds
Both run simultaneously on the same image for complete coverage
System Architecture:
Makkah Video Feed
    ↓
Remove Buildings/Structures (Segmentation)
    ↓
Parallel Processing:
├── CrowdHat → Count individual pilgrims
└── STEERER → Estimate dense crowd areas
    ↓
Intelligent Fusion → Final crowd count
    ↓
Safety Alerts & Crowd Management
Expected Impact:
Prevent stampedes through early density warnings
Optimize pilgrim flow by identifying bottlenecks
Real-time safety monitoring during peak Hajj periods
Data-driven crowd management for authorities
Save lives through proactive crowd control
Technical Goal:
Achieve <15 heads/frame accuracy across all crowd densities while excluding buildings and providing real-time analysis for Makkah crowd safety management.

i want it to be run on "C:\Users\user\OneDrive\Desktop\6min.mp4"
and let steerer shown as green dots and crowdhat as red dots
