---
UID: NS.mfidl.IMFInputTrustAuthorityVtbl
title: IMFInputTrustAuthorityVtbl
author: windows-driver-content
description: 
ms.assetid: 5272c9a7-d531-4895-878b-5e9c1db440c2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFInputTrustAuthorityVtbl, IMFInputTrustAuthorityVtbl
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

# IMFInputTrustAuthorityVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFInputTrustAuthority *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFInputTrustAuthority *This) AddRef			
 	
### -field ULONG(* )(IMFInputTrustAuthority *This) Release			
 	
### -field HRESULT(* )(IMFInputTrustAuthority *This,REFIID riid, void **ppv) GetDecrypter			
 	
### -field HRESULT(* )(IMFInputTrustAuthority *This,MFPOLICYMANAGER_ACTION Action,IMFActivate **ppContentEnablerActivate) RequestAccess			
 	
### -field HRESULT(* )(IMFInputTrustAuthority *This,MFPOLICYMANAGER_ACTION Action,IMFOutputPolicy **ppPolicy) GetPolicy			
 	
### -field HRESULT(* )(IMFInputTrustAuthority *This,MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS *pParam) BindAccess			
 	
### -field HRESULT(* )(IMFInputTrustAuthority *This,MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS *pParam) UpdateAccess			
 	
### -field HRESULT(* )(IMFInputTrustAuthority *This) Reset			
 	
## -remarks

## -see-also