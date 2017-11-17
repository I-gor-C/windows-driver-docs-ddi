---
UID: NF.ndis.NdisFSendNetBufferLists
title: NdisFSendNetBufferLists
author: windows-driver-content
description: Filter drivers call the NdisFSendNetBufferLists function to send a list of network data buffers.
old-location: netvista\ndisfsendnetbufferlists.htm
ms.assetid: fe0896ab-2d20-465f-a8bc-bfc0033701d6
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFSendNetBufferLists
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Filter_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisFSendNetBufferLists
req.iface: 
---

# NdisFSendNetBufferLists function



## -description
<p>Filter drivers call the 
  <b>NdisFSendNetBufferLists</b> function to send a list of network data buffers.</p>


## -syntax

````
VOID NdisFSendNetBufferLists(
  _In_ NDIS_HANDLE      NdisFilterHandle,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ NDIS_PORT_NUMBER PortNumber,
  _In_ ULONG            SendFlags
);
````


## -parameters
<dl>

### -param <i>NdisFilterHandle</i> [in]

<dd>
<p>The NDIS handle that identifies this filter module. NDIS passed the handle to the filter driver in
     a call to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>
</dd>

### -param <i>NetBufferLists</i> [in]

<dd>
<p>A pointer to a linked list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures. Each
     <b>NET_BUFFER_LIST</b> structure describes a list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures.</p>
</dd>

### -param <i>PortNumber</i> [in]

<dd>
<p>A port number that identifies a miniport adapter port. Miniport adapter port numbers are assigned
     by calling the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a> function. A zero
     value identifies the default port of a miniport adapter.</p>
</dd>

### -param <i>SendFlags</i> [in]

<dd>
<p>Flags that define attributes for the send operation. The flags can be combined with an OR
     operation. To clear all the flags, set this member to zero. This function supports the following flags:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_SEND_FLAGS_DISPATCH_LEVEL"></a><a id="ndis_send_flags_dispatch_level"></a>NDIS_SEND_FLAGS_DISPATCH_LEVEL

<dd>
<p>Specifies that the current IRQL is DISPATCH_LEVEL. For more information about this flag, see 
       <a href="NULL">Dispatch IRQL Tracking</a>.</p>
</dd>

### -param <a id="NDIS_SEND_FLAGS_CHECK_FOR_LOOPBACK"></a><a id="ndis_send_flags_check_for_loopback"></a>NDIS_SEND_FLAGS_CHECK_FOR_LOOPBACK

<dd>
<p>Specifies that NDIS should check for loopback. By default, NDIS does not loop back data to the
       driver that submitted the send request. An overlying driver can override this behavior by setting this
       flag. When this flag is set, NDIS identifies all the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures that contain data that
       matches the receive criteria for the binding. NDIS indicates NET_BUFFER structures that match the
       criteria to the overlying driver. This flag has no affect on checking for loopback, or looping back,
       on other bindings.</p>
</dd>

### -param <a id="NDIS_SEND_FLAGS_SWITCH_SINGLE_SOURCE"></a><a id="ndis_send_flags_switch_single_source"></a>NDIS_SEND_FLAGS_SWITCH_SINGLE_SOURCE

<dd>
<p>If this flag is set, all packets in a linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures originated from the same Hyper-V extensible switch source port.</p>
<p>For more information, see <a href="NULL">Hyper-V Extensible Switch Send and Receive Flags</a>.</p>
<div class="alert"><b>Note</b>  If each packet in the linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures uses the same source port, the extension should set the <b>NDIS_SEND_COMPLETE_FLAGS_SWITCH_SINGLE_SOURCE</b> flag in the <i>SendCompleteFlags</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> when it completes the send request.</div>
<div> </div>
<div class="alert"><b>Note</b>  This flag is available in NDIS 6.30 and later.</div>
<div> </div>
</dd>

### -param <a id="NDIS_SEND_FLAGS_SWITCH_DESTINATION_GROUP"></a><a id="ndis_send_flags_switch_destination_group"></a>NDIS_SEND_FLAGS_SWITCH_DESTINATION_GROUP

<dd>
<p>If this flag is set, all packets in a linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures are to be forwarded to the same extensible switch destination port.</p>
<p>For more information, see <a href="NULL">Hyper-V Extensible Switch Send and Receive Flags</a>.</p>
<div class="alert"><b>Note</b>  This flag is available in NDIS 6.30 and later.</div>
<div> </div>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>After a filter driver calls the 
    <b>NdisFSendNetBufferLists</b> function, NDIS submits the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to the underlying
    drivers.</p>

<p>A filter driver can originate send requests or it can filter the requests that it receives from
    overlying drivers. If the filter driver originates send requests, the driver must allocate buffers pools.
    The filter driver allocates each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure from a pool.</p>

<p>The filter driver can preallocate <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures or it can allocate the structures just
    before calling 
    <b>NdisFSendNetBufferLists</b> and then free them when the send operation is complete.</p>

<p>A filter driver must set the 
    <b>SourceHandle</b> member of each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that it originates to the same value that it
    passes to the 
    <i>NdisFilterHandle</i> parameter. The filter handle provides the information that NDIS requires to return
    the <b>NET_BUFFER_LIST</b> structure to the filter driver. The filter driver must not modify the 
    <b>SourceHandle</b> member in any <b>NET_BUFFER_LIST</b> structures that it did not originate.</p>

<p>Before calling 
    <b>NdisFSendNetBufferLists</b>, a filter driver can set information that accompanies the send request
    with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro. The
    underlying drivers can retrieve this information with the <b>NET_BUFFER_LIST_INFO</b> macro.</p>

<p>NDIS calls a filter driver's 
    <a href="https://msdn.microsoft.com/1b3fc0c8-95da-47e5-8ff1-b7967f5148e7">
    FilterSendNetBufferLists</a> function to pass on send requests from overlying drivers. A filter driver
    can pass on such requests by passing the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>T structures that it received in 
    <i>FilterSendNetBufferLists</i> to 
    <b>NdisFSendNetBufferLists</b>.</p>

<p>As soon as a filter driver calls the 
    <b>NdisFSendNetBufferLists</b> function, it relinquishes ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures and
    all associated resources. NDIS calls the 
    <a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">
    FilterSendNetBufferListsComplete</a> function to return the structures and data to the filter driver.
    NDIS can collect the structures and data from multiple send requests into a single linked list of
    <b>NET_BUFFER_LIST</b> structures before it passes the list to 
    <i>FilterSendNetBufferListsComplete</i>.</p>

<p>Until NDIS calls 
    <a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">FilterSendNetBufferListsComplete</a>, the current status of the send request is not available to the
    filter driver. A filter driver temporarily releases ownership of all resources that are associated with a
    send request when it calls 
    <b>NdisFSendNetBufferLists</b>. A filter driver should never try to examine the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
    structures or any associated data after calling 
    <b>NdisFSendNetBufferLists</b>.</p>

<p>After a filter driver calls the 
    <b>NdisFSendNetBufferLists</b> function, NDIS submits the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to the underlying
    drivers.</p>

<p>A filter driver can originate send requests or it can filter the requests that it receives from
    overlying drivers. If the filter driver originates send requests, the driver must allocate buffers pools.
    The filter driver allocates each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure from a pool.</p>

<p>The filter driver can preallocate <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures or it can allocate the structures just
    before calling 
    <b>NdisFSendNetBufferLists</b> and then free them when the send operation is complete.</p>

<p>A filter driver must set the 
    <b>SourceHandle</b> member of each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that it originates to the same value that it
    passes to the 
    <i>NdisFilterHandle</i> parameter. The filter handle provides the information that NDIS requires to return
    the <b>NET_BUFFER_LIST</b> structure to the filter driver. The filter driver must not modify the 
    <b>SourceHandle</b> member in any <b>NET_BUFFER_LIST</b> structures that it did not originate.</p>

<p>Before calling 
    <b>NdisFSendNetBufferLists</b>, a filter driver can set information that accompanies the send request
    with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro. The
    underlying drivers can retrieve this information with the <b>NET_BUFFER_LIST_INFO</b> macro.</p>

<p>NDIS calls a filter driver's 
    <a href="https://msdn.microsoft.com/1b3fc0c8-95da-47e5-8ff1-b7967f5148e7">
    FilterSendNetBufferLists</a> function to pass on send requests from overlying drivers. A filter driver
    can pass on such requests by passing the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>T structures that it received in 
    <i>FilterSendNetBufferLists</i> to 
    <b>NdisFSendNetBufferLists</b>.</p>

<p>As soon as a filter driver calls the 
    <b>NdisFSendNetBufferLists</b> function, it relinquishes ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures and
    all associated resources. NDIS calls the 
    <a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">
    FilterSendNetBufferListsComplete</a> function to return the structures and data to the filter driver.
    NDIS can collect the structures and data from multiple send requests into a single linked list of
    <b>NET_BUFFER_LIST</b> structures before it passes the list to 
    <i>FilterSendNetBufferListsComplete</i>.</p>

<p>Until NDIS calls 
    <a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">FilterSendNetBufferListsComplete</a>, the current status of the send request is not available to the
    filter driver. A filter driver temporarily releases ownership of all resources that are associated with a
    send request when it calls 
    <b>NdisFSendNetBufferLists</b>. A filter driver should never try to examine the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
    structures or any associated data after calling 
    <b>NdisFSendNetBufferLists</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547930">Irql_Filter_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1b3fc0c8-95da-47e5-8ff1-b7967f5148e7">FilterSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">
   FilterSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFSendNetBufferLists function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
