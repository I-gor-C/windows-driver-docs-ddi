---
UID: NS.mfidl.IMFMetadataVtbl
title: IMFMetadataVtbl
author: windows-driver-content
description: 
ms.assetid: a3f20f12-7219-428b-91a7-be56565ff159
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMetadataVtbl, IMFMetadataVtbl
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

# IMFMetadataVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMetadata *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMetadata *This) AddRef			
 	
### -field ULONG(* )(IMFMetadata *This) Release			
 	
### -field HRESULT(* )(IMFMetadata *This,LPCWSTR pwszRFC1766) SetLanguage			
 	
### -field HRESULT(* )(IMFMetadata *This,LPWSTR *ppwszRFC1766) GetLanguage			
 	
### -field HRESULT(* )(IMFMetadata *This,PROPVARIANT *ppvLanguages) GetAllLanguages			
 	
### -field HRESULT(* )(IMFMetadata *This,LPCWSTR pwszName, const PROPVARIANT *ppvValue) SetProperty			
 	
### -field HRESULT(* )(IMFMetadata *This,LPCWSTR pwszName,PROPVARIANT *ppvValue) GetProperty			
 	
### -field HRESULT(* )(IMFMetadata *This,LPCWSTR pwszName) DeleteProperty			
 	
### -field HRESULT(* )(IMFMetadata *This,PROPVARIANT *ppvNames) GetAllPropertyNames			
 	
## -remarks

## -see-also