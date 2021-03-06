

class Memory:

    def __init__(self, size: int) -> None:
        self.size = size
        self.memory = bytearray(size)
    

    def get_data(self, address: int, size: int) -> int:
        """
        Get data from memory.
        """
        # TODO: fix data retirval bugs
        data = self.memory[address : address + size]
        return int.from_bytes(data, byteorder='little', signed=False)


    def store_data(self, address: int, data: int, size: int) -> None:
        """
        Store data to memory.
        """
        self.memory[address : address + size] = data.to_bytes(size, byteorder='little')


    def store_bytes(self, address: int, data: bytes) -> None:
        """
        Store bytes to memory.
        """
        self.memory[address : address + len(data)] = data


