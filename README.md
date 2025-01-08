# PowerPlan

PowerPlan is a Python application designed to customize power settings on Windows devices to balance performance and energy consumption. It allows users to list available power plans, set a specific power plan, and customize particular power settings.

## Features

- List all available power plans on your Windows device.
- Set a specific power plan using its GUID.
- Retrieve the current active power plan.
- Customize specific power settings such as display timeout.
- Balance performance and energy consumption with pre-defined settings.

## Requirements

- Windows Operating System
- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PowerPlan.git
   ```
2. Navigate to the directory:
   ```bash
   cd PowerPlan
   ```

## Usage

Run the script using Python:

```bash
python powerplan.py
```

The program will display available power plans, show the current power plan, and apply settings to balance performance and energy consumption.

## Customization

You can modify the `balance_performance_and_energy` method in `powerplan.py` to customize power settings according to your needs. For example, you can change the display timeout or other power settings by using the `customize_power_settings` method.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.