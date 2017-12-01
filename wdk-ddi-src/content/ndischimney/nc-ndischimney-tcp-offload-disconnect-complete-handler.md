---
UID: NC.ndischimney.TCP_OFFLOAD_DISCONNECT_COMPLETE_HANDLER
title: TCP_OFFLOAD_DISCONNECT_COMPLETE_HANDLER
author: windows-driver-content
description: NDIS calls a protocol driver's or intermediate driver's ProtocolTcpOffloadDisconnectComplete function to complete a disconnect operation that the driver previously initiated by calling the NdisOffloadTcpDisconnect function.
old-location: netvista\protocoltcpoffloaddisconnectcomplete.htm
old-project: netvista
ms.assetid: 56244148-638f-4d93-82a6-2cced9744046
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BINARY_DATA, BINARY_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolTcpOffloadDisconnectComplete
req.alt-loc: Ndischimney.h
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

# TCP_OFFLOAD_DISCONNECT_COMPLETE_HANDLER callback



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>NDIS calls a protocol driver's or intermediate driver's 
  <i>ProtocolTcpOffloadDisconnectComplete</i> function to complete a disconnect operation that the driver
  previously initiated by calling the 
  <a href="..\ndischimney\nf-ndischimney-ndisoffloadtcpdisconnect.md">
  NdisOffloadTcpDisconnect</a> function.</p>


## -prototype

````
TCP_OFFLOAD_DISCONNECT_COMPLETE_HANDLER ProtocolTcpOffloadDisconnectComplete;

VOID ProtocolTcpOffloadDisconnectComplete(
  _In_ NDIS_HANDLE      ProtocolBindingContext,
  _In_ PNET_BUFFER_LIST NetBufferList
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProtocolBindingContext</i> [in]

<dd>
<p>A handle to a context area allocated by the protocol driver. The driver maintains the per binding
     context information in this context area. The driver supplied this handle to NDIS when the driver called
     the 
     <a href="..\ndis\nf-ndis-ndisopenadapterex.md">NdisOpenAdapterEx</a> function.</p>
</dd>

### -param <i>NetBufferList</i> [in]

<dd>
<p>When non-NULL, a pointer to a single 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure. The driver
     supplied this pointer as an input parameter in a previous call to the 
     <a href="..\ndischimney\nf-ndischimney-ndisoffloadtcpdisconnect.md">
     NdisOffloadTcpDisconnect</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>In response to an underlying driver's or offload target's call to the 
    <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-disconnect-complete.md">
    NdisTcpOffloadDisconnectComplete</a> function, NDIS calls the overlying protocol driver's or
    intermediate driver's 
    <i>ProtocolTcpOffloadDisconnectComplete</i> function.</p>

<p>To propagate the completion of the disconnect operation to the overlying driver, the intermediate
    driver calls the 
    <b>NdisOffloadTcpDisconnectComplete</b> function, passing in the following:</p>

<p>A 
      <i>ProtocolBindingContext</i>, which is a handle that uniquely identifies the intermediate driver.</p>

<p>The same PNET_BUFFER_LIST pointer that NDIS passed to the intermediate driver's 
      <i>ProtocolTcpOffloadDisconnectComplete</i> function.</p>

<p>In response, NDIS calls the overlying driver's 
    <i>ProtocolTcpOffloadDisconnectComplete</i> function, passing a 
    <i>ProtocolBindingContext</i> handle and the PNET_BUFFER_LIST pointer passed by the intermediate driver to
    the 
    <b>NdisOffloadTcpDisconnectComplete</b> function.</p>

<p>Before returning, the 
    <i>ProtocolTcpOffloadDisconnectComplete</i> function should deallocate the memory for any context that it
    created for the NET_BUFFER_LIST structure that was passed to the function.</p>

<p>Note that, if an intermediate driver exports more than one interface to overlying protocols, it must
    determine which protocol should receive the completion of the disconnect. To make this determination, the
    intermediate driver uses information that it stored in the 
    <a href="netvista.net_buffer_list_context_structure">
    NET_BUFFER_LIST_CONTEXT</a> structure, which is associated with the NET_BUFFER_LIST structure.</p>

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
<a href="..\ndischimney\nc-ndischimney-w-tcp-offload-disconnect-handler.md">
   MiniportTcpOffloadDisconnect</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndisoffloadtcpdisconnect.md">NdisOffloadTcpDisconnect</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisopenadapterex.md">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-disconnect-complete.md">
   NdisTcpOffloadDisconnectComplete</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20TCP_OFFLOAD_DISCONNECT_COMPLETE_HANDLER callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
