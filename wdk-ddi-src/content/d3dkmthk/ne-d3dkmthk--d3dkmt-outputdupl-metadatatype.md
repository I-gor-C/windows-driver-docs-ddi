---
UID: NE.d3dkmthk._D3DKMT_OUTPUTDUPL_METADATATYPE
title: D3DKMT_OUTPUTDUPL_METADATATYPE
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outputdupl_metadatatype.htm
old-project: display
ms.assetid: 662ddca6-628a-48e7-82dd-344f6bcfb1b1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OUTPUTDUPL_METADATATYPE
req.alt-loc: D3dkmthk.h
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

# D3DKMT_OUTPUTDUPL_METADATATYPE enumeration



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef enum _D3DKMT_OUTPUTDUPL_METADATATYPE { 
  D3DKMT_OUTPUTDUPL_METADATATYPE_DIRTY_RECTS  = 0,
  D3DKMT_OUTPUTDUPL_METADATATYPE_MOVE_RECTS   = 1
} D3DKMT_OUTPUTDUPL_METADATATYPE;
````


## -enum-fields
<dl>

### -field D3DKMT_OUTPUTDUPL_METADATATYPE_DIRTY_RECTS

<dd></dd>

### -field D3DKMT_OUTPUTDUPL_METADATATYPE_MOVE_RECTS

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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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