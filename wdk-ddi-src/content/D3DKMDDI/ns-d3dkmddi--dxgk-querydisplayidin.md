---
UID: NS.d3dkmddi._DXGK_QUERYDISPLAYIDIN
title: DXGK_QUERYDISPLAYIDIN
author: windows-driver-content
description: Used to query a display ID.
old-location: display\dxgk_querydisplayidin.htm
ms.assetid: C7A2CECA-AAE5-4804-92FF-C47984BA38AF
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
req.alt-api: DXGK_QUERYDISPLAYIDIN
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
ms.keywords: DXGK_QUERYDISPLAYIDIN, DXGK_QUERYDISPLAYIDIN
req.iface: 
---

# DXGK_QUERYDISPLAYIDIN structure



## -description
<p>Used to query a display ID.</p>


## -syntax

````
typedef struct _DXGK_QUERYDISPLAYIDIN {
  D3DDDI_VIDEO_PRESENT_TARGET_ID TargetId;
} DXGK_QUERYDISPLAYIDIN;
````


## -struct-fields
<dl>

### -field <b>TargetId</b>

<dd>
<p>The ID being queried.</p>
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