---
UID: NS.d3dkmthk._D3DKMT_CREATEHWQUEUE
title: D3DKMT_CREATEHWQUEUE
author: windows-driver-content
description: A structure holding information to create a hardware queue.
old-location: display\d3dkmt_createhwqueue.htm
old-project: display
ms.assetid: DBD99353-4798-4540-89DB-EA08521B276E
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_CREATEHWQUEUE, D3DKMT_CREATEHWQUEUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_CREATEHWQUEUE
req.alt-loc: d3dkmthk.h
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

# D3DKMT_CREATEHWQUEUE structure



## -description
<p>A structure holding information to create a hardware queue.</p>


## -syntax

````
typedef struct _D3DKMT_CREATEHWQUEUE {
  D3DKMT_HANDLE             hHwContext;
  D3DDDI_CREATEHWQUEUEFLAGS Flags;
  UINT                      PrivateDriverDataSize;
  VOID                      *pPrivateDriverData;
  D3DKMT_HANDLE             hHwQueue;
  D3DKMT_HANDLE             hHwQueueProgressFence;
  VOID                      *HwQueueProgressFenceCPUVirtualAddress;
  D3DGPU_VIRTUAL_ADDRESS    HwQueueProgressFenceGPUVirtualAddress;
} D3DKMT_CREATEHWQUEUE;
````


## -struct-fields
<dl>

### -field hHwContext

<dd>
<p>Handle to the hardware context the queue is associated with.
</p>
</dd>

### -field Flags

<dd>
<p>Hardware queue creation flags.
</p>
</dd>

### -field PrivateDriverDataSize

<dd>
<p>Size of private driver data.</p>
</dd>

### -field pPrivateDriverData

<dd>
<p>Private driver data.</p>
</dd>

### -field hHwQueue

<dd>
<p>Handle to the hardware queue object to submit work to.</p>
</dd>

### -field hHwQueueProgressFence

<dd>
<p>Handle to the monitored fence object used to monitor the queue progress.</p>
</dd>

### -field HwQueueProgressFenceCPUVirtualAddress

<dd>
<p>Read-only mapping of the queue progress fence value for the CPU.</p>
</dd>

### -field HwQueueProgressFenceGPUVirtualAddress

<dd>
<p>Read/write mapping of the queue progress fence value for the GPU.</p>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>