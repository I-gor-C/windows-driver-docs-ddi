---
UID: NS.filterpipeline.IXpsDocumentVtbl
title: IXpsDocumentVtbl
author: windows-driver-content
description: 
ms.assetid: 2d21ae5f-260b-4269-85cf-5d9072572458
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IXpsDocumentVtbl, IXpsDocumentVtbl
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

# IXpsDocumentVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IXpsDocument *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IXpsDocument *This) AddRef			
 	
### -field ULONG(* )(IXpsDocument *This) Release			
 	
### -field HRESULT(* )(IXpsDocument *This,IPartThumbnail **ppThumbnail) GetThumbnail			
 	
### -field HRESULT(* )(IXpsDocument *This,IPartThumbnail *pThumbnail) SetThumbnail			
 	
## -remarks

## -see-also