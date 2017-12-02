---
UID: NF.strmini.StreamClassStreamNotification
title: StreamClassStreamNotification
author: windows-driver-content
description: Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred.
old-location: stream\streamclassstreamnotification.htm
old-project: stream
ms.assetid: 67dd0ea0-9c69-415a-8b37-0e8700b6fbd8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: StreamClassStreamNotification
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
req.alt-api: StreamClassStreamNotification
req.alt-loc: Stream.lib,Stream.dll
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
req.iface: 
req.product: Windows 10 or later.
---

# StreamClassStreamNotification function



## -description
<p>Streams use the <b>StreamClassStreamNotification</b> routine to notify the class driver that it has completed a stream request, or that an event has occurred.</p>


## -syntax

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


## -parameters
<dl>

### -param NotificationType [in]

<dd>
<p>This is an enumeration value that contains the type of notification that the minidriver is sending.</p>
<p></p>
<dl>

### -param StreamRequestComplete

<dd>
<p>Indicates that the minidriver has completed its handling of the stream-oriented stream request block that is pointed to by the optional third argument of this routine, <i>pSrb</i>.</p>
</dd>

### -param ReadyForNextStreamDataRequest

<dd>
<p>Indicates that this stream is ready to receive another data request. </p>
</dd>

### -param ReadyForNextStreamControlRequest

<dd>
<p>Indicates that this stream is ready to receive another control request. </p>
</dd>

### -param SignalStreamEvent

<dd>
<p>Signals that the event specified by the <i>EventEntry</i> parameter has occurred.</p>
</dd>

### -param SignalMultipleStreamEvents

<dd>
<p>Signals that all events that match the criteria specified in the <i>EventSet</i> and <i>EventId</i> parameters have occurred.</p>
</dd>

### -param DeleteStreamEvent

<dd>
<p>Deletes the event specified by the <i>EventEntry</i> parameter.</p>
</dd>
</dl>
</dd>

### -param StreamObject [in]

<dd>
<p>Points to the stream object of the stream that the class driver is being notified about.</p>
</dd>

### -param pSrb 

<dd>
<p>Pointer to an <a href="..\strmini\ns-strmini--hw-stream-request-block.md">HW_STREAM_REQUEST_BLOCK</a> structure. Specify only if <i>NotificationType</i> equals <b>StreamRequestComplete</b>. Pointer to the stream request block that the minidriver has completed processing. Once this routine completes, this address is no longer valid. This parameter is optional.</p>
</dd>

### -param EventEntry 

<dd>
<p>Specify only if <i>NotificationType</i> equals either <b>SignalStreamEvent</b> or <b>DeleteStreamEvent</b>. Pointer to the event to be signaled or deleted. This parameter is optional. </p>
</dd>

### -param EventSet 

<dd>
<p>Identifies the event set against which to match in the event queue for this stream. Specify only if <i>NotificationType</i> equals <b>SignalMultipleStreamEvents</b>. This parameter is optional. </p>
</dd>

### -param EventId 

<dd>
<p>Indicates the event ID against which to match in the event queue for this stream. Specify only if <i>NotificationType</i> equals <b>SignalMultipleStreamEvents</b>. This parameter is optional.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The minidriver uses this routine for requests or events that apply to the minidriver as a whole. Stream-specific requests or events use <a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Stream.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20StreamClassStreamNotification routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
