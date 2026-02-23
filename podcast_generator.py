"""
AUTONOMOUS PODCAST GENERATOR - FIXED VERSION
Architecture: Multi-agent system with fallback mechanisms and state persistence
Primary Failure Mode Addressed: Unhandled external service dependencies
"""

import asyncio
import logging
import json
import sys
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum
import requests
from pathlib import Path

# Firebase imports for state persistence
try:
    import firebase_admin
    from firebase_admin import credentials, firestore
    FIREBASE_AVAILABLE = True
except ImportError:
    logging.warning("Firebase not available - using local state only")
    FIREBASE_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(