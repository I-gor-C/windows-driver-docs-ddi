---
UID: NF.ndischimney.NdisOffloadTcpSend
title: NdisOffloadTcpSend
author: windows-driver-content
description: A protocol driver or intermediate driver calls the NdisOffloadTcpSend function to transmit data on an offloaded TCP connection.
old-location: netvista\ndisoffloadtcpsend.htm
old-project: netvista
ms.assetid: a2743bbb-a6fa-4b7e-8087-132e221a5624
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisOffloadTcpSend
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisOffloadTcpSend
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
req.iface: 
---

# NdisOffloadTcpSend function



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>A protocol driver or intermediate driver calls the 
  <b>NdisOffloadTcpSend</b> function to transmit data on an offloaded TCP connection.</p>


## -syntax

````
NDIS_STATUS NdisOffloadTcpSend(
  _In_ PNDIS_OFFLOAD_HANDLE NdisOffloadHandle,
  _In_ PNET_BUFFER_LIST     NetBufferList
);
````


## -parameters
<dl>

### -param NdisOffloadHandle [in]

<dd>
<p>A handle to an 
     <a href="..\ndischimney\ns-ndischimney--ndis-offload-handle.md">NDIS_OFFLOAD_HANDLE</a> structure in the
     caller's context for the offloaded TCP connection. For more information, see 
     <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
     Referencing Offloaded State Through an Intermediate Driver</a>.</p>
</dd>

### -param NetBufferList [in]

<dd>
<p>A pointer to a 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure. This structure
     can be a stand-alone structure or the first structure in a linked list of NET_BUFFER_LIST structures.
     Each NET_BUFFER_LIST structure in the list describes a list of 
     <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures. Each NET_BUFFER structure
     in the list points to a chain of memory descriptor lists (MDLs). The MDLs contain the data to be
     transmitted. The NET_BUFFER_LIST and associated structures are locked so that they remain resident in
     physical memory. However, they are not mapped into system memory.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>NdisOffloadTcpSend</b> function always returns NDIS_STATUS_PENDING. The send operation is always
     completed asynchronously.</p>

## -remarks
<p>In response to a call to its 
    <a href="..\ndischimney\nc-ndischimney-w-tcp-offload-send-handler.md">MiniportTcpOffloadSend</a> function,
    an intermediate driver calls the 
    <b>NdisOffloadTcpSend</b> function to propagate the send operation to the underlying intermediate driver
    or offload target. For more information, see 
    <a href="netvista.propagating_i_o_operations">Propagating I/O Operations</a>.</p>

<p>To the 
    <b>NdisOffloadTcpSend</b> function, the intermediate driver passes the following:</p>

<p>An 
      <i>NdisOffloadHandle</i> that references the NDIS_OFFLOAD_HANDLE structure stored in the intermediate
      driver's context for the offloaded TCP connection. For more information, see 
      <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
      Referencing Offloaded State Through an Intermediate Driver</a>.</p>

<p>The same PNET_BUFFER_LIST pointer that NDIS passed to the intermediate driver's 
      <i>MiniportTcpOffloadSend</i> function.</p>

<p>When the underlying driver or offload target subsequently completes the send operation by calling the 
    <b>NdisTcpOffloadSendComplete</b> function, NDIS calls the intermediate driver's 
    <i>ProtocolOffloadSendComplete</i> function. The intermediate driver then calls the 
    <b>NdisTcpOffloadSendComplete</b> function to propagate the completion of the send operation.</p>

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
<a href="..\ndischimney\nc-ndischimney-w-tcp-offload-send-handler.md">MiniportTcpOffloadSend</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--ndis-offload-handle.md">NDIS_OFFLOAD_HANDLE</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-send-complete.md">NdisTcpOffloadSendComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-tcp-offload-send-complete-handler.md">
   ProtocolTcpOffloadSendComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisOffloadTcpSend function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
