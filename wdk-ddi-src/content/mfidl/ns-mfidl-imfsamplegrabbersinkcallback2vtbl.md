---
UID: NS.mfidl.IMFSampleGrabberSinkCallback2Vtbl
title: IMFSampleGrabberSinkCallback2Vtbl
author: windows-driver-content
description: 
ms.assetid: 2d78881b-9482-46aa-9380-eafb576a0d54
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSampleGrabberSinkCallback2Vtbl, IMFSampleGrabberSinkCallback2Vtbl
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

# IMFSampleGrabberSinkCallback2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSampleGrabberSinkCallback2 *This) AddRef			
 	
### -field ULONG(* )(IMFSampleGrabberSinkCallback2 *This) Release			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,MFTIME hnsSystemTime,LONGLONG llClockStartOffset) OnClockStart			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,MFTIME hnsSystemTime) OnClockStop			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,MFTIME hnsSystemTime) OnClockPause			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,MFTIME hnsSystemTime) OnClockRestart			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,MFTIME hnsSystemTime, float flRate) OnClockSetRate			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,IMFPresentationClock *pPresentationClock) OnSetPresentationClock			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,REFGUID guidMajorMediaType,DWORD dwSampleFlags,LONGLONG llSampleTime,LONGLONG llSampleDuration, const BYTE *pSampleBuffer,DWORD dwSampleSize) OnProcessSample			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This) OnShutdown			
 	
### -field HRESULT(* )(IMFSampleGrabberSinkCallback2 *This,REFGUID guidMajorMediaType,DWORD dwSampleFlags,LONGLONG llSampleTime,LONGLONG llSampleDuration, const BYTE *pSampleBuffer,DWORD dwSampleSize,IMFAttributes *pAttributes) OnProcessSampleEx			
 	
## -remarks

## -see-also