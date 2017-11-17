---
UID: NS.mfidl.IMFMediaSinkVtbl
title: IMFMediaSinkVtbl
author: windows-driver-content
description: 
ms.assetid: fa8af864-ac59-417d-951a-96712d2485c9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaSinkVtbl, IMFMediaSinkVtbl
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

# IMFMediaSinkVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaSink *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaSink *This) AddRef			
 	
### -field ULONG(* )(IMFMediaSink *This) Release			
 	
### -field HRESULT(* )(IMFMediaSink *This,DWORD *pdwCharacteristics) GetCharacteristics			
 	
### -field HRESULT(* )(IMFMediaSink *This,DWORD dwStreamSinkIdentifier,IMFMediaType *pMediaType,IMFStreamSink **ppStreamSink) AddStreamSink			
 	
### -field HRESULT(* )(IMFMediaSink *This,DWORD dwStreamSinkIdentifier) RemoveStreamSink			
 	
### -field HRESULT(* )(IMFMediaSink *This,DWORD *pcStreamSinkCount) GetStreamSinkCount			
 	
### -field HRESULT(* )(IMFMediaSink *This,DWORD dwIndex,IMFStreamSink **ppStreamSink) GetStreamSinkByIndex			
 	
### -field HRESULT(* )(IMFMediaSink *This,DWORD dwStreamSinkIdentifier,IMFStreamSink **ppStreamSink) GetStreamSinkById			
 	
### -field HRESULT(* )(IMFMediaSink *This,IMFPresentationClock *pPresentationClock) SetPresentationClock			
 	
### -field HRESULT(* )(IMFMediaSink *This,IMFPresentationClock **ppPresentationClock) GetPresentationClock			
 	
### -field HRESULT(* )(IMFMediaSink *This) Shutdown			
 	
## -remarks

## -see-also