---
UID: NS.d3dkmthk._D3DKMT_DESTROYHWQUEUE
title: D3DKMT_DESTROYHWQUEUE
author: windows-driver-content
description: A structure holding information to destroy a hardware queue.
old-location: display\d3dkmt_destroyhwqueue.htm
old-project: display
ms.assetid: 076B47F5-8312-43E3-AE75-D4DDA8C0A181
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_DESTROYHWQUEUE, D3DKMT_DESTROYHWQUEUE
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
req.alt-api: D3DKMT_DESTROYHWQUEUE
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

# D3DKMT_DESTROYHWQUEUE structure



## -description
<p>A structure holding information to destroy a hardware queue.</p>


## -syntax

````
typedef struct _D3DKMT_DESTROYHWQUEUE {
  D3DKMT_HANDLE hHwQueue;
} D3DKMT_DESTROYHWQUEUE;
````


## -struct-fields
<dl>

### -field hHwQueue

<dd>
<p>Handle to the hardware queue to be destroyed.
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