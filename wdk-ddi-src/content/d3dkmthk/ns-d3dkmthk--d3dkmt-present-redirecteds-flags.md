---
UID: NS.d3dkmthk._D3DKMT_PRESENT_REDIRECTEDS_FLAGS
title: D3DKMT_PRESENT_REDIRECTEDS_FLAGS
author: windows-driver-content
description: The flags used in D3DKMT_PRESENT_REDIRECTED.
old-location: display\d3dkmt-present-redirecteds-flags.htm
old-project: display
ms.assetid: 30d7d326-c25f-4a3e-af04-61629bc1a5c1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT_REDIRECTEDS_FLAGS, D3DKMT_PRESENT_REDIRECTED_FLAGS
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
req.alt-api: D3DKMT_PRESENT_REDIRECTEDS_FLAGS
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

# D3DKMT_PRESENT_REDIRECTEDS_FLAGS structure



## -description
<p>The flags used in D3DKMT_PRESENT_REDIRECTED.</p>


## -syntax

````
typedef struct _D3DKMT_PRESENT_REDIRECTEDS_FLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT Value;
  };
} D3DKMT_PRESENT_REDIRECTEDS_FLAGS;
````


## -struct-fields
<dl>

### -field Reserved

<dd>
<p>This value is reserved for use by the operating system.</p>
</dd>

### -field Value

<dd>
<p>This value is used to operate over the other members.</p>
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