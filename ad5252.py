import smbus
import time

I2C_INDEX = 1
I2C_ADDRESS = 0x2C
VALID_CHANNELS = [0,1]
CHANNEL_ADDRESSES = [0x01, 0x03]
WIPER_POSITIONS = 256
KOHM_MAX_RESISTANCE = 10
BYTE_TO_OHMS = KOHM_MAX_RESISTANCE / WIPER_POSITIONS


class AD5252(object):
    def __init__(self):
        self.bus = smbus.SMBus(I2C_INDEX)

    def write(self, kohm_resistance, channel):
        assert channel in VALID_CHANNELS
        assert 0 <= kohm_resistance <= KOHM_MAX_RESISTANCE
        write_out = int(kohm_resistance / BYTE_TO_OHMS)
        self.bus.write_i2c_block_data(
            I2C_ADDRESS,
            CHANNEL_ADDRESSES[channel],
            [write_out]
        )

    def read(self, channel):
        assert channel in VALID_CHANNELS
        return self.bus.read_byte_data(
            I2C_ADDRESS,
            CHANNEL_ADDRESSES[channel]
        ) * BYTE_TO_OHMS

