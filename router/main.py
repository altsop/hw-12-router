from router.endDevice import EndDevice
from router.packet import Packet
from router.router import Router

if __name__ == "__main__":
    """Main for testing the functions."""
    # Initialize router
    router = Router("192.168.1.1")
    print(router.get_ip_address())  # 192.168.1.1
    print(router.get_devices())     # []
    print()

    # Initialize end devices
    device1 = EndDevice()
    device2 = EndDevice()
    print(f"{device1.get_ip_address()!a}")     # ''
    print()

    # Add devices to router
    print(router.add_device(device1))   # True
    print(router.add_device(device1))   # False (no duplicates allowed)
    print(router.add_device(device2))   # True
    print(len(router.get_devices()))    # 2
    print()

    # Check generated IP addresses
    print(device1.get_ip_address().startswith("192.168.1."))                # True (correct subnet)
    print(1 < int(device1.get_ip_address().split(".")[-1]) < 255)           # True (correct ending)
    print(device1.get_ip_address() == device2.get_ip_address())             # False (different IP addresses generated)
    print(router.get_device_by_ip(device1.get_ip_address()) == device1)     # True
    print()

    # Create packet from device1 to device2
    packet1 = Packet("message1", device1.get_ip_address(), device2.get_ip_address(), 1, 1)
    print(packet1)                          # message1 from 192.168.1.[some number] to 192.168.1.[some number](1:1)
    router.receive_packet(packet1)          # (this should send packet to device2)
    print(len(device2.get_all_packets()))   # 1
    print(len(device1.get_all_packets()))   # 0
    print(len(device2.get_all_packets_by_id(1)))    # 1
    print(len(device2.get_all_packets_by_source_ip(device1.get_ip_address())))  # 1
    print()

    # Create packet from device1 to unknown destination
    packet2 = Packet("message2", device1.get_ip_address(), "10.0.255.44", 2, 1)
    router.receive_packet(packet2)          # (this should drop the packet)
    print(len(device1.get_all_packets()))   # 0
    print(len(device2.get_all_packets()))   # 1
    print()

    # Remove end device from router
    print(router.remove_device(device1))    # True
    print(router.remove_device(device1))    # False (already removed)
    print(f"{device1.get_ip_address()!a}")  # ''
    print(len(router.get_devices()))        # 1