---
UID: NF.ndis.NdisMFreeSharedMemory
title: NdisMFreeSharedMemory
author: windows-driver-content
description: NdisMFreeSharedMemory frees memory that was previously allocated by NdisMAllocateSharedMemory or NdisMAllocateSharedMemoryAsyncEx by the driver of a DMA NIC.
old-location: netvista\ndismfreesharedmemory.htm
old-project: netvista
ms.assetid: 6ab11b97-e422-4ce9-b98b-51496974cb47
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisMFreeSharedMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMFreeSharedMemory (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMFreeSharedMemory (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMFreeSharedMemory
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function, NdisMFreeSharedMemory
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisMFreeSharedMemory function



## -description
<p><b>NdisMFreeSharedMemory</b> frees memory that was previously allocated by 
  <a href="..\ndis\nf-ndis-ndismallocatesharedmemory.md">NdisMAllocateSharedMemory</a> or 
  <a href="..\ndis\nf-ndis-ndismallocatesharedmemoryasyncex.md">
  NdisMAllocateSharedMemoryAsyncEx</a> by the driver of a DMA NIC.</p>


## -syntax

````
VOID NdisMFreeSharedMemory(
  _In_ NDIS_HANDLE           MiniportAdapterHandle,
  _In_ ULONG                 Length,
  _In_ BOOLEAN               Cached,
  _In_ PVOID                 VirtualAddress,
  _In_ NDIS_PHYSICAL_ADDRESS PhysicalAddress
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>Specifies the handle originally input to 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the number of bytes originally allocated.</p>
</dd>

### -param <i>Cached</i> [in]

<dd>
<p>Specifies <b>TRUE</b> if the original allocation was cacheable.</p>
</dd>

### -param <i>VirtualAddress</i> [in]

<dd>
<p>Specifies the base virtual address returned by 
     <b>NdisMAllocateSharedMemory</b> or 
     <b>NdisMAllocateSharedMemoryAsyncEx</b>.</p>
</dd>

### -param <i>PhysicalAddress</i> [in]

<dd>
<p>Specifies the corresponding physical address returned by 
     <b>NdisMAllocateSharedMemory</b> or 
     <b>NdisMAllocateSharedMemoryAsyncEx</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If it has already made a successful call to 
    <a href="..\ndis\nf-ndis-ndismallocatesharedmemory.md">NdisMAllocateSharedMemory</a> or 
    <a href="..\ndis\nf-ndis-ndismallocatesharedmemoryasyncex.md">
    NdisMAllocateSharedMemoryAsyncEx</a>, the miniport driver of a DMA device calls 
    <b>NdisMFreeSharedMemory</b> if any of the following occurs:</p>

<p>Its 
      <i>MiniportInitializeEx</i> function is unable to initialize the NIC, so this function must release all
      existing claims on hardware resources for that NIC before it returns control.</p>

<p>The NIC for which the miniport driver allocated the memory is being removed.</p>

<p>The driver is being unloaded, whether because the system is shutting down or because the user
      reconfigured the network components used in the machine.</p>

<p>The driver allocated additional shared memory with 
      <b>NdisMAllocateSharedMemoryAsyncEx</b> when I/O demand on a NIC was high but network traffic has now
      subsided to an average level.</p>

<p>A miniport driver cannot call 
    <b>NdisMFreeSharedMemory</b> to free a subrange within an allocated shared memory range. The parameters
    passed to 
    <b>NdisMFreeSharedMemory</b> must match exactly those that were passed to 
    <b>NdisMAllocateSharedMemory</b> or 
    <b>NdisMAllocateSharedMemoryAsyncEx</b>.</p>

<p><b>NdisMFreeSharedMemory</b> cannot be called from a 
    <a href="..\ndis\nc-ndis-miniport-shutdown.md">MiniportShutdownEx</a> function.</p>

<p>Microsoft Windows Server 2003, Windows XP Service Pack 1, and later versions of Windows allow both
    bus-master DMA NICs and subordinate DMA NICs to call 
    <b>NdisMFreeSharedMemory</b>. Prior releases allow only bus-master DMA NICs to call 
    <b>NdisMFreeSharedMemory</b>.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/4865da58-57eb-4386-8773-96e3fe7fb317">NdisMFreeSharedMemory (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMFreeSharedMemory (NDIS
   5.1)</b>) in Windows XP.</p>
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
<a href="devtest.ndis_irql_miniport_driver_function">Irql_Miniport_Driver_Function</a>, <a href="..\ndis\nf-ndis-ndismfreesharedmemory.md">NdisMFreeSharedMemory</a>
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
<a href="..\ndis\nc-ndis-miniport-shutdown.md">MiniportShutdownEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismallocatesharedmemory.md">NdisMAllocateSharedMemory</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismallocatesharedmemoryasyncex.md">
   NdisMAllocateSharedMemoryAsyncEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMFreeSharedMemory function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
