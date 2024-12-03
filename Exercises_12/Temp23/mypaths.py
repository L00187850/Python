"""
File Name:mypaths.py
By: Philip Stewart
Student Number: L00187850
Date: 03 Dec 2024
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
UDP_SETTINGS = str(PROJECT_ROOT / "Network/UDP/settings/udp.py")

TCP_SETTINGS = str(PROJECT_ROOT / "Network/TCP/settings/tcp.py")