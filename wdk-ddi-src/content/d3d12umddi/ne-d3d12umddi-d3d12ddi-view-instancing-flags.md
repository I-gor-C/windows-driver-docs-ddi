---
UID: NE.d3d12umddi.D3D12DDI_VIEW_INSTANCING_FLAGS
title: D3D12DDI_VIEW_INSTANCING_FLAGS
author: windows-driver-content
description: Defines the view instancing flags.
old-location: display\d3d12ddi-view-instancing-flags.htm
old-project: display
ms.assetid: fa44933f-aa3b-466a-8ee2-2d34d0311562
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIEW_INSTANCING_FLAGS
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

# D3D12DDI_VIEW_INSTANCING_FLAGS enumeration



## -description
<p>Defines the view instancing flags.</p>


## -syntax

````
typedef enum _D3D12DDI_VIEW_INSTANCING_FLAGS { 
  D3D12DDI_VIEW_INSTANCING_FLAG_NONE,
  D3D12DDI_VIEW_INSTANCING_FLAG_ENABLE_VIEW_INSTANCE_MASKING
} D3D12DDI_VIEW_INSTANCING_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_VIEW_INSTANCING_FLAG_NONE"></a><a id="d3d12ddi_view_instancing_flag_none"></a><b>D3D12DDI_VIEW_INSTANCING_FLAG_NONE</b>

<dd>
<p>No view instancing flag is defined.</p>
</dd>

### -field <a id="D3D12DDI_VIEW_INSTANCING_FLAG_ENABLE_VIEW_INSTANCE_MASKING"></a><a id="d3d12ddi_view_instancing_flag_enable_view_instance_masking"></a><b>D3D12DDI_VIEW_INSTANCING_FLAG_ENABLE_VIEW_INSTANCE_MASKING</b>

<dd>
<p>The view instancing flag is enable view instance masking.</p>
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