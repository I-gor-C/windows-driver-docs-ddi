---
UID: NS.mfidl.IMFStreamSinkVtbl
title: IMFStreamSinkVtbl
author: windows-driver-content
description: 
ms.assetid: 9981fc4c-36f3-4d08-b7aa-7a197f9edd9f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFStreamSinkVtbl, IMFStreamSinkVtbl
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

# IMFStreamSinkVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFStreamSink *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFStreamSink *This) AddRef			
 	
### -field ULONG(* )(IMFStreamSink *This) Release			
 	
### -field HRESULT(* )(IMFStreamSink *This,DWORD dwFlags,IMFMediaEvent **ppEvent) GetEvent			
 	
### -field HRESULT(* )(IMFStreamSink *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginGetEvent			
 	
### -field HRESULT(* )(IMFStreamSink *This,IMFAsyncResult *pResult,IMFMediaEvent **ppEvent) EndGetEvent			
 	
### -field HRESULT(* )(IMFStreamSink *This,MediaEventType met,REFGUID guidExtendedType,HRESULT hrStatus, const PROPVARIANT *pvValue) QueueEvent			
 	
### -field HRESULT(* )(IMFStreamSink *This,IMFMediaSink **ppMediaSink) GetMediaSink			
 	
### -field HRESULT(* )(IMFStreamSink *This,DWORD *pdwIdentifier) GetIdentifier			
 	
### -field HRESULT(* )(IMFStreamSink *This,IMFMediaTypeHandler **ppHandler) GetMediaTypeHandler			
 	
### -field HRESULT(* )(IMFStreamSink *This,IMFSample *pSample) ProcessSample			
 	
### -field HRESULT(* )(IMFStreamSink *This,MFSTREAMSINK_MARKER_TYPE eMarkerType, const PROPVARIANT *pvarMarkerValue, const PROPVARIANT *pvarContextValue) PlaceMarker			
 	
### -field HRESULT(* )(IMFStreamSink *This) Flush			
 	
## -remarks

## -see-also