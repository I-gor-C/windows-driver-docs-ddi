---
UID: NS.mfidl.IMFByteStreamBufferingVtbl
title: IMFByteStreamBufferingVtbl
author: windows-driver-content
description: 
ms.assetid: 4c457042-dda5-4047-ade7-4d3a2e0271c2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFByteStreamBufferingVtbl, IMFByteStreamBufferingVtbl
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

# IMFByteStreamBufferingVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFByteStreamBuffering *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFByteStreamBuffering *This) AddRef			
 	
### -field ULONG(* )(IMFByteStreamBuffering *This) Release			
 	
### -field HRESULT(* )(IMFByteStreamBuffering *This,MFBYTESTREAM_BUFFERING_PARAMS *pParams) SetBufferingParams			
 	
### -field HRESULT(* )(IMFByteStreamBuffering *This,BOOL fEnable) EnableBuffering			
 	
### -field HRESULT(* )(IMFByteStreamBuffering *This) StopBuffering			
 	
## -remarks

## -see-also