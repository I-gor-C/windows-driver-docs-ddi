---
UID: NS.mfidl.IMFVideoProcessorControlVtbl
title: IMFVideoProcessorControlVtbl
author: windows-driver-content
description: 
ms.assetid: e704482e-1ed6-4760-b482-8efe77eef254
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFVideoProcessorControlVtbl, IMFVideoProcessorControlVtbl
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

# IMFVideoProcessorControlVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFVideoProcessorControl *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFVideoProcessorControl *This) AddRef			
 	
### -field ULONG(* )(IMFVideoProcessorControl *This) Release			
 	
### -field HRESULT(* )(IMFVideoProcessorControl *This,MFARGB *pBorderColor) SetBorderColor			
 	
### -field HRESULT(* )(IMFVideoProcessorControl *This,RECT *pSrcRect) SetSourceRectangle			
 	
### -field HRESULT(* )(IMFVideoProcessorControl *This,RECT *pDstRect) SetDestinationRectangle			
 	
### -field HRESULT(* )(IMFVideoProcessorControl *This,MF_VIDEO_PROCESSOR_MIRROR eMirror) SetMirror			
 	
### -field HRESULT(* )(IMFVideoProcessorControl *This,MF_VIDEO_PROCESSOR_ROTATION eRotation) SetRotation			
 	
### -field HRESULT(* )(IMFVideoProcessorControl *This,SIZE *pConstrictionSize) SetConstrictionSize			
 	
## -remarks

## -see-also