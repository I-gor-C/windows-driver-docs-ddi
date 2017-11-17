---
UID: NS.dxgiddi.DXGI1_5_DDI_BASE_FUNCTIONS
title: DXGI1_5_DDI_BASE_FUNCTIONS
author: windows-driver-content
description: 
ms.assetid: 2203af3d-724f-44dd-aa66-90daed323da5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXGI1_5_DDI_BASE_FUNCTIONS, DXGI1_5_DDI_BASE_FUNCTIONS
req.header: dxgiddi.h
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

# DXGI1_5_DDI_BASE_FUNCTIONS structure

## -description



## -struct-fields

### -field HRESULT(* )(DXGI_DDI_ARG_PRESENT *) pfnPresent			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_GET_GAMMA_CONTROL_CAPS *) pfnGetGammaCaps			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_SETDISPLAYMODE *) pfnSetDisplayMode			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_SETRESOURCEPRIORITY *) pfnSetResourcePriority			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_QUERYRESOURCERESIDENCY *) pfnQueryResourceResidency			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES *) pfnRotateResourceIdentities			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_BLT *) pfnBlt			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_RESOLVESHAREDRESOURCE *) pfnResolveSharedResource			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_BLT1 *) pfnBlt1			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_OFFERRESOURCES1 *) pfnOfferResources1			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_RECLAIMRESOURCES *) pfnReclaimResources			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_GETMULTIPLANEOVERLAYCAPS *) pfnGetMultiplaneOverlayCaps			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_GETMULTIPLANEOVERLAYGROUPCAPS *) pfnGetMultiplaneOverlayGroupCaps			
 	
### -field HRESULT(* )(void *) pfnReserved1			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_PRESENTMULTIPLANEOVERLAY *) pfnPresentMultiplaneOverlay			
 	
### -field HRESULT(* )(void *) pfnReserved2			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_PRESENT1 *) pfnPresent1			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT *) pfnCheckPresentDurationSupport			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_TRIMRESIDENCYSET *) pfnTrimResidencySet			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYCOLORSPACESUPPORT *) pfnCheckMultiplaneOverlayColorSpaceSupport			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_PRESENTMULTIPLANEOVERLAY1 *) pfnPresentMultiplaneOverlay1			
 	
### -field HRESULT(* )(DXGI_DDI_ARG_RECLAIMRESOURCES1 *) pfnReclaimResources1			
 	
## -remarks

## -see-also