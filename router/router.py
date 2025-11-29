from router.endDevice import EndDevice
from router.packet import Packet


class Router:
    """Router class."""

    def __validate_ipv4(self, ip_address: str) -> bool:
        """Validate IPv4."""
        # Write your code here
        pass

    def __init__(self, ip_address: str):
        """
        Initialize router.

        IP address must be a string in the format "x.x.x.1"
        where x is a number in the range [0, 255], such as "192.168.0.1".

        If the IP address does not match this criteria, set the IP address to "192.168.0.1".

        The first 3 sections ("192.168.0" in this example) form a subnet. You will need this later!
        """
        # Write your code here
        pass

    def get_ip_address(self) -> str:
        """Return the current IP address of the router."""
        # Write your code here
        pass

    def generate_ip_address(self) -> str:
        """
        Generate a valid IP address.

        The IP address must be in the router's subnet.
        This means that the first 3 sections of the IP address must be the same as in the router's IP.

        The final section can be a random number in the range [2, 254].

        Make sure you can't generate an IP address that's already in use by a device!

        If there are no possible IP addresses to generate, raise an IPv4AddressSpaceExhaustedException().
        """
        # Write your code here
        pass

    def add_device(self, device: EndDevice) -> bool:
        """
        Add end device to router.

        The same device can not be added twice.
        Each device should be assigned an unique IP address in the correct subnet.

        The method should return True if device was added, else False.
        """
        # Write your code here
        pass

    def remove_device(self, device: EndDevice) -> bool:
        """
        Remove an end device from the router.

        If a device is removed from the router, then the router can no longer send
        packets to the device and the device's IP address is set to an empty string.

        The method should return True if device was removed, else False.
        """
        # Write your code here
        pass

    def get_devices(self) -> list[EndDevice]:
        """Get all devices that are connected to the router in the order they were connected."""
        # Write your code here
        pass

    def get_device_by_ip(self, ip: str) -> EndDevice | None:
        """
        Get a device by given IP.

        If there is no device with given IP, then return None.
        Otherwise return the found device.
        """
        # Write your code here
        pass

    def receive_packet(self, packet: Packet) -> None:
        """
        Receive a packet from the Internet.

        If there is a device with the destination IP in this subnet then forward this packet to this device.
        Otherwise drop this packet. (don't do anything with it)
        """
        # Write your code here
        pass

