---
UID: NS.d3dumddi._D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE
title: D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE
author: windows-driver-content
description: A structure that holds information to wait for synchronized objects.
old-location: display\d3dddicb_submitwaitforsyncobjectstohwqueue.htm
ms.assetid: 9890EB61-2CED-41AB-9A87-76D5020D84A0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE
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
ms.keywords: D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE, D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE
req.iface: 
---

# D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE structure



## -description
<p>A structure that holds information to wait for synchronized objects. </p>


## -syntax

````
typedef struct _D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE {
  HANDLE              hHwQueue;
  UINT                ObjectCount;
  const D3DKMT_HANDLE *ObjectHandleArray;
  const UINT64        *FenceValueArray;
} D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE;
````


## -struct-fields
<dl>

### -field <b>hHwQueue</b>

<dd>
<p>Hardware queue to queue the wait on.
</p>
</dd>

### -field <b>ObjectCount</b>

<dd>
<p>Number of objects to wait on.
</p>
</dd>

### -field <b>ObjectHandleArray</b>

<dd>
<p>Handles to monitored fence synchronization objects to wait on.
</p>
</dd>

### -field <b>FenceValueArray</b>

<dd>
<p>Monitored fence values to be waited on.
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