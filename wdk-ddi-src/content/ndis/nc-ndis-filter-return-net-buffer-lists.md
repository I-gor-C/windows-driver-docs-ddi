---
UID: NC.ndis.FILTER_RETURN_NET_BUFFER_LISTS
title: FILTER_RETURN_NET_BUFFER_LISTS
author: windows-driver-content
description: NDIS calls the FilterReturnNetBufferLists function to return a linked list of NET_BUFFER_LIST structures and associated data to a filter driver.Note  You must declare the function by using the FILTER_RETURN_NET_BUFFER_LISTS type.
old-location: netvista\filterreturnnetbufferlists.htm
old-project: netvista
ms.assetid: 8d7e362f-62da-4ce7-9497-1cfaff2b678e
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: FilterReturnNetBufferLists
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

# FILTER_RETURN_NET_BUFFER_LISTS callback



## -description
<p>NDIS calls the 
  <i>FilterReturnNetBufferLists</i> function to return a linked list of 
  <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures and associated data
  to a filter driver.</p>


## -prototype

````
FILTER_RETURN_NET_BUFFER_LISTS FilterReturnNetBufferLists;

VOID FilterReturnNetBufferLists(
  _In_ NDIS_HANDLE      FilterModuleContext,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ ULONG            ReturnFlags
)
{ ... }
````


## -parameters
<dl>

### -param FilterModuleContext [in]

<dd>
<p>A handle to the context area for the filter module. The filter driver created and initialized this
     context area in the 
     <a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a> function.</p>
</dd>

### -param NetBufferLists [in]

<dd>
<p>A linked list of <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures that the filter driver indicated by calling the 
     <a href="..\ndis\nf-ndis-ndisfindicatereceivenetbufferlists.md">
     NdisFIndicateReceiveNetBufferLists</a> function. The list can include <b>NET_BUFFER_LIST</b> structures from
     multiple calls to 
     <b>NdisFIndicateReceiveNetBufferLists</b>.</p>
</dd>

### -param ReturnFlags [in]

<dd>
<p>NDIS flags that can be combined with an OR operation. To clear all the flags, set this member to
     zero.This function supports the following flags: </p>
<p></p>
<dl>

### -param NDIS_RETURN_FLAGS_DISPATCH_LEVEL

<dd>
<p>Specifies that the current IRQL is DISPATCH_LEVEL. For more information about this flag, see 
       <a href="netvista.dispatch_irql_tracking">Dispatch IRQL Tracking</a>.</p>
</dd>

### -param NDIS_RETURN_FLAGS_SWITCH_SINGLE_SOURCE

<dd>
<p>If this flag is set, all packets in a linked list of <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures originated from the same Hyper-V extensible switch source port.</p>
<p>For more information, see <a href="netvista.hyper_v_extensible_switch_send_and_receive_flags">Hyper-V Extensible Switch Send and Receive Flags</a>.</p>
<div class="alert"><b>Note</b>  If each packet in the linked list of <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures uses the same source port, the extension should set the <b>NDIS_RECEIVE_FLAGS_SWITCH_SINGLE_SOURCE</b> flag in the <i>ReceiveFlags</i> parameter of <a href="..\ndis\nc-ndis-filter-receive-net-buffer-lists.md">FilterReceiveNetBufferLists</a>  when it sends the request.</div>
<div> </div>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><i>FilterReturnNetBufferLists</i> is an optional function. If a filter driver does not filter receive indications, it can set the entry point for this function to <b>NULL</b> when it calls the 
    <a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> function.</p>

<p>The filter driver can call the 
    <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> function,
    from the 
    <a href="netvista.filtersetmoduleoptions">FilterSetModuleOptions</a> function, to
    specify a 
    <i>FilterReturnNetBufferLists</i> function for a filter module.</p>

<p>When NDIS calls 
    <i>FilterReturnNetBufferLists</i>, the filter driver regains ownership of the 
    <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures and associated
    data.</p>

<p>If an underlying driver initiated the receive indication, the filter driver should call the 
    <a href="..\ndis\nf-ndis-ndisfreturnnetbufferlists.md">
    NdisFReturnNetBufferLists</a> function to complete the receive indication.</p>

<p>If the filter driver originated the receive indication, 
    <i>FilterReturnNetBufferLists</i> can either release the NET_BUFFER_LIST structures and associated data or
    prepare them for reuse in a subsequent call to 
    <b>NdisFIndicateReceiveNetBufferLists</b>.</p>

<p>A filter driver should keep track of receive indications that it initiates and make sure that it does
    not call 
    <b>NdisFReturnNetBufferLists</b> when NDIS calls 
    <i>FilterReturnNetBufferLists</i>.</p>

<p>NDIS calls 
    <i>FilterReturnNetBufferLists</i> at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>FilterReturnNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterReturnNetBufferLists</i> function that is named "MyReturnNetBufferLists", use the <b>FILTER_RETURN_NET_BUFFER_LISTS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_RETURN_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_RETURN_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/232c4272-0bf0-4a4e-9560-3bceeca8a3e3">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a>
</dt>
<dt>
<a href="netvista.filtersetmoduleoptions">FilterSetModuleOptions</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-status.md">FilterStatus</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfindicatereceivenetbufferlists.md">
   NdisFIndicateReceiveNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreturnnetbufferlists.md">NdisFReturnNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FILTER_RETURN_NET_BUFFER_LISTS callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
