---
UID: NC.ndis.NDIS_PD_ALLOCATE_COUNTER
title: NDIS_PD_ALLOCATE_COUNTER
author: windows-driver-content
description: The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDAllocateCounter function to allocate a counter object.
old-location: netvista\ndispdallocatecounter.htm
old-project: netvista
ms.assetid: 86AA537D-952F-4A7A-ACA4-24B8C1AE932A
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: NdisPDAllocateCounter
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

# NDIS_PD_ALLOCATE_COUNTER callback



## -description
<p>The PacketDirect (PD) platform calls a PD-capable miniport driver's 
   <i>NdisPDAllocateCounter</i> function to allocate a counter object. There are three kinds of counters:<ul>
<li>
<p>Receive queue counters are used for tracking receive queue activity.</p>
</li>
<li>
<p>Transmit queue counters are used for tracking transmit queue activity.</p>
</li>
<li>
<p>Filter counters are used for tracking filter match activity.</p>
</li>
</ul>
<div class="alert"><b>Note</b>  You must declare the function by using the <b>NDIS_PD_ALLOCATE_COUNTER</b> type. For more
   information, see the following Examples section.</div>
<div> </div>
</p>
<p>Receive queue counters are used for tracking receive queue activity.</p>
<p>Transmit queue counters are used for tracking transmit queue activity.</p>
<p>Filter counters are used for tracking filter match activity.</p>


## -prototype

````
NDIS_PD_ALLOCATE_COUNTER NdisPDAllocateCounter;

NTSTATUS NdisPDAllocateCounter(
  _In_        NDIS_PD_PROVIDER_HANDLE    ProviderHandle,
  _In_  const NDIS_PD_COUNTER_PARAMETERS *CounterParameters,
  _Out_       NDIS_PD_COUNTER_HANDLE     *CounterHandle
)
{ ... }
````


## -parameters
<dl>

### -param ProviderHandle [in]

<dd>
<p>A provider handle that identifies the PD-capable miniport driver's provider object.</p>
</dd>

### -param CounterParameters [in]

<dd>
<p>An <a href="..\ndis\ns-ndis--ndis-pd-counter-parameters.md">NDIS_PD_COUNTER_PARAMETERS</a> structure that specifies information such as the counter type.</p>
</dd>

### -param CounterHandle [out]

<dd>
<p>A pointer to a driver-allocated counter handle variable. If the counter allocation succeeds, the miniport driver returns a handle to the newly allocated counter in this variable.</p>
</dd>
</dl>

## -returns
<p><i>NdisPDAllocateCounter</i> can return one of the following status values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The miniport driver successfully allocated the counter and returned a handle in the <i>CounterHandle</i> parameter.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p> The allocation failed due to insufficient resources.</p>

<p> </p>

## -remarks
<p>The same counter object can be associated with multiple  queue or filter objects of the same  type as the counter. For example, if there are  5 receive queues (RQ1 through RQ5) and 2 receive counters (RC1 and RC2), receive counter RC1 could be associated with receive queues RQ1, RQ2, RQ3, and receive counter RC2 could be associated with receive queues RQ4 and RQ5.</p>

<p>To define a <i>NdisPDAllocateCounter</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NdisPDAllocateCounter</i> function that is named "MyPDAllocateCounter", use the <b>NDIS_PD_ALLOCATE_COUNTER</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_PD_ALLOCATE_COUNTER</b> function type is defined in the Ntddndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_PD_ALLOCATE_COUNTER</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/232c4272-0bf0-4a4e-9560-3bceeca8a3e3">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--ndis-pd-counter-parameters.md">NDIS_PD_COUNTER_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-pd-free-counter.md">NdisPDFreeCounter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PD_ALLOCATE_COUNTER callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
