---
UID: NE.d3d12umddi.D3D12DDI_VIEW_INSTANCING_TIER
title: D3D12DDI_VIEW_INSTANCING_TIER
author: windows-driver-content
description: Defines the view instancing tier.
old-location: display\d3d12ddi-view-instancing-tier.htm
old-project: display
ms.assetid: 4d52ddb2-818f-4b46-b19f-d6eea36a07da
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
req.alt-api: D3D12DDI_VIEW_INSTANCING_TIER
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

# D3D12DDI_VIEW_INSTANCING_TIER enumeration



## -description
<p>Defines the view instancing tier.</p>


## -syntax

````
typedef enum _D3D12DDI_VIEW_INSTANCING_TIER { 
  D3D12DDI_VIEW_INSTANCING_TIER_NOT_SUPPORTED,
  D3D12DDI_VIEW_INSTANCING_TIER_1,
  D3D12DDI_VIEW_INSTANCING_TIER_2,
  D3D12DDI_VIEW_INSTANCING_TIER_3
} D3D12DDI_VIEW_INSTANCING_TIER;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_VIEW_INSTANCING_TIER_NOT_SUPPORTED"></a><a id="d3d12ddi_view_instancing_tier_not_supported"></a><b>D3D12DDI_VIEW_INSTANCING_TIER_NOT_SUPPORTED</b>

<dd>
<p>The view instancing tier is not supported.</p>
</dd>

### -field <a id="D3D12DDI_VIEW_INSTANCING_TIER_1"></a><a id="d3d12ddi_view_instancing_tier_1"></a><b>D3D12DDI_VIEW_INSTANCING_TIER_1</b>

<dd>
<p>The view instancing tier is 1.</p>
</dd>

### -field <a id="D3D12DDI_VIEW_INSTANCING_TIER_2"></a><a id="d3d12ddi_view_instancing_tier_2"></a><b>D3D12DDI_VIEW_INSTANCING_TIER_2</b>

<dd>
<p>The view instancing tier is 2.</p>
</dd>

### -field <a id="D3D12DDI_VIEW_INSTANCING_TIER_3"></a><a id="d3d12ddi_view_instancing_tier_3"></a><b>D3D12DDI_VIEW_INSTANCING_TIER_3</b>

<dd>
<p>The view instancing teir is 3.</p>
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