---
UID: NS.mfidl.IMFVideoSampleAllocatorExVtbl
title: IMFVideoSampleAllocatorExVtbl
author: windows-driver-content
description: 
ms.assetid: c97b5de0-bd8e-4a0f-bf02-b442ab1ac740
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFVideoSampleAllocatorExVtbl, IMFVideoSampleAllocatorExVtbl
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

# IMFVideoSampleAllocatorExVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFVideoSampleAllocatorEx *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFVideoSampleAllocatorEx *This) AddRef			
 	
### -field ULONG(* )(IMFVideoSampleAllocatorEx *This) Release			
 	
### -field HRESULT(* )(IMFVideoSampleAllocatorEx *This,IUnknown *pManager) SetDirectXManager			
 	
### -field HRESULT(* )(IMFVideoSampleAllocatorEx *This) UninitializeSampleAllocator			
 	
### -field HRESULT(* )(IMFVideoSampleAllocatorEx *This,DWORD cRequestedFrames,IMFMediaType *pMediaType) InitializeSampleAllocator			
 	
### -field HRESULT(* )(IMFVideoSampleAllocatorEx *This,IMFSample **ppSample) AllocateSample			
 	
### -field HRESULT(* )(IMFVideoSampleAllocatorEx *This,DWORD cInitialSamples,DWORD cMaximumSamples,IMFAttributes *pAttributes,IMFMediaType *pMediaType) InitializeSampleAllocatorEx			
 	
## -remarks

## -see-also