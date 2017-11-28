---
UID: NF.ndis.NdisMSendNetBufferListsComplete
title: NdisMSendNetBufferListsComplete
author: windows-driver-content
description: Miniport drivers call the NdisMSendNetBufferListsComplete function to return a linked list of NET_BUFFER_LIST structures to an overlying driver and to return the final status of a send request.
old-location: netvista\ndismsendnetbufferlistscomplete.htm
old-project: netvista
ms.assetid: 33890582-5eba-4cc1-a0d9-ec07f18da453
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMSendNetBufferListsComplete
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
req.alt-api: NdisMSendNetBufferListsComplete
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_SendRcv_Function, NdisTimedDataHang, NdisTimedDataSend
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

# NdisMSendNetBufferListsComplete function



## -description
<p>Miniport drivers call the 
  <b>NdisMSendNetBufferListsComplete</b> function to return a linked list of 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to an overlying
  driver and to return the final status of a send request.</p>


## -syntax

````
VOID NdisMSendNetBufferListsComplete(
  _In_ NDIS_HANDLE      MiniportAdapterHandle,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ ULONG            SendCompleteFlags
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The miniport handle that NDIS passed to the 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param <i>NetBufferLists</i> [in]

<dd>
<p>A pointer to a linked list of NET_BUFFER_LIST structures. The miniport driver received the
     NET_BUFFER_LIST structures in previous calls to its 
     <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
     MiniportSendNetBufferLists</a> function.</p>
</dd>

### -param <i>SendCompleteFlags</i> [in]

<dd>
<p>NDIS flags that can be combined with an OR operation. To clear all the flags, set this member to
     zero. This function supports the NDIS_SEND_COMPLETE_FLAGS_DISPATCH_LEVEL flag which; if set, indicates
     that the current IRQL is DISPATCH_LEVEL. For more information about this flag, see 
     <a href="NULL">Dispatch IRQL Tracking</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A miniport driver calls 
    <b>NdisMSendNetBufferListsComplete</b> to complete send requests that NDIS made to the driver's 
    <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
    MiniportSendNetBufferLists</a> function. The miniport driver specifies a linked list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that are
    associated with the completed send requests. While the status of the send requests is pending, the
    miniport driver retains ownership of the NET_BUFFER_LIST structures and all the protocol-allocated
    resources that are associated with the NET_BUFFER_LIST structures.</p>

<p>After a miniport driver calls 
    <b>NdisMSendNetBufferListsComplete</b>, NDIS calls the 
    <a href="..\ndis\nc-ndis-protocol-send-net-buffer-lists-complete.md">
    ProtocolSendNetBufferListsComplete</a> function of the driver that called the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564535">NdisSendNetBufferLists</a> function to
    initiate the send request.</p>

<p>The miniport driver can complete send requests in any order. For example, the miniport driver could
    concatenate the NET_BUFFER_LIST structure lists from multiple 
    <i>MiniportSendNetBufferLists</i> calls or split up a list from a 
    <i>MiniportSendNetBufferLists</i> call. However, the miniport driver must not modify the list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures that are associated with a
    NET_BUFFER_LIST structure.</p>

<p>The miniport driver must set one of the following status codes in the 
    <b>Status</b> member of each NET_BUFFER_LIST structure that the 
    <i>NetBufferLists</i> parameter specifies:</p>

<p></p><dl>
<dt><a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS</dt>
<dd>
<p>All the network data that the NET_BUFFER_LIST structure and the associated NET_BUFFER structures
      describe was successfully processed for transmission. For example, the miniport driver copied the data
      to a queue or the data has already been transmitted.</p>
</dd>
<dt><a id="NDIS_STATUS_INVALID_LENGTH"></a><a id="ndis_status_invalid_length"></a>NDIS_STATUS_INVALID_LENGTH</dt>
<dd>
<p>The size of the data in some NET_BUFFER structures associated with this NET_BUFFER_LIST structure
      was too large for the underlying NIC.</p>
</dd>
<dt><a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES</dt>
<dd>
<p>The send request for this NET_BUFFER_LIST structure failed due to insufficient resources.</p>
</dd>
<dt><a id="NDIS_STATUS_PAUSED"></a><a id="ndis_status_paused"></a>NDIS_STATUS_PAUSED</dt>
<dd>
<p>The miniport adapter is in the 
      <i>Paused</i> state, as described on the reference page for the 
      <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function.</p>
</dd>
<dt><a id="NDIS_STATUS_SEND_ABORTED"></a><a id="ndis_status_send_aborted"></a>NDIS_STATUS_SEND_ABORTED</dt>
<dd>
<p>NDIS called the 
      <a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a> function to
      cancel the send operation for this NET_BUFFER_LIST structure.</p>
</dd>
<dt><a id="NDIS_STATUS_RESET_IN_PROGRESS"></a><a id="ndis_status_reset_in_progress"></a>NDIS_STATUS_RESET_IN_PROGRESS</dt>
<dd>
<p>The miniport driver aborted the send request due to a reset.</p>
</dd>
<dt><a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE</dt>
<dd>
<p>The miniport driver failed the send request because of some reason other than those previously
      described. For example, the miniport driver can fail the send request due to a hardware failure.</p>
</dd>
</dl><p>All the network data that the NET_BUFFER_LIST structure and the associated NET_BUFFER structures
      describe was successfully processed for transmission. For example, the miniport driver copied the data
      to a queue or the data has already been transmitted.</p>

<p>The size of the data in some NET_BUFFER structures associated with this NET_BUFFER_LIST structure
      was too large for the underlying NIC.</p>

<p>The send request for this NET_BUFFER_LIST structure failed due to insufficient resources.</p>

<p>The miniport adapter is in the 
      <i>Paused</i> state, as described on the reference page for the 
      <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function.</p>

<p>NDIS called the 
      <a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a> function to
      cancel the send operation for this NET_BUFFER_LIST structure.</p>

<p>The miniport driver aborted the send request due to a reset.</p>

<p>The miniport driver failed the send request because of some reason other than those previously
      described. For example, the miniport driver can fail the send request due to a hardware failure.</p>

<p>A miniport driver's call to 
    <b>NdisMSendNetBufferListsComplete</b> does not necessarily mean that the data for a send request has been
    transmitted over the network. The data might be queued in the NIC hardware.</p>

<p>A miniport driver calls 
    <b>NdisMSendNetBufferListsComplete</b> to complete send requests that NDIS made to the driver's 
    <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
    MiniportSendNetBufferLists</a> function. The miniport driver specifies a linked list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that are
    associated with the completed send requests. While the status of the send requests is pending, the
    miniport driver retains ownership of the NET_BUFFER_LIST structures and all the protocol-allocated
    resources that are associated with the NET_BUFFER_LIST structures.</p>

<p>After a miniport driver calls 
    <b>NdisMSendNetBufferListsComplete</b>, NDIS calls the 
    <a href="..\ndis\nc-ndis-protocol-send-net-buffer-lists-complete.md">
    ProtocolSendNetBufferListsComplete</a> function of the driver that called the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564535">NdisSendNetBufferLists</a> function to
    initiate the send request.</p>

<p>The miniport driver can complete send requests in any order. For example, the miniport driver could
    concatenate the NET_BUFFER_LIST structure lists from multiple 
    <i>MiniportSendNetBufferLists</i> calls or split up a list from a 
    <i>MiniportSendNetBufferLists</i> call. However, the miniport driver must not modify the list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures that are associated with a
    NET_BUFFER_LIST structure.</p>

<p>The miniport driver must set one of the following status codes in the 
    <b>Status</b> member of each NET_BUFFER_LIST structure that the 
    <i>NetBufferLists</i> parameter specifies:</p>

<p></p><dl>
<dt><a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS</dt>
<dd>
<p>All the network data that the NET_BUFFER_LIST structure and the associated NET_BUFFER structures
      describe was successfully processed for transmission. For example, the miniport driver copied the data
      to a queue or the data has already been transmitted.</p>
</dd>
<dt><a id="NDIS_STATUS_INVALID_LENGTH"></a><a id="ndis_status_invalid_length"></a>NDIS_STATUS_INVALID_LENGTH</dt>
<dd>
<p>The size of the data in some NET_BUFFER structures associated with this NET_BUFFER_LIST structure
      was too large for the underlying NIC.</p>
</dd>
<dt><a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES</dt>
<dd>
<p>The send request for this NET_BUFFER_LIST structure failed due to insufficient resources.</p>
</dd>
<dt><a id="NDIS_STATUS_PAUSED"></a><a id="ndis_status_paused"></a>NDIS_STATUS_PAUSED</dt>
<dd>
<p>The miniport adapter is in the 
      <i>Paused</i> state, as described on the reference page for the 
      <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function.</p>
</dd>
<dt><a id="NDIS_STATUS_SEND_ABORTED"></a><a id="ndis_status_send_aborted"></a>NDIS_STATUS_SEND_ABORTED</dt>
<dd>
<p>NDIS called the 
      <a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a> function to
      cancel the send operation for this NET_BUFFER_LIST structure.</p>
</dd>
<dt><a id="NDIS_STATUS_RESET_IN_PROGRESS"></a><a id="ndis_status_reset_in_progress"></a>NDIS_STATUS_RESET_IN_PROGRESS</dt>
<dd>
<p>The miniport driver aborted the send request due to a reset.</p>
</dd>
<dt><a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE</dt>
<dd>
<p>The miniport driver failed the send request because of some reason other than those previously
      described. For example, the miniport driver can fail the send request due to a hardware failure.</p>
</dd>
</dl><p>All the network data that the NET_BUFFER_LIST structure and the associated NET_BUFFER structures
      describe was successfully processed for transmission. For example, the miniport driver copied the data
      to a queue or the data has already been transmitted.</p>

<p>The size of the data in some NET_BUFFER structures associated with this NET_BUFFER_LIST structure
      was too large for the underlying NIC.</p>

<p>The send request for this NET_BUFFER_LIST structure failed due to insufficient resources.</p>

<p>The miniport adapter is in the 
      <i>Paused</i> state, as described on the reference page for the 
      <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function.</p>

<p>NDIS called the 
      <a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a> function to
      cancel the send operation for this NET_BUFFER_LIST structure.</p>

<p>The miniport driver aborted the send request due to a reset.</p>

<p>The miniport driver failed the send request because of some reason other than those previously
      described. For example, the miniport driver can fail the send request due to a hardware failure.</p>

<p>A miniport driver's call to 
    <b>NdisMSendNetBufferListsComplete</b> does not necessarily mean that the data for a send request has been
    transmitted over the network. The data might be queued in the NIC hardware.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548004">Irql_SendRcv_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305118">NdisTimedDataHang</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305119">NdisTimedDataSend</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">MiniportSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564535">NdisSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMSendNetBufferListsComplete function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
