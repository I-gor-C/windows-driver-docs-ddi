---
UID: NS.mfidl.IMFSAMIStyleVtbl
title: IMFSAMIStyleVtbl
author: windows-driver-content
description: 
ms.assetid: ee401e68-8934-4fb7-93dd-a4bd5be047ac
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSAMIStyleVtbl, IMFSAMIStyleVtbl
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

# IMFSAMIStyleVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSAMIStyle *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSAMIStyle *This) AddRef			
 	
### -field ULONG(* )(IMFSAMIStyle *This) Release			
 	
### -field HRESULT(* )(IMFSAMIStyle *This,DWORD *pdwCount) GetStyleCount			
 	
### -field HRESULT(* )(IMFSAMIStyle *This,PROPVARIANT *pPropVarStyleArray) GetStyles			
 	
### -field HRESULT(* )(IMFSAMIStyle *This,LPCWSTR pwszStyle) SetSelectedStyle			
 	
### -field HRESULT(* )(IMFSAMIStyle *This,LPWSTR *ppwszStyle) GetSelectedStyle			
 	
## -remarks

## -see-also