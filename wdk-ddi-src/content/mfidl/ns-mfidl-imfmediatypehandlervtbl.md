---
UID: NS.mfidl.IMFMediaTypeHandlerVtbl
title: IMFMediaTypeHandlerVtbl
author: windows-driver-content
description: 
ms.assetid: b496107e-7613-4553-baf2-26fdce4a0c27
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaTypeHandlerVtbl, IMFMediaTypeHandlerVtbl
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

# IMFMediaTypeHandlerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaTypeHandler *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaTypeHandler *This) AddRef			
 	
### -field ULONG(* )(IMFMediaTypeHandler *This) Release			
 	
### -field HRESULT(* )(IMFMediaTypeHandler *This,IMFMediaType *pMediaType,IMFMediaType **ppMediaType) IsMediaTypeSupported			
 	
### -field HRESULT(* )(IMFMediaTypeHandler *This,DWORD *pdwTypeCount) GetMediaTypeCount			
 	
### -field HRESULT(* )(IMFMediaTypeHandler *This,DWORD dwIndex,IMFMediaType **ppType) GetMediaTypeByIndex			
 	
### -field HRESULT(* )(IMFMediaTypeHandler *This,IMFMediaType *pMediaType) SetCurrentMediaType			
 	
### -field HRESULT(* )(IMFMediaTypeHandler *This,IMFMediaType **ppMediaType) GetCurrentMediaType			
 	
### -field HRESULT(* )(IMFMediaTypeHandler *This,GUID *pguidMajorType) GetMajorType			
 	
## -remarks

## -see-also