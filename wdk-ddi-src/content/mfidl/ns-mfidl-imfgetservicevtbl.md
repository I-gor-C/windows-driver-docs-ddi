---
UID: NS.mfidl.IMFGetServiceVtbl
title: IMFGetServiceVtbl
author: windows-driver-content
description: 
ms.assetid: be3f1910-778c-4bde-bdaf-f8df7515b77a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFGetServiceVtbl, IMFGetServiceVtbl
req.header: mfidl.h
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

# IMFGetServiceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFGetService *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFGetService *This) AddRef			
 	
### -field ULONG(* )(IMFGetService *This) Release			
 	
### -field HRESULT(* )(IMFGetService *This,REFGUID guidService,REFIID riid,LPVOID *ppvObject) GetService			
 	
## -remarks

## -see-also