---
UID: NS.mfidl.IMFObjectReferenceStreamVtbl
title: IMFObjectReferenceStreamVtbl
author: windows-driver-content
description: 
ms.assetid: d5d6f514-6d48-45a6-9410-a36a5049116a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFObjectReferenceStreamVtbl, IMFObjectReferenceStreamVtbl
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

# IMFObjectReferenceStreamVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFObjectReferenceStream *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFObjectReferenceStream *This) AddRef			
 	
### -field ULONG(* )(IMFObjectReferenceStream *This) Release			
 	
### -field HRESULT(* )(IMFObjectReferenceStream *This,REFIID riid,IUnknown *pUnk) SaveReference			
 	
### -field HRESULT(* )(IMFObjectReferenceStream *This,REFIID riid, void **ppv) LoadReference			
 	
## -remarks

## -see-also