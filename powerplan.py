import ctypes
import subprocess
import platform

class PowerPlan:
    def __init__(self):
        if platform.system() != "Windows":
            raise EnvironmentError("PowerPlan is only supported on Windows devices.")

    def _run_command(self, command):
        """Helper method to run a shell command and return the output."""
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        return result.stdout.strip()

    def list_power_plans(self):
        """List all available power plans."""
        command = "powercfg -list"
        return self._run_command(command)

    def set_power_plan(self, plan_guid):
        """Set the power plan based on the provided GUID."""
        command = f"powercfg -setactive {plan_guid}"
        self._run_command(command)

    def get_current_power_plan(self):
        """Retrieve the current power plan GUID."""
        command = "powercfg -getactivescheme"
        output = self._run_command(command)
        return output.split(":")[1].strip()

    def customize_power_settings(self, setting, value):
        """Customize specific power settings."""
        command = f"powercfg -change {setting} {value}"
        self._run_command(command)

    def balance_performance_and_energy(self):
        """An example method to balance performance and energy consumption."""
        # Example: Set the power plan to 'Balanced'
        balanced_guid = "381b4222-f694-41f0-9685-ff5bb260df2e"
        self.set_power_plan(balanced_guid)

        # Customize specific settings if needed
        # Example: Set the display timeout to 10 minutes (600 seconds)
        self.customize_power_settings("monitor-timeout-dc", 600)

def main():
    power_plan = PowerPlan()
    print("Available Power Plans:")
    print(power_plan.list_power_plans())

    print("\nCurrent Power Plan:")
    print(power_plan.get_current_power_plan())

    print("\nBalancing Performance and Energy...")
    power_plan.balance_performance_and_energy()

    print("\nUpdated Power Plan:")
    print(power_plan.get_current_power_plan())

if __name__ == "__main__":
    main()