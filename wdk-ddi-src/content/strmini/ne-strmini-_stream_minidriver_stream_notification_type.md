---
UID: NE:strmini._STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
title: "_STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE"
author: windows-driver-content
description: "."
old-location: stream\stream_minidriver_stream_notification_type.htm
old-project: stream
ms.assetid: 13D8152C-FE7E-46EB-9C7F-9CA0135A4B76
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, DeleteStreamEvent, HardwareStarved, PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration pointer [Streaming Media Devices], ReadyForNextStreamControlRequest, ReadyForNextStreamDataRequest, STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration [Streaming Media Devices], SignalMultipleStreamEvents, SignalStreamEvent, StreamNotificationMaximum, StreamRequestComplete, _STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, stream.stream_minidriver_stream_notification_type, strmini/DeleteStreamEvent, strmini/HardwareStarved, strmini/PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, strmini/ReadyForNextStreamControlRequest, strmini/ReadyForNextStreamDataRequest, strmini/STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, strmini/SignalMultipleStreamEvents, strmini/SignalStreamEvent, strmini/StreamNotificationMaximum, strmini/StreamRequestComplete"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Strmini.h
api_name:
-	STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
product: Windows
targetos: Windows
req.typenames: STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, *PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
req.product: Windows 10 or later.
---

# _STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE Enumeration


## Syntax
```
typedef enum _STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE {
  ReadyForNextStreamDataRequest     ,
  ReadyForNextStreamControlRequest  ,
  HardwareStarved                   ,
  StreamRequestComplete             ,
  SignalMultipleStreamEvents        ,
  SignalStreamEvent                 ,
  DeleteStreamEvent                 ,
  StreamNotificationMaximum
} *PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>ReadyForNextStreamDataRequest</td>
                    <td>Indicates that the minidriver is ready for the next stream data request.</td>
                </tr>
            
                <tr>
                    <td>ReadyForNextStreamControlRequest</td>
                    <td>Indicates that the minidriver is ready for the next stream control request.</td>
                </tr>
            
                <tr>
                    <td>HardwareStarved</td>
                    <td>Indicates that the hardware is starved for data.</td>
                </tr>
            
                <tr>
                    <td>StreamRequestComplete</td>
                    <td>Indicates that the specified stream SRB has completed.</td>
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
                    <td>DeleteStreamEvent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>StreamNotificationMaximum</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h |