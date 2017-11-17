---
UID: NS.mfidl.IMFClockStateSinkVtbl
title: IMFClockStateSinkVtbl
author: windows-driver-content
description: 
ms.assetid: 6e7ff2ca-d753-4f35-8b7f-66b543947ffc
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFClockStateSinkVtbl, IMFClockStateSinkVtbl
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

# IMFClockStateSinkVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFClockStateSink *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFClockStateSink *This) AddRef			
 	
### -field ULONG(* )(IMFClockStateSink *This) Release			
 	
### -field HRESULT(* )(IMFClockStateSink *This,MFTIME hnsSystemTime,LONGLONG llClockStartOffset) OnClockStart			
 	
### -field HRESULT(* )(IMFClockStateSink *This,MFTIME hnsSystemTime) OnClockStop			
 	
### -field HRESULT(* )(IMFClockStateSink *This,MFTIME hnsSystemTime) OnClockPause			
 	
### -field HRESULT(* )(IMFClockStateSink *This,MFTIME hnsSystemTime) OnClockRestart			
 	
### -field HRESULT(* )(IMFClockStateSink *This,MFTIME hnsSystemTime, float flRate) OnClockSetRate			
 	
## -remarks

## -see-also