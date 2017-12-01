---
UID: NC.hdaudio.PREGISTER_NOTIFICATION_EVENT
title: PREGISTER_NOTIFICATION_EVENT
author: windows-driver-content
description: The RegisterNotificationEvent routine registers a kernel event so that it can receive DMA progress notifications.The function pointer type for a RegisterNotificationEvent routine is defined as follows.
old-location: audio\registernotificationevent.htm
old-project: audio
ms.assetid: 44702d79-80ac-411f-ae47-bf60b9cb541d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SM_SetRNIDMgmtInfo_OUT, SM_SetRNIDMgmtInfo_OUT, *PSM_SetRNIDMgmtInfo_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: hdaudio.h
req.include-header: Hdaudio.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RegisterNotificationEvent
req.alt-loc: Hdaudio.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PREGISTER_NOTIFICATION_EVENT callback



## -description
<p>The <i>RegisterNotificationEvent</i> routine registers a kernel event so that it can receive DMA progress notifications.</p>
<p>The function pointer type for a <i>RegisterNotificationEvent</i> routine is defined as follows.</p>


## -prototype

````
PREGISTER_NOTIFICATION_EVENT RegisterNotificationEvent;

typedef NTSTATUS RegisterNotificationEvent(
  _In_ PVOID   context,
  _In_ HANDLE  handle,
  _In_ PKEVENT notificationEvent
)
{ ... }
````


## -parameters
<dl>

### -param <i>context</i> [in]

<dd>
<p>Specifies the context value from the Context member of the <a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface-v2.md">HDAUDIO_BUS_INTERFACE_V2</a> structure.</p>
</dd>

### -param <i>handle</i> [in]

<dd>
<p>Handle that identifies the DMA engine. This handle value was obtained from a previous call to <a href="..\hdaudio\nc-hdaudio-pallocate-capture-dma-engine.md">AllocateCaptureDmaEngine</a> or <a href="..\hdaudio\nc-hdaudio-pallocate-render-dma-engine.md">AllocateRenderDmaEngine</a>.</p>
</dd>

### -param <i>notificationEvent</i> [in]

<dd>
<p>A pointer to a kernel event that must be notified as DMA progresses.  Depending on the notification count parameter that is used with <a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer-with-notification.md">AllocateDmaBufferWithNotification</a>, the registered event is signaled one or two times for every time that the DMA passes through the audio buffer.</p>
</dd>
</dl>

## -returns
<p><i>RegisterNotificationEvent</i> returns STATUS_SUCCESS if the call successfully registers the event. Otherwise, the routine returns STATUS_INSUFFICIENT_RESOURCES to indicate that there are insufficient resources that are available to complete the operation.</p>

## -remarks
<p><i>RegisterNotificationEvent</i> registers a kernel event with the HD Audio bus driver.  The HD Audio bus driver maintains a list of registered notification events for each DMA engine, and signals them every time that the engine receives an IOC interrupt.  Events are unregistered by using <a href="..\hdaudio\nc-hdaudio-punregister-notification-event.md">UnregisterNotificationEvent</a>.</p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hdaudio.h (include Hdaudio.h)</dt>
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
<a href="..\hdaudio\nc-hdaudio-pallocate-capture-dma-engine.md">AllocateCaptureDmaEngine</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer-with-notification.md">AllocateDmaBufferWithNotification</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-render-dma-engine.md">AllocateRenderDmaEngine</a>
</dt>
<dt>
<a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface-v2.md">HDAUDIO_BUS_INTERFACE_V2</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-punregister-notification-event.md">UnregisterNotificationEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PREGISTER_NOTIFICATION_EVENT callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
