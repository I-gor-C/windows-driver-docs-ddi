---
UID: NS.mfidl.IMFMediaSourceVtbl
title: IMFMediaSourceVtbl
author: windows-driver-content
description: 
ms.assetid: 5658cdbd-c523-4142-abfd-d72144f2ea2e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaSourceVtbl, IMFMediaSourceVtbl
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

# IMFMediaSourceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaSource *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaSource *This) AddRef			
 	
### -field ULONG(* )(IMFMediaSource *This) Release			
 	
### -field HRESULT(* )(IMFMediaSource *This,DWORD dwFlags,IMFMediaEvent **ppEvent) GetEvent			
 	
### -field HRESULT(* )(IMFMediaSource *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginGetEvent			
 	
### -field HRESULT(* )(IMFMediaSource *This,IMFAsyncResult *pResult,IMFMediaEvent **ppEvent) EndGetEvent			
 	
### -field HRESULT(* )(IMFMediaSource *This,MediaEventType met,REFGUID guidExtendedType,HRESULT hrStatus, const PROPVARIANT *pvValue) QueueEvent			
 	
### -field HRESULT(* )(IMFMediaSource *This,DWORD *pdwCharacteristics) GetCharacteristics			
 	
### -field HRESULT(* )(IMFMediaSource *This,IMFPresentationDescriptor **ppPresentationDescriptor) CreatePresentationDescriptor			
 	
### -field HRESULT(* )(IMFMediaSource *This,IMFPresentationDescriptor *pPresentationDescriptor, const GUID *pguidTimeFormat, const PROPVARIANT *pvarStartPosition) Start			
 	
### -field HRESULT(* )(IMFMediaSource *This) Stop			
 	
### -field HRESULT(* )(IMFMediaSource *This) Pause			
 	
### -field HRESULT(* )(IMFMediaSource *This) Shutdown			
 	
## -remarks

## -see-also