---
UID: NS.mfidl.IMFTimecodeTranslateVtbl
title: IMFTimecodeTranslateVtbl
author: windows-driver-content
description: 
ms.assetid: cb062324-3022-470c-83f7-00a2dfa132f5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTimecodeTranslateVtbl, IMFTimecodeTranslateVtbl
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

# IMFTimecodeTranslateVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTimecodeTranslate *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTimecodeTranslate *This) AddRef			
 	
### -field ULONG(* )(IMFTimecodeTranslate *This) Release			
 	
### -field HRESULT(* )(IMFTimecodeTranslate *This, const PROPVARIANT *pPropVarTimecode,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginConvertTimecodeToHNS			
 	
### -field HRESULT(* )(IMFTimecodeTranslate *This,IMFAsyncResult *pResult,MFTIME *phnsTime) EndConvertTimecodeToHNS			
 	
### -field HRESULT(* )(IMFTimecodeTranslate *This,MFTIME hnsTime,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginConvertHNSToTimecode			
 	
### -field HRESULT(* )(IMFTimecodeTranslate *This,IMFAsyncResult *pResult,PROPVARIANT *pPropVarTimecode) EndConvertHNSToTimecode			
 	
## -remarks

## -see-also