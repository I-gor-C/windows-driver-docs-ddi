---
UID: NS.mfidl.IMFVideoProcessorControl2Vtbl
title: IMFVideoProcessorControl2Vtbl
author: windows-driver-content
description: 
ms.assetid: 263eaefe-2193-45f6-bea8-24aba1b5d3e5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFVideoProcessorControl2Vtbl, IMFVideoProcessorControl2Vtbl
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

# IMFVideoProcessorControl2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFVideoProcessorControl2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFVideoProcessorControl2 *This) AddRef			
 	
### -field ULONG(* )(IMFVideoProcessorControl2 *This) Release			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,MFARGB *pBorderColor) SetBorderColor			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,RECT *pSrcRect) SetSourceRectangle			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,RECT *pDstRect) SetDestinationRectangle			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,MF_VIDEO_PROCESSOR_MIRROR eMirror) SetMirror			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,MF_VIDEO_PROCESSOR_ROTATION eRotation) SetRotation			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,SIZE *pConstrictionSize) SetConstrictionSize			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,UINT uiRotation) SetRotationOverride			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,BOOL fEnabled) EnableHardwareEffects			
 	
### -field HRESULT(* )(IMFVideoProcessorControl2 *This,UINT *puiSupport) GetSupportedHardwareEffects			
 	
## -remarks

## -see-also