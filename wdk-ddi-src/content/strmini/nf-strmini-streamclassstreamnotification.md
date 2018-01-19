---
UID : NF:strmini.StreamClassStreamNotification
title : StreamClassStreamNotification function
author : windows-driver-content
description : Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred.
old-location : stream\streamclassstreamnotification.htm
old-project : stream
ms.assetid : 67dd0ea0-9c69-415a-8b37-0e8700b6fbd8
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : StreamClassStreamNotification
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : strmini.h
req.include-header : Strmini.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : StreamClassStreamNotification
req.alt-loc : Stream.lib,Stream.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Stream.lib
req.dll : 
req.irql : 
req.typenames : STREAM_PRIORITY, *PSTREAM_PRIORITY
req.product : Windows 10 or later.
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

`StreamObject`

Points to the stream object of the stream that the class driver is being notified about.

``




## Return Value

None

## Remarks

The minidriver uses this routine for requests or events that apply to the minidriver as a whole. Stream-specific requests or events use <a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | strmini.h (include Strmini.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20StreamClassStreamNotification routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>