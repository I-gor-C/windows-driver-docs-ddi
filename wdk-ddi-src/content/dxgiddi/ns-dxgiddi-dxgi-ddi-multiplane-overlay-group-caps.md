---
UID: NS.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS
title: DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS
author: windows-driver-content
description: Used by the user-mode display driver to specify groups of overlay plane capabilities.
old-location: display\dxgi_ddi_multiplane_overlay_group_caps.htm
old-project: display
ms.assetid: A8BAD8D4-1009-43D0-B82F-8252062A029C
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS, DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS
req.alt-loc: Dxgiddi.h
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

# DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS structure



## -description
<p>Used by the user-mode display driver to specify groups of overlay plane capabilities.</p>


## -syntax

````
typedef struct _DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS {
  UINT  NumPlanes;
  float MaxStretchFactor;
  float MaxShrinkFactor;
  UINT  OverlayCaps;
  UINT  StereoCaps;
} DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS;
````


## -struct-fields
<dl>

### -field <b>NumPlanes</b>

<dd>
<p>Specifies the number of overlay planes that are supported by the overlay planes within the capability group.</p>
</dd>

### -field <b>MaxStretchFactor</b>

<dd>
<p>Specifies the maximum stretch factor that is supported by the overlay planes within the capability group.</p>
<p>The stretch factor is the ratio of the final, stretched overlay plane size to the original size. For example, if the original overlay plane is 100 x 100 pixels, a value of 2.5 means that it can be stretched to 250 x 250 pixels.</p>
<p>It's not guaranteed that this stretch factor can be applied in all scenarios. For example, it might be possible to stretch only one overlay plane out of several using this factor.</p>
</dd>

### -field <b>MaxShrinkFactor</b>

<dd>
<p>Specifies the maximum shrink factor that is supported by the overlay planes within the capability group.</p>
<p>The shrink factor is the ratio of the final, shrunk overlay plane size to the original size. For example, if the original overlay plane is 100 x 100 pixels, a value of 0.25 means that it can be shrunk to 25 x 25 pixels.</p>
<p>It's not guaranteed that this shrink factor can be applied in all scenarios. For example, it might be possible to shrink only one overlay plane out of several using this factor.</p>
</dd>

### -field <b>OverlayCaps</b>

<dd>
<p>The overlay capabilities, given as a bitwise <b>OR</b> of values from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh780286">DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS</a> enumeration.</p>
</dd>

### -field <b>StereoCaps</b>

<dd>
<p>Reserved for system use. Set this value to zero.</p>
</dd>
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
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>