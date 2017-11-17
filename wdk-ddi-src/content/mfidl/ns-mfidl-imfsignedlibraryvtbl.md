---
UID: NS.mfidl.IMFSignedLibraryVtbl
title: IMFSignedLibraryVtbl
author: windows-driver-content
description: 
ms.assetid: d559e97b-1759-4ee3-9c4d-6606219c8fad
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSignedLibraryVtbl, IMFSignedLibraryVtbl
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

# IMFSignedLibraryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSignedLibrary *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSignedLibrary *This) AddRef			
 	
### -field ULONG(* )(IMFSignedLibrary *This) Release			
 	
### -field HRESULT(* )(IMFSignedLibrary *This,LPCSTR name,PVOID *address) GetProcedureAddress			
 	
## -remarks

## -see-also