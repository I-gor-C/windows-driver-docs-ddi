---
UID: NS.filterpipeline.IPartPrintTicketVtbl
title: IPartPrintTicketVtbl
author: windows-driver-content
description: 
ms.assetid: de478a38-6d2b-4174-a7f7-6944d2451770
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartPrintTicketVtbl, IPartPrintTicketVtbl
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

# IPartPrintTicketVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartPrintTicket *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartPrintTicket *This) AddRef			
 	
### -field ULONG(* )(IPartPrintTicket *This) Release			
 	
### -field HRESULT(* )(IPartPrintTicket *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IPartPrintTicket *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IPartPrintTicket *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IPartPrintTicket *This,EXpsCompressionOptions compression) SetPartCompression			
 	
## -remarks

## -see-also