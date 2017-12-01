---
UID: NF.ndis.NdisMCoSendNetBufferListsComplete
title: NdisMCoSendNetBufferListsComplete
author: windows-driver-content
description: The NdisMCoSendNetBufferListsComplete function returns a linked list of NET_BUFFER_LIST structures to an overlying driver and returns the final status of a CoNDIS send request.
old-location: netvista\ndismcosendnetbufferlistscomplete.htm
old-project: netvista
ms.assetid: c4978122-6d13-4e9b-8eb7-d06cd7372268
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisMCoSendNetBufferListsComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCoSendNetBufferListsComplete
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_MCO_Function
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

# NdisMCoSendNetBufferListsComplete function



## -description
<p>The 
  <b>NdisMCoSendNetBufferListsComplete</b> function returns a linked list of 
  <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures to an overlying
  driver and returns the final status of a CoNDIS send request.</p>


## -syntax

````
VOID NdisMCoSendNetBufferListsComplete(
  _In_ NDIS_HANDLE      NdisVcHandle,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ ULONG            SendCompleteFlags
);
````


## -parameters
<dl>

### -param <i>NdisVcHandle</i> [in]

<dd>
<p>A handle that identifies a virtual connection (VC). The miniport driver obtained this handle as an
     input parameter to its 
     <a href="..\ndis\nc-ndis-miniport-co-create-vc.md">MiniportCoCreateVc</a> function, either
     when a client set up an outgoing call or when the call manager created a VC for a client-registered
     service access point (SAP) to indicate an incoming-call notification on.</p>
</dd>

### -param <i>NetBufferLists</i> [in]

<dd>
<p>A pointer to a linked list of 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures. The miniport
     driver received the NET_BUFFER_LIST structures in previous calls to its 
     <a href="..\ndis\nc-ndis-miniport-co-send-net-buffer-lists.md">
     MiniportCoSendNetBufferLists</a> function.</p>
</dd>

### -param <i>SendCompleteFlags</i> [in]

<dd>
<p>NDIS flags that can be combined with a bitwise OR operation. To clear all of the flags, set this
     parameter to zero. 
     <b>NdisMCoSendNetBufferListsComplete</b> supports the NDIS_SEND_COMPLETE_FLAGS_DISPATCH_LEVEL flag,
     which; if set, indicates that the current IRQL is DISPATCH_LEVEL. For more information about this flag,
     see 
     <a href="NULL">Dispatch IRQL Tracking</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A miniport driver calls 
    <b>NdisMCoSendNetBufferListsComplete</b> to complete send requests that NDIS made to the driver's 
    <a href="..\ndis\nc-ndis-miniport-co-send-net-buffer-lists.md">
    MiniportCoSendNetBufferLists</a> function. The miniport driver specifies a linked list of 
    <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures that are
    associated with the completed send requests.</p>

<p>While the status of the send requests is pending, the miniport driver retains ownership of the
    NET_BUFFER_LIST structures and all of the resources that are associated with the NET_BUFFER_LIST
    structures.</p>

<p>After a miniport driver calls 
    <b>NdisMCoSendNetBufferListsComplete</b>, NDIS returns the NET_BUFFER_LIST structures and associated data
    to the overlying driver that originated the send request.</p>

<p>The miniport driver can complete send requests in any order. For example, the miniport driver could
    concatenate the NET_BUFFER_LIST structure lists from multiple 
    <i>MiniportCoSendNetBufferLists</i> calls or split up a list from a 
    <i>MiniportCoSendNetBufferLists</i> call. However, the miniport driver must not modify the list of
    NET_BUFFER structures that are associated with a NET_BUFFER_LIST structure.</p>

<p>The miniport driver must set one of the following status codes in the 
    <b>Status</b> member of each NET_BUFFER_LIST structure that the 
    <i>NetBufferLists</i> parameter specifies:</p>

<p></p>

<p>All of the network data that is described by NET_BUFFER structures that are associated with this
      NET_BUFFER_LIST structure was successfully transmitted over the network.</p>

<p>The size of the data in some NET_BUFFER structures that are associated with this NET_BUFFER_LIST
      structure was too large for the underlying network interface card (NIC).</p>

<p>The send request for this NET_BUFFER_LIST structure failed because of insufficient
      resources.</p>

<p>NDIS called the 
      <a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a> function to
      cancel the send operation for this NET_BUFFER_LIST structure.</p>

<p>The miniport driver aborted the send request because of a reset.</p>

<p>The miniport driver failed the send request because of some reason other than those previously
      described. For example, the miniport driver can fail the send request due to a hardware failure.</p>

<p>A miniport driver's call to 
    <b>NdisMCoSendNetBufferListsComplete</b> does not necessarily indicate that the data for a send request
    has been transmitted over the network. For example, the data might be queued in the NIC hardware.</p>

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
<a href="devtest.ndis_irql_mco_function">Irql_MCO_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-co-create-vc.md">MiniportCoCreateVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-co-send-net-buffer-lists.md">
   MiniportCoSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCoSendNetBufferListsComplete function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
