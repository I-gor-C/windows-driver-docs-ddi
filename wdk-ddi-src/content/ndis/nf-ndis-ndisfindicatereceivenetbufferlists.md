---
UID: NF.ndis.NdisFIndicateReceiveNetBufferLists
title: NdisFIndicateReceiveNetBufferLists
author: windows-driver-content
description: A filter driver calls NdisFIndicateReceiveNetBufferLists to indicate that it has received network data. For more information, see Receiving Data in a Filter Driver.
old-location: netvista\ndisfindicatereceivenetbufferlists.htm
old-project: netvista
ms.assetid: ff2457bb-158a-411c-8c6b-7a7e402497ef
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisFIndicateReceiveNetBufferLists
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
req.alt-api: NdisFIndicateReceiveNetBufferLists
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
req.iface: 
---

# NdisFIndicateReceiveNetBufferLists function



## -description
<p>A filter driver calls 
  <b>NdisFIndicateReceiveNetBufferLists</b> to indicate that it has received network data. For more information, see <a href="NULL">Receiving Data in a Filter Driver</a>.</p>


## -syntax

````
VOID NdisFIndicateReceiveNetBufferLists(
  _In_ NDIS_HANDLE      NdisFilterHandle,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ NDIS_PORT_NUMBER PortNumber,
  _In_ ULONG            NumberOfNetBufferLists,
  _In_ ULONG            ReceiveFlags
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
<p>A linked list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures. Each
     <b>NET_BUFFER_LIST</b> structure contains one 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure.</p>
</dd>

### -param <i>PortNumber</i> [in]

<dd>
<p>A port number that identifies a miniport adapter port. Miniport adapter port numbers are assigned
     by calling the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a> function. A zero
     value identifies the default port of a miniport adapter.</p>
</dd>

### -param <i>NumberOfNetBufferLists</i> [in]

<dd>
<p>The number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that are in the linked list of structures at 
     <i>NetBufferLists</i> .</p>
</dd>

### -param <i>ReceiveFlags</i> [in]

<dd>
<p>Flags that define attributes for the receive indication. The flags can be combined with an OR
     operation. To clear all the flags, set this member to zero. This function supports the following flags:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_RECEIVE_FLAGS_DISPATCH_LEVEL"></a><a id="ndis_receive_flags_dispatch_level"></a>NDIS_RECEIVE_FLAGS_DISPATCH_LEVEL

<dd>
<p>Specifies that the current IRQL is <b>DISPATCH_LEVEL</b>. For more information about this flag, see 
       <a href="NULL">Dispatch IRQL Tracking</a>.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_RESOURCES"></a><a id="ndis_receive_flags_resources"></a>NDIS_RECEIVE_FLAGS_RESOURCES

<dd>
<p>Specifies that the filter driver reclaims ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures and any
       attached <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures immediately after the call to 
       <b>NdisFIndicateReceiveNetBufferLists</b> returns.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_SINGLE_ETHER_TYPE"></a><a id="ndis_receive_flags_single_ether_type"></a>NDIS_RECEIVE_FLAGS_SINGLE_ETHER_TYPE

<dd>
<p>Specifies that all the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> have the same protocol type (EtherType).</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_SINGLE_VLAN"></a><a id="ndis_receive_flags_single_vlan"></a>NDIS_RECEIVE_FLAGS_SINGLE_VLAN

<dd>
<p>Specifies that all the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> belong to the same VLAN.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_PERFECT_FILTERED"></a><a id="ndis_receive_flags_perfect_filtered"></a>NDIS_RECEIVE_FLAGS_PERFECT_FILTERED

<dd>
<p>Specifies that all the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> include only data that matches the packet filter and multicast address list that are
       assigned to the miniport adapter.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_SINGLE_QUEUE"></a><a id="ndis_receive_flags_single_queue"></a>NDIS_RECEIVE_FLAGS_SINGLE_QUEUE

<dd>
<p>Specifies that all the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> belong to the same VM queue. A miniport driver must set this flag for all receive
       indications on a queue if the <b>NDIS_RECEIVE_QUEUE_PARAMETERS_PER_QUEUE_RECEIVE_INDICATION</b> flag was set
       in the 
       <b>Flags</b> member of the 
       <a href="..\ntddndis\ns-ntddndis--ndis-receive-queue-parameters.md">
       NDIS_RECEIVE_QUEUE_PARAMETERS</a> structure when that queue was allocated.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_SHARED_MEMORY_INFO_VALID"></a><a id="ndis_receive_flags_shared_memory_info_valid"></a>NDIS_RECEIVE_FLAGS_SHARED_MEMORY_INFO_VALID

<dd>
<p>Specifies that all the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> contain shared memory information that is valid. When this flag is set on a
       received <b>NET_BUFFER_LIST</b>, NDIS treats the shared memory information as valid. When this flag is not
       set, NDIS and drivers ignore the shared memory information. For example, intermediate drivers that
       modify packet data can use this flag to determine if data should be copied. Miniport drivers can use
       the flag to determine how to free the memory that is associated with a VM queue when a queue is
       deleted.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_MORE_NBLS"></a><a id="ndis_receive_flags_more_nbls"></a>NDIS_RECEIVE_FLAGS_MORE_NBLS

<dd>
<p>Reserved.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_SWITCH_SINGLE_SOURCE"></a><a id="ndis_receive_flags_switch_single_source"></a>NDIS_RECEIVE_FLAGS_SWITCH_SINGLE_SOURCE

<dd>
<p>If this flag is set, all packets in a linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures originated from the same Hyper-V extensible switch source port.</p>
<p>For more information, see <a href="NULL">Hyper-V Extensible Switch Send and Receive Flags</a>.</p>
<div class="alert"><b>Note</b>  If each packet in the linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures uses the same source port, the extension should set the <b>NDIS_RETURN_FLAGS_SWITCH_SINGLE_SOURCE</b> flag in the <i>ReturnFlags</i> parameter of <a href="..\ndis\nc-ndis-filter-return-net-buffer-lists.md">FilterReturnNetBufferLists</a>  when the receive request completes. The extension must set this flag in the <i>ReturnFlags</i> parameter if it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff562613">NdisFReturnNetBufferLists</a> to return packets that it did not originate or clone.</div>
<div> </div>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_SWITCH_DESTINATION_GROUP"></a><a id="ndis_receive_flags_switch_destination_group"></a>NDIS_RECEIVE_FLAGS_SWITCH_DESTINATION_GROUP

<dd>
<p>If this flag is set, all packets in a linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures are to be forwarded to the same extensible switch destination port.</p>
<p>For more information, see <a href="NULL">Hyper-V Extensible Switch Send and Receive Flags</a>.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When a filter driver calls the 
    <b>NdisFIndicateReceiveNetBufferLists</b> function, it specifies a list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures in the 
    <i>NetBufferLists</i> parameter. NDIS passes the <b>NET_BUFFER_LIST</b> structures to the overlying drivers.</p>

<p>Filter drivers can call 
    <b>NdisFIndicateReceiveNetBufferLists</b> to originate a receive indication.</p>

<p>Filter drivers can also filter receive indications that are originated by underlying drivers. NDIS
    calls the 
    <a href="..\ndis\nc-ndis-filter-receive-net-buffer-lists.md">
    FilterReceiveNetBufferLists</a> function to filter such receive indications.</p>

<p>A filter driver must set the 
    <b>SourceHandle</b> member of each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that it originates to the same value as the 
    <i>NdisFilterHandle</i> parameter. The filter driver must not modify the 
    <b>SourceHandle</b> member in any <b>NET_BUFFER_LIST</b> structures that it did not originate.</p>

<p>The filter driver must properly initialize the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures, attached 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures, and any attached MDLs.</p>

<p>If a filter driver calls the 
    <b>NdisFIndicateReceiveNetBufferLists</b> function and clears the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter, NDIS returns the indicated <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to the filter
    driver's 
    <a href="..\ndis\nc-ndis-filter-return-net-buffer-lists.md">
    FilterReturnNetBufferLists</a> function. In this case, the filter driver must not reclaim the
    <b>NET_BUFFER_LIST</b> structures until NDIS returns the <b>NET_BUFFER_LIST</b> structures to 
    <i>FilterReturnNetBufferLists</i>.</p>

<p>If a filter driver calls 
    <b>NdisFIndicateReceiveNetBufferLists</b> and sets the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter, this indicates that the filter driver must regain ownership of the
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures immediately. In this case, NDIS does not call the filter driver's 
    <a href="..\ndis\nc-ndis-filter-return-net-buffer-lists.md">FilterReturnNetBufferLists</a> function to return the <b>NET_BUFFER_LIST</b> structures. Instead, NDIS returns
    the <b>NET_BUFFER_LIST</b> structures to the filter driver upon return from 
    <b>NdisFIndicateReceiveNetBufferLists</b>. The filter driver should reclaim the <b>NET_BUFFER_LIST</b>
    structures immediately after 
    <b>NdisFIndicateReceiveNetBufferLists</b> returns. To reclaim the <b>NET_BUFFER_LIST</b> structures, a filter
    driver can call its own 
    <i>FilterReturnNetBufferLists</i> function.</p>

<p>Setting the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter forces the overlying drivers to copy the network data and release the
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to the filter driver.</p>

<p>When a filter driver calls the 
    <b>NdisFIndicateReceiveNetBufferLists</b> function, it specifies a list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures in the 
    <i>NetBufferLists</i> parameter. NDIS passes the <b>NET_BUFFER_LIST</b> structures to the overlying drivers.</p>

<p>Filter drivers can call 
    <b>NdisFIndicateReceiveNetBufferLists</b> to originate a receive indication.</p>

<p>Filter drivers can also filter receive indications that are originated by underlying drivers. NDIS
    calls the 
    <a href="..\ndis\nc-ndis-filter-receive-net-buffer-lists.md">
    FilterReceiveNetBufferLists</a> function to filter such receive indications.</p>

<p>A filter driver must set the 
    <b>SourceHandle</b> member of each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that it originates to the same value as the 
    <i>NdisFilterHandle</i> parameter. The filter driver must not modify the 
    <b>SourceHandle</b> member in any <b>NET_BUFFER_LIST</b> structures that it did not originate.</p>

<p>The filter driver must properly initialize the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures, attached 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures, and any attached MDLs.</p>

<p>If a filter driver calls the 
    <b>NdisFIndicateReceiveNetBufferLists</b> function and clears the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter, NDIS returns the indicated <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to the filter
    driver's 
    <a href="..\ndis\nc-ndis-filter-return-net-buffer-lists.md">
    FilterReturnNetBufferLists</a> function. In this case, the filter driver must not reclaim the
    <b>NET_BUFFER_LIST</b> structures until NDIS returns the <b>NET_BUFFER_LIST</b> structures to 
    <i>FilterReturnNetBufferLists</i>.</p>

<p>If a filter driver calls 
    <b>NdisFIndicateReceiveNetBufferLists</b> and sets the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter, this indicates that the filter driver must regain ownership of the
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures immediately. In this case, NDIS does not call the filter driver's 
    <a href="..\ndis\nc-ndis-filter-return-net-buffer-lists.md">FilterReturnNetBufferLists</a> function to return the <b>NET_BUFFER_LIST</b> structures. Instead, NDIS returns
    the <b>NET_BUFFER_LIST</b> structures to the filter driver upon return from 
    <b>NdisFIndicateReceiveNetBufferLists</b>. The filter driver should reclaim the <b>NET_BUFFER_LIST</b>
    structures immediately after 
    <b>NdisFIndicateReceiveNetBufferLists</b> returns. To reclaim the <b>NET_BUFFER_LIST</b> structures, a filter
    driver can call its own 
    <i>FilterReturnNetBufferLists</i> function.</p>

<p>Setting the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter forces the overlying drivers to copy the network data and release the
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to the filter driver.</p>

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
<a href="..\ndis\nc-ndis-filter-receive-net-buffer-lists.md">FilterReceiveNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-return-net-buffer-lists.md">FilterReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567211">NDIS_RECEIVE_QUEUE_PARAMETERS</a>
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
<a href="NULL">Receiving Data in a Filter Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFIndicateReceiveNetBufferLists function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
