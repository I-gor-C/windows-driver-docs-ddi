---
UID: NS.d3dukmdt._D3DDDI_CREATEHWQUEUEFLAGS
title: D3DDDI_CREATEHWQUEUEFLAGS
author: windows-driver-content
description: A structure used to create hardware queue flags.
old-location: display\d3dddi_createhwqueueflags_.htm
old-project: display
ms.assetid: 50318DEC-8EE4-4208-8E7D-E8BFEA4BA06B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_CREATEHWQUEUEFLAGS, D3DDDI_CREATEHWQUEUEFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_CREATEHWQUEUEFLAGS
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
req.iface: 
---

# D3DDDI_CREATEHWQUEUEFLAGS structure



## -description
<p>A structure used to create hardware queue flags.</p>


## -syntax

````
typedef struct _D3DDDI_CREATEHWQUEUEFLAGS  {
  union {
    struct {
      UINT DisableGpuTimeout  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} D3DDDI_CREATEHWQUEUEFLAGS ;
````


## -struct-fields
<dl>

### -field DisableGpuTimeout

<dd>
<p>Indicates that GPU timeout should be disabled.</p>
</dd>

### -field Reserved

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field Value

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