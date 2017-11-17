---
UID: NS.d3dkmthk._D3DKMT_MPO3DDI_SUPPORT
title: D3DKMT_MPO3DDI_SUPPORT
author: windows-driver-content
description: A structure that holds the support status.
old-location: display\d3dkmt_mpo3ddi_support.htm
ms.assetid: 993E0BC3-DE46-48B9-A346-386E49CE28CE
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_MPO3DDI_SUPPORT
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
ms.keywords: D3DKMT_MPO3DDI_SUPPORT, D3DKMT_MPO3DDI_SUPPORT
req.iface: 
---

# D3DKMT_MPO3DDI_SUPPORT structure



## -description
<p>A structure that holds the support status.</p>


## -syntax

````
typedef struct _D3DKMT_MPO3DDI_SUPPORT {
  BOOL Supported;
} D3DKMT_MPO3DDI_SUPPORT;
````


## -struct-fields
<dl>

### -field <b>Supported</b>

<dd>
<p>Indicates whether support exists.</p>
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