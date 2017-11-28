---
UID: NS.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_CAPS
title: DXGI_DDI_MULTIPLANE_OVERLAY_CAPS
author: windows-driver-content
description: Used by the user-mode display driver to specify overlay plane capabilities.
old-location: display\dxgi_ddi_multiplane_overlay_caps.htm
old-project: display
ms.assetid: 269d9a51-bc01-4de4-b160-35c725c174f7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_DDI_MULTIPLANE_OVERLAY_CAPS, DXGI_DDI_MULTIPLANE_OVERLAY_CAPS
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
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_CAPS
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

# DXGI_DDI_MULTIPLANE_OVERLAY_CAPS structure



## -description
<p>Used by the user-mode display driver to specify overlay plane capabilities.</p>


## -syntax

````
typedef struct DXGI_DDI_MULTIPLANE_OVERLAY_CAPS {
  UINT MaxPlanes;
  UINT NumCapabilityGroups;
} DXGI_DDI_MULTIPLANE_OVERLAY_CAPS;
````


## -struct-fields
<dl>

### -field <b>MaxPlanes</b>

<dd>
<p>The maximum number of inputs, including the primary surface, to the display hardware that can be supported in the current mode. This value can change if the mode changes.</p>
<p>For example, if the hardware allows one overlay plane and one normal primary surface, the driver should set <b>MaxPlanes</b> to 2.</p>
</dd>

### -field <b>NumCapabilityGroups</b>

<dd>
<p>The number of different types of overlay planes that can be supported.</p>
<p>Here are 2 examples:</p>
<ul>
<li>If the hardware supports 2 RGB-only planes with limited stretching capabilities, plus 2 YUV planes with more flexible stretching capabilities, then the driver should set <b>NumCapabilityGroups</b> to 2.</li>
<li>If the hardware supports one RGB-only plane with no stretching capabilities, plus 2 RGB-only planes with full  stretching capabilities, plus 2 RGB/YUV planes with full stretching capabilities, then the driver should set <b>NumCapabilityGroups</b> to 3.</li>
</ul>
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