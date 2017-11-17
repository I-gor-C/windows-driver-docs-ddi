---
UID: NS.filterpipeline.IXpsPartIteratorVtbl
title: IXpsPartIteratorVtbl
author: windows-driver-content
description: 
ms.assetid: 062fed03-e4d0-4070-bbdf-5d1c6a9b4e42
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IXpsPartIteratorVtbl, IXpsPartIteratorVtbl
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

# IXpsPartIteratorVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IXpsPartIterator *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IXpsPartIterator *This) AddRef			
 	
### -field ULONG(* )(IXpsPartIterator *This) Release			
 	
### -field void(* )(IXpsPartIterator *This) Reset			
 	
### -field HRESULT(* )(IXpsPartIterator *This,BSTR *pUri,IUnknown **ppXpsPart) Current			
 	
### -field BOOL(* )(IXpsPartIterator *This) IsDone			
 	
### -field void(* )(IXpsPartIterator *This) Next			
 	
## -remarks

## -see-also