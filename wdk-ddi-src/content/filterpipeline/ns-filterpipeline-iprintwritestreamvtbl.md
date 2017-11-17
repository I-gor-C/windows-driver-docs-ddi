---
UID: NS.filterpipeline.IPrintWriteStreamVtbl
title: IPrintWriteStreamVtbl
author: windows-driver-content
description: 
ms.assetid: 750dd3af-dbd2-4da8-a574-9e7b8ccf25fb
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintWriteStreamVtbl, IPrintWriteStreamVtbl
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

# IPrintWriteStreamVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintWriteStream *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintWriteStream *This) AddRef			
 	
### -field ULONG(* )(IPrintWriteStream *This) Release			
 	
### -field HRESULT(* )(IPrintWriteStream *This, const void *pvBuffer,ULONG cbBuffer,ULONG *pcbWritten) WriteBytes			
 	
### -field void(* )(IPrintWriteStream *This) Close			
 	
## -remarks

## -see-also