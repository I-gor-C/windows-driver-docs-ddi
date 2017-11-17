---
UID: NS.d3dukmdt._D3DDDI_CREATEHWCONTEXTFLAGS
title: D3DDDI_CREATEHWCONTEXTFLAGS
author: windows-driver-content
description: A structure used to create hardware context flags.
old-location: display\d3dddi_createhwcontextflags.htm
ms.assetid: 429A1C54-14F0-4E50-B0D6-BB73FCFD1904
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dukmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_CREATEHWCONTEXTFLAGS
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
ms.keywords: D3DDDI_CREATEHWCONTEXTFLAGS, D3DDDI_CREATEHWCONTEXTFLAGS
req.iface: 
---

# D3DDDI_CREATEHWCONTEXTFLAGS structure



## -description
<p>A structure used to create hardware context flags.</p>


## -syntax

````
typedef struct _D3DDDI_CREATEHWCONTEXTFLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT Value;
  };
} D3DDDI_CREATEHWCONTEXTFLAGS;
````


## -struct-fields
<dl>

### -field <b>Reserved</b>

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>This value is used to operate over the members collectively.</p>
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
<dt>D3dukmdt.h</dt>
</dl>
</td>
</tr>
</table>