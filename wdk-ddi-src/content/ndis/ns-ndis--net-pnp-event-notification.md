---
UID: NS.ndis._NET_PNP_EVENT_NOTIFICATION
title: NET_PNP_EVENT_NOTIFICATION
author: windows-driver-content
description: The NET_PNP_EVENT_NOTIFICATION structure describes a network Plug and Play (PnP) event, an NDIS PnP event, or a power management event.
old-location: netvista\net_pnp_event_notification.htm
old-project: netvista
ms.assetid: 58d3baf3-a1fa-42ae-b795-2774a148aeda
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NET_PNP_EVENT_NOTIFICATION, NET_PNP_EVENT_NOTIFICATION, *PNET_PNP_EVENT_NOTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NET_PNP_EVENT_NOTIFICATION
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NET_PNP_EVENT_NOTIFICATION structure



## -description
<p>The NET_PNP_EVENT_NOTIFICATION structure describes a network Plug and Play (PnP) event, an NDIS PnP
  event, or a power management event.</p>


## -syntax

````
typedef struct _NET_PNP_EVENT_NOTIFICATION {
  NDIS_OBJECT_HEADER Header;
  NDIS_PORT_NUMBER   PortNumber;
  NET_PNP_EVENT      NetPnPEvent;
} NET_PNP_EVENT_NOTIFICATION, *PNET_PNP_EVENT_NOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NET_PNP_EVENT_NOTIFICATION structure. NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NET_PNP_EVENT_NOTIFICATION_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_NET_PNP_EVENT_NOTIFICATION_REVISION_1.</p>
</dd>

### -field <b>PortNumber</b>

<dd>
<p>The source port of the event notification. If the status indication is not specific to a port, 
     <b>PortNumber</b> is zero.</p>
</dd>

### -field <b>NetPnPEvent</b>

<dd>
<p>A
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568751">NET_PNP_EVENT</a> structure that describes the
     event.</p>
</dd>
</dl>

## -remarks
<p>When the operating system issues a system PnP event or a power management event to a target device
    object that represents an adapter, NDIS translates the event into a NET_PNP_EVENT_NOTIFICATION
    structure.</p>

<p>The 
    <b>NetPnPEvent</b> member is a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568751">NET_PNP_EVENT</a> structure. The 
    <b>NetEvent</b> member of this NET_PNP_EVENT structure specifies an event code that identifies the network
    PnP event, NDIS PnP event, or power management event.</p>

<p>The 
    <b>Buffer</b> member, which is in the NET_PNP_EVENT structure that is specified in the 
    <b>NetPnPEvent</b> member of NET_PNP_EVENT_NOTIFICATION, specifies the address of a buffer that contains
    information that is specific to the event that is indicated by the 
    <b>NetEvent</b> member.</p>

<p>NDIS also issues PnP event notifications for NDIS PnP events such as 
    <b>NetEventPause</b>, 
    <b>NetEventRestart</b>, 
    <b>NetEventPortActivation</b>, and 
    <b>NetEventPortDeactivation</b>.</p>

<p>NDIS passes a pointer to a NET_PNP_EVENT_NOTIFICATION structure to the 
    <a href="..\ndis\nc-ndis-filter-net-pnp-event.md">FilterNetPnPEvent</a> function of
    overlying filter drivers and to the 
    <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a> function of
    overlying protocol drivers.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-filter-net-pnp-event.md">FilterNetPnPEvent</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568751">NET_PNP_EVENT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_PNP_EVENT_NOTIFICATION structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
