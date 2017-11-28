---
UID: NF.ndis.NdisCancelSendNetBufferLists
title: NdisCancelSendNetBufferLists
author: windows-driver-content
description: Protocol drivers call the NdisCancelSendNetBufferLists function to cancel the transmission of network data.
old-location: netvista\ndiscancelsendnetbufferlists.htm
old-project: netvista
ms.assetid: 7b61db73-ddd4-4d46-b378-9a82fdf041ea
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisCancelSendNetBufferLists
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCancelSendNetBufferLists
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_SendRcv_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisCancelSendNetBufferLists function



## -description
<p>Protocol drivers call the 
  <b>NdisCancelSendNetBufferLists</b> function to cancel the transmission of network data.</p>


## -syntax

````
VOID NdisCancelSendNetBufferLists(
  _In_ NDIS_HANDLE NdisBindingHandle,
  _In_ PVOID       CancelId
);
````


## -parameters
<dl>

### -param <i>NdisBindingHandle</i> [in]

<dd>
<p>The handle returned by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function that
     identifies the miniport driver or virtual miniport to which the cancellation applies.</p>
</dd>

### -param <i>CancelId</i> [in]

<dd>
<p>The cancellation identifier. This identifier specifies the network data for which transmission is
     being canceled.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A protocol driver maps IRPs that it receives from higher-level software to NDIS network data. A list
    of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures describes the
    network data that the protocol driver sends to lower-level drivers for transmission. If an IRP is
    canceled, a protocol driver can call the 
    <b>NdisCancelSendNetBufferLists</b> function to cancel the pending transmission of the corresponding NDIS
    network data.</p>

<p>Call the 
    <a href="netvista.ndis_set_net_buffer_list_cancel_id">
    NDIS_SET_NET_BUFFER_LIST_CANCEL_ID</a> macro for each NET_BUFFER_LIST structure that is passed to
    lower-level drivers for transmission. The NDIS_SET_NET_BUFFER_LIST_CANCEL_ID macro marks the specified
    packet with a cancellation identifier.</p>

<p><b>NdisCancelSendNetBufferLists</b> cancels the transmission of all data that is marked with the specified
    cancellation identifier and is associated with the specified miniport driver. The binding handle that is
    specified in the 
    <i>NdisBindingHandle</i> parameter identifies the miniport driver.</p>

<p>The 
    <b>NdisCancelSendNetBufferLists</b> function cancels network data transmissions on a single binding. To
    cancel network data transmissions on more than one binding, a protocol driver must call the 
    <b>NdisCancelSendNetBufferLists</b> function once for each binding.</p>

<p>The protocol driver must ensure that the handle that the 
    <i>NdisBindingHandle</i> parameter specifies remains valid for the duration of the call to 
    <b>NdisCancelSendNetBufferLists</b>. That is, the protocol driver must not call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561640">NdisCloseAdapterEx</a> function to close
    the binding before 
    <b>NdisCancelSendNetBufferLists</b> returns.</p>

<p>There is no guarantee that calling 
    <b>NdisCancelSendNetBufferLists</b> will cancel the pending transmission of all network data with the
    specified cancellation identifier. For example, if the next-lower driver to which the protocol driver is
    bound does not provide a 
    <a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a> function, a call
    to 
    <b>NdisCancelSendNetBufferLists</b> does nothing.</p>

<p>In all cases, NDIS returns network data that was submitted for transmission to the originating
    protocol driver's 
    <a href="..\ndis\nc-ndis-protocol-send-net-buffer-lists-complete.md">
    ProtocolSendNetBufferListsComplete</a> function. NDIS returns canceled send data with a completion
    status of NDIS_STATUS_SEND_ABORTED. The delay between calling 
    <b>NdisCancelSendNetBufferLists</b> and the return of the canceled NET_BUFFER_LIST structures can vary and
    therefore cannot be exactly specified.</p>

<p>A protocol driver maps IRPs that it receives from higher-level software to NDIS network data. A list
    of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures describes the
    network data that the protocol driver sends to lower-level drivers for transmission. If an IRP is
    canceled, a protocol driver can call the 
    <b>NdisCancelSendNetBufferLists</b> function to cancel the pending transmission of the corresponding NDIS
    network data.</p>

<p>Call the 
    <a href="netvista.ndis_set_net_buffer_list_cancel_id">
    NDIS_SET_NET_BUFFER_LIST_CANCEL_ID</a> macro for each NET_BUFFER_LIST structure that is passed to
    lower-level drivers for transmission. The NDIS_SET_NET_BUFFER_LIST_CANCEL_ID macro marks the specified
    packet with a cancellation identifier.</p>

<p><b>NdisCancelSendNetBufferLists</b> cancels the transmission of all data that is marked with the specified
    cancellation identifier and is associated with the specified miniport driver. The binding handle that is
    specified in the 
    <i>NdisBindingHandle</i> parameter identifies the miniport driver.</p>

<p>The 
    <b>NdisCancelSendNetBufferLists</b> function cancels network data transmissions on a single binding. To
    cancel network data transmissions on more than one binding, a protocol driver must call the 
    <b>NdisCancelSendNetBufferLists</b> function once for each binding.</p>

<p>The protocol driver must ensure that the handle that the 
    <i>NdisBindingHandle</i> parameter specifies remains valid for the duration of the call to 
    <b>NdisCancelSendNetBufferLists</b>. That is, the protocol driver must not call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561640">NdisCloseAdapterEx</a> function to close
    the binding before 
    <b>NdisCancelSendNetBufferLists</b> returns.</p>

<p>There is no guarantee that calling 
    <b>NdisCancelSendNetBufferLists</b> will cancel the pending transmission of all network data with the
    specified cancellation identifier. For example, if the next-lower driver to which the protocol driver is
    bound does not provide a 
    <a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a> function, a call
    to 
    <b>NdisCancelSendNetBufferLists</b> does nothing.</p>

<p>In all cases, NDIS returns network data that was submitted for transmission to the originating
    protocol driver's 
    <a href="..\ndis\nc-ndis-protocol-send-net-buffer-lists-complete.md">
    ProtocolSendNetBufferListsComplete</a> function. NDIS returns canceled send data with a completion
    status of NDIS_STATUS_SEND_ABORTED. The delay between calling 
    <b>NdisCancelSendNetBufferLists</b> and the return of the canceled NET_BUFFER_LIST structures can vary and
    therefore cannot be exactly specified.</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548004">Irql_SendRcv_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a>
</dt>
<dt>
<a href="netvista.ndis_set_net_buffer_list_cancel_id">
   NDIS_SET_NET_BUFFER_LIST_CANCEL_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561640">NdisCloseAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-send-net-buffer-lists-complete.md">
   ProtocolSendNetBufferListsComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCancelSendNetBufferLists function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
