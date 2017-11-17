---
UID: NS.wudfddi.IWDFNamedPropertyStore2Vtbl
title: IWDFNamedPropertyStore2Vtbl
author: windows-driver-content
description: 
ms.assetid: ee450572-e59f-4cb3-9143-707ed35777e5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFNamedPropertyStore2Vtbl, IWDFNamedPropertyStore2Vtbl
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

# IWDFNamedPropertyStore2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFNamedPropertyStore2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFNamedPropertyStore2 *This) AddRef			
 	
### -field ULONG(* )(IWDFNamedPropertyStore2 *This) Release			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore2 *This,LPCWSTR pszName,PROPVARIANT *pv) GetNamedValue			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore2 *This,LPCWSTR pszName, const PROPVARIANT *pv) SetNamedValue			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore2 *This,DWORD *pdwCount) GetNameCount			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore2 *This,DWORD iProp,PWSTR *ppwszName) GetNameAt			
 	
### -field HRESULT(* )(IWDFNamedPropertyStore2 *This,LPCWSTR pwszName) DeleteNamedValue			
 	
## -remarks

## -see-also