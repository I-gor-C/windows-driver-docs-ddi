---
UID: NS.mfidl.IMFSecureChannelVtbl
title: IMFSecureChannelVtbl
author: windows-driver-content
description: 
ms.assetid: 4b96e8df-19bc-4d9d-8a3a-4d524380447a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSecureChannelVtbl, IMFSecureChannelVtbl
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

# IMFSecureChannelVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSecureChannel *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSecureChannel *This) AddRef			
 	
### -field ULONG(* )(IMFSecureChannel *This) Release			
 	
### -field HRESULT(* )(IMFSecureChannel *This,BYTE **ppCert,DWORD *pcbCert) GetCertificate			
 	
### -field HRESULT(* )(IMFSecureChannel *This,BYTE *pbEncryptedSessionKey,DWORD cbSessionKey) SetupSession			
 	
## -remarks

## -see-also