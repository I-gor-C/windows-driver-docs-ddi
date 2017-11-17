---
UID: NS.filterpipeline.IPartResourceDictionaryVtbl
title: IPartResourceDictionaryVtbl
author: windows-driver-content
description: 
ms.assetid: 915136b8-c887-4ec6-966b-aadbdae78b79
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartResourceDictionaryVtbl, IPartResourceDictionaryVtbl
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

# IPartResourceDictionaryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartResourceDictionary *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartResourceDictionary *This) AddRef			
 	
### -field ULONG(* )(IPartResourceDictionary *This) Release			
 	
### -field HRESULT(* )(IPartResourceDictionary *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IPartResourceDictionary *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IPartResourceDictionary *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IPartResourceDictionary *This,EXpsCompressionOptions compression) SetPartCompression			
 	
## -remarks

## -see-also