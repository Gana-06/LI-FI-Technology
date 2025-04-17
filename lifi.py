import time

def text_to_binary(text):
    """Convert text to binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    """Convert binary representation back to text."""
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def transmit_lifi(data):
    """Simulate Li-Fi transmission using light pulses."""
    binary_data = text_to_binary(data)
    print("\nTransmitting Data via Light Signals...\n")

    transmitted_signal = []
    for bit in binary_data:
        if bit == '1':
            print("💡 Light ON (1)", end=" ", flush=True)
            transmitted_signal.append(1)
        else:
            print("⚫ Light OFF (0)", end=" ", flush=True)
            transmitted_signal.append(0)
        time.sleep(0.5)  # Simulate light pulse duration

    print("\n\nTransmission Complete!")
    return transmitted_signal

def receive_lifi(signal):
    """Simulate Li-Fi receiver decoding the signal."""
    print("\nReceiving Data...")
    
    binary_received = ''.join(str(bit) for bit in signal)
    decoded_text = binary_to_text(binary_received)
    
    print("\nDecoded Message: ", decoded_text)
    return decoded_text

# Example usage
if _name_ == "_main_":
    message = input("Enter a message to transmit via Li-Fi: ")
    transmitted_signal = transmit_lifi(message)
    received_message = receive_lifi(transmitted_signal)