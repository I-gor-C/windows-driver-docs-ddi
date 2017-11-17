---
UID: NS.mfidl.IMFByteStreamCacheControl2Vtbl
title: IMFByteStreamCacheControl2Vtbl
author: windows-driver-content
description: 
ms.assetid: 797e2724-6576-4158-843b-0281864e92d0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFByteStreamCacheControl2Vtbl, IMFByteStreamCacheControl2Vtbl
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

# IMFByteStreamCacheControl2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFByteStreamCacheControl2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFByteStreamCacheControl2 *This) AddRef			
 	
### -field ULONG(* )(IMFByteStreamCacheControl2 *This) Release			
 	
### -field HRESULT(* )(IMFByteStreamCacheControl2 *This) StopBackgroundTransfer			
 	
### -field HRESULT(* )(IMFByteStreamCacheControl2 *This,DWORD *pcRanges,MF_BYTE_STREAM_CACHE_RANGE **ppRanges) GetByteRanges			
 	
### -field HRESULT(* )(IMFByteStreamCacheControl2 *This,QWORD qwBytes) SetCacheLimit			
 	
### -field HRESULT(* )(IMFByteStreamCacheControl2 *This,BOOL *pfActive) IsBackgroundTransferActive			
 	
## -remarks

## -see-also