---
UID: NS.mfidl.IMFTrustedInputVtbl
title: IMFTrustedInputVtbl
author: windows-driver-content
description: 
ms.assetid: d75f5146-89fa-41bd-84a7-2006c0361de2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTrustedInputVtbl, IMFTrustedInputVtbl
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

# IMFTrustedInputVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTrustedInput *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTrustedInput *This) AddRef			
 	
### -field ULONG(* )(IMFTrustedInput *This) Release			
 	
### -field HRESULT(* )(IMFTrustedInput *This,DWORD dwStreamID,REFIID riid,IUnknown **ppunkObject) GetInputTrustAuthority			
 	
## -remarks

## -see-also