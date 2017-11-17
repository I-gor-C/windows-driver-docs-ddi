---
UID: NS.mfidl.IMFVideoSampleAllocatorVtbl
title: IMFVideoSampleAllocatorVtbl
author: windows-driver-content
description: 
ms.assetid: 2be441fb-0c6a-439f-87b6-bbc55a94cc6b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFVideoSampleAllocatorVtbl, IMFVideoSampleAllocatorVtbl
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

# IMFVideoSampleAllocatorVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFVideoSampleAllocator *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFVideoSampleAllocator *This) AddRef			
 	
### -field ULONG(* )(IMFVideoSampleAllocator *This) Release			
 	
### -field HRESULT(* )(IMFVideoSampleAllocator *This,IUnknown *pManager) SetDirectXManager			
 	
### -field HRESULT(* )(IMFVideoSampleAllocator *This) UninitializeSampleAllocator			
 	
### -field HRESULT(* )(IMFVideoSampleAllocator *This,DWORD cRequestedFrames,IMFMediaType *pMediaType) InitializeSampleAllocator			
 	
### -field HRESULT(* )(IMFVideoSampleAllocator *This,IMFSample **ppSample) AllocateSample			
 	
## -remarks

## -see-also