---
UID: NS.filterpipeline.IPartFont2Vtbl
title: IPartFont2Vtbl
author: windows-driver-content
description: 
ms.assetid: 50a80ff9-6e4c-4a53-8d3c-a267efad1d7a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartFont2Vtbl, IPartFont2Vtbl
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

# IPartFont2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartFont2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartFont2 *This) AddRef			
 	
### -field ULONG(* )(IPartFont2 *This) Release			
 	
### -field HRESULT(* )(IPartFont2 *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IPartFont2 *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IPartFont2 *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IPartFont2 *This,EXpsCompressionOptions compression) SetPartCompression			
 	
### -field HRESULT(* )(IPartFont2 *This,BSTR *pContentType,EXpsFontOptions *pFontOptions) GetFontProperties			
 	
### -field HRESULT(* )(IPartFont2 *This, const wchar_t *pContentType) SetFontContent			
 	
### -field HRESULT(* )(IPartFont2 *This,EXpsFontOptions options) SetFontOptions			
 	
### -field HRESULT(* )(IPartFont2 *This,EXpsFontRestriction *pRestriction) GetFontRestriction			
 	
## -remarks

## -see-also