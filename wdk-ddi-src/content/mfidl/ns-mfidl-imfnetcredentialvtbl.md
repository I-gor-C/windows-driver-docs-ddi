---
UID: NS.mfidl.IMFNetCredentialVtbl
title: IMFNetCredentialVtbl
author: windows-driver-content
description: 
ms.assetid: 2c19fa22-5d14-418a-84d9-21f15bc22bfa
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFNetCredentialVtbl, IMFNetCredentialVtbl
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

# IMFNetCredentialVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFNetCredential *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFNetCredential *This) AddRef			
 	
### -field ULONG(* )(IMFNetCredential *This) Release			
 	
### -field HRESULT(* )(IMFNetCredential *This,BYTE *pbData,DWORD cbData,BOOL fDataIsEncrypted) SetUser			
 	
### -field HRESULT(* )(IMFNetCredential *This,BYTE *pbData,DWORD cbData,BOOL fDataIsEncrypted) SetPassword			
 	
### -field HRESULT(* )(IMFNetCredential *This,BYTE *pbData,DWORD *pcbData,BOOL fEncryptData) GetUser			
 	
### -field HRESULT(* )(IMFNetCredential *This,BYTE *pbData,DWORD *pcbData,BOOL fEncryptData) GetPassword			
 	
### -field HRESULT(* )(IMFNetCredential *This,BOOL *pfLoggedOnUser) LoggedOnUser			
 	
## -remarks

## -see-also