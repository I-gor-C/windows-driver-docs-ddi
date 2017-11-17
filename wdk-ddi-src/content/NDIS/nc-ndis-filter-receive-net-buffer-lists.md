---
UID: NC.ndis.FILTER_RECEIVE_NET_BUFFER_LISTS
title: FILTER_RECEIVE_NET_BUFFER_LISTS
author: windows-driver-content
description: NDIS calls the FilterReceiveNetBufferLists function to request a filter driver to process a receive indication.Note  You must declare the function by using the FILTER_RECEIVE_NET_BUFFER_LISTS type.
old-location: netvista\filterreceivenetbufferlists.htm
ms.assetid: 6359c2a7-1208-41ea-bbf9-015c91b6e8f6
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FilterReceiveNetBufferLists
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# FILTER_RECEIVE_NET_BUFFER_LISTS callback



## -description
<p>NDIS calls the 
  <i>FilterReceiveNetBufferLists</i> function to request a filter driver to process a receive
  indication.</p>


## -prototype

````
FILTER_RECEIVE_NET_BUFFER_LISTS FilterReceiveNetBufferLists;

VOID FilterReceiveNetBufferLists(
  _In_ NDIS_HANDLE      FilterModuleContext,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ NDIS_PORT_NUMBER PortNumber,
  _In_ ULONG            NumberOfNetBufferLists,
  _In_ ULONG            ReceiveFlags
)
{ ... }
````


## -parameters
<dl>

### -param <i>FilterModuleContext</i> [in]

<dd>
<p>A handle to the context area for the filter module. The filter driver created and initialized this
     context area in the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>
</dd>

### -param <i>NetBufferLists</i> [in]

<dd>
<p>A linked list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that were
     allocated by underlying drivers. Each <b>NET_BUFFER_LIST</b> structure contains one 
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
<p>Specifies that the current IRQL is DISPATCH_LEVEL. For more information about this flag, see 
       <a href="NULL">Dispatch IRQL Tracking</a>.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_RESOURCES"></a><a id="ndis_receive_flags_resources"></a>NDIS_RECEIVE_FLAGS_RESOURCES

<dd>
<p>Specifies that NDIS reclaims ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures and any attached
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures immediately after the call to 
       <i>FilterReceiveNetBufferLists</i> returns.</p>
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
       indications on a queue if the NDIS_RECEIVE_QUEUE_PARAMETERS_PER_QUEUE_RECEIVE_INDICATION flag was set
       in the 
       <b>Flags</b> member of the 
       <a href="https://msdn.microsoft.com/fba87554-766d-45e2-8257-584ee78dd873">
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
<div class="alert"><b>Note</b>  If each packet in the linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures uses the same source port, the extension should set the <b>NDIS_RETURN_FLAGS_SWITCH_SINGLE_SOURCE</b> flag in the <i>ReturnFlags</i> parameter of <a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">FilterReturnNetBufferLists</a>  when the receive request completes. The extension must set this flag in the <i>ReturnFlags</i> parameter if it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff562613">NdisFReturnNetBufferLists</a> to return packets that it did not originate or clone.</div>
<div> </div>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_SWITCH_DESTINATION_GROUP"></a><a id="ndis_receive_flags_switch_destination_group"></a>NDIS_RECEIVE_FLAGS_SWITCH_DESTINATION_GROUP

<dd>
<p>If this flag is set, all packets in a linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures are to be forwarded to the same extensible switch destination port.</p>
<p>For more information, see <a href="NULL">Hyper-V Extensible Switch Send and Receive Flags</a>.</p>
<div class="alert"><b>Note</b>  If each packet in the linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures uses the same destination ports, the extension should set the <b>NDIS_RECEIVE_FLAGS_SWITCH_DESTINATION_GROUP</b> flag in the <i>ReturnFlags</i> parameter of <a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">FilterReturnNetBufferLists</a>  when the receive request completes. The extension must set this flag in the <i>ReturnFlags</i> parameter if it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff562613">NdisFReturnNetBufferLists</a> to return packets that it did not originate or clone.</div>
<div> </div>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><i>FilterReceiveNetBufferLists</i> is an optional function. If a filter driver does not filter receive
    indications, it can set the entry point for this function to <b>NULL</b> when it calls the 
    <a href="https://msdn.microsoft.com/14381de2-36d9-4ec8-9d4e-7af3e6d8ecf3">
    NdisFRegisterFilterDriver</a> function.</p>

<p>The filter driver can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function,
    from the 
    <a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">FilterSetModuleOptions</a> function,
    to specify a 
    <i>FilterReceiveNetBufferLists</i> function for a filter module.</p>

<p>NDIS calls 
    <i>FilterReceiveNetBufferLists</i> to process receive indications that are initiated by underlying
    drivers. NDIS can also call this function as a result of loopback.</p>

<p>If the filter driver did not specify a 
    <i>FilterReceiveNetBufferLists</i> function, NDIS calls the next higher filter driver in the stack that did specify a 
    <i>FilterReceiveNetBufferLists</i> function. If there is no such filter driver, NDIS calls an overlying
    driver's 
    <a href="https://msdn.microsoft.com/c964b4b8-ab07-4a07-9965-5cc06c028c20">
    ProtocolReceiveNetBufferLists</a> function.</p>

<p>If the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter is not set, the filter driver retains ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
    structures until it calls the 
    <a href="https://msdn.microsoft.com/083cf25d-7436-4c4e-b29a-c9a2702b136d">
    NdisFReturnNetBufferLists</a> function.</p>

<p>If the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter is set, the filter driver cannot keep the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure and
    associated underlying-driver-allocated resources. This flag can indicate that the underlying driver is
    running low on receive resources. The 
    <i>FilterReceiveNetBufferLists</i> function should return as quickly as possible. Before returning, the 
    <i>FilterReceiveNetBufferLists</i> function can copy the received data into filter-driver-allocated
    storage or pass the buffer on by calling the 
    <a href="https://msdn.microsoft.com/ff2457bb-158a-411c-8c6b-7a7e402497ef">
    NdisFIndicateReceiveNetBufferLists</a> function.</p>

<p>Filter drivers can filter received data before indicating the data to overlying drivers. For each
    buffer that is submitted to its 
    <i>FilterReceiveNetBufferLists</i> function, a filter driver can do the following:</p>

<p>Pass the buffer on to the next overlying driver by calling the 
      <a href="https://msdn.microsoft.com/ff2457bb-158a-411c-8c6b-7a7e402497ef">
      NdisFIndicateReceiveNetBufferLists</a> function.</p>

<p>The driver can modify the contents of the buffer before calling 
      <b>NdisFIndicateReceiveNetBufferLists</b>.</p>

<p>The driver can change the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag setting that NDIS passed to 
      <i>FilterReceiveNetBufferLists</i> or simply pass it on to 
      <b>NdisFIndicateReceiveNetBufferLists</b>.</p>

<p>Discard the buffer. If NDIS cleared the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag, call the 
      <b>NdisFReturnNetBufferLists</b> function to discard the buffer. If NDIS set the
      <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag, take no action and return from 
      <i>FilterReceiveNetBufferLists</i> to discard the buffer.</p>

<p>Queue the buffer in a local data structure for later processing. If NDIS set the
      <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag of 
      <i>FilterReceiveNetBufferLists</i>, the filter driver must create a copy before returning from 
      <i>FilterReceiveNetBufferLists</i>.</p>

<p>Copy the buffer and originate a receive indication with the copy. The receive indication is similar
      to a filter-driver-initiated receive indication. In this case, the driver must return the original
      buffer to the underlying driver.</p>

<p>If the filter driver called 
    <b>NdisFIndicateReceiveNetBufferLists</b> and did not set the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag, NDIS
    calls the 
    <a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">
    FilterReturnNetBufferLists</a> function for the filter module. In its 
    <i>FilterReturnNetBufferLists</i> function, the filter driver will undo the operations that it performed
    on the buffer on the receive indication path.</p>

<p>If a filter module is in the 
    <i>Paused</i> state, the filter driver must not originate any receive indications for that filter module.
    The filter driver must not pass buffers that it created to 
    <b>NdisFIndicateReceiveNetBufferLists</b>. However, the driver can pass on a receive indication from an
    underlying driver.</p>

<p>NDIS calls 
    <i>FilterReceiveNetBufferLists</i> at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>FilterReceiveNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterReceiveNetBufferLists</i> function that is named "MyReceiveNetBufferLists", use the <b>FILTER_RECEIVE_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_RECEIVE_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_RECEIVE_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>FilterReceiveNetBufferLists</i> is an optional function. If a filter driver does not filter receive
    indications, it can set the entry point for this function to <b>NULL</b> when it calls the 
    <a href="https://msdn.microsoft.com/14381de2-36d9-4ec8-9d4e-7af3e6d8ecf3">
    NdisFRegisterFilterDriver</a> function.</p>

<p>The filter driver can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function,
    from the 
    <a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">FilterSetModuleOptions</a> function,
    to specify a 
    <i>FilterReceiveNetBufferLists</i> function for a filter module.</p>

<p>NDIS calls 
    <i>FilterReceiveNetBufferLists</i> to process receive indications that are initiated by underlying
    drivers. NDIS can also call this function as a result of loopback.</p>

<p>If the filter driver did not specify a 
    <i>FilterReceiveNetBufferLists</i> function, NDIS calls the next higher filter driver in the stack that did specify a 
    <i>FilterReceiveNetBufferLists</i> function. If there is no such filter driver, NDIS calls an overlying
    driver's 
    <a href="https://msdn.microsoft.com/c964b4b8-ab07-4a07-9965-5cc06c028c20">
    ProtocolReceiveNetBufferLists</a> function.</p>

<p>If the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter is not set, the filter driver retains ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
    structures until it calls the 
    <a href="https://msdn.microsoft.com/083cf25d-7436-4c4e-b29a-c9a2702b136d">
    NdisFReturnNetBufferLists</a> function.</p>

<p>If the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter is set, the filter driver cannot keep the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure and
    associated underlying-driver-allocated resources. This flag can indicate that the underlying driver is
    running low on receive resources. The 
    <i>FilterReceiveNetBufferLists</i> function should return as quickly as possible. Before returning, the 
    <i>FilterReceiveNetBufferLists</i> function can copy the received data into filter-driver-allocated
    storage or pass the buffer on by calling the 
    <a href="https://msdn.microsoft.com/ff2457bb-158a-411c-8c6b-7a7e402497ef">
    NdisFIndicateReceiveNetBufferLists</a> function.</p>

<p>Filter drivers can filter received data before indicating the data to overlying drivers. For each
    buffer that is submitted to its 
    <i>FilterReceiveNetBufferLists</i> function, a filter driver can do the following:</p>

<p>Pass the buffer on to the next overlying driver by calling the 
      <a href="https://msdn.microsoft.com/ff2457bb-158a-411c-8c6b-7a7e402497ef">
      NdisFIndicateReceiveNetBufferLists</a> function.</p>

<p>The driver can modify the contents of the buffer before calling 
      <b>NdisFIndicateReceiveNetBufferLists</b>.</p>

<p>The driver can change the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag setting that NDIS passed to 
      <i>FilterReceiveNetBufferLists</i> or simply pass it on to 
      <b>NdisFIndicateReceiveNetBufferLists</b>.</p>

<p>Discard the buffer. If NDIS cleared the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag, call the 
      <b>NdisFReturnNetBufferLists</b> function to discard the buffer. If NDIS set the
      <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag, take no action and return from 
      <i>FilterReceiveNetBufferLists</i> to discard the buffer.</p>

<p>Queue the buffer in a local data structure for later processing. If NDIS set the
      <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag of 
      <i>FilterReceiveNetBufferLists</i>, the filter driver must create a copy before returning from 
      <i>FilterReceiveNetBufferLists</i>.</p>

<p>Copy the buffer and originate a receive indication with the copy. The receive indication is similar
      to a filter-driver-initiated receive indication. In this case, the driver must return the original
      buffer to the underlying driver.</p>

<p>If the filter driver called 
    <b>NdisFIndicateReceiveNetBufferLists</b> and did not set the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag, NDIS
    calls the 
    <a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">
    FilterReturnNetBufferLists</a> function for the filter module. In its 
    <i>FilterReturnNetBufferLists</i> function, the filter driver will undo the operations that it performed
    on the buffer on the receive indication path.</p>

<p>If a filter module is in the 
    <i>Paused</i> state, the filter driver must not originate any receive indications for that filter module.
    The filter driver must not pass buffers that it created to 
    <b>NdisFIndicateReceiveNetBufferLists</b>. However, the driver can pass on a receive indication from an
    underlying driver.</p>

<p>NDIS calls 
    <i>FilterReceiveNetBufferLists</i> at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>FilterReceiveNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterReceiveNetBufferLists</i> function that is named "MyReceiveNetBufferLists", use the <b>FILTER_RECEIVE_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_RECEIVE_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_RECEIVE_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">FilterReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">FilterSetModuleOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567211">NDIS_RECEIVE_QUEUE_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ff2457bb-158a-411c-8c6b-7a7e402497ef">
   NdisFIndicateReceiveNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562613">NdisFReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c964b4b8-ab07-4a07-9965-5cc06c028c20">
   ProtocolReceiveNetBufferLists</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FILTER_RECEIVE_NET_BUFFER_LISTS callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
