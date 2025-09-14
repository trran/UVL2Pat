# 🎯 UVL2Pat

**Universal Design Patterns Generator - From UVL Feature Models to Swift Code**

Transform Universal Variability Language models into Swift design pattern implementations with future multi-language support

---

## 📊 Project Stats

| Design Patterns | Primary Language | Pattern Variants | Feature Models |
|:---------------:|:----------------:|:----------------:|:--------------:|
| 7+ | Swift | ∞ | UVL |

---

## ✨ Features

- **Swift Code Generation**: Generate high-quality Swift implementations of design patterns
- **UVL Integration**: Use Universal Variability Language for feature modeling
- **Template-Based Generation**: Flexible Jinja2 templates for Swift code
- **Constraint Validation**: Automatic validation of feature model constraints
- **Pattern Variants**: Generate multiple implementations of the same pattern
- **FlamaPy Integration**: Advanced feature model analysis and operations
- **Future Multi-Language Support**: Architecture designed for Kotlin, Java, Dart, C# expansion

## 🌐 Supported Languages

| Language | Status | Description |
|----------|--------|-------------|
| 🍎 **Swift** | ✅ **Available Now** | iOS/macOS Development |
| 🤖 **Kotlin** | 🚧 Planned | Android/JVM Development |
| ☕ **Java** | 🚧 Planned | Enterprise Development |
| 🎯 **Dart** | 🚧 Planned | Flutter Development |
| ⚡ **C#** | 🚧 Planned | .NET Development |
| 🚀 **More** | 🔮 Future | Extensible Architecture |

> **Current Focus:** UVL2Pat currently supports Swift with a robust, extensible architecture designed for future multi-language expansion. The template system and UVL integration provide a solid foundation for adding support for Kotlin, Java, Dart, C#, and other languages.

## 📋 Requirements

```bash
pip install jinja2 flamapy-fm pathlib click
```

## 📁 Project Structure

```
UVL2Pat/
├── patterns/
│   ├── behavioral/
│   │   ├── strategy/
│   │   │   ├── strategy.uvl
│   │   │   ├── templates/
│   │   │   │   └── strategy.swift.j2
│   │   │   └── configurations/
│   │   │       └── strategy.json
│   │   └── observer/
│   │       ├── observer.uvl
│   │       ├── templates/
│   │       │   └── observer.swift.j2
│   │       └── configurations/
│   │           └── observer.json
│   ├── creational/
│   │   ├── factory_method/
│   │   │   ├── factory_method.uvl
│   │   │   ├── templates/
│   │   │   │   └── factory_method.swift.j2
│   │   │   └── configurations/
│   │   └── singleton/
│   │       ├── singleton.uvl
│   │       ├── templates/
│   │       │   └── singleton.swift.j2
│   │       └── configurations/
│   │           └── singleton.json
│   └── structural/
│       ├── adapter/
│       ├── bridge/
│       └── decorator/
├── src/
├── tests/
├── requirements.txt
└── README.md
```

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/trran/UVL2Pat.git
   cd UVL2Pat
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install UVL2Pat:**
   ```bash
   pip install -e .
   ```

## 🎯 Quick Start

> **Generate your first pattern in 3 steps!**

### Python Script Usage

```python
import pathlib, json
from jinja2 import Environment, FileSystemLoader
import random
import pattern_generator
from flamapy.metamodels.fm_metamodel.transformations import UVLReader

base_dir = pathlib.Path(__file__).parent

# Available patterns by category:
# behavioral: strategy, observer
# creational: factory_method, singleton
# structural: adapter, bridge, decorator

# Configure pattern to generate
general_group = "creational"
pattern = "singleton"

# Setup paths
config_name = f"{pattern}.json"
template_name = f"{pattern}.swift.j2"
configuration_path = "configurations"
template_path = "templates"

template_dir = base_dir / "patterns" / general_group / pattern / template_path
json_configuration_dir = base_dir / "patterns" / general_group / pattern / configuration_path
configuration = json_configuration_dir / config_name

# Load configuration and generate
json_config = json.loads(configuration.read_text(encoding="utf-8"))
context = {
    "features": json_config
}

# Generate Swift code
pattern_generator.generate(context, template_name, template_dir, "")
```

### UVL Feature Model Integration

```python
def load_feature_model(uvl_file_path):
    """Load UVL feature model for advanced pattern generation"""
    fm = UVLReader(uvl_file_path).transform()
    return fm

# Example: Load and use UVL model
# fm = load_feature_model("patterns/creational/singleton/singleton.uvl")
# config = get_random_configuration(fm)
# features_dict = configuration_to_dict(config, fm)
```

### Pattern Generation Examples

```python
# Generate Singleton Pattern
general_group = "creational"
pattern = "singleton"
# Uses: singleton.json, singleton.swift.j2, singleton.uvl

# Generate Observer Pattern
general_group = "behavioral"
pattern = "observer"
# Uses: observer.json, observer.swift.j2, observer.uvl

# Generate Decorator Pattern
general_group = "structural"
pattern = "decorator"
# Uses: decorator.json, decorator.swift.j2, decorator.uvl
```

## 📝 Available Patterns

### 🎭 Behavioral Patterns
- **Strategy**: Encapsulate algorithms and make them interchangeable
- **Observer**: Define subscription mechanism for object state notifications
- **Command**: Encapsulate requests as objects `Coming Soon`
- **State**: Alter object behavior when internal state changes `Coming Soon`

### 🏭 Creational Patterns
- **Singleton**: Ensure single instance with global access point
- **Factory Method**: Create objects without specifying exact classes
- **Abstract Factory**: Create families of related objects `Coming Soon`
- **Builder**: Construct complex objects step by step `Coming Soon`

### 🏗️ Structural Patterns
- **Adapter**: Make incompatible interfaces work together
- **Bridge**: Separate abstraction from implementation
- **Decorator**: Add behavior to objects dynamically
- **Facade**: Provide simplified interface to complex subsystem `Coming Soon`

## ⚙️ Configuration System

### UVL Model Example (singleton.uvl)
```uvl
features
    "Singleton Pattern" {abstract}
        mandatory
            "Initialization" {abstract}
                alternative
                    "Eager"
                    "Lazy"
            "Access Method" {abstract}
                alternative
                    "getInstance()"
                    "Static Field"
                    "Property"
        optional
            "Thread Safety"
            "Serialization Support"
            String "Class Name"
            String "Namespace"

constraints
    "Eager" => !"Thread Safety"
    "Static Field" => "Eager"
    "Serialization Support" => "Thread Safety"
```

### JSON Configuration (singleton_threadsafe.json)
```json
{
  "Eager": false,
  "Lazy": true,
  "Initialization": true,
  "Access Method": true,
  "Thread Safety": true,
  "Serialization Support": false,
  "Class Name": "DatabaseManager",
  "Namespace": "com.example.data",
  "getInstance()": true,
  "Static Field": false,
  "Property": false
}
```

### Swift Template (singleton.swift.j2)
```swift
{% set class_name = features.get("Class Name", "Singleton") %}
{% if features.get("Namespace") %}// Namespace: {{ features.get("Namespace") }}{% endif %}
import Foundation
{% if features.get("Thread Safety") and features.get("Lazy") %}
import Dispatch
{% endif %}

class {{ class_name }} {
    {% if features.get("Eager") %}
    static let shared = {{ class_name }}()
    {% elif features.get("Lazy") %}
    {% if features.get("Thread Safety") %}
    private static var _instance: {{ class_name }}?
    private static let queue = DispatchQueue(label: "{{ class_name.lower() }}.queue")
    {% else %}
    private static var _instance: {{ class_name }}?
    {% endif %}
    {% endif %}
    
    private init() {
        // Private initializer
    }
}
```

### Generated Swift Code
```swift
// Namespace: com.example.data
import Foundation
import Dispatch

class DatabaseManager {
    private static var _instance: DatabaseManager?
    private static let queue = DispatchQueue(label: "databasemanager.queue")
    
    private init() {
        // Private initializer
    }
    
    static func getInstance() -> DatabaseManager {
        return queue.sync {
            if _instance == nil {
                _instance = DatabaseManager()
            }
            return _instance!
        }
    }
}
```

## 🔧 Advanced Usage

### Pattern Variants Generation

```python
# Generate different singleton variants
configurations = ["singleton_eager.json", "singleton_lazy.json", "singleton_threadsafe.json"]

for config_file in configurations:
    configuration = json_configuration_dir / config_file
    json_config = json.loads(configuration.read_text(encoding="utf-8"))
    context = {"features": json_config}
    
    # Generate with specific configuration
    output_file = f"Singleton_{config_file.replace('.json', '.swift')}"
    pattern_generator.generate(context, template_name, template_dir, output_file)
```

### Custom Template Directory

```python
# Use custom template location
custom_template_dir = base_dir / "custom_templates" / "singleton"

# Generate with custom template
pattern_generator.generate(context, template_name, custom_template_dir, "CustomSingleton.swift")
```

### Batch Pattern Generation

```python
# Generate multiple patterns
patterns_to_generate = [
    ("creational", "singleton"),
    ("behavioral", "observer"),
    ("structural", "decorator")
]

for group, pattern_name in patterns_to_generate:
    # Setup paths for each pattern
    template_dir = base_dir / "patterns" / group / pattern_name / "templates"
    config_dir = base_dir / "patterns" / group / pattern_name / "configurations"
    
    # Load configuration
    config_file = config_dir / f"{pattern_name}.json"
    json_config = json.loads(config_file.read_text(encoding="utf-8"))
    
    # Generate Swift code
    context = {"features": json_config}
    template_name = f"{pattern_name}.swift.j2"
    pattern_generator.generate(context, template_name, template_dir, f"{pattern_name.title()}.swift")
```

### UVL Feature Model Validation

```python
from flamapy.metamodels.fm_metamodel.transformations import UVLReader

def validate_configuration(uvl_path, config_dict):
    """Validate configuration against UVL constraints"""
    fm = UVLReader(uvl_path).transform()
    
    # Add validation logic here
    # This would check if the configuration satisfies UVL constraints
    return True  # Simplified for example

# Example usage
uvl_file = base_dir / "patterns" / general_group / pattern / f"{pattern}.uvl"
is_valid = validate_configuration(uvl_file, json_config)

if is_valid:
    pattern_generator.generate(context, template_name, template_dir, "")
else:
    print("Configuration violates UVL constraints")
```

## 📊 Feature Analysis

| Pattern | Swift Support | UVL Model | Configurations | Template Features |
|---------|---------------|-----------|----------------|-------------------|
| **Singleton** | ✅ Complete | ✅ | 8 variants | Thread Safety, Lazy/Eager, Access Methods |
| **Observer** | ✅ Complete | ✅ | 6 variants | Type Safety, Weak References, Combine |
| **Strategy** | ✅ Complete | ✅ | 4 variants | Protocol-based, Generic Implementation |
| **Factory Method** | 🚧 In Progress | ✅ | 5 variants | Generic Factories, Protocol Conformance |
| **Decorator** | 🚧 In Progress | ✅ | 3 variants | Protocol Extensions, Composition |

## 🚨 Constraint Validation

### UVL Constraint Examples:
- `"Eager" => !"Thread Safety"`: Eager initialization excludes thread safety
- `"Static Field" => "Eager"`: Static field access requires eager initialization
- `"Serialization Support" => "Thread Safety"`: Serialization requires thread-safe implementation

> **Validation Process:** UVL2Pat automatically validates configurations against UVL constraints before code generation, ensuring only valid pattern variants are created.

## 🤝 Contributing

### Adding New Patterns (Swift)
1. Create UVL feature model: `patterns/{category}/{pattern}/{pattern}.uvl`
2. Create Swift template: `patterns/{category}/{pattern}/templates/{pattern}.swift.j2`
3. Add configuration examples: `patterns/{category}/{pattern}/configurations/`
4. Write comprehensive tests for Swift implementation
5. Update documentation

### Preparing for Multi-Language Support
1. Design language-agnostic UVL models
2. Create template structure for future languages
3. Implement language detection and routing
4. Design extensible architecture for new language support

### Swift-Specific Contributions
- **iOS Optimizations**: Memory management, lifecycle patterns
- **SwiftUI Integration**: ObservableObject, StateObject patterns
- **Combine Framework**: Publisher/Subscriber implementations
- **Concurrency**: async/await pattern variations

### Development Process:
1. Fork the repository: `https://github.com/trran/UVL2Pat`
2. Create feature branch: `git checkout -b feature/new-pattern`
3. Implement Swift patterns with tests
4. Submit pull request with comprehensive documentation

## 🐛 Troubleshooting

### Common Issues and Solutions:
- **Swift Template Error**: Check Jinja2 syntax and Swift-specific constructs
- **UVL Parse Error**: Validate UVL syntax using FlamaPy tools
- **Constraint Violation**: Review configuration against UVL constraints
- **Generation Failed**: Verify template variables match JSON configuration
- **Swift Compilation Error**: Check generated Swift code syntax and imports
- **iOS Framework Issues**: Ensure proper Foundation/UIKit imports in templates

### Debug Mode
```python
# Enable verbose output
uvl2pat generate --pattern singleton --verbose

# Show template variables and Swift output
uvl2pat debug --pattern observer --config typed

# Validate Swift syntax
uvl2pat validate-swift --file ./output/Singleton.swift
```

## 📚 API Reference

### Core Functions
```python
import pattern_generator
from flamapy.metamodels.fm_metamodel.transformations import UVLReader

# Main generation function
pattern_generator.generate(
    context={"features": json_config},
    template_name="singleton.swift.j2",
    template_dir=template_directory,
    output_file=""  # Empty string for default output
)

# UVL model loading
def load_feature_model(uvl_file_path):
    fm = UVLReader(uvl_file_path).transform()
    return fm
```

### Pattern Configuration
```python
# Available pattern categories and their patterns
AVAILABLE_PATTERNS = {
    "behavioral": ["strategy", "observer"],
    "creational": ["factory_method", "singleton"], 
    "structural": ["adapter", "bridge", "decorator"]
}

# Path structure for patterns
def get_pattern_paths(base_dir, general_group, pattern):
    template_dir = base_dir / "patterns" / general_group / pattern / "templates"
    config_dir = base_dir / "patterns" / general_group / pattern / "configurations"
    uvl_file = base_dir / "patterns" / general_group / pattern / f"{pattern}.uvl"
    
    return template_dir, config_dir, uvl_file
```

### Configuration Loading
```python
# Load JSON configuration
def load_configuration(config_path):
    return json.loads(config_path.read_text(encoding="utf-8"))

# Create template context
def create_context(json_config):
    return {"features": json_config}

# Complete example
json_config = load_configuration(configuration_file)
context = create_context(json_config)
pattern_generator.generate(context, template_name, template_dir, output_file)
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support & Community

- **Issues**: Report bugs and request features on [GitHub Issues](https://github.com/trran/UVL2Pat/issues)
- **Discussions**: Join community discussions on [GitHub Discussions](https://github.com/trran/UVL2Pat/discussions)
- **Documentation**: Full documentation at [uvl2pat.readthedocs.io](https://uvl2pat.readthedocs.io)
- **Examples**: More Swift examples in the [examples/](https://github.com/trran/UVL2Pat/tree/main/examples) directory

---

<div align="center">

**🌟 Made with ❤️ for the Software Engineering Research Community 🌟**

*Transforming Feature Models into Code, One Pattern at a Time*

</div>
