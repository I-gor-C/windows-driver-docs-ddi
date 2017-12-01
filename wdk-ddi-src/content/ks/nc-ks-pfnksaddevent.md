---
UID: NC.ks.PFNKSADDEVENT
title: PFNKSADDEVENT
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniAddEvent routine is called when a client registers to be notified of an event. This routine is optional.
old-location: stream\avstrminiaddevent.htm
old-project: stream
ms.assetid: ff80bbc7-93b1-4319-a549-f896ce0f4611
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVStrMiniAddEvent
req.alt-loc: ks.h
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
req.iface: 
---

# PFNKSADDEVENT callback



## -description
<p>An AVStream minidriver's <i>AVStrMiniAddEvent</i> routine is called when a client registers to be notified of an event. This routine is optional.</p>


## -prototype

````
PFNKSADDEVENT AVStrMiniAddEvent;

NTSTATUS AVStrMiniAddEvent(
  _In_ PIRP                  Irp,
  _In_ PKSEVENTDATA          EventData,
  _In_ struct _KSEVENT_ENTRY *EventEntry
)
{ ... }
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP describing the event add request.</p>
</dd>

### -param <i>EventData</i> [in]

<dd>
<p>Pointer to a <a href="stream.kseventdata">KSEVENTDATA</a> structure describing the notification method for this event.</p>
</dd>

### -param <i>EventEntry</i> [in]

<dd>
<p>Pointer to an AVStream-generated <a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a> structure describing how the event is triggered.</p>
</dd>
</dl>

## -returns
<p><i>AVStrMiniAddEvent</i> should return STATUS_SUCCESS or an error specific to the event being enabled.  </p>

## -remarks
<p>If you do not provide an add event handler, AVStream adds the event to the object list. See <a href="NULL">Event Handling in AVStream</a>.</p>

<p>Frequently this callback implements vendor-specific behavior and then calls <a href="..\ks\nf-ks-ksfilteraddevent.md">KsFilterAddEvent</a> or <a href="..\ks\nf-ks-kspinaddevent.md">KsPinAddEvent</a>. The minidriver passes the <i>EventEntry</i> pointer received here in calls to <i>KsFilterAddEvent</i> or <i>KsPinAddEvent</i>.</p>

<p>The minidriver specifies this routine's address in the <b>AddHandler</b> member of a <a href="stream.ksevent_item">KSEVENT_ITEM</a> structure. <a href="NULL">Event Handling in AVStream</a> describes how the minidriver provides this structure to the class driver.</p>

<p>If an AVStream minidriver specifies <b>AddHandler</b> as non-NULL, AVStream does not add the item to the object's event list. If minidriver specifies an <b>AddHandler</b> and does not add the event to the object's event list through <b>KsDefaultAddEventHandler()</b> or a <b>Ks*AddEvent </b>call, the minidriver is responsible for cleaning up the event.</p>

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
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.kseventdata">KSEVENTDATA</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a>
</dt>
<dt>
<a href="stream.ksevent_item">KSEVENT_ITEM</a>
</dt>
<dt>
<a href="stream.ksautomation_table">KSAUTOMATION_TABLE</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfilteraddevent.md">KsFilterAddEvent</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspinaddevent.md">KsPinAddEvent</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfiltergenerateevents.md">KsFilterGenerateEvents</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingenerateevents.md">KsPinGenerateEvents</a>
</dt>
<dt>
<a href="stream.avstrminiremoveevent">AVStrMiniRemoveEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniAddEvent routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
