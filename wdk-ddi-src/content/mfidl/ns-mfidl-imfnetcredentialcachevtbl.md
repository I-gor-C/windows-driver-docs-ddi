---
UID: NS.mfidl.IMFNetCredentialCacheVtbl
title: IMFNetCredentialCacheVtbl
author: windows-driver-content
description: 
ms.assetid: 8028fe51-ad67-4c82-bb59-10142ecc28f2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFNetCredentialCacheVtbl, IMFNetCredentialCacheVtbl
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

# IMFNetCredentialCacheVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFNetCredentialCache *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFNetCredentialCache *This) AddRef			
 	
### -field ULONG(* )(IMFNetCredentialCache *This) Release			
 	
### -field HRESULT(* )(IMFNetCredentialCache *This,LPCWSTR pszUrl,LPCWSTR pszRealm,DWORD dwAuthenticationFlags,IMFNetCredential **ppCred,DWORD *pdwRequirementsFlags) GetCredential			
 	
### -field HRESULT(* )(IMFNetCredentialCache *This,IMFNetCredential *pCred,BOOL fGood) SetGood			
 	
### -field HRESULT(* )(IMFNetCredentialCache *This,IMFNetCredential *pCred,DWORD dwOptionsFlags) SetUserOptions			
 	
## -remarks

## -see-also