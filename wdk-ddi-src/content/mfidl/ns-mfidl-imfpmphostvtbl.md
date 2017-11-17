---
UID: NS.mfidl.IMFPMPHostVtbl
title: IMFPMPHostVtbl
author: windows-driver-content
description: 
ms.assetid: 9625b0b0-60a7-4d71-9de3-e12f4156a73d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFPMPHostVtbl, IMFPMPHostVtbl
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

# IMFPMPHostVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFPMPHost *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFPMPHost *This) AddRef			
 	
### -field ULONG(* )(IMFPMPHost *This) Release			
 	
### -field HRESULT(* )(IMFPMPHost *This) LockProcess			
 	
### -field HRESULT(* )(IMFPMPHost *This) UnlockProcess			
 	
### -field HRESULT(* )(IMFPMPHost *This,REFCLSID clsid,IStream *pStream,REFIID riid, void **ppv) CreateObjectByCLSID			
 	
## -remarks

## -see-also