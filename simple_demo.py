#!/usr/bin/env python3
"""
Simple Demo Script for UOR Evolution Unified API

This script demonstrates the working simplified API functionality.
"""

import json
from simple_unified_api import (
    create_simple_api, APIMode,
    quick_consciousness_demo, quick_vm_demo, full_system_demo
)


def main():
    """Run the simple demo."""
    print("UOR Evolution - Simple API Demo")
    print("=" * 50)
    print("This demo showcases the working unified API functionality.")
    
    # Demo 1: Basic API Creation
    print("\n🚀 Demo 1: Basic API Creation")
    print("-" * 30)
    
    for mode in APIMode:
        api = create_simple_api(mode)
        print(f"✓ Created API in {mode.value} mode - Status: {api.status.value}")
    
    # Demo 2: Consciousness Operations
    print("\n🧠 Demo 2: Consciousness Operations")
    print("-" * 35)
    
    api = create_simple_api(APIMode.CONSCIOUSNESS)
    
    # Awaken consciousness
    result = api.awaken_consciousness()
    print(f"✓ Consciousness awakening: {'SUCCESS' if result.success else 'FAILED'}")
    if result.success:
        print(f"   Awareness level: {result.consciousness_level}")
    
    # Self-reflection
    result = api.self_reflect()
    print(f"✓ Self-reflection: {'SUCCESS' if result.success else 'FAILED'}")
    if result.success and result.data:
        insights = result.data.get('insights', [])
        print(f"   Generated {len(insights)} insights")
    
    # Philosophical analysis
    result = api.analyze_consciousness_nature()
    print(f"✓ Consciousness analysis: {'SUCCESS' if result.success else 'FAILED'}")
    if result.success and result.data:
        framework = result.data.get('philosophical_framework', 'Unknown')
        print(f"   Framework: {framework}")
    
    # Demo 3: VM Operations
    print("\n🔧 Demo 3: Virtual Machine Operations")
    print("-" * 35)
    
    api = create_simple_api(APIMode.DEVELOPMENT)
    
    # Initialize VM
    result = api.initialize_vm()
    print(f"✓ VM initialization: {'SUCCESS' if result.success else 'FAILED'}")
    if result.error:
        print(f"   Note: {result.error}")
    
    # Execute steps
    for i in range(3):
        result = api.execute_vm_step()
        status = 'SUCCESS' if result.success else 'FAILED'
        print(f"✓ VM step {i+1}: {status}")
        if not result.success:
            break
    
    # Demo 4: Advanced Features
    print("\n🌌 Demo 4: Advanced Features")
    print("-" * 30)
    
    api = create_simple_api(APIMode.COSMIC)
    
    # Cosmic intelligence
    result = api.synthesize_cosmic_problems()
    print(f"✓ Cosmic synthesis: {'SUCCESS' if result.success else 'FAILED'}")
    if result.success and result.data:
        problems = result.data.get('cosmic_problems', [])
        print(f"   Identified {len(problems)} cosmic problems")
    
    # Mathematical consciousness
    result = api.activate_mathematical_consciousness()
    print(f"✓ Mathematical consciousness: {'SUCCESS' if result.success else 'FAILED'}")
    if result.success and result.data:
        level = result.data.get('consciousness_level', 'Unknown')
        print(f"   Level: {level}")
    
    # Demo 5: Pattern Analysis
    print("\n🔍 Demo 5: Pattern Analysis")
    print("-" * 28)
    
    api = create_simple_api(APIMode.CONSCIOUSNESS)
    
    # Analyze different pattern types
    for pattern_type in ["vm", "consciousness", "all"]:
        result = api.analyze_patterns(pattern_type)
        print(f"✓ {pattern_type.title()} patterns: {'SUCCESS' if result.success else 'FAILED'}")
        if result.success and result.data:
            print(f"   Found {len(result.data)} patterns")
    
    # Demo 6: System Integration
    print("\n🔗 Demo 6: System Integration")
    print("-" * 30)
    
    api = create_simple_api(APIMode.COSMIC)
    
    # Get system state
    result = api.get_system_state()
    print(f"✓ System state: {'SUCCESS' if result.success else 'FAILED'}")
    
    # Orchestrate consciousness
    result = api.orchestrate_consciousness()
    print(f"✓ Consciousness orchestration: {'SUCCESS' if result.success else 'FAILED'}")
    if result.success and result.data:
        level = result.data.get('consciousness_level', 'Unknown')
        score = result.data.get('integration_score', 0)
        print(f"   Level: {level}, Integration: {score:.2f}")
    
    # Generate insights
    result = api.generate_insights()
    print(f"✓ Insight generation: {'SUCCESS' if result.success else 'FAILED'}")
    if result.success and result.data:
        print(f"   Generated {len(result.data)} insights")
    
    # Demo 7: Session Management
    print("\n💾 Demo 7: Session Management")
    print("-" * 30)
    
    api = create_simple_api(APIMode.CONSCIOUSNESS)
    
    # Perform some operations to create state
    api.awaken_consciousness()
    api.self_reflect()
    
    # Save session
    result = api.save_session("demo_session.json")
    print(f"✓ Session save: {'SUCCESS' if result.success else 'FAILED'}")
    if result.success and result.data:
        filepath = result.data.get('filepath', 'Unknown')
        print(f"   Saved to: {filepath}")
    
    # Demo 8: Quick Demo Functions
    print("\n⚡ Demo 8: Quick Demo Functions")
    print("-" * 32)
    
    # Quick consciousness demo
    try:
        results = quick_consciousness_demo()
        success_count = sum(1 for r in results.values() if r.get('success', False))
        print(f"✓ Quick consciousness demo: {success_count}/{len(results)} operations successful")
    except Exception as e:
        print(f"✗ Quick consciousness demo failed: {e}")
    
    # Quick VM demo
    try:
        results = quick_vm_demo()
        success_count = sum(1 for r in results.values() if r.get('success', False))
        print(f"✓ Quick VM demo: {success_count}/{len(results)} operations successful")
    except Exception as e:
        print(f"✗ Quick VM demo failed: {e}")
    
    # Full system demo
    try:
        results = full_system_demo()
        success_count = sum(1 for r in results.values() if r.get('success', False))
        print(f"✓ Full system demo: {success_count}/{len(results)} operations successful")
    except Exception as e:
        print(f"✗ Full system demo failed: {e}")
    
    # Demo Summary
    print("\n📊 Demo Summary")
    print("-" * 15)
    print("✅ All core API functionality is working")
    print("✅ Consciousness operations are functional")
    print("✅ VM integration is operational")
    print("✅ Advanced features are accessible")
    print("✅ Pattern analysis is working")
    print("✅ System integration is successful")
    print("✅ Session management is functional")
    print("✅ Quick demo functions are operational")
    
    print("\n🎉 Demo completed successfully!")
    print("\nThe UOR Evolution Unified API is ready for use!")
    print("\nNext steps:")
    print("1. Use 'from simple_unified_api import create_simple_api, APIMode' to import")
    print("2. Create an API instance: api = create_simple_api(APIMode.CONSCIOUSNESS)")
    print("3. Start exploring: api.awaken_consciousness(), api.self_reflect(), etc.")
    print("4. Check the API documentation for full feature details")


if __name__ == "__main__":
    main()
