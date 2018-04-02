---
UID: NE:d3d12umddi.D3D12DDI_VIEW_INSTANCING_TIER
title: D3D12DDI_VIEW_INSTANCING_TIER
author: windows-driver-content
description: Defines the view instancing tier.
old-location: display\d3d12ddi-view-instancing-tier.htm
old-project: display
ms.assetid: 4d52ddb2-818f-4b46-b19f-d6eea36a07da
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D12DDI_VIEW_INSTANCING_TIER, D3D12DDI_VIEW_INSTANCING_TIER enumeration [Display Devices], D3D12DDI_VIEW_INSTANCING_TIER_1, D3D12DDI_VIEW_INSTANCING_TIER_2, D3D12DDI_VIEW_INSTANCING_TIER_3, D3D12DDI_VIEW_INSTANCING_TIER_NOT_SUPPORTED, d3d12umddi/D3D12DDI_VIEW_INSTANCING_TIER, d3d12umddi/D3D12DDI_VIEW_INSTANCING_TIER_1, d3d12umddi/D3D12DDI_VIEW_INSTANCING_TIER_2, d3d12umddi/D3D12DDI_VIEW_INSTANCING_TIER_3, d3d12umddi/D3D12DDI_VIEW_INSTANCING_TIER_NOT_SUPPORTED, display.d3d12ddi-view-instancing-tier
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3d12umddi.h
api_name:
-	D3D12DDI_VIEW_INSTANCING_TIER
product:
- Windows
targetos: Windows
req.typenames: D3D12DDI_VIEW_INSTANCING_TIER
---

# D3D12DDI_VIEW_INSTANCING_TIER Enumeration
Defines the view instancing tier.

## Syntax
```
typedef enum D3D12DDI_VIEW_INSTANCING_TIER {
  D3D12DDI_VIEW_INSTANCING_TIER_NOT_SUPPORTED  ,
  D3D12DDI_VIEW_INSTANCING_TIER_1              ,
  D3D12DDI_VIEW_INSTANCING_TIER_2              ,
  D3D12DDI_VIEW_INSTANCING_TIER_3
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D12DDI_VIEW_INSTANCING_TIER_NOT_SUPPORTED</td>
                    <td>The view instancing tier is not supported.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIEW_INSTANCING_TIER_1</td>
                    <td>The view instancing tier is 1.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIEW_INSTANCING_TIER_2</td>
                    <td>The view instancing tier is 2.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIEW_INSTANCING_TIER_3</td>
                    <td>The view instancing teir is 3.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h |