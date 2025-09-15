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

4. ### Pattern Generation Examples

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
        optional
            "Thread Safety"
            String "Class Name"

constraints
    "Eager" => !"Thread Safety"
    "Static Field" => "Eager"
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
  "Class Name": "singleton",
  "getInstance()": true,
  "Static Field": false
}
```

### Swift Template

**Swift Template (singleton.swift.j2):**
```swift
{# singleton.swift.j2 #}
{% set class_name = features.get("Class Name", "Singleton") %}
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
        // Private initializer to prevent external instantiation
        print("{{ class_name }} initialized")
    }
    
    {% if features.get("Access Method") %}
    {% if features.get("getInstance()") %}
    {% if features.get("Eager") %}
    static func getInstance() -> {{ class_name }} {
        return shared
    }
    {% elif features.get("Lazy") %}
    {% if features.get("Thread Safety") %}
    static func getInstance() -> {{ class_name }} {
        return queue.sync {
            if _instance == nil {
                _instance = {{ class_name }}()
            }
            return _instance!
        }
    }
    {% else %}
    static func getInstance() -> {{ class_name }} {
        if _instance == nil {
            _instance = {{ class_name }}()
        }
        return _instance!
    }
    {% endif %}
    {% endif %}
    {% endif %}
    
    {% if features.get("Static Field") %}
    {% if features.get("Eager") %}
    static var instance: {{ class_name }} {
        return shared
    }
    {% elif features.get("Lazy") %}
    {% if features.get("Thread Safety") %}
    static var instance: {{ class_name }} {
        return queue.sync {
            if _instance == nil {
                _instance = {{ class_name }}()
            }
            return _instance!
        }
    }
    {% else %}
    static var instance: {{ class_name }} {
        if _instance == nil {
            _instance = {{ class_name }}()
        }
        return _instance!
    }
    {% endif %}
    {% endif %}
    {% endif %}
    {% endif %}
    
    // MARK: - Public Methods
    
    func doSomething() {
        print("{{ class_name }} is doing something...")
    }
    
    func performTask(with data: String) -> String {
        print("{{ class_name }} performing task with: \(data)")
        return "Task completed by {{ class_name }}"
    }
    
    func getStatus() -> String {
        return "{{ class_name }} is active and ready"
    }
}
```
### Generated Swift Code
    import Foundation
    import Dispatch
    class singleton {
    private static var _instance: singleton?
    private static let queue = DispatchQueue(label: "singleton.queue")
    
    private init() {
        // Private initializer to prevent external instantiation
        print("singleton initialized")
    }

    static func getInstance() -> singleton {
        return queue.sync {
            if _instance == nil {
                _instance = singleton()
            }
            return _instance!
        }
    }

    // MARK: - Public Methods

    func doSomething() {
        print("singleton is doing something...")
    }

    func performTask(with data: String) -> String {
        print("singleton performing task with: \(data)")
        return "Task completed by singleton"
    }

    func getStatus() -> String {
        return "singleton is active and ready"
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

<div align="center">

*Transforming Feature Models into Code, One Pattern at a Time*

</div>
