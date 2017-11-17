---
UID: NS.mfidl.IMFNetProxyLocatorFactoryVtbl
title: IMFNetProxyLocatorFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: 01d06006-cc71-48ad-aacb-ac7076863645
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFNetProxyLocatorFactoryVtbl, IMFNetProxyLocatorFactoryVtbl
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

# IMFNetProxyLocatorFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFNetProxyLocatorFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFNetProxyLocatorFactory *This) AddRef			
 	
### -field ULONG(* )(IMFNetProxyLocatorFactory *This) Release			
 	
### -field HRESULT(* )(IMFNetProxyLocatorFactory *This,LPCWSTR pszProtocol,IMFNetProxyLocator **ppProxyLocator) CreateProxyLocator			
 	
## -remarks

## -see-also