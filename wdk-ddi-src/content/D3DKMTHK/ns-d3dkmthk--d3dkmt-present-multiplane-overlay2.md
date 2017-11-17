---
UID: NS.d3dkmthk._D3DKMT_PRESENT_MULTIPLANE_OVERLAY2
title: D3DKMT_PRESENT_MULTIPLANE_OVERLAY2
author: windows-driver-content
description: 
ms.assetid: ee68a49a-5ada-4374-bec5-4e059497c85a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY2, D3DKMT_PRESENT_MULTIPLANE_OVERLAY2
req.header: d3dkmthk.h
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

# D3DKMT_PRESENT_MULTIPLANE_OVERLAY2 structure

## -description



## -struct-fields

### -field union __unnamed_union_0bca_18			
 	
### -field D3DKMT_HANDLE hAdapter			
 	
### -field ULONG BroadcastContextCount			
 	
### -field D3DKMT_HANDLE [D3DDDI_MAX_BROADCAST_CONTEXT] BroadcastContext			
 	
### -field D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId			
 	
### -field UINT PresentCount			
 	
### -field D3DDDI_FLIPINTERVAL_TYPE FlipInterval			
 	
### -field D3DKMT_PRESENTFLAGS Flags			
 	
### -field UINT PresentPlaneCount			
 	
### -field D3DKMT_MULTIPLANE_OVERLAY2 * pPresentPlanes			
 	
### -field UINT Duration			
 	
### -field D3DKMT_HANDLE hDevice			
 	
### -field D3DKMT_HANDLE hContext			
 	
## -remarks

## -see-also