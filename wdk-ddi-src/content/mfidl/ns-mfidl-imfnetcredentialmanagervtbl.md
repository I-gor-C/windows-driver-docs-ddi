---
UID: NS.mfidl.IMFNetCredentialManagerVtbl
title: IMFNetCredentialManagerVtbl
author: windows-driver-content
description: 
ms.assetid: 601dccac-5183-485e-9761-032dbdb03914
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFNetCredentialManagerVtbl, IMFNetCredentialManagerVtbl
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

# IMFNetCredentialManagerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFNetCredentialManager *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFNetCredentialManager *This) AddRef			
 	
### -field ULONG(* )(IMFNetCredentialManager *This) Release			
 	
### -field HRESULT(* )(IMFNetCredentialManager *This,MFNetCredentialManagerGetParam *pParam,IMFAsyncCallback *pCallback,IUnknown *pState) BeginGetCredentials			
 	
### -field HRESULT(* )(IMFNetCredentialManager *This,IMFAsyncResult *pResult,IMFNetCredential **ppCred) EndGetCredentials			
 	
### -field HRESULT(* )(IMFNetCredentialManager *This,IMFNetCredential *pCred,BOOL fGood) SetGood			
 	
## -remarks

## -see-also