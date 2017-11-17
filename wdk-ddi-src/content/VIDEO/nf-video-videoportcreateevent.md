---
UID: NF.video.VideoPortCreateEvent
title: VideoPortCreateEvent
author: windows-driver-content
description: The VideoPortCreateEvent function creates an event object.
old-location: display\videoportcreateevent.htm
ms.assetid: bb1ef5f0-ccf3-487b-99e6-9ec733c7cd63
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortCreateEvent
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
ms.keywords: VideoPortCreateEvent
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortCreateEvent function



## -description
<p>The <b>VideoPortCreateEvent</b> function creates an event object.</p>


## -syntax

````
VP_STATUS VideoPortCreateEvent(
  _In_  PVOID  HwDeviceExtension,
  _In_  ULONG  EventFlag,
  _In_  PVOID  Unused,
  _Out_ PEVENT *ppEvent
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>EventFlag</i> [in]

<dd>
<p>Specifies the event type and initial event state. This can be an ORed combination of the following flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>INITIAL_EVENT_SIGNALED</p>
</td>
<td>
<p>Set this flag to indicate the signaled state for the event object. Otherwise, the initial state of the event is nonsignaled.</p>
</td>
</tr>
<tr>
<td>
<p> NOTIFICATION_EVENT</p>
</td>
<td>
<p>Set this flag to create a notification event. If this flag is not set, a synchronization event is created.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Unused</i> [in]

<dd>
<p>Is currently ignored by the video port driver and must be set to <b>NULL</b>.</p>
</dd>

### -param <i>ppEvent</i> [out]

<dd>
<p>Pointer to the memory location at which a pointer to the event object will be returned.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortCreateEvent</b> returns NO_ERROR if the event object is successfully created.</p>

## -remarks
<p>When a synchronization event is set to the signaled state, a single thread that was waiting for the signaled state is released (its dispatch state transitions from waiting to ready, standby, or running), and the event is automatically reset to the nonsignaled state.</p>

<p>When a notification event is set to the signaled state, all threads that were waiting for the signaled state are released, and the event remains in the signaled state until it is explicitly reset to the nonsignaled state. </p>

<p>When a synchronization event is set to the signaled state, a single thread that was waiting for the signaled state is released (its dispatch state transitions from waiting to ready, standby, or running), and the event is automatically reset to the nonsignaled state.</p>

<p>When a notification event is set to the signaled state, all threads that were waiting for the signaled state are released, and the event remains in the signaled state until it is explicitly reset to the nonsignaled state. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570292">VideoPortDeleteEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortCreateEvent function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
