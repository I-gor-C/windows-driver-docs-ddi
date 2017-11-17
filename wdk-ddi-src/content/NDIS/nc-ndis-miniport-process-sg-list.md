---
UID: NC.ndis.MINIPORT_PROCESS_SG_LIST
title: MINIPORT_PROCESS_SG_LIST
author: windows-driver-content
description: A bus-master miniport driver provides a MiniportProcessSGList function to process scatter/gather lists for network data.
old-location: netvista\miniportprocesssglist.htm
ms.assetid: ddd5d14f-f886-40d0-9fc8-eeb37da63ebd
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
req.alt-api: MiniportProcessSGList
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
req.irql: DISPATCH_LEVEL
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# MINIPORT_PROCESS_SG_LIST callback



## -description
<p>A bus-master miniport driver provides a
   <i>MiniportProcessSGList</i> function to process scatter/gather lists for network data.</p>


## -prototype

````
MINIPORT_PROCESS_SG_LIST MiniportProcessSGList;

VOID MiniportProcessSGList(
  _In_ PDEVICE_OBJECT       pDO,
  _In_ PVOID                Reserved,
  _In_ PSCATTER_GATHER_LIST pSGL,
  _In_ PVOID                Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>pDO</i> [in]

<dd>
<p>Miniport drivers should ignore this parameter.</p>
</dd>

### -param <i>Reserved</i> [in]

<dd>
<p>Miniport drivers should ignore this parameter.</p>
</dd>

### -param <i>pSGL</i> [in]

<dd>
<p>A pointer to a scatter/gather list buffer. This is not necessarily the same buffer as the one the
     driver specified in the call to the 
     <a href="https://msdn.microsoft.com/3fd8d121-a249-433a-a93d-4027a4bfcb61">
     NdisMAllocateNetBufferSGList</a> function</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to a context area that the miniport driver created prior to calling 
     <b>NdisMAllocateNetBufferSGList</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Miniport drivers call the 
    <a href="https://msdn.microsoft.com/90ce64a2-9140-4b5f-88aa-b4f01a3d0c6f">
    NdisMRegisterScatterGatherDma</a> function to register a 
    <i>MiniportProcessSGList</i> function. When a miniport driver calls 
    <b>NdisMAllocateNetBufferSGList</b> to create a scatter/gather list, NDIS calls HAL to create the list.
    After creating the list, NDIS calls the miniport driver's 
    <i>MiniportProcessSGList</i> function.</p>

<p>When NDIS calls 
    <i>MiniportProcessSGList</i>, the driver can send the NET_BUFFER structure to the hardware. MiniportProcessSGList submits the physical addresses of the scatter/gather list to the NIC's DMA
    and issues a send command to the NIC.</p>

<p>HAL can call 
    <i>MiniportProcessSGList</i> before or after NDIS returns from 
    <b>NdisMAllocateNetBufferSGList</b>. Therefore, driver writers should not assume that the call is made
    within the context of 
    <b>NdisMAllocateNetBufferSGList</b>.</p>

<p>NDIS calls 
    <i>MiniportProcessSGList</i> at IRQL = DISPATCH_LEVEL.</p>

<p>To define a <i>MiniportProcessSGList</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportProcessSGList</i> function that is named "MyProcessSGList", use the <b>MINIPORT_PROCESS_SG_LIST</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_PROCESS_SG_LIST</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_PROCESS_SG_LIST</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>Miniport drivers call the 
    <a href="https://msdn.microsoft.com/90ce64a2-9140-4b5f-88aa-b4f01a3d0c6f">
    NdisMRegisterScatterGatherDma</a> function to register a 
    <i>MiniportProcessSGList</i> function. When a miniport driver calls 
    <b>NdisMAllocateNetBufferSGList</b> to create a scatter/gather list, NDIS calls HAL to create the list.
    After creating the list, NDIS calls the miniport driver's 
    <i>MiniportProcessSGList</i> function.</p>

<p>When NDIS calls 
    <i>MiniportProcessSGList</i>, the driver can send the NET_BUFFER structure to the hardware. MiniportProcessSGList submits the physical addresses of the scatter/gather list to the NIC's DMA
    and issues a send command to the NIC.</p>

<p>HAL can call 
    <i>MiniportProcessSGList</i> before or after NDIS returns from 
    <b>NdisMAllocateNetBufferSGList</b>. Therefore, driver writers should not assume that the call is made
    within the context of 
    <b>NdisMAllocateNetBufferSGList</b>.</p>

<p>NDIS calls 
    <i>MiniportProcessSGList</i> at IRQL = DISPATCH_LEVEL.</p>

<p>To define a <i>MiniportProcessSGList</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportProcessSGList</i> function that is named "MyProcessSGList", use the <b>MINIPORT_PROCESS_SG_LIST</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_PROCESS_SG_LIST</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_PROCESS_SG_LIST</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562776">NdisMAllocateNetBufferSGList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/90ce64a2-9140-4b5f-88aa-b4f01a3d0c6f">
   NdisMRegisterScatterGatherDma</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_PROCESS_SG_LIST callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
