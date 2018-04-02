---
UID: NF:strmini.StreamClassDeviceNotification
title: StreamClassDeviceNotification function
author: windows-driver-content
description: Minidrivers use the StreamClassDeviceNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred.
old-location: stream\streamclassdevicenotification.htm
old-project: stream
ms.assetid: 80383159-c2c3-4d05-92e8-9245408e5243
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: StreamClassDeviceNotification, StreamClassDeviceNotification routine [Streaming Media Devices], strclass-routines_bddec484-f87c-4ebc-b8e1-ea52d265cbc4.xml, stream.streamclassdevicenotification, strmini/StreamClassDeviceNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
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
req.lib: Stream.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Stream.lib
-	Stream.dll
api_name:
-	StreamClassDeviceNotification
product:
- Windows
targetos: Windows
req.typenames: STREAM_PRIORITY, *PSTREAM_PRIORITY
req.product: Windows 10 or later.
---


# StreamClassDeviceNotification function
Minidrivers use the <b>StreamClassDeviceNotification</b> routine to notify the class driver that it has completed a stream request, or that an event has occurred.

## Syntax

```
void StreamClassDeviceNotification(
  STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE NotificationType,
  PVOID                                      HwDeviceExtension,
  ...                                        
);
```

## Parameters

`NotificationType`

This is an enumeration value that contains the type of notification that the minidriver is sending.





#### DeviceRequestComplete

Indicates that the minidriver has completed its handling of the device stream request block pointed to by the optional third argument of this routine, <i>pSrb</i>. Once the minidriver calls <b>StreamClassDeviceNotification</b> with this value, the relevant SRB is owned by the class driver, which is free to deallocate it.



#### ReadyForNextDeviceRequest

Indicates that the minidriver is ready to receive another device request. 



#### SignalDeviceEvent

Signals that the event specified by the <i>EventEntry</i> parameter has occurred.



#### SignalMultipleDeviceEvents

Signals all events that match the criteria specified in the <i>EventSet</i> and <i>EventId</i> parameters.



#### DeleteDeviceEvent

Deletes the event specified by the <i>EventEntry</i> parameter.

`HwDeviceExtension`

Pointer to the minidriver's device extension. The minidriver specifies the size of this buffer in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="https://msdn.microsoft.com/library/windows/hardware/ff568263">StreamClassRegisterMinidriver</a>. The class driver then passes pointers to the buffer in the <b>HwDeviceExtension</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559706">HW_TIME_CONTEXT</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.

`Arg1`




## Return Value

None

## Remarks

The minidriver uses this routine for requests or events that apply to the minidriver as a whole. Stream-specific requests or events use <a href="https://msdn.microsoft.com/library/windows/hardware/ff568266">StreamClassStreamNotification</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | strmini.h (include Strmini.h) |
| **Library** | Stream.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568266">StreamClassStreamNotification</a>