---
UID: NF:strmini.StreamClassStreamNotification
title: StreamClassStreamNotification function
author: windows-driver-content
description: Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred.
old-location: stream\streamclassstreamnotification.htm
old-project: stream
ms.assetid: 67dd0ea0-9c69-415a-8b37-0e8700b6fbd8
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: StreamClassStreamNotification, StreamClassStreamNotification routine [Streaming Media Devices], strclass-routines_22bc1b48-b75e-4dce-9aae-16e16b1ca1f9.xml, stream.streamclassstreamnotification, strmini/StreamClassStreamNotification
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
-	StreamClassStreamNotification
product: Windows
targetos: Windows
req.typenames: STREAM_PRIORITY, *PSTREAM_PRIORITY
req.product: Windows 10 or later.
---


# StreamClassStreamNotification function
Streams use the <b>StreamClassStreamNotification</b> routine to notify the class driver that it has completed a stream request, or that an event has occurred.

## Syntax

````
VOID  StreamClassStreamNotification(
  _In_ STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE NotificationType,
  _In_ PHW_STREAM_OBJECT                          StreamObject,
       PHW_STREAM_REQUEST_BLOCK                   pSrb,
       PKSEVENT_ENTRY                             EventEntry,
       GUID                                       *EventSet,
       ULONG                                      EventId
);
````

## Parameters

`NotificationType`

This is an enumeration value that contains the type of notification that the minidriver is sending.





#### StreamRequestComplete

Indicates that the minidriver has completed its handling of the stream-oriented stream request block that is pointed to by the optional third argument of this routine, <i>pSrb</i>.



#### ReadyForNextStreamDataRequest

Indicates that this stream is ready to receive another data request. 



#### ReadyForNextStreamControlRequest

Indicates that this stream is ready to receive another control request. 



#### SignalStreamEvent

Signals that the event specified by the <i>EventEntry</i> parameter has occurred.



#### SignalMultipleStreamEvents

Signals that all events that match the criteria specified in the <i>EventSet</i> and <i>EventId</i> parameters have occurred.



#### DeleteStreamEvent

Deletes the event specified by the <i>EventEntry</i> parameter.

`StreamObject`

Points to the stream object of the stream that the class driver is being notified about.

`Arg1`




## Return Value

None

## Remarks

The minidriver uses this routine for requests or events that apply to the minidriver as a whole. Stream-specific requests or events use <a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | strmini.h (include Strmini.h) |
| **Library** | Stream.lib |

## See Also

<a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a>