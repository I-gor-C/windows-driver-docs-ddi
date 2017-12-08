---
UID: NE.d3dkmthk.D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS
title: D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_ycbcr_flags.htm
old-project: display
ms.assetid: 3bfcd424-961f-4efe-a928-2ee7fbd29f4a
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS, D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS
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

# D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS enumeration



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef enum D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS { 
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE  = 0x1,
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709          = 0x2,
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC          = 0x4
} D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS;
````


## -enum-fields

### -field D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE


### -field D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709


### -field D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC


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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>