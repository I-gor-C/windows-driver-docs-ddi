---
UID: NS.mfidl.IMFRemoteProxyVtbl
title: IMFRemoteProxyVtbl
author: windows-driver-content
description: 
ms.assetid: 7a94b636-a9c5-4e4a-9729-d2f59ade7219
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFRemoteProxyVtbl, IMFRemoteProxyVtbl
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

# IMFRemoteProxyVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFRemoteProxy *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFRemoteProxy *This) AddRef			
 	
### -field ULONG(* )(IMFRemoteProxy *This) Release			
 	
### -field HRESULT(* )(IMFRemoteProxy *This,REFIID riid, void **ppv) GetRemoteObject			
 	
### -field HRESULT(* )(IMFRemoteProxy *This,REFIID riid, void **ppv) GetRemoteHost			
 	
## -remarks

## -see-also