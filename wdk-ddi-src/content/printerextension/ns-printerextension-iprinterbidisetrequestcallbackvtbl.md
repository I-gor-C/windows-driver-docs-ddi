---
UID: NS.printerextension.IPrinterBidiSetRequestCallbackVtbl
title: IPrinterBidiSetRequestCallbackVtbl
author: windows-driver-content
description: 
ms.assetid: 3333cab8-0eb5-4625-ac86-925d9e2848c7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterBidiSetRequestCallbackVtbl, IPrinterBidiSetRequestCallbackVtbl
req.header: printerextension.h
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

# IPrinterBidiSetRequestCallbackVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterBidiSetRequestCallback *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterBidiSetRequestCallback *This) AddRef			
 	
### -field ULONG(* )(IPrinterBidiSetRequestCallback *This) Release			
 	
### -field HRESULT(* )(IPrinterBidiSetRequestCallback *This,BSTR bstrResponse,HRESULT hrStatus) Completed			
 	
## -remarks

## -see-also