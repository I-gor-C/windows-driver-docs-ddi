---
UID: NS.d3dumddi._D3DDDICB_CREATEHWCONTEXT
title: D3DDDICB_CREATEHWCONTEXT
author: windows-driver-content
description: A structure that gives information for creating a hardware context.
old-location: display\d3dddicb_createhwcontext.htm
ms.assetid: DA1C3976-0261-4FF1-8E49-EDF93D7BED22
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
req.alt-api: D3DDDICB_CREATEHWCONTEXT
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
ms.keywords: D3DDDICB_CREATEHWCONTEXT, D3DDDICB_CREATEHWCONTEXT
req.iface: 
---

# D3DDDICB_CREATEHWCONTEXT structure



## -description
<p>A structure that gives information for creating a hardware context.</p>


## -syntax

````
typedef struct _D3DDDICB_CREATEHWCONTEXT {
  UINT                         NodeOrdinal;
  UINT                         EngineAffinity;
  3DDDI_CREATEHWCONTEXTFLAGS   Flags;
  UINT                         PrivateDriverDataSize;
  VOID                         *pPrivateDriverData;
  HANDLE                       hHwContext;
} D3DDDICB_CREATEHWCONTEXT;
````


## -struct-fields
<dl>

### -field <b>NodeOrdinal</b>

<dd>
<p>Specifies the node ordinal this context is targeted to.</p>
</dd>

### -field <b>EngineAffinity</b>

<dd>
<p>Specifies the engine affinity within the node.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Hardware context creation flags.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>Size of private driver data.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>Pointer to private driver data.</p>
</dd>

### -field <b>hHwContext</b>

<dd>
<p>Handle to the created context.</p>
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