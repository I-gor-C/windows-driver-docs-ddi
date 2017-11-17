---
UID: NS.mfidl.IMFMediaSource2Vtbl
title: IMFMediaSource2Vtbl
author: windows-driver-content
description: 
ms.assetid: 9e820358-8dbc-4f77-9840-935ab7b6e7e9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaSource2Vtbl, IMFMediaSource2Vtbl
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

# IMFMediaSource2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaSource2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaSource2 *This) AddRef			
 	
### -field ULONG(* )(IMFMediaSource2 *This) Release			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,DWORD dwFlags,IMFMediaEvent **ppEvent) GetEvent			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginGetEvent			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,IMFAsyncResult *pResult,IMFMediaEvent **ppEvent) EndGetEvent			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,MediaEventType met,REFGUID guidExtendedType,HRESULT hrStatus, const PROPVARIANT *pvValue) QueueEvent			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,DWORD *pdwCharacteristics) GetCharacteristics			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,IMFPresentationDescriptor **ppPresentationDescriptor) CreatePresentationDescriptor			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,IMFPresentationDescriptor *pPresentationDescriptor, const GUID *pguidTimeFormat, const PROPVARIANT *pvarStartPosition) Start			
 	
### -field HRESULT(* )(IMFMediaSource2 *This) Stop			
 	
### -field HRESULT(* )(IMFMediaSource2 *This) Pause			
 	
### -field HRESULT(* )(IMFMediaSource2 *This) Shutdown			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,IMFAttributes **ppAttributes) GetSourceAttributes			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,DWORD dwStreamIdentifier,IMFAttributes **ppAttributes) GetStreamAttributes			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,IUnknown *pManager) SetD3DManager			
 	
### -field HRESULT(* )(IMFMediaSource2 *This,DWORD dwStreamID,IMFMediaType *pMediaType) SetMediaType			
 	
## -remarks

## -see-also