Currently only tested on Raspbian jessie on raspberry pi 3

For bluetooth passcode authentication on linux (with raspi) the following steps are needed:
1. Create a file named bluetooth.cfg on /root with the following contents in it
`BT_MAC_ADDRESS BT_PASSWORD`
For the OBD reader the BT_PASSWORD is 1234
2. Create the following script
```
sudo hciconfig hci0 sspmode 0
sudo bt-agent -c NoInputNoOutput -p /root/bluetooth.cfg
```
3. Run the script on bg with script.sh &
4. Run the program main and bt authentication should work seamlessly once all libraries are loaded into pip

## Warning
Currently the program offers no support for OBDII disconnections, run the program once the OBD reader is powered on and working.

## TODO
1. Add support for bluetooth retry until successful connection
2. Add support for configurable PID reading and expand support for more useful PID
3. Add support for seamless Ubidots connection, currently there needs to be a file named dataStoring.py with a constant called 'UBI_USER'
