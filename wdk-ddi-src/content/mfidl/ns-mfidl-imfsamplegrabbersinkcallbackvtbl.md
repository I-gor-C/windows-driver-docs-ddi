---
UID: NS.mfidl.IMFSampleGrabberSinkCallbackVtbl
title: IMFSampleGrabberSinkCallbackVtbl
author: windows-driver-content
description: 
ms.assetid: 07ddeee2-24a6-4b85-b1dd-737e53a247e1
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSampleGrabberSinkCallbackVtbl, IMFSampleGrabberSinkCallbackVtbl
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

# IMFSampleGrabberSinkCallbackVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSampleGrabberSinkCallback *This) AddRef			
 	
### -field ULONG(* )(IMFSampleGrabberSinkCallback *This) Release			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This,MFTIME hnsSystemTime,LONGLONG llClockStartOffset) OnClockStart			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This,MFTIME hnsSystemTime) OnClockStop			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This,MFTIME hnsSystemTime) OnClockPause			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This,MFTIME hnsSystemTime) OnClockRestart			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This,MFTIME hnsSystemTime, float flRate) OnClockSetRate			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This,IMFPresentationClock *pPresentationClock) OnSetPresentationClock			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This,REFGUID guidMajorMediaType,DWORD dwSampleFlags,LONGLONG llSampleTime,LONGLONG llSampleDuration, const BYTE *pSampleBuffer,DWORD dwSampleSize) OnProcessSample			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback *This) OnShutdown			
 	
## -remarks

## -see-also