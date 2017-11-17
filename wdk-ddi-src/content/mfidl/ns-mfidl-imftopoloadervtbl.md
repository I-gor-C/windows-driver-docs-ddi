---
UID: NS.mfidl.IMFTopoLoaderVtbl
title: IMFTopoLoaderVtbl
author: windows-driver-content
description: 
ms.assetid: aa859ae8-084d-42c9-b92d-3384dd5ac2ff
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTopoLoaderVtbl, IMFTopoLoaderVtbl
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

# IMFTopoLoaderVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTopoLoader *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTopoLoader *This) AddRef			
 	
### -field ULONG(* )(IMFTopoLoader *This) Release			
 	
### -field HRESULT(* )(IMFTopoLoader *This,IMFTopology *pInputTopo,IMFTopology **ppOutputTopo,IMFTopology *pCurrentTopo) Load			
 	
## -remarks

## -see-also