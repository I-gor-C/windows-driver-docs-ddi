---
UID : NS:d3d12umddi.D3D12DDI_D3D12_OPTIONS_DATA_0031
title : D3D12DDI_D3D12_OPTIONS_DATA_0031
author : windows-driver-content
description : Display options data.
old-location : display\d3d12ddi-d3d12-options-data-0031.htm
old-project : display
ms.assetid : 3e60f42a-ea95-4876-b370-5c2f0585dc97
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : d3d12umddi/D3D12DDI_D3D12_OPTIONS_DATA_0031, display.d3d12ddi-d3d12-options-data-0031, D3D12DDI_D3D12_OPTIONS_DATA_0031 structure [Display Devices], D3D12DDI_D3D12_OPTIONS_DATA_0031
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3d12umddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3D12DDI_D3D12_OPTIONS_DATA_0031
---

# D3D12DDI_D3D12_OPTIONS_DATA_0031 structure
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

Display options data.

## Syntax
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

## Members


`ConservativeRasterizationTier`

Conservative rasterization tier.

`CopyQueueTimestampQueriesSupported`

Copy queue timestamp queries supported.

`CrossNodeSharingTier`

Cross node sharing tier.

`DepthBoundsTestSupported`

Depth bounds test supported.

`OutputMergerLogicOp`

Output merger logic option.

`ProgrammableSamplePositionsTier`

Programmable sample positions tier.

`ResourceBindingTier`

Resource binding tier.

`ResourceHeapTier`

Resource heap tier.

`TiledResourcesTier`

Tiled resources tier.

`VPAndRTArrayIndexFromAnyShaderFeedingRasterizerSupportedWithoutGSEmulation`

VP and RT array index from any shader feeding rasterizer supported without GS emulation.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h |