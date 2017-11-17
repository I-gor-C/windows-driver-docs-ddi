---
UID: NF.ndis.NdisQueueIoWorkItem
title: NdisQueueIoWorkItem
author: windows-driver-content
description: NDIS drivers call the NdisQueueIoWorkItem function to queue a work item.
old-location: netvista\ndisqueueioworkitem.htm
ms.assetid: f5065217-a74e-41b6-bc23-59b39948a450
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisQueueIoWorkItem
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisQueueIoWorkItem
req.iface: 
---

# NdisQueueIoWorkItem function



## -description
<p>NDIS drivers call the 
  <b>NdisQueueIoWorkItem</b> function to queue a work item.</p>


## -syntax

````
VOID NdisQueueIoWorkItem(
  _In_ NDIS_HANDLE              NdisIoWorkItemHandle,
  _In_ NDIS_IO_WORKITEM_ROUTINE Routine,
  _In_ PVOID                    WorkItemContext
);
````


## -parameters
<dl>

### -param <i>NdisIoWorkItemHandle</i> [in]

<dd>
<p>A handle to a private <a href="https://msdn.microsoft.com/library/windows/hardware/ff550679">IO_WORKITEM</a> structure that was returned by a previous call to the 
     <a href="https://msdn.microsoft.com/54977838-381e-4c86-a6ca-646202fdc619">
     NdisAllocateIoWorkItem</a> function.</p>
</dd>

### -param <i>Routine</i> [in]

<dd>
<p>The entry point to the function that NDIS calls to process the work item. NDIS calls this routine
     in the context of a system thread. </p>
<div class="alert"><b>Note</b>  You must declare the function by using the <b>NDIS_IO_WORKITEM_FUNCTION</b> type (not <b>NDIS_IO_WORKITEM_ROUTINE</b>). For more
   information, see the following Examples section.</div>
<div> </div>
<p>The routine includes the following input parameters:</p>
<p></p>
<dl>

### -param <a id="WorkItemContext"></a><a id="workitemcontext"></a><a id="WORKITEMCONTEXT"></a><i>WorkItemContext</i>

<dd>
<p>A pointer to the context area that the driver passed to the 
       <i>WorkItemContext</i> parameter of 
       <b>NdisQueueIoWorkItem</b>.</p>
</dd>

### -param <a id="NdisIoWorkItemHandle"></a><a id="ndisioworkitemhandle"></a><a id="NDISIOWORKITEMHANDLE"></a><i>NdisIoWorkItemHandle</i>

<dd>
<p>A handle to a private <b>NDIS_IO_WORKITEM</b> structure that was returned by a previous call to the 
       <a href="https://msdn.microsoft.com/54977838-381e-4c86-a6ca-646202fdc619">
     NdisAllocateIoWorkItem</a> function.</p>
</dd>
</dl>
</dd>

### -param <i>WorkItemContext</i> [in]

<dd>
<p>A pointer to a caller-supplied context area that NDIS passes through to the callback routine. 
     <i>WorkItemContext</i> can be any caller-specified data that the driver requires to manage the work
     item.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisQueueIoWorkItem</b> calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff549466">IoQueueWorkItem</a> to queue a work item. NDIS
    work items use the 
    <b>CriticalWorkQueue</b> queue type.</p>

<p>The caller-supplied callback routine (NDIS_IO_WORKITEM_ROUTINE) runs in a system thread context at
    IRQL = PASSIVE_LEVEL.</p>

<p>This caller-supplied routine can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561855">NdisFreeIoWorkItem</a> function to reclaim
    the storage allocated for the work item.</p>

<p>To define a <i>Routine</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>Routine</i> function that is named "MyWorkitemRoutine", use the <b>NDIS_IO_WORKITEM_FUNCTION</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_IO_WORKITEM_FUNCTION</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_IO_WORKITEM_FUNCTION</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><b>NdisQueueIoWorkItem</b> calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff549466">IoQueueWorkItem</a> to queue a work item. NDIS
    work items use the 
    <b>CriticalWorkQueue</b> queue type.</p>

<p>The caller-supplied callback routine (NDIS_IO_WORKITEM_ROUTINE) runs in a system thread context at
    IRQL = PASSIVE_LEVEL.</p>

<p>This caller-supplied routine can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561855">NdisFreeIoWorkItem</a> function to reclaim
    the storage allocated for the work item.</p>

<p>To define a <i>Routine</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>Routine</i> function that is named "MyWorkitemRoutine", use the <b>NDIS_IO_WORKITEM_FUNCTION</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_IO_WORKITEM_FUNCTION</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_IO_WORKITEM_FUNCTION</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547982">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549466">IoQueueWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561604">NdisAllocateIoWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561855">NdisFreeIoWorkItem</a>
</dt>
<dt>
<a href="NULL">NDIS I/O Work Items</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisQueueIoWorkItem function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
