---
UID: NS.mfidl.IMFByteStreamTimeSeekVtbl
title: IMFByteStreamTimeSeekVtbl
author: windows-driver-content
description: 
ms.assetid: f8e231bb-c282-4639-8bd4-199b8293dc65
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFByteStreamTimeSeekVtbl, IMFByteStreamTimeSeekVtbl
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

# IMFByteStreamTimeSeekVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFByteStreamTimeSeek *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFByteStreamTimeSeek *This) AddRef			
 	
### -field ULONG(* )(IMFByteStreamTimeSeek *This) Release			
 	
### -field HRESULT(* )(IMFByteStreamTimeSeek *This,BOOL *pfTimeSeekIsSupported) IsTimeSeekSupported			
 	
### -field HRESULT(* )(IMFByteStreamTimeSeek *This,QWORD qwTimePosition) TimeSeek			
 	
### -field HRESULT(* )(IMFByteStreamTimeSeek *This,QWORD *pqwStartTime,QWORD *pqwStopTime,QWORD *pqwDuration) GetTimeSeekResult			
 	
## -remarks

## -see-also