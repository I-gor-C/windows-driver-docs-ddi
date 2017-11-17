---
UID: NS.mfidl.IMFQualityAdviseLimitsVtbl
title: IMFQualityAdviseLimitsVtbl
author: windows-driver-content
description: 
ms.assetid: fb61dece-a3d9-4ff0-afeb-6a6f9e3e73d2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFQualityAdviseLimitsVtbl, IMFQualityAdviseLimitsVtbl
req.header: mfidl.h
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

# IMFQualityAdviseLimitsVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFQualityAdviseLimits *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFQualityAdviseLimits *This) AddRef			
 	
### -field ULONG(* )(IMFQualityAdviseLimits *This) Release			
 	
### -field HRESULT(* )(IMFQualityAdviseLimits *This,MF_QUALITY_DROP_MODE *peDropMode) GetMaximumDropMode			
 	
### -field HRESULT(* )(IMFQualityAdviseLimits *This,MF_QUALITY_LEVEL *peQualityLevel) GetMinimumQualityLevel			
 	
## -remarks

## -see-also