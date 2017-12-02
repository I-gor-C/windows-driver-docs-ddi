---
UID: NS.wdm._DMA_OPERATIONS~r1
title: DMA_OPERATIONS
author: windows-driver-content
description: The DMA_OPERATIONS structure provides a table of pointers to functions that control the operation of a DMA controller.
old-location: kernel\dma_operations.htm
old-project: kernel
ms.assetid: b4a5d830-252b-410e-be2c-390371af971c
ms.author: windowsdriverdev
ms.date: 11/28/2017
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

### -field Size

<dd>
<p>The size, in bytes, of this <b>DMA_OPERATIONS</b> structure.</p>
</dd>

### -field PutDmaAdapter

<dd>
<p>A pointer to a system-defined routine to free a <a href="..\wdm\ns-wdm--dma-adapter.md">DMA_ADAPTER</a> structure. For more information, see <a href="kernel.putdmaadapter">PutDmaAdapter</a>.</p>
</dd>

### -field AllocateCommonBuffer

<dd>
<p>A pointer to a system-defined routine to allocate a physically contiguous DMA buffer. For more information, see <a href="kernel.allocatecommonbuffer">AllocateCommonBuffer</a>.</p>
</dd>

### -field FreeCommonBuffer

<dd>
<p>A pointer to a system-defined routine to free a physically contiguous DMA buffer previously allocated by <b>AllocateCommonBuffer</b>. For more information, see <a href="kernel.freecommonbuffer">FreeCommonBuffer</a>.</p>
</dd>

### -field AllocateAdapterChannel

<dd>
<p>A pointer to a system-defined routine to allocate a channel for DMA operations. For more information, see <a href="kernel.allocateadapterchannel">AllocateAdapterChannel</a>.</p>
</dd>

### -field FlushAdapterBuffers

<dd>
<p>A pointer to a system-defined routine to flush data from the system or bus-master adapter's internal cache after a DMA operation. For more information, see <a href="kernel.flushadapterbuffers">FlushAdapterBuffers</a>.</p>
</dd>

### -field FreeAdapterChannel

<dd>
<p>A pointer to a system-defined routine to free a channel previously allocated for DMA operations by <b>AllocateAdapterChannel</b>. For more information, see <a href="kernel.freeadapterchannel">FreeAdapterChannel</a>.</p>
</dd>

### -field FreeMapRegisters

<dd>
<p>A pointer to a system-defined routine to free map registers allocated for DMA operations. For more information, see <a href="kernel.freemapregisters">FreeMapRegisters</a>.</p>
</dd>

### -field MapTransfer

<dd>
<p>A pointer to a system-defined routine to begin a DMA operation. For more information, see <a href="kernel.maptransfer">MapTransfer</a>.</p>
</dd>

### -field GetDmaAlignment

<dd>
<p>A pointer to a system-defined routine to obtain the DMA alignment requirements of the controller. For more information, see <a href="kernel.getdmaalignment">GetDmaAlignment</a>.</p>
</dd>

### -field ReadDmaCounter

<dd>
<p>A pointer to a system-defined routine to obtain the current transfer count for a DMA operation. For more information, see <a href="kernel.readdmacounter">ReadDmaCounter</a>.</p>
</dd>

### -field GetScatterGatherList

<dd>
<p>A pointer to a system-defined routine that allocates map registers and creates a scatter/gather list for DMA. For more information, see <a href="kernel.getscattergatherlist">GetScatterGatherList</a>.</p>
</dd>

### -field PutScatterGatherList

<dd>
<p>A pointer to a system-defined routine that frees map registers and a scatter/gather list after a DMA operation is complete. For more information, see <a href="kernel.putscattergatherlist">PutScatterGatherList</a>.</p>
</dd>

### -field CalculateScatterGatherList

<dd>
<p>A pointer to a system-defined routine that determines the buffer size needed to hold the scatter/gather list that describes an I/O data  buffer. This member is available only in versions 2 and later of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.calculatescattergatherlist">CalculateScatterGatherList</a>.</p>
</dd>

### -field BuildScatterGatherList

<dd>
<p>A pointer to a system-defined routine that allocates map registers and creates a scatter/gather list for DMA in a driver-supplied buffer. This member is available only in versions 2 and later of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.buildscattergatherlist">BuildScatterGatherList</a>.</p>
</dd>

### -field BuildMdlFromScatterGatherList

<dd>
<p>A pointer to a system-defined routine that builds an MDL corresponding to a scatter/gather list. This member is available only in versions 2 and later of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.buildmdlfromscattergatherlist">BuildMdlFromScatterGatherList</a>.</p>
</dd>

### -field GetDmaAdapterInfo

<dd>
<p>A pointer to a system-defined routine that describes the capabilities of a bus-master DMA device or a system DMA controller. <b>GetDmaAdapterInfo</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.getdmaadapterinfo">GetDmaAdapterInfo</a>.</p>
</dd>

### -field GetDmaTransferInfo

<dd>
<p>A pointer to a system-defined routine that describes the allocation requirements for a scatter/gather list. This routine replaces <a href="kernel.calculatescattergatherlist">CalculateScatterGatherList</a>. <b>GetDmaTransferInfo</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.getdmatransferinfo">GetDmaTransferInfo</a>.</p>
</dd>

### -field InitializeDmaTransferContext

<dd>
<p>A pointer to a system-defined routine that initializes an opaque DMA transfer context. The operating system stores the internal status of a DMA transfer in this context. <b>InitializeDmaTransferContext</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.initializedmatransfercontext">InitializeDmaTransferContext</a>.</p>
</dd>

### -field AllocateCommonBufferEx

<dd>
<p>A pointer to a system-defined routine that allocates memory for a common buffer and maps this memory so that it can accessed both by the processor and by a DMA device. <b>AllocateCommonBufferEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.allocatecommonbufferex">AllocateCommonBufferEx</a>.</p>
</dd>

### -field AllocateAdapterChannelEx

<dd>
<p>A pointer to a system-defined routine that allocates the resources required for a DMA transfer and then calls the driver-supplied <i>AdapterControl</i> routine to initiate the DMA transfer. <b>AllocateAdapterChannelEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.allocateadapterchannelex">AllocateAdapterChannelEx</a>.</p>
</dd>

### -field ConfigureAdapterChannel

<dd>
<p>A pointer to a system-defined routine enables a custom function that is implemented by the DMA controller. <b>ConfigureAdapterChannel</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.configureadapterchannel">ConfigureAdapterChannel</a>.</p>
</dd>

### -field CancelAdapterChannel

<dd>
<p>A pointer to a system-defined routine that tries to cancel a pending request to allocate a DMA channel. <b>CancelAdapterChannel</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.canceladapterchannel">CancelAdapterChannel</a>.</p>
</dd>

### -field MapTransferEx

<dd>
<p>A pointer to a system-defined routine that sets up map registers to map the physical addresses in a scatter/gather list to the logical addresses that are required to do a DMA transfer. <b>MapTransferEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.maptransferex">MapTransferEx</a>.</p>
</dd>

### -field GetScatterGatherListEx

<dd>
<p>A pointer to a system-defined routine that   allocates resources required for a DMA transfer, builds a scatter/gather list, and then calls the driver-supplied <a href="kernel.adapterlistcontrol">AdapterListControl</a> routine to initiate the DMA transfer. <b>GetScatterGatherListEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.getscattergatherlistex">GetScatterGatherListEx</a>. This routine is a wrapper of <b>AllocateAdapterChannelEx</b> and <b>MapTransferEx</b>.</p>
</dd>

### -field BuildScatterGatherListEx

<dd>
<p>A pointer to a system-defined routine that   builds a scatter/gather list in a caller-allocated buffer, and then calls the driver-supplied <i>AdapterListControl</i> routine to initiate the DMA transfer. <b>BuildScatterGatherListEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.buildscattergatherlistex">BuildScatterGatherListEx</a>.</p>
</dd>

### -field FlushAdapterBuffersEx

<dd>
<p>A pointer to a system-defined routine that  flushes any data that remains in the system DMA controller's internal cache or in a bus-master adapter's internal cache at the end of a DMA transfer. For a device that uses a system DMA controller, this routine cancels the current DMA transfer on the controller if the transfer is not complete. <b>FlushAdapterBuffersEx</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.flushadapterbuffersex">FlushAdapterBuffersEx</a>.</p>
</dd>

### -field FreeAdapterObject

<dd>
<p>A pointer to a system-defined routine that releases the specified adapter object after a driver has completed all DMA operations. <b>FreeAdapterObject</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.freeadapterobject">FreeAdapterObject</a>.</p>
</dd>

### -field CancelMappedTransfer

<dd>
<p>A pointer to a system-defined routine that cancels a mapped transfer. <b>CancelMappedTransfer</b> is available only in version 3 of <b>DMA_OPERATIONS</b>. For more information, see <a href="kernel.cancelmappedtransfer">CancelMappedTransfer</a>.</p>
</dd>
</dl>

## -remarks
<p>All members of this structure, with the exception of <b>Size</b>, are pointers to functions that drivers use to perform DMA operations for their devices. Drivers obtain these pointers by calling the <a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a> routine. The version of the <b>DMA_OPERATIONS</b> structure that this routine returns depends on the <b>Version</b> member of the <a href="..\wdm\ns-wdm--device-description.md">DEVICE_DESCRIPTION</a> structure that is passed to <b>IoGetDmaAdapter</b> as an input parameter. If <b>Version</b> is DEVICE_DESCRIPTION_VERSION or DEVICE_DESCRIPTION_VERSION1, version 1 of this structure is returned. If <b>Version</b> is DEVICE_DESCRIPTION_VERSION2, version 2 of this structure is returned. Version 2 of <b>DMA_OPERATIONS</b> is available starting with  Windows XP. If <b>Version</b> is DEVICE_DESCRIPTION_VERSION3, version 3 of this structure is returned. Version 3 of <b>DMA_OPERATIONS</b> is available starting with  Windows 8.</p>

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
<a href="kernel.allocateadapterchannel">AllocateAdapterChannel</a>
</dt>
<dt>
<a href="kernel.allocateadapterchannelex">AllocateAdapterChannelEx</a>
</dt>
<dt>
<a href="kernel.allocatecommonbuffer">AllocateCommonBuffer</a>
</dt>
<dt>
<a href="kernel.allocatecommonbufferex">AllocateCommonBufferEx</a>
</dt>
<dt>
<a href="kernel.buildmdlfromscattergatherlist">BuildMdlFromScatterGatherList</a>
</dt>
<dt>
<a href="kernel.buildscattergatherlist">BuildScatterGatherList</a>
</dt>
<dt>
<a href="kernel.buildscattergatherlistex">BuildScatterGatherListEx</a>
</dt>
<dt>
<a href="kernel.calculatescattergatherlist">CalculateScatterGatherList</a>
</dt>
<dt>
<a href="kernel.canceladapterchannel">CancelAdapterChannel</a>
</dt>
<dt>
<a href="kernel.cancelmappedtransfer">CancelMappedTransfer</a>
</dt>
<dt>
<a href="kernel.configureadapterchannel">ConfigureAdapterChannel</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--device-description.md">DEVICE_DESCRIPTION</a>
</dt>
<dt>
<a href="kernel.flushadapterbuffers">FlushAdapterBuffers</a>
</dt>
<dt>
<a href="kernel.flushadapterbuffersex">FlushAdapterBuffersEx</a>
</dt>
<dt>
<a href="kernel.freeadapterchannel">FreeAdapterChannel</a>
</dt>
<dt>
<a href="kernel.freeadapterobject">FreeAdapterObject</a>
</dt>
<dt>
<a href="kernel.freecommonbuffer">FreeCommonBuffer</a>
</dt>
<dt>
<a href="kernel.freemapregisters">FreeMapRegisters</a>
</dt>
<dt>
<a href="kernel.getdmaadapterinfo">GetDmaAdapterInfo</a>
</dt>
<dt>
<a href="kernel.getdmaalignment">GetDmaAlignment</a>
</dt>
<dt>
<a href="kernel.getdmatransferinfo">GetDmaTransferInfo</a>
</dt>
<dt>
<a href="kernel.getscattergatherlist">GetScatterGatherList</a>
</dt>
<dt>
<a href="kernel.getscattergatherlistex">GetScatterGatherListEx</a>
</dt>
<dt>
<a href="kernel.initializedmatransfercontext">InitializeDmaTransferContext</a>
</dt>
<dt>
<a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a>
</dt>
<dt>
<a href="kernel.maptransfer">MapTransfer</a>
</dt>
<dt>
<a href="kernel.maptransferex">MapTransferEx</a>
</dt>
<dt>
<a href="kernel.putdmaadapter">PutDmaAdapter</a>
</dt>
<dt>
<a href="kernel.putscattergatherlist">PutScatterGatherList</a>
</dt>
<dt>
<a href="kernel.readdmacounter">ReadDmaCounter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DMA_OPERATIONS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
