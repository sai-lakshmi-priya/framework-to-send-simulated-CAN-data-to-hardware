from PCANBasic import *
channel = PCAN_USBBUS1
baud = PCAN_BAUD_500K
N=1

## The Plug & Play Channel (PCAN-USB) is initialized
##
#objPCAN =# The Plug & Play Channel (PCAN-USB) is initialized
#
objPCAN = PCANBasic()
result = objPCAN.Initialize(channel, baud)
if result != PCAN_ERROR_OK:
	# An error occured, get a text describing the error and show it
	#
	result = objPCAN.GetErrorText(result)
	print(result[1])
	channel = PCAN_USBBUS2
	objPCAN = PCANBasic()
	result = objPCAN.Initialize(channel, baud)
	if result != PCAN_ERROR_OK:
		# An error occured, get a text describing the error and show it
		#
		result = objPCAN.GetErrorText(result)
		print(result[1])
	else:
		print("PCAN-USBx was initialized")
else:
	print("PCAN-USBx was initialized")

	# Check the status of the USB Channel
	#
	result = objPCAN.GetStatus(channel)
if result == PCAN_ERROR_BUSLIGHT:
	print("PCAN-USB (Ch-x): Handling a BUS-LIGHT status...")
elif result == PCAN_ERROR_BUSHEAVY:
	print("PCAN-USB (Ch-x): Handling a BUS-HEAVY status...")
elif result == PCAN_ERROR_BUSOFF:
	print("PCAN-USB (Ch-x): Handling a BUS-OFF status...")
elif result == PCAN_ERROR_OK:
	print("PCAN_USB (Ch-x): Status is OK")
else:
	# An error occured, get a text describing the error and show it
	#
	result = objPCAN.GetErrorText(result)
	print(result[1])

while(N>0):
    
    msg = PCANMsg()
    msg.ID = 0x610
    msg.MSGTYPE = PCAN_MESSAGE_STANDARD
    msg.LEN = 8
    msg.DATA[0] = 0x01
    msg.DATA[1] = 0x08
    msg.DATA[2] = 0x0F
    msg.DATA[3] = 0x0E
    msg.DATA[4] = 0x0E
    msg.DATA[5] = 0x0C
    msg.DATA[6] = 0x03
    msg.DATA[7] = 0x01
    result = objPCAN.Write(channel, msg)
    if result != PCAN_ERROR_OK:
        result = objPCAN.GetErrorText(result)
        print(result)
    else:
        print("Message sent successfully")
        readResult = objPCAN.Read(channel) ## Read message from the USB Channel
        if readResult[0] == PCAN_ERROR_OK:
        # Process the received message
        #
            print("A message was received")
            print('[0]',readResult[0])      # A PCANStatus error code
            print('[1]',readResult[1])      # A PCANMsg structure with the CAN message read
            print('[2]',readResult[2])      # A PCANTimestamp structure with the time when the message was read
            msg     = readResult[1] 
            print('MSGTYPE = ',msg.MSGTYPE)
            if msg.LEN==8:
                if(msg.DATA==0x123FF000):
                    print('DATA[0] = ',msg.DATA[0])
                    print('DATA[1] = ',msg.DATA[1])
                    print('DATA[2] = ',msg.DATA[2])
                    print('DATA[3] = ',msg.DATA[3])
                    print('DATA[4] = ',msg.DATA[4])
                    print('DATA[5] = ',msg.DATA[5])
                    print('DATA[6] = ',msg.DATA[6])
                    print('DATA[7] = ',msg.DATA[7])
                else:
                    result = objPCAN.GetErrorText(readResult[0])
                    print(result[1])
N = N + 1

	
	
