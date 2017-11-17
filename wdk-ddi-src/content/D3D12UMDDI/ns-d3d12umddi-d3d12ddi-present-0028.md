---
UID: NS.d3d12umddi.D3D12DDI_PRESENT_0028
title: D3D12DDI_PRESENT_0028
author: windows-driver-content
description: 
ms.assetid: 99aa1ed1-de9c-4fe3-97d2-55ad09f8d384
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: D3D12DDI_PRESENT_0028, D3D12DDI_PRESENT_0028
req.header: d3d12umddi.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# D3D12DDI_PRESENT_0028 structure

## -description



## -struct-fields

### -field D3DKMT_HANDLE hSrcAllocation			
 	
### -field D3DKMT_HANDLE hDstAllocation			
 	
### -field HANDLE hContext			
 	
### -field UINT BroadcastContextCount			
 	
### -field HANDLE [D3DDDI_MAX_BROADCAST_CONTEXT] BroadcastContext			
 	
### -field D3DKMT_HANDLE [D3DDDI_MAX_BROADCAST_CONTEXT] BroadcastSrcAllocation			
 	
### -field D3DKMT_HANDLE [D3DDDI_MAX_BROADCAST_CONTEXT] BroadcastDstAllocation			
 	
### -field BOOL AddedGpuWork			
 	
### -field UINT BackBufferMultiplicity			
 	
### -field BOOL SyncIntervalOverrideValid			
 	
### -field DXGI_DDI_FLIP_INTERVAL_TYPE SyncIntervalOverride			
 	
## -remarks

## -see-also