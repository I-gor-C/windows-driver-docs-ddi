---
UID: NS.mfidl.IMFSystemIdVtbl
title: IMFSystemIdVtbl
author: windows-driver-content
description: 
ms.assetid: 9e5cc1f1-eb4b-480f-95ce-85514c01974d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSystemIdVtbl, IMFSystemIdVtbl
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

# IMFSystemIdVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSystemId *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSystemId *This) AddRef			
 	
### -field ULONG(* )(IMFSystemId *This) Release			
 	
### -field HRESULT(* )(IMFSystemId *This,UINT32 *size,BYTE **data) GetData			
 	
### -field HRESULT(* )(IMFSystemId *This,UINT32 stage,UINT32 cbIn, const BYTE *pbIn,UINT32 *pcbOut,BYTE **ppbOut) Setup			
 	
## -remarks

## -see-also