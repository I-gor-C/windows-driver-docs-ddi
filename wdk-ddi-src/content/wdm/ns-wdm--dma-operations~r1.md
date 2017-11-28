---
UID: NS.wdm._DMA_OPERATIONS~r1
title: DMA_OPERATIONS
author: windows-driver-content
description: The DMA_OPERATIONS structure provides a table of pointers to functions that control the operation of a DMA controller.
old-location: kernel\dma_operations.htm
old-project: kernel
ms.assetid: b4a5d830-252b-410e-be2c-390371af971c
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: DMA_OPERATIONS, DMA_OPERATIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DMA_OPERATIONS
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# DMA_OPERATIONS structure



## -description
<p>The <b>DMA_OPERATIONS</b> structure provides a table of pointers to functions that control the operation of a DMA controller.</p>


## -syntax

````
typedef struct _DMA_OPERATIONS {
  ULONG                               Size;
  PPUT_DMA_ADAPTER                    PutDmaAdapter;
  PALLOCATE_COMMON_BUFFER             AllocateCommonBuffer;
  PFREE_COMMON_BUFFER                 FreeCommonBuffer;
  PALLOCATE_ADAPTER_CHANNEL           AllocateAdapterChannel;
  PFLUSH_ADAPTER_BUFFERS              FlushAdapterBuffers;
  PFREE_ADAPTER_CHANNEL               FreeAdapterChannel;
  PFREE_MAP_REGISTERS                 FreeMapRegisters;
  PMAP_TRANSFER                       MapTransfer;
  PGET_DMA_ALIGNMENT                  GetDmaAlignment;
  PREAD_DMA_COUNTER                   ReadDmaCounter;
  PGET_SCATTER_GATHER_LIST            GetScatterGatherList;
  PPUT_SCATTER_GATHER_LIST            PutScatterGatherList;
  PCALCULATE_SCATTER_GATHER_LIST_SIZE CalculateScatterGatherList;
  PBUILD_SCATTER_GATHER_LIST          BuildScatterGatherList;
  PBUILD_MDL_FROM_SCATTER_GATHER_LIST BuildMdlFromScatterGatherList;
  PGET_DMA_ADAPTER_INFO               GetDmaAdapterInfo;
  PGET_DMA_TRANSFER_INFO              GetDmaTransferInfo;
  PINITIALIZE_DMA_TRANSFER_CONTEXT    InitializeDmaTransferContext;
  PALLOCATE_COMMON_BUFFER_EX          AllocateCommonBufferEx;
  PALLOCATE_ADAPTER_CHANNEL_EX        AllocateAdapterChannelEx;
  PCONFIGURE_ADAPTER_CHANNEL          ConfigureAdapterChannel;
  PCANCEL_ADAPTER_CHANNEL             CancelAdapterChannel;
  PMAP_TRANSFER_EX                    MapTransferEx;
  PGET_SCATTER_GATHER_LIST_EX         GetScatterGatherListEx;
  PBUILD_SCATTER_GATHER_LIST_EX       BuildScatterGatherListEx;
  PFLUSH_ADAPTER_BUFFERS_EX           FlushAdapterBuffersEx;
  PFREE_ADAPTER_OBJECT                FreeAdapterObject;
  PCANCEL_MAPPED_TRANSFER             CancelMappedTransfer;
} DMA_OPERATIONS, *PDMA_OPERATIONS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this <b>DMA_OPERATIONS</b> structure.</p>
</dd>

### -field <b>PutDmaAdapter</b>

<dd>
<p>A pointer to a system-defined routine to free a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544062">DMA_ADAPTER</a> structure. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559965">PutDmaAdapter</a>.</p>
</dd>

### -field <b>AllocateCommonBuffer</b>

<dd>
<p>A pointer to a system-defined routine to allocate a physically contiguous DMA buffer. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540575">AllocateCommonBuffer</a>.</p>
</dd>

### -field <b>FreeCommonBuffer</b>

<dd>
<p>A pointer to a system-defined routine to free a physically contiguous DMA buffer previously allocated by <b>AllocateCommonBuffer</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546511">FreeCommonBuffer</a>.</p>
</dd>

### -field <b>AllocateAdapterChannel</b>

<dd>
<p>A pointer to a system-defined routine to allocate a channel for DMA operations. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540573">AllocateAdapterChannel</a>.</p>
</dd>

### -field <b>FlushAdapterBuffers</b>

<dd>
<p>A pointer to a system-defined routine to flush data from the system or bus-master adapter's internal cache after a DMA operation. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545917">FlushAdapterBuffers</a>.</p>
</dd>

### -field <b>FreeAdapterChannel</b>

<dd>
<p>A pointer to a system-defined routine to free a channel previously allocated for DMA operations by <b>AllocateAdapterChannel</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546507">FreeAdapterChannel</a>.</p>
</dd>

### -field <b>FreeMapRegisters</b>

<dd>
<p>A pointer to a system-defined routine to free map registers allocated for DMA operations. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546513">FreeMapRegisters</a>.</p>
</dd>

### -field <b>MapTransfer</b>

<dd>
<p>A pointer to a system-defined routine to begin a DMA operation. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554402">MapTransfer</a>.</p>
</dd>

### -field <b>GetDmaAlignment</b>

<dd>
<p>A pointer to a system-defined routine to obtain the DMA alignment requirements of the controller. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546530">GetDmaAlignment</a>.</p>
</dd>

### -field <b>ReadDmaCounter</b>

<dd>
<p>A pointer to a system-defined routine to obtain the current transfer count for a DMA operation. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560782">ReadDmaCounter</a>.</p>
</dd>

### -field <b>GetScatterGatherList</b>

<dd>
<p>A pointer to a system-defined routine that allocates map registers and creates a scatter/gather list for DMA. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546531">GetScatterGatherList</a>.</p>
</dd>

### -field <b>PutScatterGatherList</b>

<dd>
<p>A pointer to a system-defined routine that frees map registers and a scatter/gather list after a DMA operation is complete. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559967">PutScatterGatherList</a>.</p>
</dd>

### -field <b>CalculateScatterGatherList</b>

<dd>
<p>A pointer to a system-defined routine that determines the buffer size needed to hold the scatter/gather list that describes an I/O data  buffer. This member is available only in versions 2 and later of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540716">CalculateScatterGatherList</a>.</p>
</dd>

### -field <b>BuildScatterGatherList</b>

<dd>
<p>A pointer to a system-defined routine that allocates map registers and creates a scatter/gather list for DMA in a driver-supplied buffer. This member is available only in versions 2 and later of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540689">BuildScatterGatherList</a>.</p>
</dd>

### -field <b>BuildMdlFromScatterGatherList</b>

<dd>
<p>A pointer to a system-defined routine that builds an MDL corresponding to a scatter/gather list. This member is available only in versions 2 and later of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540686">BuildMdlFromScatterGatherList</a>.</p>
</dd>

### -field <b>GetDmaAdapterInfo</b>

<dd>
<p>A pointer to a system-defined routine that describes the capabilities of a bus-master DMA device or a system DMA controller. <b>GetDmaAdapterInfo</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451121">GetDmaAdapterInfo</a>.</p>
</dd>

### -field <b>GetDmaTransferInfo</b>

<dd>
<p>A pointer to a system-defined routine that describes the allocation requirements for a scatter/gather list. This routine replaces <a href="https://msdn.microsoft.com/library/windows/hardware/ff540716">CalculateScatterGatherList</a>. <b>GetDmaTransferInfo</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451125">GetDmaTransferInfo</a>.</p>
</dd>

### -field <b>InitializeDmaTransferContext</b>

<dd>
<p>A pointer to a system-defined routine that initializes an opaque DMA transfer context. The operating system stores the internal status of a DMA transfer in this context. <b>InitializeDmaTransferContext</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451191">InitializeDmaTransferContext</a>.</p>
</dd>

### -field <b>AllocateCommonBufferEx</b>

<dd>
<p>A pointer to a system-defined routine that allocates memory for a common buffer and maps this memory so that it can accessed both by the processor and by a DMA device. <b>AllocateCommonBufferEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406344">AllocateCommonBufferEx</a>.</p>
</dd>

### -field <b>AllocateAdapterChannelEx</b>

<dd>
<p>A pointer to a system-defined routine that allocates the resources required for a DMA transfer and then calls the driver-supplied <i>AdapterControl</i> routine to initiate the DMA transfer. <b>AllocateAdapterChannelEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406340">AllocateAdapterChannelEx</a>.</p>
</dd>

### -field <b>ConfigureAdapterChannel</b>

<dd>
<p>A pointer to a system-defined routine enables a custom function that is implemented by the DMA controller. <b>ConfigureAdapterChannel</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh450939">ConfigureAdapterChannel</a>.</p>
</dd>

### -field <b>CancelAdapterChannel</b>

<dd>
<p>A pointer to a system-defined routine that tries to cancel a pending request to allocate a DMA channel. <b>CancelAdapterChannel</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406374">CancelAdapterChannel</a>.</p>
</dd>

### -field <b>MapTransferEx</b>

<dd>
<p>A pointer to a system-defined routine that sets up map registers to map the physical addresses in a scatter/gather list to the logical addresses that are required to do a DMA transfer. <b>MapTransferEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406521">MapTransferEx</a>.</p>
</dd>

### -field <b>GetScatterGatherListEx</b>

<dd>
<p>A pointer to a system-defined routine that   allocates resources required for a DMA transfer, builds a scatter/gather list, and then calls the driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff540513">AdapterListControl</a> routine to initiate the DMA transfer. <b>GetScatterGatherListEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451134">GetScatterGatherListEx</a>. This routine is a wrapper of <b>AllocateAdapterChannelEx</b> and <b>MapTransferEx</b>.</p>
</dd>

### -field <b>BuildScatterGatherListEx</b>

<dd>
<p>A pointer to a system-defined routine that   builds a scatter/gather list in a caller-allocated buffer, and then calls the driver-supplied <i>AdapterListControl</i> routine to initiate the DMA transfer. <b>BuildScatterGatherListEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406371">BuildScatterGatherListEx</a>.</p>
</dd>

### -field <b>FlushAdapterBuffersEx</b>

<dd>
<p>A pointer to a system-defined routine that  flushes any data that remains in the system DMA controller's internal cache or in a bus-master adapter's internal cache at the end of a DMA transfer. For a device that uses a system DMA controller, this routine cancels the current DMA transfer on the controller if the transfer is not complete. <b>FlushAdapterBuffersEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451102">FlushAdapterBuffersEx</a>.</p>
</dd>

### -field <b>FreeAdapterObject</b>

<dd>
<p>A pointer to a system-defined routine that releases the specified adapter object after a driver has completed all DMA operations. <b>FreeAdapterObject</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451107">FreeAdapterObject</a>.</p>
</dd>

### -field <b>CancelMappedTransfer</b>

<dd>
<p>A pointer to a system-defined routine that cancels a mapped transfer. <b>CancelMappedTransfer</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406377">CancelMappedTransfer</a>.</p>
</dd>
</dl>

## -remarks
<p>All members of this structure, with the exception of <b>Size</b>, are pointers to functions that drivers use to perform DMA operations for their devices. Drivers obtain these pointers by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a> routine. The version of the <b>DMA_OPERATIONS</b> structure that this routine returns depends on the <b>Version</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a> structure that is passed to <b>IoGetDmaAdapter</b> as an input parameter. If <b>Version</b> is DEVICE_DESCRIPTION_VERSION or DEVICE_DESCRIPTION_VERSION1, version 1 of this structure is returned. If <b>Version</b> is DEVICE_DESCRIPTION_VERSION2, version 2 of this structure is returned. Version 2 of <b>DMA_OPERATIONS</b> is available starting with  Windows XP. If <b>Version</b> is DEVICE_DESCRIPTION_VERSION3, version 3 of this structure is returned. Version 3 of <b>DMA_OPERATIONS</b> is available starting with  Windows 8.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540573">AllocateAdapterChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406340">AllocateAdapterChannelEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540575">AllocateCommonBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406344">AllocateCommonBufferEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540686">BuildMdlFromScatterGatherList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540689">BuildScatterGatherList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406371">BuildScatterGatherListEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540716">CalculateScatterGatherList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406374">CancelAdapterChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406377">CancelMappedTransfer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450939">ConfigureAdapterChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545917">FlushAdapterBuffers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451102">FlushAdapterBuffersEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546507">FreeAdapterChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451107">FreeAdapterObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546511">FreeCommonBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546513">FreeMapRegisters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451121">GetDmaAdapterInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546530">GetDmaAlignment</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451125">GetDmaTransferInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546531">GetScatterGatherList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451134">GetScatterGatherListEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451191">InitializeDmaTransferContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554402">MapTransfer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406521">MapTransferEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559965">PutDmaAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559967">PutScatterGatherList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560782">ReadDmaCounter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DMA_OPERATIONS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
