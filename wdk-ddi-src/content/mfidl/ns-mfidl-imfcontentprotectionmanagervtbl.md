---
UID: NS.mfidl.IMFContentProtectionManagerVtbl
title: IMFContentProtectionManagerVtbl
author: windows-driver-content
description: 
ms.assetid: 01ddc47f-d29a-49a7-83a3-bc03f7847dcc
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFContentProtectionManagerVtbl, IMFContentProtectionManagerVtbl
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

# IMFContentProtectionManagerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFContentProtectionManager *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFContentProtectionManager *This) AddRef			
 	
### -field ULONG(* )(IMFContentProtectionManager *This) Release			
 	
### -field HRESULT(* )(IMFContentProtectionManager *This,IMFActivate *pEnablerActivate,IMFTopology *pTopo,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginEnableContent			
 	
### -field HRESULT(* )(IMFContentProtectionManager *This,IMFAsyncResult *pResult) EndEnableContent			
 	
## -remarks

## -see-also