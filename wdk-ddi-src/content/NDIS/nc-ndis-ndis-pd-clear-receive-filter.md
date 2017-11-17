---
UID: NC.ndis.NDIS_PD_CLEAR_RECEIVE_FILTER
title: NDIS_PD_CLEAR_RECEIVE_FILTER
author: windows-driver-content
description: The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDClearReceiveFilter function to clear this filter from the PD platform.
old-location: netvista\ndispdclearreceivefilter.htm
ms.assetid: C91F2E5D-C37F-48A9-9AE0-F5A8C5D8F54D
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisPDClearReceiveFilter
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
req.irql: PASSIVE_LEVEL
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# NDIS_PD_CLEAR_RECEIVE_FILTER callback



## -description
<p>The PacketDirect (PD) platform calls a PD-capable miniport driver's 
   <i>NdisPDClearReceiveFilter</i> function to clear this filter from the PD platform.<div class="alert"><b>Note</b>  You must declare the function by using the <b>NDIS_PD_CLEAR_RECEIVE_FILTER</b> type. For more
   information, see the following Examples section.</div>
<div> </div>
</p>


## -prototype

````
NDIS_PD_CLEAR_RECEIVE_FILTER NdisPDClearReceiveFilter;

void NdisPDClearReceiveFilter(
  _In_ __drv_freesMem (Mem) NDIS_PD_FILTER_HANDLE FilterHandle
)
{ ... }
````


## -parameters
<dl>

### -param <i>FilterHandle</i> [in]

<dd>
<p>A handle to a PD platform filter.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>After this function returns, it's guaranteed that no more newly arriving packet will match this filter. However, there may still be in-flight packets that have already matched this filter and they are on their way to being placed into the target receive queue.</p>

<p>To define a <i>NdisPDClearReceiveFilter</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NdisPDClearReceiveFilter</i> function that is named "MyPDClearReceiveFilter", use the <b>NDIS_PD_CLEAR_RECEIVE_FILTER</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_PD_CLEAR_RECEIVE_FILTER</b> function type is defined in the Ntddndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_PD_CLEAR_RECEIVE_FILTER</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>After this function returns, it's guaranteed that no more newly arriving packet will match this filter. However, there may still be in-flight packets that have already matched this filter and they are on their way to being placed into the target receive queue.</p>

<p>To define a <i>NdisPDClearReceiveFilter</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NdisPDClearReceiveFilter</i> function that is named "MyPDClearReceiveFilter", use the <b>NDIS_PD_CLEAR_RECEIVE_FILTER</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_PD_CLEAR_RECEIVE_FILTER</b> function type is defined in the Ntddndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_PD_CLEAR_RECEIVE_FILTER</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>