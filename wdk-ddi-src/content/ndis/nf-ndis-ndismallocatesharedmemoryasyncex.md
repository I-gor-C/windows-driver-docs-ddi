---
UID: NF.ndis.NdisMAllocateSharedMemoryAsyncEx
title: NdisMAllocateSharedMemoryAsyncEx
author: windows-driver-content
description: Miniport drivers call the NdisMAllocateSharedMemoryAsyncEx function to allocate additional memory shared between the driver and its bus-master DMA NIC, usually when the miniport driver is running low on available NIC receive buffers.
old-location: netvista\ndismallocatesharedmemoryasyncex.htm
old-project: netvista
ms.assetid: ccbe98ca-7da9-4159-ac1a-c25ec6745ff4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMAllocateSharedMemoryAsyncEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMAllocateSharedMemoryAsyncEx
req.alt-loc: ndis.h
req.ddi-compliance: Irql_Gather_DMA_Function
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

# NdisMAllocateSharedMemoryAsyncEx function



## -description
<p>Miniport drivers call the 
  <b>NdisMAllocateSharedMemoryAsyncEx</b> function to allocate additional memory shared between the driver and
  its bus-master DMA NIC, usually when the miniport driver is running low on available NIC receive
  buffers.</p>


## -syntax

````
NDIS_STATUS NdisMAllocateSharedMemoryAsyncEx(
  _In_ NDIS_HANDLE MiniportDmaHandle,
  _In_ ULONG       Length,
  _In_ BOOLEAN     Cached,
  _In_ PVOID       Context
);
````


## -parameters
<dl>

### -param <i>MiniportDmaHandle</i> [in]

<dd>
<p>A handle to a context area that NDIS uses to manage a DMA resource. The caller obtained this
     handle by calling the 
     <a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
     NdisMRegisterScatterGatherDma</a> function.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to allocate.</p>
</dd>

### -param <i>Cached</i> [in]

<dd>
<p>This parameter is ignored (cached memory is always used on x86 and x64 systems).</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to driver-determined context to be passed to the 
     <a href="..\ndis\nc-ndis-miniport-allocate-shared-mem-complete.md">MiniportSharedMemoryAllocateComplete</a> function when it is called.</p>
</dd>
</dl>

## -returns
<p><b>NdisMAllocateSharedMemoryAsyncEx</b> can return one of the following:</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>NDIS will call the 
       <a href="..\ndis\nc-ndis-miniport-allocate-shared-mem-complete.md">MiniportSharedMemoryAllocateComplete</a> function and provide information that describes the
       allocated shared memory. If the attempt to allocate shared memory fails, NDIS calls 
       <i>MiniportSharedMemoryAllocateComplete</i> and passes <b>NULL</b> pointers.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The requested memory could not be allocated at this time. If 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff562784">NdisMAllocateSharedMemoryAsyncEx</a> returns this status, a subsequent call with the same parameters
       might succeed, depending on whether system resources have become available.</p>

<p> </p>

## -remarks
<p>Drivers of bus-master DMA NICs call 
    <b>NdisMAllocateSharedMemoryAsyncEx</b> to dynamically allocate shared memory. Such drivers also allocate
    shared memory space during initialization. These drivers use the dynamically allocated shared memory for
    transfer operations when high network traffic places excessive demands on the existing shared memory
    space.</p>

<p>Such a miniport driver usually maintains one or more state variables to track the number of shared
    memory buffers available for incoming transfers. When the number of available buffers reaches a
    driver-determined low, the miniport driver calls 
    <b>NdisMAllocateSharedMemoryAsyncEx</b> to allocate more buffer space in shared memory. When the number of
    available buffers climbs to a driver-determined high, the miniport driver calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563589">NdisMFreeSharedMemory</a> one or more
    times to release its preceding dynamic allocations.</p>

<p>Usually, such a miniport driver retains the block of shared memory that its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function
    allocated with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562782">NdisMAllocateSharedMemory</a> until
    a NIC is removed. When the NIC is removed, NDIS calls the miniport driver's 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function. This allocation
    is sufficient to handle an average demand for transfers through the NIC.</p>

<p>A miniport driver should set a limit on how much shared memory it can allocate. This limit is
    driver-specific and should be high enough so that the driver does not run out of buffers. Do not et a
    limit that is excessively high, as this could result in a wasteful consumption of shared memory that
    could reduce system performance.</p>

<p>Any miniport driver that calls 
    <b>NdisMAllocateSharedMemoryAsyncEx</b> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562782">NdisMAllocateSharedMemory</a> must release all outstanding allocations with one or more calls to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563589">NdisMFreeSharedMemory</a> when its NIC is removed.</p>

<p>Drivers of bus-master DMA NICs call 
    <b>NdisMAllocateSharedMemoryAsyncEx</b> to dynamically allocate shared memory. Such drivers also allocate
    shared memory space during initialization. These drivers use the dynamically allocated shared memory for
    transfer operations when high network traffic places excessive demands on the existing shared memory
    space.</p>

<p>Such a miniport driver usually maintains one or more state variables to track the number of shared
    memory buffers available for incoming transfers. When the number of available buffers reaches a
    driver-determined low, the miniport driver calls 
    <b>NdisMAllocateSharedMemoryAsyncEx</b> to allocate more buffer space in shared memory. When the number of
    available buffers climbs to a driver-determined high, the miniport driver calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563589">NdisMFreeSharedMemory</a> one or more
    times to release its preceding dynamic allocations.</p>

<p>Usually, such a miniport driver retains the block of shared memory that its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function
    allocated with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562782">NdisMAllocateSharedMemory</a> until
    a NIC is removed. When the NIC is removed, NDIS calls the miniport driver's 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function. This allocation
    is sufficient to handle an average demand for transfers through the NIC.</p>

<p>A miniport driver should set a limit on how much shared memory it can allocate. This limit is
    driver-specific and should be high enough so that the driver does not run out of buffers. Do not et a
    limit that is excessively high, as this could result in a wasteful consumption of shared memory that
    could reduce system performance.</p>

<p>Any miniport driver that calls 
    <b>NdisMAllocateSharedMemoryAsyncEx</b> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562782">NdisMAllocateSharedMemory</a> must release all outstanding allocations with one or more calls to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563589">NdisMFreeSharedMemory</a> when its NIC is removed.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547934">Irql_Gather_DMA_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-allocate-shared-mem-complete.md">
   MiniportSharedMemoryAllocateComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562782">NdisMAllocateSharedMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563589">NdisMFreeSharedMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563646">NdisMRegisterDmaChannel</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
   NdisMRegisterScatterGatherDma</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMAllocateSharedMemoryAsyncEx function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
