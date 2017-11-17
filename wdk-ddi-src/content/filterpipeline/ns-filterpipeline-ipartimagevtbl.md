---
UID: NS.filterpipeline.IPartImageVtbl
title: IPartImageVtbl
author: windows-driver-content
description: 
ms.assetid: 9c43f0a4-a99d-45ef-b9fa-77ccd86d6fba
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartImageVtbl, IPartImageVtbl
req.header: filterpipeline.h
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

# IPartImageVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartImage *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartImage *This) AddRef			
 	
### -field ULONG(* )(IPartImage *This) Release			
 	
### -field HRESULT(* )(IPartImage *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IPartImage *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IPartImage *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IPartImage *This,EXpsCompressionOptions compression) SetPartCompression			
 	
### -field HRESULT(* )(IPartImage *This,BSTR *pContentType) GetImageProperties			
 	
### -field HRESULT(* )(IPartImage *This, const wchar_t *pContentType) SetImageContent			
 	
## -remarks

## -see-also