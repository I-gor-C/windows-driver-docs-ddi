---
UID: NS.mfidl.IMFPMPHostAppVtbl
title: IMFPMPHostAppVtbl
author: windows-driver-content
description: 
ms.assetid: e409c40f-4dfc-4d20-81d4-fb3608d5878b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFPMPHostAppVtbl, IMFPMPHostAppVtbl
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

# IMFPMPHostAppVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFPMPHostApp *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFPMPHostApp *This) AddRef			
 	
### -field ULONG(* )(IMFPMPHostApp *This) Release			
 	
### -field HRESULT(* )(IMFPMPHostApp *This) LockProcess			
 	
### -field HRESULT(* )(IMFPMPHostApp *This) UnlockProcess			
 	
### -field HRESULT(* )(IMFPMPHostApp *This,LPCWSTR id,IStream *pStream,REFIID riid, void **ppv) ActivateClassById			
 	
## -remarks

## -see-also