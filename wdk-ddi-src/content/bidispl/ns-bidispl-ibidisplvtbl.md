---
UID: NS.bidispl.IBidiSplVtbl
title: IBidiSplVtbl
author: windows-driver-content
description: 
ms.assetid: 2a5c2a5e-9e0d-4a0d-98a6-ddbe22e005bc
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IBidiSplVtbl, IBidiSplVtbl
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

# IBidiSplVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IBidiSpl *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IBidiSpl *This) AddRef			
 	
### -field ULONG(* )(IBidiSpl *This) Release			
 	
### -field HRESULT(* )(IBidiSpl *This, const LPCWSTR pszDeviceName, const DWORD dwAccess) BindDevice			
 	
### -field HRESULT(* )(IBidiSpl *This) UnbindDevice			
 	
### -field HRESULT(* )(IBidiSpl *This, const LPCWSTR pszAction,IBidiRequest *pRequest) SendRecv			
 	
### -field HRESULT(* )(IBidiSpl *This, const LPCWSTR pszAction,IBidiRequestContainer *pRequestContainer) MultiSendRecv			
 	
## -remarks

## -see-also