---
UID: NS.d3dkmthk._D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE
title: D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE
author: windows-driver-content
description: A structure that contains information to submit a wait on the hardware queue.
old-location: display\d3dkmt_submitwaitforsyncobjectstohwqueue_.htm
old-project: display
ms.assetid: 365253FC-9FC0-4FFF-9D84-503754095327
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE, D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE
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
req.alt-api: D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE
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

# D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE structure



## -description
<p>A structure that contains information to submit a wait on the hardware queue.</p>


## -syntax

````
typedef struct _D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE  {
  D3DKMT_HANDLE       hHwQueue;
  UINT                ObjectCount;
  const D3DKMT_HANDLE *ObjectHandleArray;
  const UINT64        *FenceValueArray;
} D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE ;
````


## -struct-fields
<dl>

### -field hHwQueue

<dd>
<p>Context queue to submit the command to.
</p>
</dd>

### -field ObjectCount

<dd>
<p>Number of objects to wait on.
</p>
</dd>

### -field ObjectHandleArray

<dd>
<p>Handles to monitored fence synchronization objects to wait on.
</p>
</dd>

### -field FenceValueArray

<dd>
<p>Monitored fence values to be waited.
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>