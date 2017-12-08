---
UID: NS.ndischimney._NDIS_TCP_OFFLOAD_EVENT_HANDLERS
title: NDIS_TCP_OFFLOAD_EVENT_HANDLERS
author: windows-driver-content
description: The NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure contains the entry points for the NDIS functions for the TCP chimney.
old-location: netvista\ndis_tcp_offload_event_handlers.htm
old-project: netvista
ms.assetid: 72863a3e-9907-43e1-ad83-831a972ab823
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_TCP_OFFLOAD_EVENT_HANDLERS, NDIS_TCP_OFFLOAD_EVENT_HANDLERS, *PNDIS_TCP_OFFLOAD_EVENT_HANDLERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_TCP_OFFLOAD_EVENT_HANDLERS
req.alt-loc: ndischimney.h
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

# NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure contains the entry points for the NDIS functions for
  the TCP chimney.</p>


## -syntax

````
typedef struct _NDIS_TCP_OFFLOAD_EVENT_HANDLERS {
  NDIS_OBJECT_HEADER                   Header;
  NDIS_TCP_OFFLOAD_EVENT_INDICATE      NdisTcpOffloadEventHandler;
  NDIS_TCP_OFFLOAD_RECEIVE_INDICATE    NdisTcpOffloadReceiveHandler;
  NDIS_TCP_OFFLOAD_SEND_COMPLETE       NdisTcpOffloadSendComplete;
  NDIS_TCP_OFFLOAD_RECEIVE_COMPLETE    NdisTcpOffloadReceiveComplete;
  NDIS_TCP_OFFLOAD_DISCONNECT_COMPLETE NdisTcpOffloadDisconnectComplete;
  NDIS_TCP_OFFLOAD_FORWARD_COMPLETE    NdisTcpOffloadForwardComplete;
} NDIS_TCP_OFFLOAD_EVENT_HANDLERS, *PNDIS_TCP_OFFLOAD_EVENT_HANDLERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The NDIS object header, which is formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
</dd>

### -field NdisTcpOffloadEventHandler

<dd>
<p>The entry point for the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-event-indicate.md">
     NdisTcpOffloadEventHandler</a> function.</p>
</dd>

### -field NdisTcpOffloadReceiveHandler

<dd>
<p>The entry point for the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-indicate.md">
     NdisTcpOffloadReceiveHandler</a> function.</p>
</dd>

### -field NdisTcpOffloadSendComplete

<dd>
<p>The entry point for the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-send-complete.md">
     NdisTcpOffloadSendComplete</a> function.</p>
</dd>

### -field NdisTcpOffloadReceiveComplete

<dd>
<p>The entry point for the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-complete.md">
     NdisTcpOffloadReceiveComplete</a> function.</p>
</dd>

### -field NdisTcpOffloadDisconnectComplete

<dd>
<p>The entry point for the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-disconnect-complete.md">
     NdisTcpOffloadDisconnectComplete</a> function.</p>
</dd>

### -field NdisTcpOffloadForwardComplete

<dd>
<p>The entry point for the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-forward-complete.md">
     NdisTcpOffloadForwardComplete</a> function.</p>
</dd>
</dl>

## -remarks
<p>An offload target copies the entry points in the NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure into its
    own internal data structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndischimney.h (include Ndischimney.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndismgetoffloadhandlers.md">NdisMGetOffloadHandlers</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-disconnect-complete.md">
   NdisTcpOffloadDisconnectComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-event-indicate.md">NdisTcpOffloadEventHandler</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-complete.md">
   NdisTcpOffloadReceiveComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-indicate.md">NdisTcpOffloadReceiveHandler</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-send-complete.md">NdisTcpOffloadSendComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
