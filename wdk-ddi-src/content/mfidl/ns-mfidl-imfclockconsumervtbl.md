---
UID: NS.mfidl.IMFClockConsumerVtbl
title: IMFClockConsumerVtbl
author: windows-driver-content
description: 
ms.assetid: f9e68b9e-ea61-4e85-b1ef-00932c322c55
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFClockConsumerVtbl, IMFClockConsumerVtbl
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

# IMFClockConsumerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFClockConsumer *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFClockConsumer *This) AddRef			
 	
### -field ULONG(* )(IMFClockConsumer *This) Release			
 	
### -field HRESULT(* )(IMFClockConsumer *This,IMFPresentationClock *pPresentationClock) SetPresentationClock			
 	
### -field HRESULT(* )(IMFClockConsumer *This,IMFPresentationClock **ppPresentationClock) GetPresentationClock			
 	
## -remarks

## -see-also