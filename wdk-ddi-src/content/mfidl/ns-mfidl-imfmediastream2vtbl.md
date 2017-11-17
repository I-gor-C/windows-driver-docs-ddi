---
UID: NS.mfidl.IMFMediaStream2Vtbl
title: IMFMediaStream2Vtbl
author: windows-driver-content
description: 
ms.assetid: b989aed6-c6cf-4c60-a910-59f875529277
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaStream2Vtbl, IMFMediaStream2Vtbl
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

# IMFMediaStream2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaStream2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaStream2 *This) AddRef			
 	
### -field ULONG(* )(IMFMediaStream2 *This) Release			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,DWORD dwFlags,IMFMediaEvent **ppEvent) GetEvent			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginGetEvent			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,IMFAsyncResult *pResult,IMFMediaEvent **ppEvent) EndGetEvent			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,MediaEventType met,REFGUID guidExtendedType,HRESULT hrStatus, const PROPVARIANT *pvValue) QueueEvent			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,IMFMediaSource **ppMediaSource) GetMediaSource			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,IMFStreamDescriptor **ppStreamDescriptor) GetStreamDescriptor			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,IUnknown *pToken) RequestSample			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,MF_STREAM_STATE value) SetStreamState			
 	
### -field HRESULT(* )(IMFMediaStream2 *This,MF_STREAM_STATE *value) GetStreamState			
 	
## -remarks

## -see-also