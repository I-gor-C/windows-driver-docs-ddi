---
UID: NC.ndis.PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS
title: PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS
author: windows-driver-content
description: The ProtocolCoReceiveNetBufferLists function processes receive indications from underlying drivers.Note  You must declare the function by using the PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS type.
old-location: netvista\protocolcoreceivenetbufferlists.htm
ms.assetid: 1755804c-d82f-465d-862f-8a2340516f8e
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
req.alt-api: ProtocolCoReceiveNetBufferLists
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

# PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS callback



## -description
<p>The 
  <i>ProtocolCoReceiveNetBufferLists</i> function processes receive indications from underlying
  drivers.</p>


## -prototype

````
PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS ProtocolCoReceiveNetBufferLists;

VOID ProtocolCoReceiveNetBufferLists(
  _In_ NDIS_HANDLE        ProtocolBindingContext,
  _In_ NDIS_HANDLE        ProtocolVcContext,
  _In_ INPNET_BUFFER_LIST NetBufferLists,
  _In_ ULONG              NumberOfNetBufferLists,
  _In_ ULONG              ReceiveFlags
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProtocolBindingContext</i> [in]

<dd>
<p>A handle to a context area that the protocol driver allocated to maintain state information for a
     binding. This handle was passed to NDIS in a previous call to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>.</p>
</dd>

### -param <i>ProtocolVcContext</i> [in]

<dd>
<p>A handle to a protocol driver-allocated context area in which this driver maintains the
     per-virtual connection (VC) run-time state information. A client or stand-alone call manager supplied
     this handle either when it called the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> function or from its 
     <a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a> function.</p>
</dd>

### -param <i>NetBufferLists</i> [in]

<dd>
<p>A linked list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that the
     underlying driver allocated. Each <b>NET_BUFFER_LIST</b> structure is usually associated with one 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure.</p>
</dd>

### -param <i>NumberOfNetBufferLists</i> [in]

<dd>
<p>The number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that are in the linked list of structures that 
     <i>NetBufferLists</i> specifies.</p>
</dd>

### -param <i>ReceiveFlags</i> [in]

<dd>
<p>Flags that define attributes for the send operation. The flags can be combined with a bitwise OR
     operation. To clear all of the flags, set this parameter to zero. 
     <i>ProtocolCoReceiveNetBufferLists</i> supports the following flags:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_RECEIVE_FLAGS_DISPATCH_LEVEL"></a><a id="ndis_receive_flags_dispatch_level"></a>NDIS_RECEIVE_FLAGS_DISPATCH_LEVEL

<dd>
<p>The current IRQL is DISPATCH_LEVEL. For more information about this flag, see 
       <a href="NULL">Dispatch IRQL Tracking</a>.</p>
</dd>

### -param <a id="NDIS_RECEIVE_FLAGS_RESOURCES"></a><a id="ndis_receive_flags_resources"></a>NDIS_RECEIVE_FLAGS_RESOURCES

<dd>
<p>NDIS reclaims ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures and any attached NET_BUFFER structures
       immediately after the call to 
       <i>ProtocolCoReceiveNetBufferLists</i> returns.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <i>ProtocolCoReceiveNetBufferLists</i> function is required for CoNDIS protocol drivers. NDIS calls 
    <i>ProtocolCoReceiveNetBufferLists</i> after a bound miniport driver calls the 
    <a href="https://msdn.microsoft.com/dabd472f-9877-4434-a534-e07a047e092f">
    NdisMCoIndicateReceiveNetBufferLists</a> function. A call to 
    <i>ProtocolCoReceiveNetBufferLists</i> can also occur as a result of a loopback.</p>

<p>If the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag in the 
    <i>CoReceiveFlags</i> parameter is not set, the protocol driver retains ownership of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures until it calls
    the 
    <a href="https://msdn.microsoft.com/1a45bc5c-cdc1-46d2-905b-3d5eea3645c1">
    NdisReturnNetBufferLists</a> function. If NDIS sets the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag, the protocol
    driver cannot retain the <b>NET_BUFFER_LIST</b> structure and associated resources. <b>NDIS_RECEIVE_FLAGS_RESOURCES</b>
    indicates that an underlying driver has low receive resources. In this case, the 
    <i>ProtocolCoReceiveNetBufferLists</i> function should copy the received data into protocol-allocated
    storage and return as quickly as possible.</p>

<p>On a multiprocessor system, 
    <i>ProtocolCoReceiveNetBufferLists</i> can run concurrently on more than one processor. In this situation,
    apply protection (for example, use spin locks) to critical data structures that 
    <i>ProtocolCoReceiveNetBufferLists</i> accesses.</p>

<p>NDIS calls 
    <i>ProtocolCoReceiveNetBufferLists</i> at IRQL&lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>ProtocolCoReceiveNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCoReceiveNetBufferLists</i> function that is named "MyCoReceiveNetBufferLists", use the <b>PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>The 
    <i>ProtocolCoReceiveNetBufferLists</i> function is required for CoNDIS protocol drivers. NDIS calls 
    <i>ProtocolCoReceiveNetBufferLists</i> after a bound miniport driver calls the 
    <a href="https://msdn.microsoft.com/dabd472f-9877-4434-a534-e07a047e092f">
    NdisMCoIndicateReceiveNetBufferLists</a> function. A call to 
    <i>ProtocolCoReceiveNetBufferLists</i> can also occur as a result of a loopback.</p>

<p>If the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag in the 
    <i>CoReceiveFlags</i> parameter is not set, the protocol driver retains ownership of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures until it calls
    the 
    <a href="https://msdn.microsoft.com/1a45bc5c-cdc1-46d2-905b-3d5eea3645c1">
    NdisReturnNetBufferLists</a> function. If NDIS sets the <b>NDIS_RECEIVE_FLAGS_RESOURCES</b> flag, the protocol
    driver cannot retain the <b>NET_BUFFER_LIST</b> structure and associated resources. <b>NDIS_RECEIVE_FLAGS_RESOURCES</b>
    indicates that an underlying driver has low receive resources. In this case, the 
    <i>ProtocolCoReceiveNetBufferLists</i> function should copy the received data into protocol-allocated
    storage and return as quickly as possible.</p>

<p>On a multiprocessor system, 
    <i>ProtocolCoReceiveNetBufferLists</i> can run concurrently on more than one processor. In this situation,
    apply protection (for example, use spin locks) to critical data structures that 
    <i>ProtocolCoReceiveNetBufferLists</i> accesses.</p>

<p>NDIS calls 
    <i>ProtocolCoReceiveNetBufferLists</i> at IRQL&lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>ProtocolCoReceiveNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCoReceiveNetBufferLists</i> function that is named "MyCoReceiveNetBufferLists", use the <b>PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="https://msdn.microsoft.com/0f33ae87-164e-40dc-a915-28211a0d74b7">
   MiniportReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/dabd472f-9877-4434-a534-e07a047e092f">
   NdisMCoIndicateReceiveNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564534">NdisReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fb4b00c0-0b14-48dd-a6f2-aae659c6bb28">ProtocolCoSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545115">CoNDIS Protocol Driver Send and Receive Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
