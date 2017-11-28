---
UID: NS.d3dumddi._D3DDDICB_CREATEHWQUEUE
title: D3DDDICB_CREATEHWQUEUE
author: windows-driver-content
description: A structure that holds information to create a hardware queue.
old-location: display\d3dddicb_createhwqueue.htm
old-project: display
ms.assetid: 085CEF61-2C2E-4F9C-B143-2E2D58C51643
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_CREATEHWQUEUE, D3DDDICB_CREATEHWQUEUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_CREATEHWQUEUE
req.alt-loc: d3dumddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# D3DDDICB_CREATEHWQUEUE structure



## -description
<p>A structure that holds information to create a hardware queue.</p>


## -syntax

````
typedef struct _D3DDDICB_CREATEHWQUEUE {
  HANDLE                     hHwContext;
  D3DDDI_CREATEHWQUEUEFLAGS Flags;
  UINT                      PrivateDriverDataSize;
  VOID                      *pPrivateDriverData;
   HANDLE                   hHwQueue;
  D3DKMT_HANDLE             hHwQueueProgressFence;
  VOID                      *HwQueueProgressFenceCPUVirtualAddress;
  D3DGPU_VIRTUAL_ADDRESS    HwQueueProgressFenceGPUVirtualAddress;
} D3DDDICB_CREATEHWQUEUE;
````


## -struct-fields
<dl>

### -field <b> hHwContext</b>

<dd>
<p>Handle to the context the queue is created for.
</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Queue creation flags.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p> Size of private driver data.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>Pointer to private driver data.</p>
</dd>

### -field <b>hHwQueue</b>

<dd>
<p>Handle to the created queue.</p>
</dd>

### -field <b>hHwQueueProgressFence</b>

<dd>
<p>Handle to the hardware queue progress fence object.
</p>
</dd>

### -field <b>HwQueueProgressFenceCPUVirtualAddress</b>

<dd>
<p>Read-only mapping of the fence value for the CPU
</p>
</dd>

### -field <b>HwQueueProgressFenceGPUVirtualAddress</b>

<dd>
<p>Read/write mapping of the fence value for the GPU
</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h</dt>
</dl>
</td>
</tr>
</table>