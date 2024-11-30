"""
This class provides functions for communicating with Keysight oscilloscopes.
It was specifically created for Keysight DSOX1204G, but `Core Command`s may be
available on other oscilloscopes.

Developed by: Mahdi Hayati

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\                           CONTACT ME                         \\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\            gmail              \\   mahdihayati79@gmail.com   \\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\           GitHub              \\        MahdiHayati705       \\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""


import pyvisa


class Keysight_DSOX1204G:
    """
    Command Classifications
    -----------------------
    To help you use existing programs with your oscilloscope, or use current programs with the next generation of Keysight InfiniiVision oscilloscopes, commands are classified by the following categories:

    `Core Command`
    Core commands are a common set of commands that provide basic oscilloscope functionality on this oscilloscope and future Keysight InfiniiVision oscilloscopes. Core commands are unlikely to be modified in the future.

    `Non-Core Command`
    Non-core commands are commands that provide specific features, but are not universal across all Keysight InfiniiVision oscilloscope models. Non-core commands may be modified or deleted in the future.
    """

    def __init__(self, IO_Conf : str):
        """
        :param IO_Conf: choose if the device is connected to the PC by `USB` of `LAN`
        """
        self.IDN      = 'KEYSIGHT TECHNOLOGIES,DSOX1204G,CN60167508,02.10.2019111333\n'
        self.USB_Addr = 'USB0::10893::918::CN60167508::INSTR'
        self.LAN_Addr = 'TCPIP0::k-dx1204g-67508::hislip0::INSTR'
        rm = pyvisa.ResourceManager()
        if IO_Conf == "LAN":
            self.OS = rm.open_resource(self.LAN_Addr)
        elif IO_Conf == "USB":
            self.OS = rm.open_resource(self.USB_Addr)
    
    def close(self):
        self.OS.close()

    def IDNCheck(self):
        """
        Returns
        --------
        ``TRUE``   Device is detected.

        ``FALSE``  Device is not detected.
        """
        try:
            if self.OS.query('*IDN?') == self.IDN:
                return 1
            else:
                return 0
        except:
            return 0
        
    def single(self):
        """
        `Core Command`
        Same as pressing the Single key on the front panel.
        """
        command = ':SINGle'
        self.OS.write(command)

    def run(self):
        """
        `Core Command`
        Same as pressing the Run key on the front panel.
        """
        command = ':RUN'
        self.OS.write(command)

    def stop(self):
        """
        `Core Command`
        Same as pressing the Stop key on the front panel.
        """
        command = ':STOP'
        self.OS.write(command)

    def channelCoupling(self, Channel : int, Coupling : str):
        """
        `Core Command`
        Selects the input coupling for the specified channel.

        :param Channel: Select channel from 1 to 4.
        :param Coupling: Select coupling `AC` or `DC`.
        """
        command = f":CHANnel{Channel}:COUPling {Coupling}"
        self.OS.write(command)

    def channelDisplay(self, Channel : int, Value : bool):
        """
        `Core Command`
        Turns the display of the specified channel on or off.

        :param Channel: Select channel from 1 to 4.
        :param Value: Set the display value to {{1 | ON} or {0 | OFF}} in boolian.
        """
        command = f":CHANnel{Channel}:DISPLAY {Value}"
        self.OS.write(command)

    def channelInvert(self, Channel : int, Value : bool):
        """
        `Non-Core Command`
        Selects whether or not to invert the input signal for the specified channel.

        :param Channel: Select channel from 1 to 4.
        :param Value: Select 1 to invert and 0 to not invert.
        """
        command = f":CHANnel{Channel}:INVert {Value}"
        self.OS.write(command)

    def channelLabel(self, Channel : int, Label : str):
        """
        `Non-Core Command`
        Sets the analog channel label to the string that follows.

        :param Channel: Select channel from 1 to 4.
        :param Label: Label string have 10 characters or less. Labels with more than 10 characters are truncated to 10 characters. Lower case characters are converted to upper case.
        """
        command = f":CHANnel{Channel}:LABel '{Label}'"
        self.OS.write(command)

    def channelOffset(self, Channel : int, Offset : int, Suffix : int = 'V'):
        """
        `Core Command`
        Sets the value that is represented at the center screen for the selected channel.

        :param Channel: Select channel from 1 to 4.
        :param Offset: Select Offset value.
        :param suffix: Select suffix for offset value {`V` | `mV`}. If not entered, `V` will be selected by default.
        """
        command = f":CHANnel{Channel}:OFFSet {Offset} {Suffix}"
        self.OS.write(command)

    def channelProbeAtt(self, Channel : int, Attenuation : int):
        """
        `Core Command`
        Specifies the probe attenuation factor for the selected channel. The probe attenuation factor may be 0.1 to 10000.

        :param Channel: Select channel from 1 to 4.
        :param Attenuation: Select attenuation factor from 0.1 to 10000.
        """
        command = f":CHANnel{Channel}:PROBe {Attenuation}"
        self.OS.write(command)

    def channelRange(self, Channel : int, Range : int, Suffix : str = 'V'):
        """
        `Core Command`
        Defines the full-scale vertical axis of the selected channel. When changing probe attenuation, the range value is multiplied by the probe attenuation factor.

        :param Channel: Select channel from 1 to 4.
        :param Range: Select vertical range.
        :param Suffix: Select suffix for range value {`V` | `mV`}. If not entered, `V` will be selected by default.
        """
        command = f":CHANnel{Channel}:RANGe {Range} {Suffix}"
        self.OS.write(command)

    def channelScale(self, Channel : int, Scale : int, Suffix : str = 'V'):
        """
        `Non-Core Command`
        Sets the vertical scale, or units per division, of the selected channel. If the probe attenuation is changed, the scale value is multiplied by the probe's attenuation factor.

        :param Channel: Select channel from 1 to 4.
        :param Scale: Select each vertical unit per division.
        :param Suffix: Select suffix for Value {`V` | `mV`}. If not entered, `V` will be selected by default.
        """
        command = f":CHANnel{Channel}:SCALe {Scale} {Suffix}"
        self.OS.write(command)

    def channelUnits(self, Channel : int, Unit : str):
        """
        `Non-Core Command`
        Sets the measurement units for the connected probe.

        :param Channel: Select channel from 1 to 4.
        :param Unit: Select `Volt` for a voltage probe and select `AMPere` for a current probe.
        """
        command = f":CHANnel{Channel}:UNITs {Unit}"
        self.OS.write(command)

    def displayLabel(self, status : str):
        """
        `Non-Core Command`
        Turns the analog channel labels on and off.

        :param status: {`ON` | `OFF`}
        """
        command = f":DISPlay:LABel {status}"
        self.OS.write(command)

    def saveImage(self, location : str, palette : str = 'COLor'):
        """
        `Non-Core Command`
        Saves the screen's image in the given locaiton as .png file

        :param location: Should contain "location + name + .png" of the file
        :param palette: {`COLor` | `GRAYscale`}
        
        Example
        -------

        >>> saveImage('NewFolder/screenshot.png')
        """
        command = f":DISPlay:DATA? PNG, {palette}"
        self.OS.write(command)

        # since the output of command is binary block, there is no need for decoding
        data = self.OS.read_raw()

        if data.startswith(b'#'):                                                  # Check if the response has a binary block header
            header_length = int(data[1:2])                                         # Number of digits in the length field
            data_length = int(data[2:2 + header_length])                           # Data length
            binary_data = data[2 + header_length:2 + header_length + data_length]  # Extract the binary data
        else:
            binary_data = data  # If no header, use the raw data as-is

        
        with open(location, 'wb') as f:
            f.write(binary_data)

    def measClearAll(self):
        """
        `Non-Core Command`
        Clears all selected measurements and markers from the screen.
        """
        command = ':MEASure:CLEar'
        self.OS.write(command)

    def measDutyCycle(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a duty cycle measurement on the given channel and returns its value

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return DutyCycle: duty cycle = (+pulse width/period)*100
        """
        # set DutyCycle measurement on the screen
        command = f":MEASure:DUTYcycle {source}"
        self.OS.write(command)

        # query DutyCycle value
        command   = f":MEASure:DUTYcycle? {source}"
        dutycycle = self.OS.query(command)
        return float(dutycycle)

    def measFallTime(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a fall-time measurement on the given source and returns its value

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return FallTime: fall time = time at lower threshold - time at upper threshold
        """
        # set FallTime measurement on the screen
        command = f":MEASure:FALLtime {source}"
        self.OS.write(command)

        # query FallTime value
        command  = f":MEASure:FALLtime? {source}"
        falltime = self.OS.query(command)
        return float(falltime)
    
    def measRiseTime(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a rise-time measurement on the given source and returns its value

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return RiseTime: rise time = time at upper threshold - time at lower threshold
        """
        # set RiseTime measurement on the screen
        command = f":MEASure:Risetime {source}"
        self.OS.write(command)

        # query RiseTime value
        command  = f":MEASure:Risetime? {source}"
        risetime = self.OS.query(command)
        return float(risetime)
    
    def measFrequency(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a frequency measurement on the given source and returns its value

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return Frequency: If the edge on the screen closest to the trigger reference is rising:
            THEN frequency = 1/(time at trailing rising edge - time at leading rising edge)
            ELSE frequency = 1/(time at trailing falling edge - time at leading falling edge)
        """
        # set Frequency measurement on the screen
        command = f":MEASure:FREQuency {source}"
        self.OS.write(command)

        # query Frequency value
        command  = f":MEASure:FREQuency? {source}"
        frequency = self.OS.query(command)
        return float(frequency)

    def measAmplitude(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a vertical amplitude measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return Amplitude: Vertical amplitude (float)
        """
        # set Vertical Amplitude measurement on the screen
        command = f":MEASure:VAMPlitude {source}"
        self.OS.write(command)

        # query Vertical Amplitude
        command   = f":MEASure:VAMPlitude? {source}"
        amplitude = self.OS.query(command)
        return float(amplitude)
    
    def measAverage(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts an average value measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return Average: Average value (float)
        """
        # set Average value measurement on the screen
        command = f":MEASure:VAVerage {source}"
        self.OS.write(command)

        # query Average value
        command = f":MEASure:VAVerage? {source}"
        average = self.OS.query(command)
        return float(average)
    
    def measVBase(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a waveform base value measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return Base Voltage: Unit: `Volts` (float)
        """
        # set Base measurement on the screen
        command = f":MEASure:VBASe {source}"
        self.OS.write(command)

        # query Base value
        command = f":MEASure:VBASe? {source}"
        Vbase   = self.OS.query(command)
        return float(Vbase)
    
    def measVTop(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a top value measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return Top Voltage: Unit: `Volts` (float)
        """
        # set Top measurement on the screen
        command = f":MEASure:VTOP {source}"
        self.OS.write(command)

        # query Top value
        command = f":MEASure:VTOP? {source}"
        Vtop    = self.OS.query(command)
        return float(Vtop)
    
    def measVMax(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a maximum vertical value measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return Max Voltage: Unit: `Volts` (float)
        """
        # set MAX measurement on the screen
        command = f":MEASure:VMAX {source}"
        self.OS.write(command)

        # query MAX value
        command = f":MEASure:VMAX? {source}"
        Vmax    = self.OS.query(command)
        return float(Vmax)
    
    def measVMin(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a minimum vertical value measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return Min Voltage: Unit: `Volts` (float)
        """
        # set MIN measurement on the screen
        command = f":MEASure:VMIN {source}"
        self.OS.write(command)

        # query MIN value
        command = f":MEASure:VMIN? {source}"
        Vmin    = self.OS.query(command)
        return float(Vmin)
    
    def measVPP(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts a peak-to-peak measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return Peak-to-Peak Voltage: Unit: `Volts` (float)
        """
        # set VPP measurement on the screen
        command = f":MEASure:VPP {source}"
        self.OS.write(command)

        # query VPP value
        command = f":MEASure:VPP? {source}"
        Vpp     = self.OS.query(command)
        return float(Vpp)
    
    def measVrms(self, source : str):
        """
        `Core Command`
        Installs a screen measurement and starts an RMS value measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return RMS Value: Unit: `Volts` (float)
        """
        # set RMS measurement on the screen
        command = f":MEASure:VRMS {source}"
        self.OS.write(command)

        # query RMS value
        command = f":MEASure:VRMS? {source}"
        Vrms    = self.OS.query(command)
        return float(Vrms)
    
    def measXMax(self, source : str):
        """
        `Non-Core Command`
        Installs a screen measurement and starts an X-at-Max-Y measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return X@Max: Unit: `Seconds` (float)
        """
        # set X Value measurement on the screen
        command = f":MEASure:XMAX {source}"
        self.OS.write(command)

        # query X Value
        command = f":MEASure:XMAX? {source}"
        X       = self.OS.query(command)
        return float(X)
    
    def measXMin(self, source : str):
        """
        `Non-Core Command`
        Installs a screen measurement and starts an X-at-Min-Y measurement on the given source and returns its value.

        :param source: {`CHANnel<n>` | `FUNCtion` | `MATH` | `WMEMory<r>` | `EXTernal`}  where (n) is The analog channel number and (r) is 1-2
        :return X@Min: Unit: `Seconds` (float)
        """
        # set X Value measurement on the screen
        command = f":MEASure:XMIN {source}"
        self.OS.write(command)

        # query X Value
        command = f":MEASure:XMIN? {source}"
        X       = self.OS.query(command)
        return float(X)
    
    def timeScale(self, value : float):
        """
        `Non-Core Command`
        Sets the horizontal scale or units per division for the main window.

        :param value: time/div (Second)
        """
        command = f":TIMebase:SCALe {value}"
        self.OS.write(command)

    def triggerHoldOFF(self, time : float):
        """
        `Core Command`
        Defines the holdoff time value in seconds.

        :param time: Unit: `Seconds`
        """
        command = f":TRIGger:HOLDoff {time}"
        self.OS.write(command)

    def triggerMode(self, mode : str):
        """
        `Core Command`
        Selects the trigger mode (trigger type).

        :param mode: {`EDGE` | `GLITch` | `PATTern` | `SHOLd` | `TRANsition` | `TV` | `SBUS1`}
        """
        command = f":TRIGger:MODE {mode}"
        self.OS.write(command)

    def triggerNoiseReject(self, status : bool):
        """
        `Core Command`
        Turns the noise reject filter off and on.

        :param status: {{`0` | `OFF`} | {`1` | `ON`}}
        """
        command = f":TRIGger:NREJect {status}"
        self.OS.write(command)

    def triggerlevel(self, level : float, source : str):
        """
        `Core Command`
        Sets the trigger level voltage for the given trigger source.

        :param level: Trigger level (Volts)
        :param source: {`CHANnel<n>` | `EXTernal`} where (n) is The analog channel number
        """
        command = f":TRIGger:EDGE:LEVel {level}, {source}"
        self.OS.write(command)

    def triggerSlope(self, slope : str):
        """
        `Core Command`
        Specifies the slope of the edge for the trigger. This function is not valid in TV trigger mode.

        :param slope: {`NEGative` | `POSitive` | `EITHer` | `ALTernate}`}
        """
        command = f":TRIGger:EDGE:SLOPe {slope}"
        self.OS.write(command)

    def triggerSource(self, source : str):
        """
        `Core Command`
        Selects the input that produces the trigger.

        :param source: {`CHANnel<n>` | `EXTernal` | `LINE` | `WGEN`} where (n) is The analog channel number
        """
        command = f":TRIGger:EDGE:SOURce {source}"
        self.OS.write(command)

    def WGenOutput(self, status : bool):
        """
        `Non-Core Command`
        specifies whether the waveform generator signal output is ON (1) or OFF (0).

        :param status: {{`0` | `OFF`} | {`1` | `ON`}}
        """
        command = f":WGEN:OUTPut {status}"
        self.OS.write(command)
    
    def WGenFrequency(self, frequency : float):
        """
        `Non-Core Command`
        For all waveforms except `Noise` and `DC`, this function specifies the frequency of the waveform.

        :param frequency: Unit: `Hz`
        """
        command = f":WGEN:FREQuency {frequency}"
        self.OS.write(command)

    def WGenFunction(self, signal : str):
        """
        `Non-Core Command`
        Selects the type of waveform.

        :param signal: {`SINusoid` | `SQUare` | `RAMP` | `PULSe` | `NOISe` | `DC`}
        """
        command = f":WGEN:FUNCtion {signal}"
        self.OS.write(command)

    def WGenPulseWidth(self, width : float):
        """
        `Non-Core Command`
        For Pulse waveforms, this function specifies the width of the pulse.

        :param width: Pulse width. Unit: `Seconds`
        """
        command = f":WGEN:FUNCtion:PULSe:WIDTh {width}"
        self.OS.write(command)

    def WGenRampSymmetry(self, percent : float):
        """
        `Non-Core Command`
        For Ramp waveforms, this function specifies the symmetry of the waveform.
        
        Symmetry represents the amount of time per cycle that the ramp waveform is rising.

        :param percent: Symmetry percentage from 0% to 100%
        """
        command = f":WGEN:FUNCtion:RAMP:SYMMetry {percent}"
        self.OS.write(command)

    def WGenSquareDCycle(self, DCycle : float):
        """
        `Non-Core Command`
        For Square waveforms, this function specifies the square wave duty cycle.
        
        Duty cycle is the percentage of the period that the waveform is high.

        :param DCycle: Duty cycle percentage from 1% to 99%
        """
        command = f":WGEN:FUNCtion:SQUare:DCYCle {DCycle}"
        self.OS.write(command)

    def WGenAmplitude(self, amplitude : float):
        """
         `Non-Core Command`
         For all waveforms except DC, this function specifies the waveform's amplitude.

         :param amplitude: Unit: `Volts`
        """
        command = f":WGEN:VOLTage {amplitude}"
        self.OS.write(command)

    def WGenOffset(self, offset : float):
        """
         `Non-Core Command`
         Specifies the waveform's offset voltage or the DC level.

         :param offset: Unit: `Volts`
        """
        command = f":WGEN:VOLTage:OFFSet {offset}"
        self.OS.write(command)



