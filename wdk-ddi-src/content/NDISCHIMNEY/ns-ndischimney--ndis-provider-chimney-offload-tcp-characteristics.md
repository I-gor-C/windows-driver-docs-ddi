---
UID: NS.ndischimney._NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS
title: NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure specifies an offload target's TCP chimney offload-specific entry points.
old-location: netvista\ndis_provider_chimney_offload_tcp_characteristics.htm
ms.assetid: 3eabbad5-b84b-4034-a0b6-d4d515cbc117
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS
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
ms.keywords: NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS, NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS, *PNDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS
req.iface: 
---

# NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure specifies an offload target's TCP
  chimney offload-specific entry points.</p>


## -syntax

````
typedef struct _NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                   Header;
  ULONG                                Flags;
  NDIS_CHIMNEY_OFFLOAD_TYPE            OffloadType;
  W_TCP_OFFLOAD_SEND_HANDLER           TcpOffloadSendHandler;
  W_TCP_OFFLOAD_RECEIVE_HANDLER        TcpOffloadReceiveHandler;
  W_TCP_OFFLOAD_DISCONNECT_HANDLER     TcpOffloadDisconnectHandler;
  W_TCP_OFFLOAD_FORWARD_HANDLER        TcpOffloadForwardHandler;
  W_TCP_OFFLOAD_RECEIVE_RETURN_HANDLER TcpOffloadReceiveReturnHandler;
} NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS, *PNDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header of the NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure. The header is
     formatted as an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure. The
     NDIS_OBJECT_HEADER structure contains the revision number of the
     NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure and the size of the
     NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure, including the header, in bytes. The 
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

### -field <b>TcpOffloadSendHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/7c96412f-a866-4863-a06a-9eb6adb2a33b">
     MiniportTcpOffloadSend</a> function.</p>
</dd>

### -field <b>TcpOffloadReceiveHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/9c9c033d-e892-4d8a-8f12-4ca34cdc9ea1">
     MiniportTcpOffloadReceive</a> function.</p>
</dd>

### -field <b>TcpOffloadDisconnectHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/f8be12a9-c2c0-4a22-8a57-58c8b27ef69e">
     MiniportTcpOffloadDisconnect</a> function.</p>
</dd>

### -field <b>TcpOffloadForwardHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/e5702476-60a3-4bfc-b959-198e98f0f9ba">
     MiniportTcpOffloadForward</a> function.</p>
</dd>

### -field <b>TcpOffloadReceiveReturnHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/b746f58d-d029-4fcd-a59d-baba037fc38e">
     MiniportTcpOffloadReceiveReturn</a> function.</p>
</dd>
</dl>

## -remarks
<p>To register its TCP chimney offload-specific entry points, an offload target calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function
    in the context of the 
    <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function. To the 
    <b>NdisSetOptionalHandlers</b> function, the offload target passes a pointer to the
    NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure.</p>

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
<a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f8be12a9-c2c0-4a22-8a57-58c8b27ef69e">
   MiniportTcpOffloadDisconnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e5702476-60a3-4bfc-b959-198e98f0f9ba">MiniportTcpOffloadForward</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9c9c033d-e892-4d8a-8f12-4ca34cdc9ea1">MiniportTcpOffloadReceive</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b746f58d-d029-4fcd-a59d-baba037fc38e">
   MiniportTcpOffloadReceiveReturn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7c96412f-a866-4863-a06a-9eb6adb2a33b">MiniportTcpOffloadSend</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
