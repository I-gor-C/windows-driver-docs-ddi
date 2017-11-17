---
UID: NS.d3dkmddi._DXGKARG_RENDERGDI
title: DXGKARG_RENDERGDI
author: windows-driver-content
description: The DXGKARG_RENDERGDI structure is used when submitting Windows Graphics Device Interface (GDI) commands for contexts that support virtual addressing.
old-location: display\dxgkarg_rendergdi.htm
ms.assetid: E1DC536B-581E-43F8-99B2-776DC30EEBB7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_RENDERGDI
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGKARG_RENDERGDI, DXGKARG_RENDERGDI
req.iface: 
---

# DXGKARG_RENDERGDI structure



## -description
<p>The <b>DXGKARG_RENDERGDI</b> structure is used when submitting Windows Graphics Device Interface (GDI) commands for contexts that support virtual addressing.</p>


## -syntax

````
typedef struct _DXGKARG_RENDERGDI {
  const  VOID CONST      *pCommand;
  const UINT             CommandLength;
  VOID                   *pDmaBuffer;
  D3DGPU_VIRTUAL_ADDRESS DmaBufferGpuVirtualAddress;
  UINT                   DmaSize;
  VOID                   *pDmaBufferPrivateData;
  UINT                   DmaBufferPrivateDataSize;
  DXGK_ALLOCATIONLIST    *pAllocationList;
  UINT                   AllocationListSize;
  UINT                   MultipassOffset;
} DXGKARG_RENDERGDI;
````


## -struct-fields
<dl>

### -field <b>pCommand</b>

<dd>
<p>A pointer to the start of the command buffer.</p>
</dd>

### -field <b>CommandLength</b>

<dd>
<p>The size, in bytes, of the command buffer that <b>pCommand</b> points to.</p>
</dd>

### -field <b>pDmaBuffer</b>

<dd>
<p>A pointer to the start of the DMA buffer, which is aligned on 4 KB. </p>
</dd>

### -field <b>DmaBufferGpuVirtualAddress</b>

<dd>
<p>A <b>D3DGPU_VIRTUAL_ADDRESS</b> data type that indicates the virtual address where the DMA buffer was paged in. If the physical address is zero, the DMA buffer is not correctly paged in.</p>
</dd>

### -field <b>DmaSize</b>

<dd>
<p>The size, in bytes, of the DMA buffer that <b>pDmaBuffer</b> points to.</p>
</dd>

### -field <b>pDmaBufferPrivateData</b>

<dd>
<p>A pointer to a driver-resident private data structure that is used for generating the DMA buffer that <b>pDmaBuffer</b> points to.</p>
</dd>

### -field <b>DmaBufferPrivateDataSize</b>

<dd>
<p>The number of bytes that remain in the private data structure that <b>pDmaBufferPrivateData</b> points to for the current operation.</p>
</dd>

### -field <b>pAllocationList</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560975">DXGK_ALLOCATIONLIST</a> structures for the list of allocations that the DMA buffer references. Each allocation that is referenced should appear once for optimal performance.</p>
</dd>

### -field <b>AllocationListSize</b>

<dd>
<p>The available number of elements in the array that <b>pAllocationList</b> specifies, which represents the number of allocation specifications to send through DMA to the graphics hardware.</p>
</dd>

### -field <b>MultipassOffset</b>

<dd>
<p>A value that specifies the progress of the rendering operation.</p>
</dd>
</dl>

## -remarks


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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>