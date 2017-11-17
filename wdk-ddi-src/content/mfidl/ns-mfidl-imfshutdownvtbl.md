---
UID: NS.mfidl.IMFShutdownVtbl
title: IMFShutdownVtbl
author: windows-driver-content
description: 
ms.assetid: 011fe913-70ce-4fe2-9040-2b0932a450ef
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFShutdownVtbl, IMFShutdownVtbl
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

# IMFShutdownVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFShutdown *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFShutdown *This) AddRef			
 	
### -field ULONG(* )(IMFShutdown *This) Release			
 	
### -field HRESULT(* )(IMFShutdown *This) Shutdown			
 	
### -field HRESULT(* )(IMFShutdown *This,MFSHUTDOWN_STATUS *pStatus) GetShutdownStatus			
 	
## -remarks

## -see-also