---
UID: NS.mfidl.IMFMediaStreamVtbl
title: IMFMediaStreamVtbl
author: windows-driver-content
description: 
ms.assetid: 43cb05f4-635a-4a47-abf0-29d90bef87d7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaStreamVtbl, IMFMediaStreamVtbl
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

# IMFMediaStreamVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaStream *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaStream *This) AddRef			
 	
### -field ULONG(* )(IMFMediaStream *This) Release			
 	
### -field HRESULT(* )(IMFMediaStream *This,DWORD dwFlags,IMFMediaEvent **ppEvent) GetEvent			
 	
### -field HRESULT(* )(IMFMediaStream *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginGetEvent			
 	
### -field HRESULT(* )(IMFMediaStream *This,IMFAsyncResult *pResult,IMFMediaEvent **ppEvent) EndGetEvent			
 	
### -field HRESULT(* )(IMFMediaStream *This,MediaEventType met,REFGUID guidExtendedType,HRESULT hrStatus, const PROPVARIANT *pvValue) QueueEvent			
 	
### -field HRESULT(* )(IMFMediaStream *This,IMFMediaSource **ppMediaSource) GetMediaSource			
 	
### -field HRESULT(* )(IMFMediaStream *This,IMFStreamDescriptor **ppStreamDescriptor) GetStreamDescriptor			
 	
### -field HRESULT(* )(IMFMediaStream *This,IUnknown *pToken) RequestSample			
 	
## -remarks

## -see-also