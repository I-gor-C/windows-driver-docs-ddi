---
UID: NF.ndis.NdisMQueueDpcEx
title: NdisMQueueDpcEx
author: windows-driver-content
description: NDIS miniport drivers call the NdisMQueueDpcEx function to schedule DPC calls on CPUs.
old-location: netvista\ndismqueuedpcex.htm
ms.assetid: 22074e51-9032-4ef9-94b9-217daefcab03
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMQueueDpcEx
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: Any level
ms.keywords: NdisMQueueDpcEx
req.iface: 
---

# NdisMQueueDpcEx function



## -description
<p>NDIS miniport drivers call the 
  <b>NdisMQueueDpcEx</b> function to schedule DPC calls on CPUs.</p>


## -syntax

````
KAFFINITY NdisMQueueDpcEx(
  _In_ NDIS_HANDLE     NdisInterruptHandle,
  _In_ ULONG           MessageId,
  _In_ PGROUP_AFFINITY TargetProcessors,
  _In_ PVOID           MiniportDpcContext
);
````


## -parameters
<dl>

### -param <i>NdisInterruptHandle</i> [in]

<dd>
<p>An interrupt handle that the miniport driver obtained in a previous call to the 
     <a href="https://msdn.microsoft.com/db0b3d51-5bbb-45fb-8c45-dda8c2212b5f">
     NdisMRegisterInterruptEx</a> function.</p>
</dd>

### -param <i>MessageId</i> [in]

<dd>
<p>An MSI message ID for the DPC. If the DPC is for a line-based interrupt, this parameter is not
     used and it should be set to zero. Otherwise, 
     <i>MessageId</i> is an index to the 
     <a href="https://msdn.microsoft.com/e5007381-2436-4eb6-85cd-7145361ab793">
     IO_INTERRUPT_MESSAGE_INFO_ENTRY</a> structure inside a 
     <a href="https://msdn.microsoft.com/d740d55e-6549-494d-9b2a-39d5c2e670d3">
     IO_INTERRUPT_MESSAGE_INFO</a> structure. NDIS passes a pointer to the associated
     IO_INTERRUPT_MESSAGE_INFO structure at the 
     <b>MessageInfoTable</b> member when the driver successfully registers for MSI with the 
     <b>NdisMRegisterInterruptEx</b> function.</p>
</dd>

### -param <i>TargetProcessors</i> [in]

<dd>
<p>A bitmap that indicates target processors. NDIS should schedule a DPC for each target processor
     that is indicated in the bitmap. Each bit in 
     <i>TargetProcessors</i> identifies a CPU. If the caller sets bit 0, NDIS schedules a DPC for CPU 0. If the caller sets bit 1, NDIS
     schedules a DPC for CPU 1, and so on.</p>
</dd>

### -param <i>MiniportDpcContext</i> [in]

<dd>
<p>A pointer to a caller-specified context area. NDIS passes this pointer to the 
     <i>MiniportDpcContext</i> parameter of the 
     <a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a> and 
     <a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">
     MiniportMessageInterruptDPC</a> functions.</p>
</dd>
</dl>

## -returns
<p><b>NdisMQueueDpcEx</b> returns a bitmap that indicates target processors. Each bit in the return value
      identifies a CPU.</p>

<p>NDIS successfully scheduled a DPC for each target processor that is set in the bitmap. If NDIS sets
      bit 0, NDIS scheduled a DPC for CPU 0. If NDIS sets bit 1, NDIS scheduled a DPC for CPU 1, and so
      on.</p>

<p>If the driver requested a DPC for a CPU, and NDIS indicates that it did not schedule that DPC, the
      DPC was not scheduled because a DPC was already scheduled for that CPU.</p>

## -remarks
<p>NDIS 6.20 and later miniport drivers call 
    <b>NdisMQueueDpcEx</b> to request DPC calls for other processors. NDIS calls the 
    <a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a> or 
    <a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">
    MiniportMessageInterruptDPC</a> function to complete the deferred processing of an interrupt.</p>

<p><b>NdisMQueueDpcEx</b> is the same as the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563637">NdisMQueueDpc</a> function except that the 
    <i>TargetProcessors</i> parameter has a type of KGROUP_AFFINITY. Therefore, 
    <b>NdisMQueueDpcEx</b> can schedule DPCs on processors in any processor group. To schedule DPCs in more
    than one processor group, you can use multiple calls to 
    <b>NdisMQueueDpcEx</b>.</p>

<p>NDIS 6.20 and later miniport drivers call 
    <b>NdisMQueueDpcEx</b> to request DPC calls for other processors. NDIS calls the 
    <a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a> or 
    <a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">
    MiniportMessageInterruptDPC</a> function to complete the deferred processing of an interrupt.</p>

<p><b>NdisMQueueDpcEx</b> is the same as the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563637">NdisMQueueDpc</a> function except that the 
    <i>TargetProcessors</i> parameter has a type of KGROUP_AFFINITY. Therefore, 
    <b>NdisMQueueDpcEx</b> can schedule DPCs on processors in any processor group. To schedule DPCs in more
    than one processor group, you can use multiple calls to 
    <b>NdisMQueueDpcEx</b>.</p>

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
<p>Supported in NDIS 6.20 and later.</p>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/810503b9-75cd-4b38-ab1f-de240968ded6">MiniportInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ec2e6f49-dc40-48e8-96dc-c9440a6662a3">MiniportMessageInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">MiniportMessageInterruptDPC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563637">NdisMQueueDpc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563649">NdisMRegisterInterruptEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMQueueDpcEx function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
