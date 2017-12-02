---
UID: NS.d3dkmthk._D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE
title: D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE
author: windows-driver-content
description: A structure holding information to submit a signal to the hardware queue.
old-location: display\d3dkmt_submitsignalsyncobjectstohwqueue.htm
old-project: display
ms.assetid: BD192367-4960-4FD9-867F-02263AC93A61
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE, D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE
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
req.alt-api: D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE
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

# D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE structure



## -description
<p>A structure holding information to submit a signal to the hardware queue.</p>


## -syntax

````
typedef struct _D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE {
  D3DDDICB_SIGNALFLAGS Flags;
  ULONG                BroadcastHwQueueCount;
  const D3DKMT_HANDLE  *BroadcastHwQueueArray;
  UINT                 ObjectCount;
  const D3DKMT_HANDLE  *ObjectHandleArray;
  const UINT64         *FenceValueArray;
} D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE;
````


## -struct-fields
<dl>

### -field Flags

<dd>
<p>Flags that specify signal behavior.

</p>
</dd>

### -field BroadcastHwQueueCount

<dd>
<p>Specifies the number of hardware queues to broadcast this signal to.
</p>
</dd>

### -field BroadcastHwQueueArray

<dd>
<p>Specifies hardware queue handles to broadcast to.
</p>
</dd>

### -field ObjectCount

<dd>
<p>Number of objects to signal.
</p>
</dd>

### -field ObjectHandleArray

<dd>
<p>Handles to monitored fence synchronization objects to signal.</p>
</dd>

### -field FenceValueArray

<dd>
<p>Monitored fence values to signal.
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