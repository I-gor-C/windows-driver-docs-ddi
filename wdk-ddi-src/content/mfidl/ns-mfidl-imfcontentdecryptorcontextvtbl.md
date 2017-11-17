---
UID: NS.mfidl.IMFContentDecryptorContextVtbl
title: IMFContentDecryptorContextVtbl
author: windows-driver-content
description: 
ms.assetid: 0f22ee63-020f-4335-bc36-50bbe23b7556
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFContentDecryptorContextVtbl, IMFContentDecryptorContextVtbl
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

# IMFContentDecryptorContextVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFContentDecryptorContext *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFContentDecryptorContext *This) AddRef			
 	
### -field ULONG(* )(IMFContentDecryptorContext *This) Release			
 	
### -field HRESULT(* )(IMFContentDecryptorContext *This,UINT InputPrivateDataByteCount, const void *InputPrivateData,UINT64 *OutputPrivateData) InitializeHardwareKey			
 	
## -remarks

## -see-also