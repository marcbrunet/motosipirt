
import os
#import can
import datetime

class readValues():

    canbus = None
    canbus_interface = 'can0'
    logdir = "log"
    logfd = None

    values = {}

    def __init__(self):
        # Configure CAN Bus Device
        if os.environ.get('CANDEV'):
            self.canbus_interface = os.environ.get('CANDEV')
        self.__initLogFile()
        try:
            self.canbus = can.interface.Bus(self.canbus_interface, bustype='socketcan')
        except:
            pass

    def __del__(self):
        self.logfd.close()

    def __initLogFile(self):
        ts = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        try:
            self.logfd = open(self.logdir + '/motospirit-' + ts + '.csv', 'w')
        except:
            os.makedirs(self.logdir)
            self.logfd = open(self.logdir + '/motospirit-' + ts + '.csv', 'w')
        self.logfd.write("HORA, RPM, SOC, Tbat, Tdriver, Tengine, Vbat, Imax, Vmincell, Vmaxcell, Tmincell, Tmaxcell\n")

    def canBusUpdater(self):
        self.__getCanBusValues()
        self.__logValues()
        return self.values

    def __logValues(self):
        self.logfd.write(
            datetime.datetime.now().strftime("%Y%m%d%H%M%S") +
            str(self.values['RPM']) + ',' +
            str(self.values['SOC']) + ',' +
            str(self.values['Tbat']) + ',' +
            str(self.values['Tdriver']) + ',' +
            str(self.values['Tengine']) + ',' +
            str(self.values['Vbat']) + ',' +
            str(self.values['Imax']) + ',' +
            str(self.values['Vmincell']) + ',' +
            str(self.values['Vmaxcell']) + ',' +
            str(self.values['Tmincell']) + ',' +
            str(self.values['Tmaxcell']) + '\n'
        )

    def __parseDataInt8(self, data, i=0):
        v = data[i]
        if (v >> 7): v = (-0x80 + (v & 0x7f))
        return v

    def __parseDataUInt8(self, data, i=0):
        return data[i]

    def __parseDataInt16(self, data, i=0):
        v = data[i] | (data[i + 1] << 8)
        if (v >> 15): v = (-0x8000 + (v & 0x7fff))
        return v

    def __parseDataUInt16(self, data, i=0):
        v = data[i] | (data[i + 1] << 8)
        return v

    def __getCanBusValues(self):

        # ------------------------------------
        # Controller => openCAN dictionary
        # ------------------------------------
        # RPS => 3A90.2 (Unsigned32)
        #			=> 380B.4
        #			=> 3A91.2
        #	RPM => 606C.0 (Integer32/Integer16) => PDO
        #			=> 706C.0 (Integer32) => PDO
        # Tengine => 4600.3 (Integer16) => PDO
        #					=> 4700.3 (Integer16) => PDO
        # Tdriver	=>
        # ------------------------------------
        # BMS => STPM (1 sec), start from 620
        # ------------------------------------
        # Vbat 			=> 623.0 (2) => BigEndian
        # Vmincell	=> 623.2 => 0.1V
        # Vmaxcell 	=> 623.4 => 0.1V
        # Imax			=> 624.0 (2) => BigEndian, 2's complement
        # SOC				=> 626.0 (1)
        # Tbat			=> 627.0 (1) => 2's complement
        # Tmincell	=> 627.2 (1) => 2's complement
        # Tmaxcell	=> 627.4 (1) => 2's complement
        # ------------------------------------
        # Read from CAN Bus
        while True:
            msg = self.canbus.recv(0.0)
            if msg is None:
                break

            # Engine Driver PDOs
            if msg.arbitration_id == 0x222:
                self.values['Tdriver'] = self.__parseDataInt8(msg.data, 1)
                self.values['RPM'] = self.__parseDataInt16(msg.data, 4)
            elif msg.arbitration_id == 0x223:
                self.values['Tengine'] = self.__parseDataInt16(msg.data, 0)
            # BMS PDOs
            elif msg.arbitration_id == 0x623:
                self.values['Vbat'] = self.__parseDataUInt16(msg.data, 0)
                self.values['Vmincell'] = 0.1 * self.__parseDataUInt8(msg.data, 2)
                self.values['Vmaxcell'] = 0.1 * self.__parseDataUInt8(msg.data, 4)
            elif msg.arbitration_id == 0x624:
                self.values['Imax'] = self.__parseDataInt16(msg.data, 0)
            elif msg.arbitration_id == 0x626:
                self.values['SOC'] = self.__parseDataUInt8(msg.data, 0)
            elif msg.arbitration_id == 0x627:
                self.values['Tbat'] = self.__parseDataInt8(msg.data, 0)
                self.values['Tmincell'] = self.__parseDataInt8(msg.data, 2)
                self.values['Tmaxcell'] = self.__parseDataInt8(msg.data, 4)
