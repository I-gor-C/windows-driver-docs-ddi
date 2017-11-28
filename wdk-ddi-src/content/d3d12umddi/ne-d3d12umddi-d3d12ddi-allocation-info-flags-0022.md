---
UID: NE.d3d12umddi.D3D12DDI_ALLOCATION_INFO_FLAGS_0022
title: D3D12DDI_ALLOCATION_INFO_FLAGS_0022
author: windows-driver-content
description: Contains allocation information flags.
old-location: display\d3d12ddi_allocation_info_flags_0022.htm
old-project: display
ms.assetid: DE3C133C-C1A9-4735-B1C4-9F6E791845A1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_ALLOCATION_INFO_FLAGS_0022
req.alt-loc: D3d12umddi.h
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

# D3D12DDI_ALLOCATION_INFO_FLAGS_0022 enumeration



## -description
<p>Contains allocation information flags.</p>


## -syntax

````
typedef enum D3D12DDI_ALLOCATION_INFO_FLAGS_0022 { 
  D3D12DDI_ALLOCATION_INFO_FLAGS_0022_NONE               = 0x0,
  D3D12DDI_ALLOCATION_INFO_FLAGS_0022_PRIMARY            = 0x1,
  D3D12DDI_ALLOCATION_INFO_FLAGS_0022_STEREO             = 0x2,
  D3D12DDI_ALLOCATION_INFO_FLAGS_0022_OVERRIDE_PRIORITY  = 0x4
} D3D12DDI_ALLOCATION_INFO_FLAGS_0022;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_ALLOCATION_INFO_FLAGS_0022_NONE"></a><a id="d3d12ddi_allocation_info_flags_0022_none"></a><b>D3D12DDI_ALLOCATION_INFO_FLAGS_0022_NONE</b>

<dd>
<p>No allocation information flag.</p>
</dd>

### -field <a id="D3D12DDI_ALLOCATION_INFO_FLAGS_0022_PRIMARY"></a><a id="d3d12ddi_allocation_info_flags_0022_primary"></a><b>D3D12DDI_ALLOCATION_INFO_FLAGS_0022_PRIMARY</b>

<dd>
<p>A primary value. </p>
</dd>

### -field <a id="D3D12DDI_ALLOCATION_INFO_FLAGS_0022_STEREO"></a><a id="d3d12ddi_allocation_info_flags_0022_stereo"></a><b>D3D12DDI_ALLOCATION_INFO_FLAGS_0022_STEREO</b>

<dd>
<p>A stereo value.</p>
</dd>

### -field <a id="D3D12DDI_ALLOCATION_INFO_FLAGS_0022_OVERRIDE_PRIORITY"></a><a id="d3d12ddi_allocation_info_flags_0022_override_priority"></a><b>D3D12DDI_ALLOCATION_INFO_FLAGS_0022_OVERRIDE_PRIORITY</b>

<dd>
<p>An override priority. </p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>