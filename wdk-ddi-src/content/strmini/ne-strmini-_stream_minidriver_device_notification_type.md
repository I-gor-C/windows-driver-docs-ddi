---
UID : NE:strmini._STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE
title : "_STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE"
author : windows-driver-content
description : "."
old-location : stream\stream_minidriver_device_notification_type.htm
old-project : stream
ms.assetid : 34DAA236-ACD0-4C25-BB45-00A81D2F131D
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : DeviceNotificationMaximum, *PSTREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, strmini/PSTREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, DeviceRequestComplete, DeleteDeviceEvent, SignalMultipleDeviceInstanceEvents, SignalDeviceEvent, PSTREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE enumeration pointer [Streaming Media Devices], strmini/SignalMultipleDeviceEvents, strmini/SignalMultipleDeviceInstanceEvents, SignalMultipleDeviceEvents, STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, _STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE enumeration [Streaming Media Devices], ReadyForNextDeviceRequest, strmini/ReadyForNextDeviceRequest, stream.stream_minidriver_device_notification_type, strmini/STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, strmini/DeviceNotificationMaximum, strmini/SignalDeviceEvent, PSTREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, strmini/DeleteDeviceEvent, strmini/DeviceRequestComplete
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : strmini.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, *PSTREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE
req.product : Windows 10 or later.
---

# _STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE Enumeration


## Syntax
````
typedef enum _STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE { 
  ReadyForNextDeviceRequest,
  DeviceRequestComplete,
  SignalMultipleDeviceEvents,
  SignalDeviceEvent,
  DeleteDeviceEvent,
#if (NTDDI_VERSION >= NTDDI_WINXP)
  SignalMultipleDeviceInstanceEvents,
#endif 
  DeviceNotificationMaximum
} STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, *PSTREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE;
````

## Constants

<table>

<tr>
<td>DeleteDeviceEvent</td>
<td></td>
</tr>

<tr>
<td>DeviceNotificationMaximum</td>
<td></td>
</tr>

<tr>
<td>DeviceRequestComplete</td>
<td>Indicates that the specified device SRB has completed.</td>
</tr>

<tr>
<td>ReadyForNextDeviceRequest</td>
<td>Indicates that the minidriver is ready for the next device request.</td>
</tr>

<tr>
<td>SignalDeviceEvent</td>
<td></td>
</tr>

<tr>
<td>SignalMultipleDeviceEvents</td>
<td></td>
</tr>

<tr>
<td>SignalMultipleDeviceInstanceEvents</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h |