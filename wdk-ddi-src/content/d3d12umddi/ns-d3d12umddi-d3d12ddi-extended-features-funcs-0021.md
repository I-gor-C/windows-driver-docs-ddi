---
UID: NS.d3d12umddi.D3D12DDI_EXTENDED_FEATURES_FUNCS_0021
title: D3D12DDI_EXTENDED_FEATURES_FUNCS_0021
author: windows-driver-content
description: Specifies callback functions for extended features.
old-location: display\d3d12ddi_extended_features_funcs_0021.htm
old-project: display
ms.assetid: 9E2D8EF5-18D0-4BC5-ADCA-3D3BE76D3BF1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_EXTENDED_FEATURES_FUNCS_0021, D3D12DDI_EXTENDED_FEATURES_FUNCS_0021
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_EXTENDED_FEATURES_FUNCS_0021
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

# D3D12DDI_EXTENDED_FEATURES_FUNCS_0021 structure



## -description
<p>Specifies callback functions for extended features.</p>


## -syntax

````
typedef struct D3D12DDI_EXTENDED_FEATURES_FUNCS_0021 {
  PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURES_0020         pfnGetSupportedExtendedFeatures;
  PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURE_VERSIONS_0020 pfnGetSupportedExtendedFeatureVersions;
  PFND3D12DDI_ENABLE_EXTENDED_FEATURE_0020                 pfnEnableExtendedFeature;
  PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021          pfnSetExtendedFeatureCallbacks;
} D3D12DDI_EXTENDED_FEATURES_FUNCS_0021;
````


## -struct-fields
<dl>

### -field pfnGetSupportedExtendedFeatures

<dd>
<p>A callback function that gets supported extended features.</p>
</dd>

### -field pfnGetSupportedExtendedFeatureVersions

<dd>
<p>A callback function that gets supported versions of extended features.</p>
</dd>

### -field pfnEnableExtendedFeature

<dd>
<p>A callback function that enables an extended feature.</p>
</dd>

### -field pfnSetExtendedFeatureCallbacks

<dd>
<p>A callback function that sets extended feature callbacks function. </p>
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