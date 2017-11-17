---
UID: NS.mfidl.IMFPMPServerVtbl
title: IMFPMPServerVtbl
author: windows-driver-content
description: 
ms.assetid: ab8eb960-6240-4960-9386-5b6c9552ce80
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFPMPServerVtbl, IMFPMPServerVtbl
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

# IMFPMPServerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFPMPServer *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFPMPServer *This) AddRef			
 	
### -field ULONG(* )(IMFPMPServer *This) Release			
 	
### -field HRESULT(* )(IMFPMPServer *This) LockProcess			
 	
### -field HRESULT(* )(IMFPMPServer *This) UnlockProcess			
 	
### -field HRESULT(* )(IMFPMPServer *This,REFCLSID clsid,REFIID riid, void **ppObject) CreateObjectByCLSID			
 	
## -remarks

## -see-also