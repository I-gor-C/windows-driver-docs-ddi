---
UID: NS.d3d12umddi.D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030
title: D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030
author: windows-driver-content
description: Content protection callbacks.
old-location: display\d3d12ddi-content-protection-callbacks-0030.htm
old-project: display
ms.assetid: a3a9b862-872e-4a1e-bb80-1831db983b28
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030, D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030
req.alt-loc: d3d12umddi.h
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

# D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030 structure



## -description
<p>Content protection callbacks.</p>


## -syntax

````
typedef struct _D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030 {
  PFND3D12DDI_CREATE_PROTECTED_SESSION_CB_0030  pfnCreateProtectedSessionCB;
} D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030, D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030;
````


## -struct-fields
<dl>

### -field <b>pfnCreateProtectedSessionCB</b>

<dd>
<p>Create protected session callback.</p>
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
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>