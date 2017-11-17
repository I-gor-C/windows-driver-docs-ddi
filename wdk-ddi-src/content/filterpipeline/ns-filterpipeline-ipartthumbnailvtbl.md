---
UID: NS.filterpipeline.IPartThumbnailVtbl
title: IPartThumbnailVtbl
author: windows-driver-content
description: 
ms.assetid: 8b9969ab-841d-492c-a3a1-bcdf1f31b193
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartThumbnailVtbl, IPartThumbnailVtbl
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

# IPartThumbnailVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartThumbnail *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartThumbnail *This) AddRef			
 	
### -field ULONG(* )(IPartThumbnail *This) Release			
 	
### -field HRESULT(* )(IPartThumbnail *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IPartThumbnail *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IPartThumbnail *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IPartThumbnail *This,EXpsCompressionOptions compression) SetPartCompression			
 	
### -field HRESULT(* )(IPartThumbnail *This,BSTR *pContentType) GetThumbnailProperties			
 	
### -field HRESULT(* )(IPartThumbnail *This, const wchar_t *pContentType) SetThumbnailContent			
 	
## -remarks

## -see-also