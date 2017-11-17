---
UID: NS.d3dumddi._D3DDDICB_UNLOCK2
title: D3DDDICB_UNLOCK2
author: windows-driver-content
description: D3DDDICB_UNLOCK2 describes an allocation to unlock.
old-location: display\d3dddicb_unlock2.htm
ms.assetid: 3ACE32ED-75C5-440D-BAA1-470C4E043299
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_UNLOCK2
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
ms.keywords: D3DDDICB_UNLOCK2, D3DDDICB_UNLOCK2
req.iface: 
---

# D3DDDICB_UNLOCK2 structure



## -description
<p><b>D3DDDICB_UNLOCK2</b> describes an allocation to unlock.</p>


## -syntax

````
typedef struct _D3DDDICB_UNLOCK2 {
  D3DKMT_HANDLE hAllocation;
} D3DDDICB_UNLOCK2;
````


## -struct-fields
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A driver specified <b>D3DKMT_HANDLE</b> to the allocation to unlock.</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>