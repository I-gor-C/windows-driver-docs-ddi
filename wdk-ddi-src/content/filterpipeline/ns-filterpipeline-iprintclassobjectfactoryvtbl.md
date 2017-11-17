---
UID: NS.filterpipeline.IPrintClassObjectFactoryVtbl
title: IPrintClassObjectFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: b64c791e-971c-4ea5-b881-bf68983bfd0c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintClassObjectFactoryVtbl, IPrintClassObjectFactoryVtbl
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

# IPrintClassObjectFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintClassObjectFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintClassObjectFactory *This) AddRef			
 	
### -field ULONG(* )(IPrintClassObjectFactory *This) Release			
 	
### -field HRESULT(* )(IPrintClassObjectFactory *This, const wchar_t *pszPrinterName,REFIID riid, void **ppNewObject) GetPrintClassObject			
 	
## -remarks

## -see-also