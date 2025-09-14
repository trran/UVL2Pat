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

1. **Choose your pattern** by modifying the variables in `main.py`:
   ```python
   # Available categories and patterns:
   # behavioral: strategy, observer
   # creational: factory_method, singleton
   # structural: adapter, bridge, decorator

   general_group = "creational"    # Change category
   pattern = "singleton"           # Change pattern
   ```

2. **Run the generator:**
   ```bash
   python main.py
   ```

3. **Find your generated Swift code** in the output directory.

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

### UVL Model

**Singleton Feature Model (singleton.uvl):**
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

### JSON Configuration

**Configuration (singleton_threadsafe.json):**
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

### Swift Template

**Swift Template (singleton.swift.j2):**
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
