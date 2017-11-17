---
UID: NS.wudfddi.IWDFUnifiedPropertyStoreFactoryVtbl
title: IWDFUnifiedPropertyStoreFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: 1fe8e761-e7f4-4f25-807e-4f17b4b28f2b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFUnifiedPropertyStoreFactoryVtbl, IWDFUnifiedPropertyStoreFactoryVtbl
req.header: wudfddi.h
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

# IWDFUnifiedPropertyStoreFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFUnifiedPropertyStoreFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFUnifiedPropertyStoreFactory *This) AddRef			
 	
### -field ULONG(* )(IWDFUnifiedPropertyStoreFactory *This) Release			
 	
### -field HRESULT(* )(IWDFUnifiedPropertyStoreFactory *This,PWDF_PROPERTY_STORE_ROOT RootSpecifier,IWDFUnifiedPropertyStore **PropertyStore) RetrieveUnifiedDevicePropertyStore			
 	
## -remarks

## -see-also