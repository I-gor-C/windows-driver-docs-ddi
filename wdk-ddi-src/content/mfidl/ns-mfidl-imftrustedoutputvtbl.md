---
UID: NS.mfidl.IMFTrustedOutputVtbl
title: IMFTrustedOutputVtbl
author: windows-driver-content
description: 
ms.assetid: 5e2d2f75-1741-4d10-a272-24e8719fe3e5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTrustedOutputVtbl, IMFTrustedOutputVtbl
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

# IMFTrustedOutputVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTrustedOutput *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTrustedOutput *This) AddRef			
 	
### -field ULONG(* )(IMFTrustedOutput *This) Release			
 	
### -field HRESULT(* )(IMFTrustedOutput *This,DWORD *pcOutputTrustAuthorities) GetOutputTrustAuthorityCount			
 	
### -field HRESULT(* )(IMFTrustedOutput *This,DWORD dwIndex,IMFOutputTrustAuthority **ppauthority) GetOutputTrustAuthorityByIndex			
 	
### -field HRESULT(* )(IMFTrustedOutput *This,BOOL *pfIsFinal) IsFinal			
 	
## -remarks

## -see-also