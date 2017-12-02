---
UID: NS.d3dkmthk._D3DKMT_STANDARDALLOCATION_EXISTINGHEAP
title: D3DKMT_STANDARDALLOCATION_EXISTINGHEAP
author: windows-driver-content
description: Holds information about the existing heap.
old-location: display\d3dkmt-standardallocation-existingheap.htm
old-project: display
ms.assetid: 7e97fb29-64a7-4fb5-b07e-a9810499cf1b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_STANDARDALLOCATION_EXISTINGHEAP, D3DKMT_STANDARDALLOCATION_EXISTINGHEAP
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
req.alt-api: D3DKMT_STANDARDALLOCATION_EXISTINGHEAP
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

# D3DKMT_STANDARDALLOCATION_EXISTINGHEAP structure



## -description
<p>Holds information about the existing heap.</p>


## -syntax

````
typedef struct _D3DKMT_STANDARDALLOCATION_EXISTINGHEAP {
  SIZE_T Size;
} D3DKMT_STANDARDALLOCATION_EXISTINGHEAP;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Size in bytes of the existing heap.</p>
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