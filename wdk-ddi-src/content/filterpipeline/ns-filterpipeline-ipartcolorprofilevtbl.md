---
UID: NS.filterpipeline.IPartColorProfileVtbl
title: IPartColorProfileVtbl
author: windows-driver-content
description: 
ms.assetid: 9e79da50-3403-495b-8acb-e8d0f76747de
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartColorProfileVtbl, IPartColorProfileVtbl
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

# IPartColorProfileVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartColorProfile *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartColorProfile *This) AddRef			
 	
### -field ULONG(* )(IPartColorProfile *This) Release			
 	
### -field HRESULT(* )(IPartColorProfile *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IPartColorProfile *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IPartColorProfile *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IPartColorProfile *This,EXpsCompressionOptions compression) SetPartCompression			
 	
## -remarks

## -see-also