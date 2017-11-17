---
UID: NS.mfidl.IMFPresentationTimeSourceVtbl
title: IMFPresentationTimeSourceVtbl
author: windows-driver-content
description: 
ms.assetid: a7ceb033-b67e-40f2-8f1c-96d6967ef442
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFPresentationTimeSourceVtbl, IMFPresentationTimeSourceVtbl
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

# IMFPresentationTimeSourceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFPresentationTimeSource *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFPresentationTimeSource *This) AddRef			
 	
### -field ULONG(* )(IMFPresentationTimeSource *This) Release			
 	
### -field HRESULT(* )(IMFPresentationTimeSource *This,DWORD *pdwCharacteristics) GetClockCharacteristics			
 	
### -field HRESULT(* )(IMFPresentationTimeSource *This,DWORD dwReserved,LONGLONG *pllClockTime,MFTIME *phnsSystemTime) GetCorrelatedTime			
 	
### -field HRESULT(* )(IMFPresentationTimeSource *This,DWORD *pdwContinuityKey) GetContinuityKey			
 	
### -field HRESULT(* )(IMFPresentationTimeSource *This,DWORD dwReserved,MFCLOCK_STATE *peClockState) GetState			
 	
### -field HRESULT(* )(IMFPresentationTimeSource *This,MFCLOCK_PROPERTIES *pClockProperties) GetProperties			
 	
### -field HRESULT(* )(IMFPresentationTimeSource *This,IMFClock **ppClock) GetUnderlyingClock			
 	
## -remarks

## -see-also