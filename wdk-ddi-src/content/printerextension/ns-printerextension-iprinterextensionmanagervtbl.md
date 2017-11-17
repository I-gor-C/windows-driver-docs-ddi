---
UID: NS.printerextension.IPrinterExtensionManagerVtbl
title: IPrinterExtensionManagerVtbl
author: windows-driver-content
description: 
ms.assetid: 5f303e0f-bd45-4e5a-8eba-bfc03fb4c062
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterExtensionManagerVtbl, IPrinterExtensionManagerVtbl
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

# IPrinterExtensionManagerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterExtensionManager *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterExtensionManager *This) AddRef			
 	
### -field ULONG(* )(IPrinterExtensionManager *This) Release			
 	
### -field HRESULT(* )(IPrinterExtensionManager *This,GUID printerDriverId) EnableEvents			
 	
### -field HRESULT(* )(IPrinterExtensionManager *This) DisableEvents			
 	
## -remarks

## -see-also