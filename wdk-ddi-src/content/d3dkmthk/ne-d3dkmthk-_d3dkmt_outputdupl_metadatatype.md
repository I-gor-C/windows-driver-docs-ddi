---
UID: NE.d3dkmthk._D3DKMT_OUTPUTDUPL_METADATATYPE
title: _D3DKMT_OUTPUTDUPL_METADATATYPE
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outputdupl_metadatatype.htm
old-project: display
ms.assetid: 662ddca6-628a-48e7-82dd-344f6bcfb1b1
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_OUTPUTDUPL_METADATATYPE, D3DKMT_OUTPUTDUPL_METADATATYPE
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
---

# _D3DKMT_OUTPUTDUPL_METADATATYPE enumeration



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef enum _D3DKMT_OUTPUTDUPL_METADATATYPE { 
  D3DKMT_OUTPUTDUPL_METADATATYPE_DIRTY_RECTS  = 0,
  D3DKMT_OUTPUTDUPL_METADATATYPE_MOVE_RECTS   = 1
} D3DKMT_OUTPUTDUPL_METADATATYPE;
````


## -enum-fields

### -field D3DKMT_OUTPUTDUPL_METADATATYPE_DIRTY_RECTS


### -field D3DKMT_OUTPUTDUPL_METADATATYPE_MOVE_RECTS


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>