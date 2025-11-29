from router.packet import Packet


class EndDevice:
    """End device class."""

    def __init__(self):
        """
        Initialize end device.

        End device will have an IP address if they are connected to a router.
        Also, end device will collect all packets that are sent to them.
        """
        # Write your code here
        pass

    def get_ip_address(self) -> str:
        """Return the current IP address of the device."""
        # Write your code here
        pass

    def set_ip_address(self, ip_address: str) -> None:
        """
        Set an IP address for the device.

        You don't need to validate the IP address here.
        """
        # Write your code here
        pass

    def add_packet(self, packet: Packet) -> None:
        """Add a packet to end device."""
        # Write your code here
        pass

    def clear_packet_history(self) -> None:
        """Clear all packets from history."""
        # Write your code here
        pass

    def get_all_packets(self) -> list[Packet]:
        """Get a list of all packets in the order they were added."""
        # Write your code here
        pass

    def get_all_packets_by_id(self, given_id: int) -> list[Packet]:
        """Get a list of all packets that have the given ID."""
        # Write your code here
        pass

    def get_all_packets_by_source_ip(self, given_ip: str) -> list[Packet]:
        """Get a list of all packets that have given source IP."""
        # Write your code here
        pass

