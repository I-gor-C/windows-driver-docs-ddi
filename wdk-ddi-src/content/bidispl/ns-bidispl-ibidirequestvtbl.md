---
UID: NS.bidispl.IBidiRequestVtbl
title: IBidiRequestVtbl
author: windows-driver-content
description: 
ms.assetid: cc1e5030-7671-43b1-bf96-e6b4230980d2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IBidiRequestVtbl, IBidiRequestVtbl
req.header: bidispl.h
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

# IBidiRequestVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IBidiRequest *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IBidiRequest *This) AddRef			
 	
### -field ULONG(* )(IBidiRequest *This) Release			
 	
### -field HRESULT(* )(IBidiRequest *This, const LPCWSTR pszSchema) SetSchema			
 	
### -field HRESULT(* )(IBidiRequest *This, const DWORD dwType, const BYTE *pData, const UINT uSize) SetInputData			
 	
### -field HRESULT(* )(IBidiRequest *This,HRESULT *phr) GetResult			
 	
### -field HRESULT(* )(IBidiRequest *This, const DWORD dwIndex,LPWSTR *ppszSchema,DWORD *pdwType,BYTE **ppData,ULONG *uSize) GetOutputData			
 	
### -field HRESULT(* )(IBidiRequest *This,DWORD *pdwTotal) GetEnumCount			
 	
## -remarks

## -see-also