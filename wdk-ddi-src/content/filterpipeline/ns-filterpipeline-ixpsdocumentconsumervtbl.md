---
UID: NS.filterpipeline.IXpsDocumentConsumerVtbl
title: IXpsDocumentConsumerVtbl
author: windows-driver-content
description: 
ms.assetid: f1993a5d-8b16-4a15-85a3-9c9b767e9818
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IXpsDocumentConsumerVtbl, IXpsDocumentConsumerVtbl
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

# IXpsDocumentConsumerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IXpsDocumentConsumer *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IXpsDocumentConsumer *This) AddRef			
 	
### -field ULONG(* )(IXpsDocumentConsumer *This) Release			
 	
### -field HRESULT(* )(IXpsDocumentConsumer *This,IUnknown *pUnknown) SendXpsUnknown			
 	
### -field HRESULT(* )(IXpsDocumentConsumer *This,IXpsDocument *pIXpsDocument) SendXpsDocument			
 	
### -field HRESULT(* )(IXpsDocumentConsumer *This,IFixedDocumentSequence *pIFixedDocumentSequence) SendFixedDocumentSequence			
 	
### -field HRESULT(* )(IXpsDocumentConsumer *This,IFixedDocument *pIFixedDocument) SendFixedDocument			
 	
### -field HRESULT(* )(IXpsDocumentConsumer *This,IFixedPage *pIFixedPage) SendFixedPage			
 	
### -field HRESULT(* )(IXpsDocumentConsumer *This) CloseSender			
 	
### -field HRESULT(* )(IXpsDocumentConsumer *This, const wchar_t *uri,REFIID riid, void **ppNewObject,IPrintWriteStream **ppWriteStream) GetNewEmptyPart			
 	
## -remarks

## -see-also