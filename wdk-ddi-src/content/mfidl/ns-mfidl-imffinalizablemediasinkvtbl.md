---
UID: NS.mfidl.IMFFinalizableMediaSinkVtbl
title: IMFFinalizableMediaSinkVtbl
author: windows-driver-content
description: 
ms.assetid: c5ffb5d0-f797-4938-8e4c-10035903fb27
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFFinalizableMediaSinkVtbl, IMFFinalizableMediaSinkVtbl
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

# IMFFinalizableMediaSinkVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFFinalizableMediaSink *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFFinalizableMediaSink *This) AddRef			
 	
### -field ULONG(* )(IMFFinalizableMediaSink *This) Release			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,DWORD *pdwCharacteristics) GetCharacteristics			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,DWORD dwStreamSinkIdentifier,IMFMediaType *pMediaType,IMFStreamSink **ppStreamSink) AddStreamSink			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,DWORD dwStreamSinkIdentifier) RemoveStreamSink			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,DWORD *pcStreamSinkCount) GetStreamSinkCount			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,DWORD dwIndex,IMFStreamSink **ppStreamSink) GetStreamSinkByIndex			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,DWORD dwStreamSinkIdentifier,IMFStreamSink **ppStreamSink) GetStreamSinkById			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,IMFPresentationClock *pPresentationClock) SetPresentationClock			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,IMFPresentationClock **ppPresentationClock) GetPresentationClock			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This) Shutdown			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginFinalize			
 	
### -field HRESULT(* )(IMFFinalizableMediaSink *This,IMFAsyncResult *pResult) EndFinalize			
 	
## -remarks

## -see-also