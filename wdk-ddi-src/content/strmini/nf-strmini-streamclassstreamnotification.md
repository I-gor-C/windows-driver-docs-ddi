---
UID: NF:strmini.StreamClassStreamNotification
title: StreamClassStreamNotification function
author: windows-driver-content
description: Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred.
old-location: stream\streamclassstreamnotification.htm
old-project: stream
ms.assetid: 67dd0ea0-9c69-415a-8b37-0e8700b6fbd8
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: stream.streamclassstreamnotification, strmini/StreamClassStreamNotification, StreamClassStreamNotification, strclass-routines_22bc1b48-b75e-4dce-9aae-16e16b1ca1f9.xml, StreamClassStreamNotification routine [Streaming Media Devices]
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	LibDef
apilocation:
-	Stream.lib
-	Stream.dll
apiname:
-	StreamClassStreamNotification
product: Windows
targetos: Windows
req.typenames: "*PSTREAM_PRIORITY, STREAM_PRIORITY"
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




#### DeleteStreamEvent

Deletes the event specified by the <i>EventEntry</i> parameter.


#### ReadyForNextStreamControlRequest

Indicates that this stream is ready to receive another control request. 


#### ReadyForNextStreamDataRequest

Indicates that this stream is ready to receive another data request. 


#### SignalMultipleStreamEvents

Signals that all events that match the criteria specified in the <i>EventSet</i> and <i>EventId</i> parameters have occurred.


#### SignalStreamEvent

Signals that the event specified by the <i>EventEntry</i> parameter has occurred.


#### StreamRequestComplete

Indicates that the minidriver has completed its handling of the stream-oriented stream request block that is pointed to by the optional third argument of this routine, <i>pSrb</i>.

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

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20StreamClassStreamNotification routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>