#!/usr/bin/env python3
"""
Simple test to validate the prompt execution output meets the requirements.
"""

import os
import re
from datetime import datetime

def test_generated_documentation():
    """Test that the generated documentation meets prompt requirements."""
    
    docs_path = "/home/runner/work/CopilotAspireArchitectureGeneration/CopilotAspireArchitectureGeneration/docs"
    
    # Find the most recent SolutionOverview file with timestamp format
    files = [f for f in os.listdir(docs_path) if f.startswith("SolutionOverview-") and f.endswith(".md")]
    timestamp_files = [f for f in files if re.match(r"SolutionOverview-\d{8}-\d{6}\.md", f)]
    
    if not timestamp_files:
        print("❌ No SolutionOverview files with timestamp format found")
        return False
    
    latest_file = max(timestamp_files)
    file_path = os.path.join(docs_path, latest_file)
    
    print(f"🔍 Testing generated file: {latest_file}")
    
    # Test 1: Filename format
    timestamp_pattern = r"SolutionOverview-\d{8}-\d{6}\.md"
    if not re.match(timestamp_pattern, latest_file):
        print("❌ Filename format doesn't match required pattern: SolutionOverview-yyyyMMdd-hhmmss.md")
        return False
    print("✅ Filename format is correct")
    
    # Test 2: File content requirements
    with open(file_path, 'r') as f:
        content = f.read()
    
    required_sections = [
        "# Solution Overview",
        "## Overview", 
        "## Goal and Purpose",
        "## Architecture",
        "## Architecture Diagrams",
        "### ASCII Diagram",
        "### Mermaid Chart"
    ]
    
    for section in required_sections:
        if section not in content:
            print(f"❌ Missing required section: {section}")
            return False
    print("✅ All required sections present")
    
    # Test 3: Both diagram formats present
    if "```mermaid" not in content:
        print("❌ Mermaid chart not found")
        return False
    print("✅ Mermaid chart present")
    
    if "AspireApp2" not in content or "orchestrates" not in content:
        print("❌ ASCII diagram content not found")
        return False
    print("✅ ASCII diagram present")
    
    # Test 4: Key architectural components mentioned
    components = ["AspireApp2.AppHost", "AspireApp2.Web", "AspireApp2.ApiService", "Redis", "SQL Server"]
    for component in components:
        if component not in content:
            print(f"❌ Missing architectural component: {component}")
            return False
    print("✅ All key architectural components documented")
    
    # Test 5: No mention of screenshots (as requested)
    if "screenshot" in content.lower():
        print("❌ Screenshots mentioned, but user requested no screenshots")
        return False
    print("✅ No screenshots mentioned (as requested)")
    
    print(f"✅ All tests passed! Generated documentation meets prompt requirements.")
    print(f"📄 File size: {len(content)} characters")
    
    return True

if __name__ == "__main__":
    success = test_generated_documentation()
    exit(0 if success else 1)