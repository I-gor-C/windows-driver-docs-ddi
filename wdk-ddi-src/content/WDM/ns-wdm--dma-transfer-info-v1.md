---
UID: NS.wdm._DMA_TRANSFER_INFO_V1
title: DMA_TRANSFER_INFO_V1
author: windows-driver-content
description: The DMA_TRANSFER_INFO_V1 structure contains the allocation requirements for a scatter/gather list that describes the I/O data buffer for a DMA transfer.
old-location: kernel\dma_transfer_info_v1.htm
ms.assetid: 01EAF66D-F4E8-4D0F-A52C-900EF338FCA1
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DMA_ TRANSFER _INFO_V1
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
ms.keywords: DMA_TRANSFER_INFO_V1, DMA_TRANSFER_INFO_V1, *PDMA_TRANSFER_INFO_V1
req.iface: 
req.product: Windows 10 or later.
---

# DMA_TRANSFER_INFO_V1 structure



## -description
<p>The  <b>DMA_TRANSFER_INFO_V1</b> structure contains the allocation requirements for a scatter/gather list that describes the I/O data buffer for a DMA transfer.</p>


## -syntax

````
typedef struct _DMA_TRANSFER_INFO_V1 {
  ULONG  MapRegisterCount;
  ULONG  ScatterGatherElementCount;
  ULONG  ScatterGatherListSize;
} DMA_ TRANSFER _INFO_V1, *PDMA_ TRANSFER _INFO_V1;
````


## -struct-fields
<dl>

### -field <b>MapRegisterCount</b>

<dd>
<p>The number of map registers required to translate all the physical addresses in the scatter/gather list to logical addresses.</p>
</dd>

### -field <b>ScatterGatherElementCount</b>

<dd>
<p>The number of scatter/gather elements in the scatter/gather list. Each element is a structure of type <b>SCATTER_GATHER_ELEMENT</b>.</p>
</dd>

### -field <b>ScatterGatherListSize</b>

<dd>
<p>The required size, in bytes, of the scatter/gather buffer. This buffer contains the scatter/gather list that describes the memory that is used to buffer I/O data during the DMA transfer. The scatter/gather buffer must be large enough to contain a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563664">SCATTER_GATHER_LIST</a> structure and an array of <b>SCATTER_GATHER_ELEMENT</b> structures, plus additional data that is used internally by the operating system.</p>
</dd>
</dl>

## -remarks
<p>The <b>V1</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451001">DMA_TRANSFER_INFO</a> structure is a structure of type <b>DMA_TRANSFER_INFO_V1</b>.</p>

<p>The <i>Mdl</i>, <i>Offset</i>, and <i>Length</i> parameters to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451125">GetDmaTransferInfo</a> routine together describe the I/O data buffer for a DMA transfer. For the purpose of programming a DMA controller, this buffer can more conveniently be described by a scatter/gather list. (A scatter/gather list describes the memory in an I/O data buffer but does not contain this memory.) A driver calls <b>GetDmaTransferInfo</b> to obtain the allocation requirements for this scatter/gather list. <b>GetDmaTransferInfo</b> writes the allocation requirements into the <b>V1</b> member of a caller-supplied <b>DMA_TRANSFER_INFO</b> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451125">GetDmaTransferInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451001">DMA_TRANSFER_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563664">SCATTER_GATHER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DMA_TRANSFER_INFO_V1 structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
