---
UID: NS.filterpipeline.IFixedDocumentSequenceVtbl
title: IFixedDocumentSequenceVtbl
author: windows-driver-content
description: 
ms.assetid: 35575847-6a25-49d9-bdba-cea6dd09db74
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IFixedDocumentSequenceVtbl, IFixedDocumentSequenceVtbl
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

# IFixedDocumentSequenceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IFixedDocumentSequence *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IFixedDocumentSequence *This) AddRef			
 	
### -field ULONG(* )(IFixedDocumentSequence *This) Release			
 	
### -field HRESULT(* )(IFixedDocumentSequence *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IFixedDocumentSequence *This,IPartPrintTicket **ppPrintTicket) GetPrintTicket			
 	
### -field HRESULT(* )(IFixedDocumentSequence *This,IPartPrintTicket *pPrintTicket) SetPrintTicket			
 	
## -remarks

## -see-also