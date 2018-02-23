---
UID: NE:strmini._SRB_COMMAND
title: "_SRB_COMMAND"
author: windows-driver-content
description: "."
old-location: stream\srb_command.htm
old-project: stream
ms.assetid: 2A72D3B5-286A-4C20-AFEC-77EDCDD56B6A
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: strmini/SRB_GET_DATA_FORMAT, strmini/SRB_SET_STREAM_RATE, strmini/SRB_DEVICE_METHOD, strmini/SRB_GET_DATA_INTERSECTION, SRB_BEGIN_FLUSH, SRB_CHANGE_POWER_STATE, SRB_READ_DATA, SRB_GET_DATA_FORMAT, SRB_DEVICE_METHOD, stream.srb_command, strmini/SRB_NOTIFY_IDLE_STATE, strmini/SRB_WRITE_DATA, SRB_SET_DEVICE_PROPERTY, SRB_GET_STREAM_STATE, strmini/SRB_UNINITIALIZE_DEVICE, SRB_SET_STREAM_PROPERTY, strmini/SRB_UNKNOWN_DEVICE_COMMAND, SRB_PAGING_OUT_DRIVER, strmini/SRB_GET_STREAM_STATE, strmini/SRB_INDICATE_MASTER_CLOCK, strmini/SRB_OPEN_MASTER_CLOCK, strmini/SRB_GET_DEVICE_PROPERTY, SRB_CLOSE_MASTER_CLOCK, strmini/SRB_INITIALIZE_DEVICE, strmini/SRB_GET_STREAM_INFO, SRB_END_FLUSH, SRB_SET_DATA_FORMAT, strmini/SRB_OPEN_STREAM, strmini/SRB_BEGIN_FLUSH, SRB_COMMAND enumeration [Streaming Media Devices], SRB_CLOSE_DEVICE_INSTANCE, SRB_PROPOSE_DATA_FORMAT, SRB_OPEN_STREAM, strmini/SRB_SURPRISE_REMOVAL, SRB_WRITE_DATA, SRB_CLOSE_STREAM, SRB_SET_STREAM_RATE, strmini/SRB_END_FLUSH, strmini/SRB_SET_STREAM_STATE, strmini/SRB_UNKNOWN_STREAM_COMMAND, SRB_GET_DEVICE_PROPERTY, SRB_UNINITIALIZE_DEVICE, SRB_SURPRISE_REMOVAL, SRB_GET_STREAM_INFO, SRB_INDICATE_MASTER_CLOCK, SRB_COMMAND, strmini/SRB_PROPOSE_STREAM_RATE, strmini/SRB_SET_STREAM_PROPERTY, strmini/SRB_CLOSE_MASTER_CLOCK, strmini/SRB_CLOSE_STREAM, SRB_PROPOSE_STREAM_RATE, strmini/SRB_SET_DEVICE_PROPERTY, SRB_UNKNOWN_DEVICE_COMMAND, SRB_UNKNOWN_STREAM_COMMAND, strmini/SRB_CHANGE_POWER_STATE, SRB_STREAM_METHOD, SRB_OPEN_DEVICE_INSTANCE, strmini/SRB_OPEN_DEVICE_INSTANCE, SRB_INITIALIZATION_COMPLETE, SRB_GET_STREAM_PROPERTY, strmini/SRB_PROPOSE_DATA_FORMAT, SRB_GET_DATA_INTERSECTION, strmini/SRB_STREAM_METHOD, strmini/SRB_SET_DATA_FORMAT, strmini/SRB_COMMAND, strmini/SRB_READ_DATA, _SRB_COMMAND, SRB_SET_STREAM_STATE, SRB_OPEN_MASTER_CLOCK, strmini/SRB_PAGING_OUT_DRIVER, strmini/SRB_GET_STREAM_PROPERTY, SRB_INITIALIZE_DEVICE, strmini/SRB_INITIALIZATION_COMPLETE, SRB_NOTIFY_IDLE_STATE, strmini/SRB_CLOSE_DEVICE_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Strmini.h
apiname:
-	SRB_COMMAND
product: Windows
targetos: Windows
req.typenames: SRB_COMMAND
req.product: Windows 10 or later.
---

# _SRB_COMMAND Enumeration


## Syntax
````
typedef enum _SRB_COMMAND { 
  SRB_READ_DATA,
  SRB_WRITE_DATA,
  SRB_GET_STREAM_STATE,
  SRB_SET_STREAM_STATE,
  SRB_SET_STREAM_PROPERTY,
  SRB_GET_STREAM_PROPERTY,
  SRB_OPEN_MASTER_CLOCK,
  SRB_INDICATE_MASTER_CLOCK,
  SRB_UNKNOWN_STREAM_COMMAND,
  SRB_SET_STREAM_RATE,
  SRB_PROPOSE_DATA_FORMAT,
  SRB_CLOSE_MASTER_CLOCK,
  SRB_PROPOSE_STREAM_RATE,
  SRB_SET_DATA_FORMAT,
  SRB_GET_DATA_FORMAT,
  SRB_BEGIN_FLUSH,
  SRB_END_FLUSH,
  SRB_GET_STREAM_INFO          = 0x100,
  SRB_OPEN_STREAM,
  SRB_CLOSE_STREAM,
  SRB_OPEN_DEVICE_INSTANCE,
  SRB_CLOSE_DEVICE_INSTANCE,
  SRB_GET_DEVICE_PROPERTY,
  SRB_SET_DEVICE_PROPERTY,
  SRB_INITIALIZE_DEVICE,
  SRB_CHANGE_POWER_STATE,
  SRB_UNINITIALIZE_DEVICE,
  SRB_UNKNOWN_DEVICE_COMMAND,
  SRB_PAGING_OUT_DRIVER,
  SRB_GET_DATA_INTERSECTION,
  SRB_INITIALIZATION_COMPLETE,
  SRB_SURPRISE_REMOVAL,
#if (NTDDI_VERSION >= NTDDI_WINXP)
  SRB_DEVICE_METHOD,
  SRB_STREAM_METHOD,
#if ( (NTDDI_VERSION >= NTDDI_WINXPSP2) && (NTDDI_VERSION < NTDDI_WS03) ) || (NTDDI_VERSION >= NTDDI_WS03SP1)


  SRB_NOTIFY_IDLE_STATE
#endif 

#endif } SRB_COMMAND;
````

## Constants

<table>
            
                <tr>
                    <td>SRB_BEGIN_FLUSH</td>
                    <td>Stream-specific code that begins the flush state.</td>
                </tr>
            
                <tr>
                    <td>SRB_CHANGE_POWER_STATE</td>
                    <td>Device instance-specific code that changes the power state.</td>
                </tr>
            
                <tr>
                    <td>SRB_CLOSE_DEVICE_INSTANCE</td>
                    <td>Device instance-specific code that closes an instance of the device.</td>
                </tr>
            
                <tr>
                    <td>SRB_CLOSE_MASTER_CLOCK</td>
                    <td>Stream-specific code that indicates that the master clock is closed.</td>
                </tr>
            
                <tr>
                    <td>SRB_CLOSE_STREAM</td>
                    <td>Device instance-specific code that closes the specific stream.</td>
                </tr>
            
                <tr>
                    <td>SRB_DEVICE_METHOD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>SRB_END_FLUSH</td>
                    <td>Stream-specific code that ends the flush state.</td>
                </tr>
            
                <tr>
                    <td>SRB_GET_DATA_FORMAT</td>
                    <td>Stream-specific code that returns the current data format.</td>
                </tr>
            
                <tr>
                    <td>SRB_GET_DATA_INTERSECTION</td>
                    <td>Device instance-specific code that returns stream data intersection.</td>
                </tr>
            
                <tr>
                    <td>SRB_GET_DEVICE_PROPERTY</td>
                    <td>Device instance-specific code that gets the property of the device.</td>
                </tr>
            
                <tr>
                    <td>SRB_GET_STREAM_INFO</td>
                    <td>Device instance-specific code that gets the stream information structure.</td>
                </tr>
            
                <tr>
                    <td>SRB_GET_STREAM_PROPERTY</td>
                    <td>Stream-specific code that specifies to get a property value for the stream.</td>
                </tr>
            
                <tr>
                    <td>SRB_GET_STREAM_STATE</td>
                    <td>Stream-specific code that specifies to get the state of the stream.</td>
                </tr>
            
                <tr>
                    <td>SRB_INDICATE_MASTER_CLOCK</td>
                    <td>Stream-specific code that specifies that the handle is supplied to the master clock.</td>
                </tr>
            
                <tr>
                    <td>SRB_INITIALIZATION_COMPLETE</td>
                    <td>Device instance-specific code that indicates that the initialization sequence has completed.</td>
                </tr>
            
                <tr>
                    <td>SRB_INITIALIZE_DEVICE</td>
                    <td>Device instance-specific code that initializes the device.</td>
                </tr>
            
                <tr>
                    <td>SRB_NOTIFY_IDLE_STATE</td>
                    <td>Device instance-specific code that specifies to call on first open and last close.</td>
                </tr>
            
                <tr>
                    <td>SRB_OPEN_DEVICE_INSTANCE</td>
                    <td>Device instance-specific code that opens an instance of the device.</td>
                </tr>
            
                <tr>
                    <td>SRB_OPEN_MASTER_CLOCK</td>
                    <td>Stream-specific code that indicates that the master clock is on this stream.</td>
                </tr>
            
                <tr>
                    <td>SRB_OPEN_STREAM</td>
                    <td>Device instance-specific code that opens the specified stream.</td>
                </tr>
            
                <tr>
                    <td>SRB_PAGING_OUT_DRIVER</td>
                    <td>Device instance-specific code that indicates that the driver is to be paged out only if it is enabled in the registry. Board ints should be disabled and STATUS_SUCCESS returned.</td>
                </tr>
            
                <tr>
                    <td>SRB_PROPOSE_DATA_FORMAT</td>
                    <td>Stream-specific code that specifies that a new rate is proposed, it does not change the rate.</td>
                </tr>
            
                <tr>
                    <td>SRB_PROPOSE_STREAM_RATE</td>
                    <td>Stream-specific code that indicates a new rate is proposed, it does not change the rate.</td>
                </tr>
            
                <tr>
                    <td>SRB_READ_DATA</td>
                    <td>Stream-specific code that specifies to read data from hardware.</td>
                </tr>
            
                <tr>
                    <td>SRB_SET_DATA_FORMAT</td>
                    <td>Stream-specific code that sets a new data format.</td>
                </tr>
            
                <tr>
                    <td>SRB_SET_DEVICE_PROPERTY</td>
                    <td>Device instance-specific code that sets the property of the device.</td>
                </tr>
            
                <tr>
                    <td>SRB_SET_STREAM_PROPERTY</td>
                    <td>Stream-specific code that specifies to set a property of the stream.</td>
                </tr>
            
                <tr>
                    <td>SRB_SET_STREAM_RATE</td>
                    <td>Stream-specific code that specifies that the rate is set at which the stream should run.</td>
                </tr>
            
                <tr>
                    <td>SRB_SET_STREAM_STATE</td>
                    <td>Stream-specific code that specifies to set the state of the stream.</td>
                </tr>
            
                <tr>
                    <td>SRB_STREAM_METHOD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>SRB_SURPRISE_REMOVAL</td>
                    <td>Device instance-specific code that indicates a surprise removal of hardware has occurred.</td>
                </tr>
            
                <tr>
                    <td>SRB_UNINITIALIZE_DEVICE</td>
                    <td>Device instance-specific code that uninitializes the device.</td>
                </tr>
            
                <tr>
                    <td>SRB_UNKNOWN_DEVICE_COMMAND</td>
                    <td>Device instance-specific code that specifies that the IRP function is unknown to the class driver.</td>
                </tr>
            
                <tr>
                    <td>SRB_UNKNOWN_STREAM_COMMAND</td>
                    <td>Stream-specific code that specifies that the IRP function is unknown to the class driver.</td>
                </tr>
            
                <tr>
                    <td>SRB_WRITE_DATA</td>
                    <td>Stream-specific code that specifies to write data to the hardware.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h |