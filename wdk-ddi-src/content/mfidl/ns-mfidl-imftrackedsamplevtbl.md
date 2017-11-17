---
UID: NS.mfidl.IMFTrackedSampleVtbl
title: IMFTrackedSampleVtbl
author: windows-driver-content
description: 
ms.assetid: 0313779e-fd90-40f3-b44e-6d0892b4b84e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTrackedSampleVtbl, IMFTrackedSampleVtbl
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

# IMFTrackedSampleVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTrackedSample *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTrackedSample *This) AddRef			
 	
### -field ULONG(* )(IMFTrackedSample *This) Release			
 	
### -field HRESULT(* )(IMFTrackedSample *This,IMFAsyncCallback *pSampleAllocator,IUnknown *pUnkState) SetAllocator			
 	
## -remarks

## -see-also