---
UID: NE:strmini._STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
title: "_STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE"
author: windows-driver-content
description: "."
old-location: stream\stream_minidriver_stream_notification_type.htm
old-project: stream
ms.assetid: 13D8152C-FE7E-46EB-9C7F-9CA0135A4B76
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration pointer [Streaming Media Devices], ReadyForNextStreamDataRequest, ReadyForNextStreamControlRequest, HardwareStarved, strmini/HardwareStarved, stream.stream_minidriver_stream_notification_type, StreamRequestComplete, STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration [Streaming Media Devices], StreamNotificationMaximum, strmini/StreamRequestComplete, strmini/StreamNotificationMaximum, strmini/ReadyForNextStreamControlRequest, strmini/SignalStreamEvent, strmini/ReadyForNextStreamDataRequest, SignalMultipleStreamEvents, strmini/DeleteStreamEvent, _STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, strmini/STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, SignalStreamEvent, strmini/SignalMultipleStreamEvents, PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, strmini/PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, DeleteStreamEvent"
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
-	STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
product: Windows
targetos: Windows
req.typenames: STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, *PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
req.product: Windows 10 or later.
---

# _STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE Enumeration


## Syntax
````
typedef enum _STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE { 
  ReadyForNextStreamDataRequest,
  ReadyForNextStreamControlRequest,
  HardwareStarved,
  StreamRequestComplete,
  SignalMultipleStreamEvents,
  SignalStreamEvent,
  DeleteStreamEvent,
  StreamNotificationMaximum
} STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, *PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>DeleteStreamEvent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>HardwareStarved</td>
                    <td>Indicates that the hardware is starved for data.</td>
                </tr>
            
                <tr>
                    <td>ReadyForNextStreamControlRequest</td>
                    <td>Indicates that the minidriver is ready for the next stream control request.</td>
                </tr>
            
                <tr>
                    <td>ReadyForNextStreamDataRequest</td>
                    <td>Indicates that the minidriver is ready for the next stream data request.</td>
                </tr>
            
                <tr>
                    <td>SignalMultipleStreamEvents</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>SignalStreamEvent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>StreamNotificationMaximum</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>StreamRequestComplete</td>
                    <td>Indicates that the specified stream SRB has completed.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h |