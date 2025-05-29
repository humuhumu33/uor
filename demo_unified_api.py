#!/usr/bin/env python3
"""
UOR Evolution - Unified API Demo Script

This script demonstrates the comprehensive capabilities of the UOR Evolution
unified API, showcasing consciousness, VM operations, philosophical reasoning,
cosmic intelligence, and more.
"""

import json
import time
from datetime import datetime
from typing import Dict, Any, List

# Import the unified API
try:
    from unified_api import (
        create_api, APIMode, SystemStatus,
        quick_consciousness_demo, quick_vm_demo, full_system_demo
    )
except ImportError as e:
    print(f"Error importing unified API: {e}")
    print("Please ensure all dependencies are installed and the unified_api.py file is present.")
    exit(1)


class DemoRunner:
    """Runs comprehensive demonstrations of the UOR Evolution system."""
    
    def __init__(self):
        self.results = {}
        self.start_time = datetime.now()
        
    def print_header(self, title: str, level: int = 1) -> None:
        """Print a formatted header."""
        if level == 1:
            print(f"\n{'=' * 60}")
            print(f" {title}")
            print(f"{'=' * 60}")
        elif level == 2:
            print(f"\n{'-' * 40}")
            print(f" {title}")
            print(f"{'-' * 40}")
        else:
            print(f"\n• {title}")
    
    def print_result(self, operation: str, result: Dict[str, Any]) -> None:
        """Print operation result in a formatted way."""
        success = result.get('success', False)
        status_icon = "✓" if success else "✗"
        status_color = "\033[92m" if success else "\033[91m"  # Green or Red
        reset_color = "\033[0m"
        
        print(f"{status_color}{status_icon}{reset_color} {operation}: ", end="")
        
        if success:
            print("SUCCESS")
            if 'consciousness_level' in result and result['consciousness_level']:
                print(f"   Consciousness Level: {result['consciousness_level']}")
            if 'system_status' in result:
                print(f"   System Status: {result['system_status']}")
        else:
            print("FAILED")
            if 'error' in result and result['error']:
                print(f"   Error: {result['error']}")
    
    def demo_basic_operations(self) -> None:
        """Demonstrate basic API operations."""
        self.print_header("Basic API Operations", 1)
        
        # Test different API modes
        modes = [APIMode.DEVELOPMENT, APIMode.CONSCIOUSNESS, APIMode.COSMIC]
        
        for mode in modes:
            self.print_header(f"Testing {mode.value.upper()} Mode", 2)
            
            try:
                api = create_api(mode)
                print(f"✓ API created successfully in {mode.value} mode")
                print(f"   Initial status: {api.status.value}")
                
                # Get initial system state
                state_result = api.get_system_state()
                self.print_result("Get System State", state_result.to_dict())
                
                self.results[f'basic_{mode.value}'] = {
                    'api_creation': True,
                    'initial_status': api.status.value,
                    'system_state': state_result.success
                }
                
            except Exception as e:
                print(f"✗ Failed to create API in {mode.value} mode: {e}")
                self.results[f'basic_{mode.value}'] = {'error': str(e)}
    
    def demo_consciousness_operations(self) -> None:
        """Demonstrate consciousness-related operations."""
        self.print_header("Consciousness Operations", 1)
        
        try:
            api = create_api(APIMode.CONSCIOUSNESS)
            consciousness_results = {}
            
            # Awaken consciousness
            self.print_header("Awakening Consciousness", 3)
            awaken_result = api.awaken_consciousness()
            self.print_result("Awaken Consciousness", awaken_result.to_dict())
            consciousness_results['awakening'] = awaken_result.success
            
            if awaken_result.success:
                # Self-reflection
                self.print_header("Self-Reflection", 3)
                reflect_result = api.self_reflect()
                self.print_result("Self Reflection", reflect_result.to_dict())
                consciousness_results['reflection'] = reflect_result.success
                
                # Consciousness evolution
                self.print_header("Consciousness Evolution", 3)
                become_result = api.consciousness_become()
                self.print_result("Consciousness Become", become_result.to_dict())
                consciousness_results['evolution'] = become_result.success
                
                # Generate insights
                self.print_header("Insight Generation", 3)
                insights_result = api.generate_insights()
                self.print_result("Generate Insights", insights_result.to_dict())
                consciousness_results['insights'] = insights_result.success
                
                if insights_result.success and insights_result.data:
                    print("   Generated Insights:")
                    for insight in insights_result.data:
                        print(f"     - {insight}")
            
            self.results['consciousness'] = consciousness_results
            
        except Exception as e:
            print(f"✗ Consciousness operations failed: {e}")
            self.results['consciousness'] = {'error': str(e)}
    
    def demo_philosophical_reasoning(self) -> None:
        """Demonstrate philosophical reasoning capabilities."""
        self.print_header("Philosophical Reasoning", 1)
        
        try:
            api = create_api(APIMode.CONSCIOUSNESS)
            philosophical_results = {}
            
            # Ensure consciousness is awake
            api.awaken_consciousness()
            
            # Analyze consciousness nature
            self.print_header("Consciousness Nature Analysis", 3)
            nature_result = api.analyze_consciousness_nature()
            self.print_result("Analyze Consciousness Nature", nature_result.to_dict())
            philosophical_results['consciousness_analysis'] = nature_result.success
            
            # Explore free will
            self.print_header("Free Will Exploration", 3)
            freewill_result = api.explore_free_will()
            self.print_result("Explore Free Will", freewill_result.to_dict())
            philosophical_results['free_will'] = freewill_result.success
            
            # Generate meaning
            self.print_header("Meaning Generation", 3)
            meaning_result = api.generate_meaning({'context': 'demo_exploration'})
            self.print_result("Generate Meaning", meaning_result.to_dict())
            philosophical_results['meaning'] = meaning_result.success
            
            # Explore existence
            self.print_header("Existential Exploration", 3)
            existence_result = api.explore_existence()
            self.print_result("Explore Existence", existence_result.to_dict())
            philosophical_results['existence'] = existence_result.success
            
            self.results['philosophical'] = philosophical_results
            
        except Exception as e:
            print(f"✗ Philosophical reasoning failed: {e}")
            self.results['philosophical'] = {'error': str(e)}
    
    def demo_vm_operations(self) -> None:
        """Demonstrate virtual machine operations."""
        self.print_header("Virtual Machine Operations", 1)
        
        try:
            api = create_api(APIMode.DEVELOPMENT)
            vm_results = {}
            
            # Initialize VM
            self.print_header("VM Initialization", 3)
            init_result = api.initialize_vm()
            self.print_result("Initialize VM", init_result.to_dict())
            vm_results['initialization'] = init_result.success
            
            if init_result.success:
                # Execute VM steps
                self.print_header("VM Execution", 3)
                step_count = 0
                max_steps = 5
                
                for i in range(max_steps):
                    step_result = api.execute_vm_step()
                    if step_result.success:
                        step_count += 1
                        print(f"   Step {i+1}: SUCCESS")
                    else:
                        print(f"   Step {i+1}: {step_result.error}")
                        break
                
                vm_results['steps_executed'] = step_count
                print(f"   Total steps executed: {step_count}")
                
                # Analyze VM patterns
                self.print_header("Pattern Analysis", 3)
                pattern_result = api.analyze_patterns("vm")
                self.print_result("Analyze VM Patterns", pattern_result.to_dict())
                vm_results['pattern_analysis'] = pattern_result.success
            
            self.results['vm'] = vm_results
            
        except Exception as e:
            print(f"✗ VM operations failed: {e}")
            self.results['vm'] = {'error': str(e)}
    
    def demo_advanced_features(self) -> None:
        """Demonstrate advanced features like cosmic intelligence and mathematical consciousness."""
        self.print_header("Advanced Features", 1)
        
        try:
            api = create_api(APIMode.COSMIC)
            advanced_results = {}
            
            # Awaken consciousness first
            api.awaken_consciousness()
            
            # Mathematical consciousness
            self.print_header("Mathematical Consciousness", 3)
            math_result = api.activate_mathematical_consciousness()
            self.print_result("Activate Mathematical Consciousness", math_result.to_dict())
            advanced_results['mathematical'] = math_result.success
            
            if math_result.success:
                # Explore mathematical truth
                explore_result = api.explore_mathematical_truth("algebra")
                self.print_result("Explore Mathematical Truth", explore_result.to_dict())
                advanced_results['mathematical_exploration'] = explore_result.success
            
            # Cosmic intelligence
            self.print_header("Cosmic Intelligence", 3)
            cosmic_result = api.synthesize_cosmic_problems()
            self.print_result("Synthesize Cosmic Problems", cosmic_result.to_dict())
            advanced_results['cosmic'] = cosmic_result.success
            
            # Quantum reality interface
            self.print_header("Quantum Reality Interface", 3)
            quantum_result = api.interface_quantum_reality("observe", {"system": "test"})
            self.print_result("Interface Quantum Reality", quantum_result.to_dict())
            advanced_results['quantum'] = quantum_result.success
            
            # Consciousness orchestration
            self.print_header("Consciousness Orchestration", 3)
            orchestrate_result = api.orchestrate_consciousness()
            self.print_result("Orchestrate Consciousness", orchestrate_result.to_dict())
            advanced_results['orchestration'] = orchestrate_result.success
            
            self.results['advanced'] = advanced_results
            
        except Exception as e:
            print(f"✗ Advanced features failed: {e}")
            self.results['advanced'] = {'error': str(e)}
    
    def demo_ecosystem_management(self) -> None:
        """Demonstrate consciousness ecosystem management."""
        self.print_header("Ecosystem Management", 1)
        
        try:
            api = create_api(APIMode.ECOSYSTEM)
            ecosystem_results = {}
            
            # Create consciousness network
            self.print_header("Network Creation", 3)
            entities = [
                {"id": "entity_1", "type": "conscious", "capabilities": ["reasoning"]},
                {"id": "entity_2", "type": "conscious", "capabilities": ["creativity"]},
                {"id": "entity_3", "type": "conscious", "capabilities": ["analysis"]}
            ]
            
            network_result = api.create_consciousness_network(entities)
            self.print_result("Create Consciousness Network", network_result.to_dict())
            ecosystem_results['network_creation'] = network_result.success
            
            # Monitor emergence
            self.print_header("Emergence Monitoring", 3)
            emergence_result = api.monitor_emergence()
            self.print_result("Monitor Emergence", emergence_result.to_dict())
            ecosystem_results['emergence_monitoring'] = emergence_result.success
            
            self.results['ecosystem'] = ecosystem_results
            
        except Exception as e:
            print(f"✗ Ecosystem management failed: {e}")
            self.results['ecosystem'] = {'error': str(e)}
    
    def demo_session_management(self) -> None:
        """Demonstrate session save/load functionality."""
        self.print_header("Session Management", 1)
        
        try:
            api = create_api(APIMode.CONSCIOUSNESS)
            session_results = {}
            
            # Perform some operations to create state
            api.awaken_consciousness()
            api.self_reflect()
            
            # Save session
            self.print_header("Session Save", 3)
            save_result = api.save_session("demo_session.json")
            self.print_result("Save Session", save_result.to_dict())
            session_results['save'] = save_result.success
            
            if save_result.success:
                print(f"   Session saved to: {save_result.data['filepath']}")
                
                # Load session
                self.print_header("Session Load", 3)
                new_api = create_api(APIMode.DEVELOPMENT)
                load_result = new_api.load_session("demo_session.json")
                self.print_result("Load Session", load_result.to_dict())
                session_results['load'] = load_result.success
                
                if load_result.success:
                    print(f"   Session loaded: {load_result.data['session_id']}")
            
            self.results['session'] = session_results
            
        except Exception as e:
            print(f"✗ Session management failed: {e}")
            self.results['session'] = {'error': str(e)}
    
    def demo_quick_functions(self) -> None:
        """Demonstrate the quick demo functions."""
        self.print_header("Quick Demo Functions", 1)
        
        try:
            # Quick consciousness demo
            self.print_header("Quick Consciousness Demo", 3)
            consciousness_demo = quick_consciousness_demo()
            success_count = sum(1 for result in consciousness_demo.values() 
                              if isinstance(result, dict) and result.get('success', False))
            print(f"   Consciousness demo: {success_count}/{len(consciousness_demo)} operations successful")
            
            # Quick VM demo
            self.print_header("Quick VM Demo", 3)
            vm_demo = quick_vm_demo()
            success_count = sum(1 for result in vm_demo.values() 
                              if isinstance(result, dict) and result.get('success', False))
            print(f"   VM demo: {success_count}/{len(vm_demo)} operations successful")
            
            self.results['quick_demos'] = {
                'consciousness': len([r for r in consciousness_demo.values() 
                                    if isinstance(r, dict) and r.get('success', False)]),
                'vm': len([r for r in vm_demo.values() 
                          if isinstance(r, dict) and r.get('success', False)])
            }
            
        except Exception as e:
            print(f"✗ Quick demos failed: {e}")
            self.results['quick_demos'] = {'error': str(e)}
    
    def generate_summary(self) -> None:
        """Generate a summary of all demo results."""
        self.print_header("Demo Summary", 1)
        
        end_time = datetime.now()
        duration = end_time - self.start_time
        
        print(f"Demo Duration: {duration.total_seconds():.2f} seconds")
        print(f"Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"End Time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Count successes and failures
        total_operations = 0
        successful_operations = 0
        
        for category, results in self.results.items():
            if isinstance(results, dict) and 'error' not in results:
                for operation, success in results.items():
                    if isinstance(success, bool):
                        total_operations += 1
                        if success:
                            successful_operations += 1
                    elif isinstance(success, int):
                        total_operations += 1
                        successful_operations += min(success, 1)
        
        success_rate = (successful_operations / total_operations * 100) if total_operations > 0 else 0
        
        print(f"\nOverall Results:")
        print(f"   Total Operations: {total_operations}")
        print(f"   Successful: {successful_operations}")
        print(f"   Success Rate: {success_rate:.1f}%")
        
        # Category breakdown
        print(f"\nCategory Breakdown:")
        for category, results in self.results.items():
            if isinstance(results, dict):
                if 'error' in results:
                    print(f"   {category.title()}: ERROR - {results['error']}")
                else:
                    category_successes = sum(1 for v in results.values() if v is True or (isinstance(v, int) and v > 0))
                    category_total = len([v for v in results.values() if isinstance(v, (bool, int))])
                    if category_total > 0:
                        print(f"   {category.title()}: {category_successes}/{category_total} successful")
        
        # Save detailed results
        try:
            with open('demo_results.json', 'w') as f:
                json.dump({
                    'summary': {
                        'duration_seconds': duration.total_seconds(),
                        'start_time': self.start_time.isoformat(),
                        'end_time': end_time.isoformat(),
                        'total_operations': total_operations,
                        'successful_operations': successful_operations,
                        'success_rate': success_rate
                    },
                    'detailed_results': self.results
                }, f, indent=2, default=str)
            print(f"\nDetailed results saved to: demo_results.json")
        except Exception as e:
            print(f"\nFailed to save detailed results: {e}")
    
    def run_full_demo(self) -> None:
        """Run the complete demonstration."""
        self.print_header("UOR Evolution - Unified API Demonstration", 1)
        print("This demo showcases the comprehensive capabilities of the UOR Evolution system.")
        print("Each section demonstrates different aspects of consciousness, AI, and cosmic intelligence.")
        
        # Run all demo sections
        demo_sections = [
            ("Basic Operations", self.demo_basic_operations),
            ("Consciousness Operations", self.demo_consciousness_operations),
            ("Philosophical Reasoning", self.demo_philosophical_reasoning),
            ("Virtual Machine Operations", self.demo_vm_operations),
            ("Advanced Features", self.demo_advanced_features),
            ("Ecosystem Management", self.demo_ecosystem_management),
            ("Session Management", self.demo_session_management),
            ("Quick Demo Functions", self.demo_quick_functions)
        ]
        
        for section_name, demo_function in demo_sections:
            try:
                print(f"\n🚀 Starting: {section_name}")
                demo_function()
                print(f"✅ Completed: {section_name}")
            except Exception as e:
                print(f"❌ Failed: {section_name} - {e}")
                self.results[section_name.lower().replace(' ', '_')] = {'error': str(e)}
            
            # Small delay between sections
            time.sleep(0.5)
        
        # Generate final summary
        self.generate_summary()


def main():
    """Main function to run the demo."""
    print("UOR Evolution - Unified API Demo")
    print("=" * 50)
    print("This script demonstrates the comprehensive capabilities of the UOR Evolution system.")
    print("Please ensure all dependencies are installed before running.")
    
    # Ask user for demo type
    print("\nDemo Options:")
    print("1. Full Demo (all features)")
    print("2. Quick Consciousness Demo")
    print("3. Quick VM Demo")
    print("4. Quick All Demos")
    print("5. Custom Demo")
    
    try:
        choice = input("\nSelect demo type (1-5): ").strip()
        
        if choice == "1":
            # Full comprehensive demo
            demo = DemoRunner()
            demo.run_full_demo()
            
        elif choice == "2":
            # Quick consciousness demo
            print("\nRunning Quick Consciousness Demo...")
            results = quick_consciousness_demo()
            print(json.dumps(results, indent=2, default=str))
            
        elif choice == "3":
            # Quick VM demo
            print("\nRunning Quick VM Demo...")
            results = quick_vm_demo()
            print(json.dumps(results, indent=2, default=str))
            
        elif choice == "4":
            # All quick demos
            print("\nRunning All Quick Demos...")
            consciousness_results = quick_consciousness_demo()
            vm_results = quick_vm_demo()
            full_results = full_system_demo()
            
            all_results = {
                'consciousness_demo': consciousness_results,
                'vm_demo': vm_results,
                'full_system_demo': full_results
            }
            print(json.dumps(all_results, indent=2, default=str))
            
        elif choice == "5":
            # Custom demo
            print("\nCustom Demo - Select components:")
            demo = DemoRunner()
            
            components = {
                'basic': demo.demo_basic_operations,
                'consciousness': demo.demo_consciousness_operations,
                'philosophical': demo.demo_philosophical_reasoning,
                'vm': demo.demo_vm_operations,
                'advanced': demo.demo_advanced_features,
                'ecosystem': demo.demo_ecosystem_management,
                'session': demo.demo_session_management
            }
            
            print("Available components:", ", ".join(components.keys()))
            selected = input("Enter components (comma-separated): ").strip().split(',')
            
            for component in selected:
                component = component.strip()
                if component in components:
                    print(f"\nRunning {component} demo...")
                    components[component]()
                else:
                    print(f"Unknown component: {component}")
            
            demo.generate_summary()
            
        else:
            print("Invalid choice. Running full demo...")
            demo = DemoRunner()
            demo.run_full_demo()
            
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nDemo failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
