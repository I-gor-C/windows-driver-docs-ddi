---
UID: NS.mfidl.IMFProtectedEnvironmentAccessVtbl
title: IMFProtectedEnvironmentAccessVtbl
author: windows-driver-content
description: 
ms.assetid: 2534a07a-7fc5-40cf-a02c-4fc53d2a207a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFProtectedEnvironmentAccessVtbl, IMFProtectedEnvironmentAccessVtbl
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

# IMFProtectedEnvironmentAccessVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFProtectedEnvironmentAccess *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFProtectedEnvironmentAccess *This) AddRef			
 	
### -field ULONG(* )(IMFProtectedEnvironmentAccess *This) Release			
 	
### -field HRESULT(* )(IMFProtectedEnvironmentAccess *This,UINT32 inputLength, const BYTE *input,UINT32 outputLength,BYTE *output) Call			
 	
### -field HRESULT(* )(IMFProtectedEnvironmentAccess *This,UINT32 *outputLength,BYTE **output) ReadGRL			
 	
## -remarks

## -see-also