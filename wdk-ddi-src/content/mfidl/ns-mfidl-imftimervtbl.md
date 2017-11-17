---
UID: NS.mfidl.IMFTimerVtbl
title: IMFTimerVtbl
author: windows-driver-content
description: 
ms.assetid: 9f67b0c7-15ef-4e1d-8b21-5b8666a3b83b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTimerVtbl, IMFTimerVtbl
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

# IMFTimerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTimer *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTimer *This) AddRef			
 	
### -field ULONG(* )(IMFTimer *This) Release			
 	
### -field HRESULT(* )(IMFTimer *This,DWORD dwFlags,LONGLONG llClockTime,IMFAsyncCallback *pCallback,IUnknown *punkState,IUnknown **ppunkKey) SetTimer			
 	
### -field HRESULT(* )(IMFTimer *This,IUnknown *punkKey) CancelTimer			
 	
## -remarks

## -see-also