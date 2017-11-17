---
UID: NS.d3dkmthk._D3DKMT_PRESENT_MULTIPLANE_OVERLAY3
title: D3DKMT_PRESENT_MULTIPLANE_OVERLAY3
author: windows-driver-content
description: 
ms.assetid: 907eb071-b511-4137-b571-daccb6c52785
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY3, D3DKMT_PRESENT_MULTIPLANE_OVERLAY3
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

# D3DKMT_PRESENT_MULTIPLANE_OVERLAY3 structure

## -description



## -struct-fields

### -field D3DKMT_HANDLE hAdapter			
 	
### -field UINT ContextCount			
 	
### -field D3DKMT_HANDLE * pContextList			
 	
### -field D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId			
 	
### -field UINT PresentCount			
 	
### -field D3DKMT_PRESENT_MULTIPLANE_OVERLAY_FLAGS Flags			
 	
### -field UINT PresentPlaneCount			
 	
### -field D3DKMT_MULTIPLANE_OVERLAY3 ** ppPresentPlanes			
 	
### -field D3DKMT_MULTIPLANE_OVERLAY_POST_COMPOSITION * pPostComposition			
 	
### -field UINT Duration			
 	
### -field D3DDDI_HDR_METADATA_TYPE HDRMetaDataType			
 	
### -field UINT HDRMetaDataSize			
 	
### -field const VOID * pHDRMetaData			
 	
## -remarks

## -see-also