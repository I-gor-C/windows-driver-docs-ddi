---
UID: NS.mfidl.IMFPresentationClockVtbl
title: IMFPresentationClockVtbl
author: windows-driver-content
description: 
ms.assetid: 8354c93d-1bff-4846-9867-3aadae952301
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFPresentationClockVtbl, IMFPresentationClockVtbl
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

# IMFPresentationClockVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFPresentationClock *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFPresentationClock *This) AddRef			
 	
### -field ULONG(* )(IMFPresentationClock *This) Release			
 	
### -field HRESULT(* )(IMFPresentationClock *This,DWORD *pdwCharacteristics) GetClockCharacteristics			
 	
### -field HRESULT(* )(IMFPresentationClock *This,DWORD dwReserved,LONGLONG *pllClockTime,MFTIME *phnsSystemTime) GetCorrelatedTime			
 	
### -field HRESULT(* )(IMFPresentationClock *This,DWORD *pdwContinuityKey) GetContinuityKey			
 	
### -field HRESULT(* )(IMFPresentationClock *This,DWORD dwReserved,MFCLOCK_STATE *peClockState) GetState			
 	
### -field HRESULT(* )(IMFPresentationClock *This,MFCLOCK_PROPERTIES *pClockProperties) GetProperties			
 	
### -field HRESULT(* )(IMFPresentationClock *This,IMFPresentationTimeSource *pTimeSource) SetTimeSource			
 	
### -field HRESULT(* )(IMFPresentationClock *This,IMFPresentationTimeSource **ppTimeSource) GetTimeSource			
 	
### -field HRESULT(* )(IMFPresentationClock *This,MFTIME *phnsClockTime) GetTime			
 	
### -field HRESULT(* )(IMFPresentationClock *This,IMFClockStateSink *pStateSink) AddClockStateSink			
 	
### -field HRESULT(* )(IMFPresentationClock *This,IMFClockStateSink *pStateSink) RemoveClockStateSink			
 	
### -field HRESULT(* )(IMFPresentationClock *This,LONGLONG llClockStartOffset) Start			
 	
### -field HRESULT(* )(IMFPresentationClock *This) Stop			
 	
### -field HRESULT(* )(IMFPresentationClock *This) Pause			
 	
## -remarks

## -see-also