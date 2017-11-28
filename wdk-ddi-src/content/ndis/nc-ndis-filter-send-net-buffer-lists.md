---
UID: NC.ndis.FILTER_SEND_NET_BUFFER_LISTS
title: FILTER_SEND_NET_BUFFER_LISTS
author: windows-driver-content
description: NDIS calls the FilterSendNetBufferLists function to allow a filter driver to filter a linked list of NET_BUFFER_LIST structures.Note  You must declare the function by using the FILTER_SEND_NET_BUFFER_LISTS type.
old-location: netvista\filtersendnetbufferlists.htm
old-project: netvista
ms.assetid: 1b3fc0c8-95da-47e5-8ff1-b7967f5148e7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FilterSendNetBufferLists
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
req.iface: 
---

# FILTER_SEND_NET_BUFFER_LISTS callback



## -description
<p>NDIS calls the 
  <i>FilterSendNetBufferLists</i> function to allow a filter driver to filter a linked list of 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures.</p>


## -prototype

````
FILTER_SEND_NET_BUFFER_LISTS FilterSendNetBufferLists;

VOID FilterSendNetBufferLists(
  _In_ NDIS_HANDLE      FilterModuleContext,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ NDIS_PORT_NUMBER PortNumber,
  _In_ ULONG            SendFlags
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
<p>A pointer to a linked list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that specify
     lists of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures. Each <b>NET_BUFFER</b> in the
     list maps a chain of MDLs that contain the transmit data.</p>
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
<p>Flags that define attributes for the send operation. The flags can be combined with an OR operation.
      To clear all the flags, set this member to zero. This function supports the following flags:</p>
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
        driver that submitted the send request. An overlying driver can override this behavior by setting
        this flag. When this flag is set, NDIS identifies all the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures that contain data
        that matches the receive criteria for the binding. NDIS indicates <b>NET_BUFFER</b> structures that match
        the criteria to the overlying driver. This flag has no affect on checking for loopback, or looping
        back, on other bindings.</p>
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
<p><i>FilterSendNetBufferLists</i> is an optional function. If a filter driver does not filter send requests,
    it can set the entry point for this function to <b>NULL</b> when it calls the 
    <a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> function.</p>

<p>If a filter driver specifies a 
    <i>FilterSendNetBufferLists</i> function and it queues send requests, it must also specify a 
    <a href="netvista.filtercancelsendnetbufferlists">
    FilterCancelSendNetBufferLists</a> function.</p>

<p>The filter driver can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function,
    from the 
    <a href="netvista.filtersetmoduleoptions">FilterSetModuleOptions</a> function, to
    specify a 
    <i>FilterSendNetBufferLists</i> function for a filter module.</p>

<p>If the filter driver specifies a 
    <i>FilterSendNetBufferLists</i> function, NDIS calls this function to filter the data that is contained in
    a list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures over the network. NDIS
    specifies a list of <b>NET_BUFFER</b> structures in each 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>If the filter driver did not specify 
    <i>FilterSendNetBufferLists</i>, NDIS calls the next filter driver that is lower in the driver stack that
    did specify a 
    <i>FilterSendNetBufferLists</i> function. If there are no such underlying filter drivers, NDIS calls an
    underlying driver's 
    <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
    MiniportSendNetBufferLists</a> function.</p>

<p>The filter driver can filter the data and send the filtered data to underlying drivers. For each
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure submitted to 
    <i>FilterSendNetBufferLists</i>, a filter driver can do the following:</p>

<p>Pass the buffer on to the next underlying driver by calling the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562616">NdisFSendNetBufferLists</a> function. The filter driver can modify the buffer contents before calling
      
      <b>NdisFSendNetBufferLists</b>. In this case NDIS calls the 
      <a href="..\ndis\nc-ndis-filter-send-net-buffer-lists-complete.md">
      FilterSendNetBufferListsComplete</a> function after the underlying drivers complete the send
      request.</p>

<p>Reject the buffer by calling the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> function.</p>

<p>Queue the buffer in a local data structure for later processing.</p>

<p>Copy the buffer and originate a send request with the copy. The send operation is similar to a
      filter-driver initiated send request. In this case, the driver must return the original buffer to the
      overlying driver by calling the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> function.</p>

<p>After the send operation is complete, a filter driver reverses the modifications, if any, to the
    buffer descriptors that it made in the 
    <i>FilterSendNetBufferLists</i> function. The driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> function to return the linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to
    the overlying drivers and to return the final status of the send request.</p>

<p>If a filter module is in the 
    <i>Paused</i> state, the filter driver must not originate any send requests for that filter module. If
    NDIS calls 
    <i>FilterSendNetBufferLists</i>, the driver must not call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562616">NdisFSendNetBufferLists</a> to pass on the data until the driver is restarted. The driver should call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> immediately to complete the send operation. It should set the
    complete status in each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure to NDIS_STATUS_PAUSED.</p>

<p>NDIS calls 
    <i>FilterSendNetBufferLists</i> at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>FilterSendNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterSendNetBufferLists</i> function that is named "MySendNetBufferLists", use the <b>FILTER_SEND_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_SEND_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_SEND_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>FilterSendNetBufferLists</i> is an optional function. If a filter driver does not filter send requests,
    it can set the entry point for this function to <b>NULL</b> when it calls the 
    <a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> function.</p>

<p>If a filter driver specifies a 
    <i>FilterSendNetBufferLists</i> function and it queues send requests, it must also specify a 
    <a href="netvista.filtercancelsendnetbufferlists">
    FilterCancelSendNetBufferLists</a> function.</p>

<p>The filter driver can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function,
    from the 
    <a href="netvista.filtersetmoduleoptions">FilterSetModuleOptions</a> function, to
    specify a 
    <i>FilterSendNetBufferLists</i> function for a filter module.</p>

<p>If the filter driver specifies a 
    <i>FilterSendNetBufferLists</i> function, NDIS calls this function to filter the data that is contained in
    a list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures over the network. NDIS
    specifies a list of <b>NET_BUFFER</b> structures in each 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>If the filter driver did not specify 
    <i>FilterSendNetBufferLists</i>, NDIS calls the next filter driver that is lower in the driver stack that
    did specify a 
    <i>FilterSendNetBufferLists</i> function. If there are no such underlying filter drivers, NDIS calls an
    underlying driver's 
    <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
    MiniportSendNetBufferLists</a> function.</p>

<p>The filter driver can filter the data and send the filtered data to underlying drivers. For each
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure submitted to 
    <i>FilterSendNetBufferLists</i>, a filter driver can do the following:</p>

<p>Pass the buffer on to the next underlying driver by calling the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562616">NdisFSendNetBufferLists</a> function. The filter driver can modify the buffer contents before calling
      
      <b>NdisFSendNetBufferLists</b>. In this case NDIS calls the 
      <a href="..\ndis\nc-ndis-filter-send-net-buffer-lists-complete.md">
      FilterSendNetBufferListsComplete</a> function after the underlying drivers complete the send
      request.</p>

<p>Reject the buffer by calling the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> function.</p>

<p>Queue the buffer in a local data structure for later processing.</p>

<p>Copy the buffer and originate a send request with the copy. The send operation is similar to a
      filter-driver initiated send request. In this case, the driver must return the original buffer to the
      overlying driver by calling the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> function.</p>

<p>After the send operation is complete, a filter driver reverses the modifications, if any, to the
    buffer descriptors that it made in the 
    <i>FilterSendNetBufferLists</i> function. The driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> function to return the linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to
    the overlying drivers and to return the final status of the send request.</p>

<p>If a filter module is in the 
    <i>Paused</i> state, the filter driver must not originate any send requests for that filter module. If
    NDIS calls 
    <i>FilterSendNetBufferLists</i>, the driver must not call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562616">NdisFSendNetBufferLists</a> to pass on the data until the driver is restarted. The driver should call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562618">NdisFSendNetBufferListsComplete</a> immediately to complete the send operation. It should set the
    complete status in each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure to NDIS_STATUS_PAUSED.</p>

<p>NDIS calls 
    <i>FilterSendNetBufferLists</i> at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>FilterSendNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterSendNetBufferLists</i> function that is named "MySendNetBufferLists", use the <b>FILTER_SEND_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_SEND_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_SEND_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="netvista.filtercancelsendnetbufferlists">
   FilterCancelSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-send-net-buffer-lists-complete.md">
   FilterSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="netvista.filtersetmoduleoptions">FilterSetModuleOptions</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">MiniportSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562616">NdisFSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfsendnetbufferlistscomplete.md">
   NdisFSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564672">NdisWriteEventLogEntry</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FILTER_SEND_NET_BUFFER_LISTS callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
