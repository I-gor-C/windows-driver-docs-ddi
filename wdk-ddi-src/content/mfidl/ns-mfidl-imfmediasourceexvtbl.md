---
UID: NS.mfidl.IMFMediaSourceExVtbl
title: IMFMediaSourceExVtbl
author: windows-driver-content
description: 
ms.assetid: df2f5f97-b1b9-41cc-96e3-2d5b91f1a504
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaSourceExVtbl, IMFMediaSourceExVtbl
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

# IMFMediaSourceExVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaSourceEx *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaSourceEx *This) AddRef			
 	
### -field ULONG(* )(IMFMediaSourceEx *This) Release			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,DWORD dwFlags,IMFMediaEvent **ppEvent) GetEvent			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginGetEvent			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,IMFAsyncResult *pResult,IMFMediaEvent **ppEvent) EndGetEvent			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,MediaEventType met,REFGUID guidExtendedType,HRESULT hrStatus, const PROPVARIANT *pvValue) QueueEvent			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,DWORD *pdwCharacteristics) GetCharacteristics			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,IMFPresentationDescriptor **ppPresentationDescriptor) CreatePresentationDescriptor			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,IMFPresentationDescriptor *pPresentationDescriptor, const GUID *pguidTimeFormat, const PROPVARIANT *pvarStartPosition) Start			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This) Stop			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This) Pause			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This) Shutdown			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,IMFAttributes **ppAttributes) GetSourceAttributes			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,DWORD dwStreamIdentifier,IMFAttributes **ppAttributes) GetStreamAttributes			
 	
### -field HRESULT(* )(IMFMediaSourceEx *This,IUnknown *pManager) SetD3DManager			
 	
## -remarks

## -see-also