# Example demonstrating Adapter design pattern with phone chargers.

# Target Interface
class UniversalCharger:
    """
    Defines a common interface for charging phones, regardless of their specific port types.
    """

    def charge(self):
        pass


# Adaptees
class LightningPort:
    """
    Represents phones with a Lightning port (e.g., iPhone).
    """

    def lightning_charge(self):
        return "Charging iPhone with Lightning port."


class MicroUSBPort:
    """
    Represents phones with a Micro-USB port (e.g., older Android devices).
    """

    def micro_usb_charge(self):
        return "Charging Android phone with Micro-USB port."


class USBTypeCPort:
    """
    Represents phones with a USB Type-C port (e.g., modern Android devices).
    """

    def usb_type_c_charge(self):
        return "Charging device with USB Type-C port."


# Adapters
class LightningToUniversalAdapter(UniversalCharger):
    """
    Adapter for phones with a Lightning port to use a universal charger.
    """

    def __init__(self, phone: LightningPort):
        self.phone = phone

    def charge(self):
        return self.phone.lightning_charge()


class MicroUSBToUniversalAdapter(UniversalCharger):
    """
    Adapter for phones with a Micro-USB port to use a universal charger.
    """

    def __init__(self, phone: MicroUSBPort):
        self.phone = phone

    def charge(self):
        return self.phone.micro_usb_charge()


class USBTypeCToUniversalAdapter(UniversalCharger):
    """
    Adapter for phones with a USB Type-C port to use a universal charger.
    """

    def __init__(self, phone: USBTypeCPort):
        self.phone = phone

    def charge(self):
        return self.phone.usb_type_c_charge()


# Client Code
def charge_phone(charger: UniversalCharger):
    """
    The client code relies only on the UniversalCharger interface to charge phones.
    """
    print(charger.charge())


def main():
    # Phones with different ports
    iphone = LightningPort()
    android_old = MicroUSBPort()
    android_modern = USBTypeCPort()

    # Universal chargers with adapters
    universal_charger_for_iphone = LightningToUniversalAdapter(iphone)
    universal_charger_for_android_old = MicroUSBToUniversalAdapter(android_old)
    universal_charger_for_android_modern = USBTypeCToUniversalAdapter(android_modern)

    # Charge phones
    print("Charging devices:")
    charge_phone(universal_charger_for_iphone)
    charge_phone(universal_charger_for_android_old)
    charge_phone(universal_charger_for_android_modern)


if __name__ == "__main__":
    main()
