---
UID: NS.wudfddi.IWDFNamedPropertyStoreVtbl
title: IWDFNamedPropertyStoreVtbl
author: windows-driver-content
description: 
ms.assetid: 3395ea33-b8cf-443f-929e-97914ca2c360
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFNamedPropertyStoreVtbl, IWDFNamedPropertyStoreVtbl
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

# IWDFNamedPropertyStoreVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFNamedPropertyStore *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFNamedPropertyStore *This) AddRef			
 	
### -field ULONG(* )(IWDFNamedPropertyStore *This) Release			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore *This,LPCWSTR pszName,PROPVARIANT *pv) GetNamedValue			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore *This,LPCWSTR pszName, const PROPVARIANT *pv) SetNamedValue			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore *This,DWORD *pdwCount) GetNameCount			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore *This,DWORD iProp,PWSTR *ppwszName) GetNameAt			
 	
## -remarks

## -see-also