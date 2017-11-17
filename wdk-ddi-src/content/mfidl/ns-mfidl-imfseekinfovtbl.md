---
UID: NS.mfidl.IMFSeekInfoVtbl
title: IMFSeekInfoVtbl
author: windows-driver-content
description: 
ms.assetid: 0c518e14-1898-406b-9f56-4d67fa701059
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSeekInfoVtbl, IMFSeekInfoVtbl
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

# IMFSeekInfoVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSeekInfo *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSeekInfo *This) AddRef			
 	
### -field ULONG(* )(IMFSeekInfo *This) Release			
 	
### -field HRESULT(* )(IMFSeekInfo *This, const GUID *pguidTimeFormat, const PROPVARIANT *pvarStartPosition,PROPVARIANT *pvarPreviousKeyFrame,PROPVARIANT *pvarNextKeyFrame) GetNearestKeyFrames			
 	
## -remarks

## -see-also