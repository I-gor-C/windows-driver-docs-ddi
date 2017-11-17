---
UID: NS.filterpipeline.IPartFontVtbl
title: IPartFontVtbl
author: windows-driver-content
description: 
ms.assetid: aca06cc1-4cc9-40fa-91f0-9057a04f6568
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartFontVtbl, IPartFontVtbl
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

# IPartFontVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartFont *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartFont *This) AddRef			
 	
### -field ULONG(* )(IPartFont *This) Release			
 	
### -field HRESULT(* )(IPartFont *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IPartFont *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IPartFont *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IPartFont *This,EXpsCompressionOptions compression) SetPartCompression			
 	
### -field HRESULT(* )(IPartFont *This,BSTR *pContentType,EXpsFontOptions *pFontOptions) GetFontProperties			
 	
### -field HRESULT(* )(IPartFont *This, const wchar_t *pContentType) SetFontContent			
 	
### -field HRESULT(* )(IPartFont *This,EXpsFontOptions options) SetFontOptions			
 	
## -remarks

## -see-also