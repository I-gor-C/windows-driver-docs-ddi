---
UID: NC.ndis.MINIPORT_CO_SEND_NET_BUFFER_LISTS
title: MINIPORT_CO_SEND_NET_BUFFER_LISTS
author: windows-driver-content
description: The MiniportCoSendNetBufferLists function transmits network data that is contained in a specified linked list of NET_BUFFER_LIST structures.Note  You must declare the function by using the MINIPORT_CO_SEND_NET_BUFFER_LISTS type.
old-location: netvista\miniportcosendnetbufferlists.htm
ms.assetid: 4a717842-6d71-488e-a56a-57c6e6e0c5d7
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
req.alt-api: MiniportCoSendNetBufferLists
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

# MINIPORT_CO_SEND_NET_BUFFER_LISTS callback



## -description
<p>The 
  <i>MiniportCoSendNetBufferLists</i> function transmits network data that is contained in a specified linked
  list of 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures.</p>


## -prototype

````
MINIPORT_CO_SEND_NET_BUFFER_LISTS MiniportCoSendNetBufferLists;

VOID MiniportCoSendNetBufferLists(
  _In_ NDIS_HANDLE      MiniportVcContext,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ ULONG            SendFlags
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportVcContext</i> [in]

<dd>
<p>A handle to a miniport driver-allocated context area in which the miniport driver maintains its
     per-virtual connection (VC) state. The miniport driver supplied this handle to NDIS from its 
     <a href="https://msdn.microsoft.com/99eaba29-ce17-4e79-878e-5fdf7411e56c">MiniportCoCreateVc</a> function.</p>
</dd>

### -param <i>NetBufferLists</i> [in]

<dd>
<p>A pointer to the first 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure in a linked list
     of <b>NET_BUFFER_LIST</b> structures. Each <b>NET_BUFFER_LIST</b> structure in the list describes a list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures. Each <b>NET_BUFFER</b> structure
     in the list maps to a chain of memory descriptor lists (MDLs). The MDLs contain the network data that 
     <i>MiniportCoSendNetBufferLists</i> transmits.</p>
</dd>

### -param <i>SendFlags</i> [in]

<dd>
<p>Flags that define attributes for the send operation. The flags can be combined with a bitwise OR
     operation. To clear all of the flags, set this parameter to zero. 
     <i>MiniportCoSendNetBufferLists</i> supports the following flags:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_SEND_FLAGS_DISPATCH_LEVEL"></a><a id="ndis_send_flags_dispatch_level"></a>NDIS_SEND_FLAGS_DISPATCH_LEVEL

<dd>
<p>The caller can optionally set this flag if the current IRQL is DISPATCH_LEVEL. For more information about this flag, see 
       <a href="NULL">Dispatch IRQL Tracking</a>.</p>
</dd>

### -param <a id="NDIS_SEND_FLAGS_CHECK_FOR_LOOPBACK"></a><a id="ndis_send_flags_check_for_loopback"></a>NDIS_SEND_FLAGS_CHECK_FOR_LOOPBACK

<dd>
<p>NDIS should check for loopback. By default, NDIS does not loop back data to the driver that
       submitted the send request. An overlying driver can override this behavior by setting the
       <b>NDIS_SEND_FLAGS_CHECK_FOR_LOOPBACK</b> flag. When this flag is set, NDIS identifies all of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
       structures that contain data that matches the receive criteria for the binding. NDIS indicates
       <b>NET_BUFFER</b> structures that match the criteria to the overlying driver. This flag does not affect
       checking for loopback, or looping back, on other bindings.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <i>MiniportCoSendNetBufferLists</i> function is required for CoNDIS miniport drivers. When an overlying
    driver calls the 
    <a href="https://msdn.microsoft.com/8284fdd4-26de-4622-b164-f33aee1d8742">
    NdisCoSendNetBufferLists</a> function, NDIS calls the 
    <i>MiniportCoSendNetBufferLists</i> function of the bound miniport driver.</p>

<p>The order of the linked list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that NDIS passes
    at 
    <i>NetBufferLists</i> represents the order in which the miniport driver should transmit the network data.
    In addition, a miniport driver should send the <b>NET_BUFFER_LIST</b> structures from multiple 
    <i>MiniportCoSendNetBufferLists</i> calls in the order that the miniport driver received the structures
    in.</p>

<p>CoNDIS miniport drivers must accept all of the send requests that NDIS makes by calling the 
    <i>MiniportCoSendNetBufferLists</i> function. If a miniport driver cannot complete a send request
    immediately, the driver must hold the request in a queue until it can complete the request. While a send
    request is pending, the miniport driver retains ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures and all of
    the resources that are associated with the <b>NET_BUFFER_LIST</b> structures.</p>

<p>The miniport driver must call the 
    <a href="https://msdn.microsoft.com/c4978122-6d13-4e9b-8eb7-d06cd7372268">
    NdisMCoSendNetBufferListsComplete</a> function to complete all CoNDIS send requests. To improve
    computer performance, the driver can create a linked list that contains the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures from multiple
    send requests. The driver can then pass such a linked list in a single call to 
    <b>NdisMCoSendNetBufferListsComplete</b>.</p>

<p>In addition, you should assume that the miniport driver cannot access the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures
    and other associated resources as soon as the driver calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563570">NdisMCoSendNetBufferListsComplete</a>.</p>

<p>The 
    <i>MiniportCoSendNetBufferLists</i> function must synchronize access to its internal queues of network
    data with the driver's other 
    <i>MiniportXxx</i> functions that access the same queues. A miniport driver can use spin locks to
    synchronize access to the queues.</p>

<p>Protocol drivers are responsible for determining what network data is required, based on the medium
    type that the bound miniport driver selected. However, a protocol driver can supply network data that
    specifies packets that are shorter than the minimum packet size for the selected medium. In this case, 
    <i>MiniportCoSendNetBufferLists</i> must pad the packets with zeros if the selected medium imposes a
    minimum-length requirement on the transmit packet size.</p>

<p>NDIS calls 
    <i>MiniportCoSendNetBufferLists</i> at IRQL&lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>MiniportCoSendNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportCoSendNetBufferLists</i> function that is named "MyCoSendNetBufferLists", use the <b>MINIPORT_CO_SEND_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_CO_SEND_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_CO_SEND_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>The 
    <i>MiniportCoSendNetBufferLists</i> function is required for CoNDIS miniport drivers. When an overlying
    driver calls the 
    <a href="https://msdn.microsoft.com/8284fdd4-26de-4622-b164-f33aee1d8742">
    NdisCoSendNetBufferLists</a> function, NDIS calls the 
    <i>MiniportCoSendNetBufferLists</i> function of the bound miniport driver.</p>

<p>The order of the linked list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that NDIS passes
    at 
    <i>NetBufferLists</i> represents the order in which the miniport driver should transmit the network data.
    In addition, a miniport driver should send the <b>NET_BUFFER_LIST</b> structures from multiple 
    <i>MiniportCoSendNetBufferLists</i> calls in the order that the miniport driver received the structures
    in.</p>

<p>CoNDIS miniport drivers must accept all of the send requests that NDIS makes by calling the 
    <i>MiniportCoSendNetBufferLists</i> function. If a miniport driver cannot complete a send request
    immediately, the driver must hold the request in a queue until it can complete the request. While a send
    request is pending, the miniport driver retains ownership of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures and all of
    the resources that are associated with the <b>NET_BUFFER_LIST</b> structures.</p>

<p>The miniport driver must call the 
    <a href="https://msdn.microsoft.com/c4978122-6d13-4e9b-8eb7-d06cd7372268">
    NdisMCoSendNetBufferListsComplete</a> function to complete all CoNDIS send requests. To improve
    computer performance, the driver can create a linked list that contains the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures from multiple
    send requests. The driver can then pass such a linked list in a single call to 
    <b>NdisMCoSendNetBufferListsComplete</b>.</p>

<p>In addition, you should assume that the miniport driver cannot access the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures
    and other associated resources as soon as the driver calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563570">NdisMCoSendNetBufferListsComplete</a>.</p>

<p>The 
    <i>MiniportCoSendNetBufferLists</i> function must synchronize access to its internal queues of network
    data with the driver's other 
    <i>MiniportXxx</i> functions that access the same queues. A miniport driver can use spin locks to
    synchronize access to the queues.</p>

<p>Protocol drivers are responsible for determining what network data is required, based on the medium
    type that the bound miniport driver selected. However, a protocol driver can supply network data that
    specifies packets that are shorter than the minimum packet size for the selected medium. In this case, 
    <i>MiniportCoSendNetBufferLists</i> must pad the packets with zeros if the selected medium imposes a
    minimum-length requirement on the transmit packet size.</p>

<p>NDIS calls 
    <i>MiniportCoSendNetBufferLists</i> at IRQL&lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>MiniportCoSendNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportCoSendNetBufferLists</i> function that is named "MyCoSendNetBufferLists", use the <b>MINIPORT_CO_SEND_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_CO_SEND_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_CO_SEND_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="https://msdn.microsoft.com/99eaba29-ce17-4e79-878e-5fdf7411e56c">MiniportCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c4978122-6d13-4e9b-8eb7-d06cd7372268">
   NdisMCoSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561728">NdisCoSendNetBufferLists</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_CO_SEND_NET_BUFFER_LISTS callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
