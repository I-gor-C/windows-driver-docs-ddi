---
UID: NC.ndis.NDIS_PD_FREE_QUEUE
title: NDIS_PD_FREE_QUEUE
author: windows-driver-content
description: The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDFreeQueue function to free a queue.
old-location: netvista\ndispdfreequeue.htm
old-project: netvista
ms.assetid: 1DE8582C-AF11-4CBA-8F4C-159266A7F3BA
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisPDFreeQueue
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
req.iface: 
---

# NDIS_PD_FREE_QUEUE callback



## -description
<p>The PacketDirect (PD) platform calls a PD-capable miniport driver's 
   <i>NdisPDFreeQueue</i> function to free a queue.<div class="alert"><b>Note</b>  You must declare the function by using the <b>NDIS_PD_FREE_QUEUE</b> type. For more
   information, see the following Examples section.</div>
<div> </div>
</p>


## -prototype

````
NDIS_PD_FREE_QUEUE NdisPDFreeQueue;

void NdisPDFreeQueue(
  _In_ __drv_freesMem(Mem) NDIS_PD_QUEUE *NdisPDQueue
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisPDQueue</i> [in]

<dd>
<p>Any empty queue that needs to be freed from memory. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931844">NDIS_PD_QUEUE</a> structure.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The caller is responsible for ensuring that the PD queue is empty before issuing this call. Caller is also responsible for clearing all filters that target this queue before closing the queue.</p>

<p>To define a <i>NdisPDFreeQueue</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NdisPDFreeQueue</i> function that is named "MyPDFreeQueue", use the <b>NDIS_PD_FREE_QUEUE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_PD_FREE_QUEUE</b> function type is defined in the Ntddndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_PD_FREE_QUEUE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>The caller is responsible for ensuring that the PD queue is empty before issuing this call. Caller is also responsible for clearing all filters that target this queue before closing the queue.</p>

<p>To define a <i>NdisPDFreeQueue</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NdisPDFreeQueue</i> function that is named "MyPDFreeQueue", use the <b>NDIS_PD_FREE_QUEUE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_PD_FREE_QUEUE</b> function type is defined in the Ntddndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_PD_FREE_QUEUE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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