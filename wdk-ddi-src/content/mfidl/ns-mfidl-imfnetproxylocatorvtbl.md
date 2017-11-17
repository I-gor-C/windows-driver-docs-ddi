---
UID: NS.mfidl.IMFNetProxyLocatorVtbl
title: IMFNetProxyLocatorVtbl
author: windows-driver-content
description: 
ms.assetid: bc0f03b1-1bc0-4ace-a279-896b2b011b67
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFNetProxyLocatorVtbl, IMFNetProxyLocatorVtbl
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

# IMFNetProxyLocatorVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFNetProxyLocator *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFNetProxyLocator *This) AddRef			
 	
### -field ULONG(* )(IMFNetProxyLocator *This) Release			
 	
### -field HRESULT(* )(IMFNetProxyLocator *This,LPCWSTR pszHost,LPCWSTR pszUrl,BOOL fReserved) FindFirstProxy			
 	
### -field HRESULT(* )(IMFNetProxyLocator *This) FindNextProxy			
 	
### -field HRESULT(* )(IMFNetProxyLocator *This,HRESULT hrOp) RegisterProxyResult			
 	
### -field HRESULT(* )(IMFNetProxyLocator *This,LPWSTR pszStr,DWORD *pcchStr) GetCurrentProxy			
 	
### -field HRESULT(* )(IMFNetProxyLocator *This,IMFNetProxyLocator **ppProxyLocator) Clone			
 	
## -remarks

## -see-also