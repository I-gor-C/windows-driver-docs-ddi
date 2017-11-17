---
UID: NS.mfidl.IMFClockVtbl
title: IMFClockVtbl
author: windows-driver-content
description: 
ms.assetid: 373e66d3-2d2b-4d1d-b27a-9e7eef47e42e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFClockVtbl, IMFClockVtbl
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

# IMFClockVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFClock *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFClock *This) AddRef			
 	
### -field ULONG(* )(IMFClock *This) Release			
 	
### -field HRESULT(* )(IMFClock *This,DWORD *pdwCharacteristics) GetClockCharacteristics			
 	
### -field HRESULT(* )(IMFClock *This,DWORD dwReserved,LONGLONG *pllClockTime,MFTIME *phnsSystemTime) GetCorrelatedTime			
 	
### -field HRESULT(* )(IMFClock *This,DWORD *pdwContinuityKey) GetContinuityKey			
 	
### -field HRESULT(* )(IMFClock *This,DWORD dwReserved,MFCLOCK_STATE *peClockState) GetState			
 	
### -field HRESULT(* )(IMFClock *This,MFCLOCK_PROPERTIES *pClockProperties) GetProperties			
 	
## -remarks

## -see-also