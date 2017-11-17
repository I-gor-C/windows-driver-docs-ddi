---
UID: NE.d3dkmthk._D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE
title: D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_flipmodel_independent_flip_stage.htm
ms.assetid: FF835590-36E0-4F77-80E0-45A3663D20ED
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE
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
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
req.iface: 
---

# D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE enumeration



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef enum _D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE { 
  D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE_FLIP_SUBMITTED  = 0,
  D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE_FLIP_COMPLETE   = 1
} D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE_FLIP_SUBMITTED"></a><a id="d3dkmt_flipmodel_independent_flip_stage_flip_submitted"></a><b>D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE_FLIP_SUBMITTED</b>

<dd></dd>

### -field <a id="D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE_FLIP_COMPLETE"></a><a id="d3dkmt_flipmodel_independent_flip_stage_flip_complete"></a><b>D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE_FLIP_COMPLETE</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>