---
UID: NF.strmini.StreamClassStreamNotification
title: StreamClassStreamNotification
author: windows-driver-content
description: Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred.
old-location: stream\streamclassstreamnotification.htm
ms.assetid: 67dd0ea0-9c69-415a-8b37-0e8700b6fbd8
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
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
ms.keywords: StreamClassStreamNotification
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

### -param <i>NotificationType</i> [in]

<dd>
<p>This is an enumeration value that contains the type of notification that the minidriver is sending.</p>
<p></p>
<dl>

### -param <a id="StreamRequestComplete"></a><a id="streamrequestcomplete"></a><a id="STREAMREQUESTCOMPLETE"></a><b>StreamRequestComplete</b>

<dd>
<p>Indicates that the minidriver has completed its handling of the stream-oriented stream request block that is pointed to by the optional third argument of this routine, <i>pSrb</i>.</p>
</dd>

### -param <a id="ReadyForNextStreamDataRequest"></a><a id="readyfornextstreamdatarequest"></a><a id="READYFORNEXTSTREAMDATAREQUEST"></a><b>ReadyForNextStreamDataRequest</b>

<dd>
<p>Indicates that this stream is ready to receive another data request. </p>
</dd>

### -param <a id="ReadyForNextStreamControlRequest"></a><a id="readyfornextstreamcontrolrequest"></a><a id="READYFORNEXTSTREAMCONTROLREQUEST"></a><b>ReadyForNextStreamControlRequest</b>

<dd>
<p>Indicates that this stream is ready to receive another control request. </p>
</dd>

### -param <a id="SignalStreamEvent"></a><a id="signalstreamevent"></a><a id="SIGNALSTREAMEVENT"></a><b>SignalStreamEvent</b>

<dd>
<p>Signals that the event specified by the <i>EventEntry</i> parameter has occurred.</p>
</dd>

### -param <a id="SignalMultipleStreamEvents"></a><a id="signalmultiplestreamevents"></a><a id="SIGNALMULTIPLESTREAMEVENTS"></a><b>SignalMultipleStreamEvents</b>

<dd>
<p>Signals that all events that match the criteria specified in the <i>EventSet</i> and <i>EventId</i> parameters have occurred.</p>
</dd>

### -param <a id="DeleteStreamEvent"></a><a id="deletestreamevent"></a><a id="DELETESTREAMEVENT"></a><b>DeleteStreamEvent</b>

<dd>
<p>Deletes the event specified by the <i>EventEntry</i> parameter.</p>
</dd>
</dl>
</dd>

### -param <i>StreamObject</i> [in]

<dd>
<p>Points to the stream object of the stream that the class driver is being notified about.</p>
</dd>

### -param <i>pSrb</i> 

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a> structure. Specify only if <i>NotificationType</i> equals <b>StreamRequestComplete</b>. Pointer to the stream request block that the minidriver has completed processing. Once this routine completes, this address is no longer valid. This parameter is optional.</p>
</dd>

### -param <i>EventEntry</i> 

<dd>
<p>Specify only if <i>NotificationType</i> equals either <b>SignalStreamEvent</b> or <b>DeleteStreamEvent</b>. Pointer to the event to be signaled or deleted. This parameter is optional. </p>
</dd>

### -param <i>EventSet</i> 

<dd>
<p>Identifies the event set against which to match in the event queue for this stream. Specify only if <i>NotificationType</i> equals <b>SignalMultipleStreamEvents</b>. This parameter is optional. </p>
</dd>

### -param <i>EventId</i> 

<dd>
<p>Indicates the event ID against which to match in the event queue for this stream. Specify only if <i>NotificationType</i> equals <b>SignalMultipleStreamEvents</b>. This parameter is optional.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The minidriver uses this routine for requests or events that apply to the minidriver as a whole. Stream-specific requests or events use <a href="https://msdn.microsoft.com/library/windows/hardware/ff568239">StreamClassDeviceNotification</a>.</p>

<p>The minidriver uses this routine for requests or events that apply to the minidriver as a whole. Stream-specific requests or events use <a href="https://msdn.microsoft.com/library/windows/hardware/ff568239">StreamClassDeviceNotification</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568239">StreamClassDeviceNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20StreamClassStreamNotification routine%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
