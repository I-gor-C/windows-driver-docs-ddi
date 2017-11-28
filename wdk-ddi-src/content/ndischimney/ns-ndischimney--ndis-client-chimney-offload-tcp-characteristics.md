---
UID: NS.ndischimney._NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS
title: NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure specifies a protocol or intermediate driver's TCP chimney offload-specific entry points.
old-location: netvista\ndis_client_chimney_offload_tcp_characteristics.htm
old-project: netvista
ms.assetid: 1925cfd4-f83f-48a5-b928-2c663ac0dc61
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS, NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS, *PNDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS
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
req.alt-api: NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS
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

# NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure specifies a protocol or intermediate
  driver's TCP chimney offload-specific entry points.</p>


## -syntax

````
typedef struct _NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                      Header;
  ULONG                                   Flags;
  NDIS_CHIMNEY_OFFLOAD_TYPE               OffloadType;
  TCP_OFFLOAD_SEND_COMPLETE_HANDLER       TcpOffloadSendCompleteHandler;
  TCP_OFFLOAD_RECV_COMPLETE_HANDLER       TcpOffloadReceiveCompleteHandler;
  TCP_OFFLOAD_DISCONNECT_COMPLETE_HANDLER TcpOffloadDisconnectCompleteHandler;
  TCP_OFFLOAD_FORWARD_COMPLETE_HANDLER    TcpOffloadForwardCompleteHandler;
  TCP_OFFLOAD_EVENT_HANDLER               TcpOffloadEventHandler;
  TCP_OFFLOAD_RECEIVE_INDICATE_HANDLER    TcpOffloadReceiveIndicateHandler;
} NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS, *PNDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header of the NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure. The header is
     formatted as an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure. The
     NDIS_OBJECT_HEADER structure contains the revision number of the
     NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure and the size of the
     NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure, including the header, in bytes. The 
     <b>Type</b> member of the header is not significant.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>OffloadType</b>

<dd>
<p>The chimney offload type. The only allowable value is 
     <b>NdisTcpChimneyOffload</b>, which specifies a TCP chimney.</p>
</dd>

### -field <b>TcpOffloadSendCompleteHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-tcp-offload-send-complete-handler.md">
     ProtocolTcpOffloadSendComplete</a> function.</p>
</dd>

### -field <b>TcpOffloadReceiveCompleteHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-tcp-offload-recv-complete-handler.md">
     ProtocolTcpOffloadReceiveComplete</a> function.</p>
</dd>

### -field <b>TcpOffloadDisconnectCompleteHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-tcp-offload-disconnect-complete-handler.md">
     ProtocolTcpOffloadDisconnectComplete</a> function.</p>
</dd>

### -field <b>TcpOffloadForwardCompleteHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-tcp-offload-forward-complete-handler.md">
     ProtocolTcpOffloadForwardComplete</a> function.</p>
</dd>

### -field <b>TcpOffloadEventHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-tcp-offload-event-handler.md">
     ProtocolTcpOffloadEvent</a> function.</p>
</dd>

### -field <b>TcpOffloadReceiveIndicateHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-tcp-offload-receive-indicate-handler.md">
     ProtocolTcpOffloadReceiveIndicate</a> function.</p>
</dd>
</dl>

## -remarks
<p>To register its TCP chimney offload entry points, a protocol or intermediate driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function
    in the context of the 
    <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function. To the 
    <b>NdisSetOptionalHandlers</b> function, the protocol or intermediate driver passes a pointer to the
    NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-tcp-offload-disconnect-complete-handler.md">
   ProtocolTcpOffloadDisconnectComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-tcp-offload-event-handler.md">ProtocolTcpOffloadEvent</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-tcp-offload-recv-complete-handler.md">
   ProtocolTcpOffloadReceiveComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-tcp-offload-receive-indicate-handler.md">
   ProtocolTcpOffloadReceiveIndicate</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-tcp-offload-send-complete-handler.md">
   ProtocolTcpOffloadSendComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
