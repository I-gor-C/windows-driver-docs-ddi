---
UID: NS.filterpipeline.IPartBaseVtbl
title: IPartBaseVtbl
author: windows-driver-content
description: 
ms.assetid: 6a70ee0c-4f52-4093-b845-e2d7c15d0ddf
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartBaseVtbl, IPartBaseVtbl
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

# IPartBaseVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartBase *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartBase *This) AddRef			
 	
### -field ULONG(* )(IPartBase *This) Release			
 	
### -field HRESULT(* )(IPartBase *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IPartBase *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IPartBase *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IPartBase *This,EXpsCompressionOptions compression) SetPartCompression			
 	
## -remarks

## -see-also