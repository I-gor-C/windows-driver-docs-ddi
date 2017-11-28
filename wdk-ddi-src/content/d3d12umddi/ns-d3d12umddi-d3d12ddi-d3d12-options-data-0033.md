---
UID: NS.d3d12umddi.D3D12DDI_D3D12_OPTIONS_DATA_0033
title: D3D12DDI_D3D12_OPTIONS_DATA_0033
author: windows-driver-content
description: Display options data.
old-location: display\d3d12ddi-d3d12-options-data-0033.htm
old-project: display
ms.assetid: d2b90ec1-cc4c-4a2b-8f7e-d46cd39d553b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_D3D12_OPTIONS_DATA_0033, D3D12DDI_D3D12_OPTIONS_DATA_0033
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_D3D12_OPTIONS_DATA_0033
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

# D3D12DDI_D3D12_OPTIONS_DATA_0033 structure



## -description
<p>Display options data.</p>


## -syntax

````
typedef struct _D3D12DDI_D3D12_OPTIONS_DATA_0033 {
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
  D3D12DDI_COMMAND_QUEUE_FLAGS                 WriteBufferImmediateQueueFlags;
  D3D12DDI_VIEW_INSTANCING_TIER                ViewInstancingTier;
  BOOL                                         BarycentricsSupported;
} D3D12DDI_D3D12_OPTIONS_DATA_0033, D3D12DDI_D3D12_OPTIONS_DATA_0033;
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
<p>Tiled resource tier.</p>
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

### -field <b>WriteBufferImmediateQueueFlags</b>

<dd>
<p>Write buffer immediate queue flags.</p>
</dd>

### -field <b>ViewInstancingTier</b>

<dd>
<p>View instancing tier.</p>
</dd>

### -field <b>BarycentricsSupported</b>

<dd>
<p>Barycentrics supported.</p>
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