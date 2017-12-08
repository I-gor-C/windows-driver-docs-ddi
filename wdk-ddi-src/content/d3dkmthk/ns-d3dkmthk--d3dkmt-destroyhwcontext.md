---
UID: NS.d3dkmthk._D3DKMT_DESTROYHWCONTEXT
title: D3DKMT_DESTROYHWCONTEXT
author: windows-driver-content
description: A structure holding information to destroy a hardware context.
old-location: display\d3dkmt_destroyhwcontext.htm
old-project: display
ms.assetid: DFFFE90A-C505-466A-B415-AA6C6352421B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_DESTROYHWCONTEXT, D3DKMT_DESTROYHWCONTEXT
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
req.alt-api: D3DKMT_DESTROYHWCONTEXT
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

# D3DKMT_DESTROYHWCONTEXT structure



## -description
<p>A structure holding information to destroy a hardware context.</p>


## -syntax

````
typedef struct _D3DKMT_DESTROYHWCONTEXT {
  D3DKMT_HANDLE hHwContext;
} D3DKMT_DESTROYHWCONTEXT;
````


## -struct-fields
<dl>

### -field hHwContext

<dd>
<p>A handle that identifies the context being destroyed.
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>