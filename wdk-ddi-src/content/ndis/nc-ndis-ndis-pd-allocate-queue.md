---
UID: NC.ndis.NDIS_PD_ALLOCATE_QUEUE
title: NDIS_PD_ALLOCATE_QUEUE
author: windows-driver-content
description: The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDAllocateQueue function to allocate a queue.
old-location: netvista\ndispdallocatequeue.htm
old-project: netvista
ms.assetid: E9091C69-0E21-40CC-B3D3-1F770ABA0D47
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: NdisPDAllocateQueue
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

# NDIS_PD_ALLOCATE_QUEUE callback



## -description
<p>The PacketDirect (PD) platform calls a PD-capable miniport driver's 
   <i>NdisPDAllocateQueue</i> function to allocate a queue.<div class="alert"><b>Note</b>  You must declare the function by using the <b>NDIS_PD_ALLOCATE_QUEUE</b> type. For more
   information, see the following Examples section.</div>
<div> </div>
</p>


## -prototype

````
NDIS_PD_ALLOCATE_QUEUE NdisPDAllocateQueue;

NTSTATUS NdisPDAllocateQueue(
  _In_       NDIS_PD_PROVIDER_HANDLE  ProviderHandle,
  _In_ const NDIS_PD_QUEUE_PARAMETERS *QueueParameters,
             _Outptr_ NDIS_PD_QUEUE   **NdisPDQueue
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProviderHandle</i> [in]

<dd>
<p>A provider handle that identifies the PD-capable miniport driver's provider object.</p>
</dd>

### -param <i>QueueParameters</i> [in]

<dd>
<p>All the parameters that are associated with the Queue. For more information see the <a href="netvista.ndis_pd_queue_parameters">NDIS_PD_QUEUE_PARAMETERS</a> structure.</p>
</dd>

### -param <i>NdisPDQueue</i> 

<dd>
<p>A pointer to the Queue that is to be allocated. For more information, see the <a href="..\ndis\ne-ndis-ndis-pd-queue-type.md">NDIS_PD_QUEUE</a> structure.</p>
</dd>
</dl>

## -returns
<p>This function returns STATUS_SUCCESS when it completes successful, otherwise it returns the appropriate error code.</p>

## -remarks
<p>To define a <i>NdisPDAllocateQueue</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NdisPDAllocateQueue</i> function that is named "MyPDAllocateQueue", use the <b>NDIS_PD_ALLOCATE_QUEUE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_PD_ALLOCATE_QUEUE</b> function type is defined in the Ntddndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_PD_ALLOCATE_QUEUE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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