---
UID: NS.filterpipeline.IFixedDocumentVtbl
title: IFixedDocumentVtbl
author: windows-driver-content
description: 
ms.assetid: 5aa09631-add9-4be7-8cda-3264cb24e9db
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IFixedDocumentVtbl, IFixedDocumentVtbl
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

# IFixedDocumentVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IFixedDocument *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IFixedDocument *This) AddRef			
 	
### -field ULONG(* )(IFixedDocument *This) Release			
 	
### -field HRESULT(* )(IFixedDocument *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IFixedDocument *This,IPartPrintTicket **ppPrintTicket) GetPrintTicket			
 	
### -field HRESULT(* )(IFixedDocument *This,IPartPrintTicket *pPrintTicket) SetPrintTicket			
 	
## -remarks

## -see-also