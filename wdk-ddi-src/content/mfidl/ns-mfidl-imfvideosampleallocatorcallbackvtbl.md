---
UID: NS.mfidl.IMFVideoSampleAllocatorCallbackVtbl
title: IMFVideoSampleAllocatorCallbackVtbl
author: windows-driver-content
description: 
ms.assetid: 6472ac7b-53f6-419a-95b5-e142d1957220
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFVideoSampleAllocatorCallbackVtbl, IMFVideoSampleAllocatorCallbackVtbl
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

# IMFVideoSampleAllocatorCallbackVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFVideoSampleAllocatorCallback *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFVideoSampleAllocatorCallback *This) AddRef			
 	
### -field ULONG(* )(IMFVideoSampleAllocatorCallback *This) Release			
 	
### -field HRESULT(* )(IMFVideoSampleAllocatorCallback *This,IMFVideoSampleAllocatorNotify *pNotify) SetCallback			
 	
### -field HRESULT(* )(IMFVideoSampleAllocatorCallback *This,LONG *plSamples) GetFreeSampleCount			
 	
## -remarks

## -see-also