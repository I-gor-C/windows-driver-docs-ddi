---
UID: NS.d3dkmddi._DXGK_QUERYDISPLAYIDOUT
title: DXGK_QUERYDISPLAYIDOUT
author: windows-driver-content
description: Used to query a display ID.
old-location: display\dxgk_querydisplayidout.htm
ms.assetid: BF528089-0194-4A3F-B8BA-85F80974C4C2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_QUERYDISPLAYIDOUT
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
ms.keywords: DXGK_QUERYDISPLAYIDOUT, DXGK_QUERYDISPLAYIDOUT
req.iface: 
---

# DXGK_QUERYDISPLAYIDOUT structure



## -description
<p>Used to query a display ID.</p>


## -syntax

````
typedef struct _DXGK_QUERYDISPLAYIDOUT {
  UINT Length;
  BYTE *pDescriptor;
} DXGK_QUERYDISPLAYIDOUT;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>The length of the Display ID.</p>
</dd>

### -field <b>pDescriptor</b>

<dd>
<p>A pointer to the descriptor of the ID.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>