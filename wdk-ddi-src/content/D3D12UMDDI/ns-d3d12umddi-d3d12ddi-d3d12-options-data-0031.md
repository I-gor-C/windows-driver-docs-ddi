---
UID: NS.d3d12umddi.D3D12DDI_D3D12_OPTIONS_DATA_0031
title: D3D12DDI_D3D12_OPTIONS_DATA_0031
author: windows-driver-content
description: Display options data.
old-location: display\d3d12ddi-d3d12-options-data-0031.htm
ms.assetid: 3e60f42a-ea95-4876-b370-5c2f0585dc97
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_D3D12_OPTIONS_DATA_0031
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
ms.keywords: D3D12DDI_D3D12_OPTIONS_DATA_0031, D3D12DDI_D3D12_OPTIONS_DATA_0031
req.iface: 
---

# D3D12DDI_D3D12_OPTIONS_DATA_0031 structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Display options data.</p>


## -syntax

````
typedef struct _D3D12DDI_D3D12_OPTIONS_DATA_0031 {
  D3D12DDI_RESOURCE_BINDING_TIER               ResourceBindingTier;
  D3D12DDI_CONSERVATIVE_RASTERIZATION_TIER     ConservativeRasterizationTier;
  D3D12DDI_TILED_RESOURCES_TIER                TiledResourcesTier;
  D3D12DDI_CROSS_NODE_SHARING_TIER             CrossNodeSharingTier;
  BOOL                                         VPAndRTArrayIndexFromAnyShaderFeedingRasterizerSupportedWithoutGSEmulation;
  BOOL                                         OutputMergerLogicOp;
  D3D12DDI_RESOURCE_HEAP_TIER                  ResourceHeapTier;
  BOOL                                         DepthBoundsTestSupported;
  D3D12DDI_PROGRAMMABLE_SAMPLE_POSITIONS_TIER  ProgrammableSamplePositionsTier;
  BOOL                                         CopyQueueTimestampQueriesSupported;
} D3D12DDI_D3D12_OPTIONS_DATA_0031, D3D12DDI_D3D12_OPTIONS_DATA_0031;
````


## -struct-fields
<dl>

### -field <b>ResourceBindingTier</b>

<dd>
<p>Resource binding tier.</p>
</dd>

### -field <b>ConservativeRasterizationTier</b>

<dd>
<p>Conservative rasterization tier.</p>
</dd>

### -field <b>TiledResourcesTier</b>

<dd>
<p>Tiled resources tier.</p>
</dd>

### -field <b>CrossNodeSharingTier</b>

<dd>
<p>Cross node sharing tier.</p>
</dd>

### -field <b>VPAndRTArrayIndexFromAnyShaderFeedingRasterizerSupportedWithoutGSEmulation</b>

<dd>
<p>VP and RT array index from any shader feeding rasterizer supported without GS emulation.</p>
</dd>

### -field <b>OutputMergerLogicOp</b>

<dd>
<p>Output merger logic option.</p>
</dd>

### -field <b>ResourceHeapTier</b>

<dd>
<p>Resource heap tier.</p>
</dd>

### -field <b>DepthBoundsTestSupported</b>

<dd>
<p>Depth bounds test supported.</p>
</dd>

### -field <b>ProgrammableSamplePositionsTier</b>

<dd>
<p>Programmable sample positions tier.</p>
</dd>

### -field <b>CopyQueueTimestampQueriesSupported</b>

<dd>
<p>Copy queue timestamp queries supported.</p>
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