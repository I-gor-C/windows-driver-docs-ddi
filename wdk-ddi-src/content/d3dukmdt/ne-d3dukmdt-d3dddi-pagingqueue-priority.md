---
UID: NE.d3dukmdt.D3DDDI_PAGINGQUEUE_PRIORITY
title: D3DDDI_PAGINGQUEUE_PRIORITY
author: windows-driver-content
description: The D3DDDI_PAGINGQUEUE_PRIORITY enumeration indicates the scheduling priority relative to other paging queues on a device.
old-location: display\d3dddi_pagingqueue_priority.htm
ms.assetid: A5CF6601-C0BF-4534-93DD-5FFA4F167CFC
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_PAGINGQUEUE_PRIORITY
req.alt-loc: d3dukmdt.h
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
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
req.iface: 
---

# D3DDDI_PAGINGQUEUE_PRIORITY enumeration



## -description
<p>The <b>D3DDDI_PAGINGQUEUE_PRIORITY</b> enumeration indicates the scheduling priority relative to other paging queues on a device.
  </p>


## -syntax

````
typedef enum D3DDDI_PAGINGQUEUE_PRIORITY { 
  D3DDDI_PAGINGQUEUE_PRIORITY_BELOW_NORMAL  = -1,
  D3DDDI_PAGINGQUEUE_PRIORITY_NORMAL        = 0,
  D3DDDI_PAGINGQUEUE_PRIORITY_ABOVE_NORMAL  = 1
} D3DDDI_PAGINGQUEUE_PRIORITY;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_PAGINGQUEUE_PRIORITY_BELOW_NORMAL"></a><a id="d3dddi_pagingqueue_priority_below_normal"></a><b>D3DDDI_PAGINGQUEUE_PRIORITY_BELOW_NORMAL</b>

<dd>
<p>Indicates below normal priority.</p>
</dd>

### -field <a id="D3DDDI_PAGINGQUEUE_PRIORITY_NORMAL"></a><a id="d3dddi_pagingqueue_priority_normal"></a><b>D3DDDI_PAGINGQUEUE_PRIORITY_NORMAL</b>

<dd>
<p>Indicates normal priority.</p>
</dd>

### -field <a id="D3DDDI_PAGINGQUEUE_PRIORITY_ABOVE_NORMAL"></a><a id="d3dddi_pagingqueue_priority_above_normal"></a><b>D3DDDI_PAGINGQUEUE_PRIORITY_ABOVE_NORMAL</b>

<dd>
<p>Indicates above normal priority.</p>
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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>