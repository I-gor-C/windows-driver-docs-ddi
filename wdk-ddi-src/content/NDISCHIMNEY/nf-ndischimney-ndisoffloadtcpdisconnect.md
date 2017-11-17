---
UID: NF.ndischimney.NdisOffloadTcpDisconnect
title: NdisOffloadTcpDisconnect
author: windows-driver-content
description: A protocol or intermediate driver calls the NdisOffloadTcpDisconnect function to close the send half of an offloaded TCP connection.
old-location: netvista\ndisoffloadtcpdisconnect.htm
ms.assetid: f8abff30-b641-4581-8532-8292993ca9f6
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisOffloadTcpDisconnect
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: 
ms.keywords: NdisOffloadTcpDisconnect
req.iface: 
---

# NdisOffloadTcpDisconnect function



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>A protocol or intermediate driver calls the 
  <b>NdisOffloadTcpDisconnect</b> function to close the send half of an offloaded TCP connection. In addition,
  if the disconnect to be performed is a graceful disconnect, the protocol or intermediate driver can supply
  application data that the underlying offload target must transmit on the offloaded TCP connection before it
  sends a FIN segment.</p>


## -syntax

````
NDIS_STATUS NdisOffloadTcpDisconnect(
  _In_ PNDIS_OFFLOAD_HANDLE NdisOffloadHandle,
  _In_ PNET_BUFFER_LIST     NetBufferList,
  _In_ ULONG                Flags
);
````


## -parameters
<dl>

### -param <i>NdisOffloadHandle</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566705">NDIS_OFFLOAD_HANDLE</a> structure in the
     caller's context for the offloaded TCP connection. For more information, see 
     <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
     Referencing Offloaded State Through an Intermediate Driver</a>.</p>
</dd>

### -param <i>NetBufferList</i> [in]

<dd>
<p>A pointer to a single 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. Only one 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure is associated with this
     NET_BUFFER_LIST structure.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>As one of the following values, the type of disconnect to be performed:
     </p>
<p></p>
<dl>

### -param <a id="TCP_DISCONNECT_ABORTIVE_CLOSE"></a><a id="tcp_disconnect_abortive_close"></a><b>TCP_DISCONNECT_ABORTIVE_CLOSE</b>

<dd>
<p>Specifies that the offload target perform an abortive disconnect by sending an RST
       segment.</p>
</dd>

### -param <a id="TCP_DISCONNECT_GRACEFUL_CLOSE"></a><a id="tcp_disconnect_graceful_close"></a><b>TCP_DISCONNECT_GRACEFUL_CLOSE</b>

<dd>
<p>Specifies that the offload target perform a graceful disconnect by sending a FIN segment.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>The 
     <b>NdisOffloadTcpDisconnect</b> function always returns NDIS_STATUS_PENDING. The disconnect operation is
     always completed asynchronously.</p>

## -remarks
<p>In response to a call to its 
    <a href="https://msdn.microsoft.com/f8be12a9-c2c0-4a22-8a57-58c8b27ef69e">
    MiniportTcpOffloadDisconnect</a> function, an intermediate driver calls the 
    <b>NdisOffloadTcpDisconnect</b> function to propagate the disconnect operation to the underlying
    intermediate driver or offload target. For more information, see 
    <a href="NULL">Propagating I/O Operations</a>.</p>

<p>To the 
    <b>NdisOffloadTcp<i>Xxx</i></b>
     function, the intermediate driver passes the following:</p>

<p>An 
      <i>NdisOffloadHandle</i> function that references the NDIS_OFFLOAD_HANDLE structure stored in the
      intermediate driver's context for the offloaded TCP connection. For more information, see 
      <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
      Referencing Offloaded State Through an Intermediate Driver</a>.</p>

<p>The same PNET_BUFFER_LIST pointer that NDIS passed to the intermediate driver's 
      <i>MiniportTcpOffloadDisconnect</i> function.</p>

<p>The same 
      <i>Flags</i> that NDIS passed to the intermediate driver's 
      <i>MiniportTcpOffloadDisconnect</i> function.</p>

<p>When the underlying driver or offload target subsequently completes the disconnect operation by
    calling the 
    <b>NdisTcpOffloadDisconnectComplete</b> function, NDIS calls the intermediate driver's 
    <i>ProtocolOffloadDisconnectComplete</i> function. The intermediate driver then calls the 
    <b>NdisTcpOffloadDisconnectComplete</b> function to propagate the completion of the disconnect
    operation.</p>

<p>In response to a call to its 
    <a href="https://msdn.microsoft.com/f8be12a9-c2c0-4a22-8a57-58c8b27ef69e">
    MiniportTcpOffloadDisconnect</a> function, an intermediate driver calls the 
    <b>NdisOffloadTcpDisconnect</b> function to propagate the disconnect operation to the underlying
    intermediate driver or offload target. For more information, see 
    <a href="NULL">Propagating I/O Operations</a>.</p>

<p>To the 
    <b>NdisOffloadTcp<i>Xxx</i></b>
     function, the intermediate driver passes the following:</p>

<p>An 
      <i>NdisOffloadHandle</i> function that references the NDIS_OFFLOAD_HANDLE structure stored in the
      intermediate driver's context for the offloaded TCP connection. For more information, see 
      <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
      Referencing Offloaded State Through an Intermediate Driver</a>.</p>

<p>The same PNET_BUFFER_LIST pointer that NDIS passed to the intermediate driver's 
      <i>MiniportTcpOffloadDisconnect</i> function.</p>

<p>The same 
      <i>Flags</i> that NDIS passed to the intermediate driver's 
      <i>MiniportTcpOffloadDisconnect</i> function.</p>

<p>When the underlying driver or offload target subsequently completes the disconnect operation by
    calling the 
    <b>NdisTcpOffloadDisconnectComplete</b> function, NDIS calls the intermediate driver's 
    <i>ProtocolOffloadDisconnectComplete</i> function. The intermediate driver then calls the 
    <b>NdisTcpOffloadDisconnectComplete</b> function to propagate the completion of the disconnect
    operation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/f8be12a9-c2c0-4a22-8a57-58c8b27ef69e">
   MiniportTcpOffloadDisconnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566705">NDIS_OFFLOAD_HANDLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e862d9fe-a60c-4397-95ce-62aa1ef17eae">
   NdisTcpOffloadDisconnectComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/56244148-638f-4d93-82a6-2cced9744046">
   ProtocolTcpOffloadDisconnectComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisOffloadTcpDisconnect function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
