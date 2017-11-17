---
UID: NS.mfidl.IMFOutputTrustAuthorityVtbl
title: IMFOutputTrustAuthorityVtbl
author: windows-driver-content
description: 
ms.assetid: f97ea971-010f-4e12-9979-69ce25699f28
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFOutputTrustAuthorityVtbl, IMFOutputTrustAuthorityVtbl
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

# IMFOutputTrustAuthorityVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFOutputTrustAuthority *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFOutputTrustAuthority *This) AddRef			
 	
### -field ULONG(* )(IMFOutputTrustAuthority *This) Release			
 	
### -field HRESULT(* )(IMFOutputTrustAuthority *This,MFPOLICYMANAGER_ACTION *pAction) GetAction			
 	
### -field HRESULT(* )(IMFOutputTrustAuthority *This,IMFOutputPolicy **ppPolicy,DWORD nPolicy,BYTE **ppbTicket,DWORD *pcbTicket) SetPolicy			
 	
## -remarks

## -see-also