---
UID: NS.igpupvdev.IVmGPUPGuestMsiAccessVtbl
title: IVmGPUPGuestMsiAccessVtbl
author: windows-driver-content
description: 
ms.assetid: 1dd31f47-68ab-4f24-8d4e-28ee51d34c43
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IVmGPUPGuestMsiAccessVtbl, IVmGPUPGuestMsiAccessVtbl
req.header: igpupvdev.h
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

# IVmGPUPGuestMsiAccessVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IVmGPUPGuestMsiAccess *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IVmGPUPGuestMsiAccess *This) AddRef			
 	
### -field ULONG(* )(IVmGPUPGuestMsiAccess *This) Release			
 	
### -field HRESULT(* )(IVmGPUPGuestMsiAccess *This,UINT32 DestAddr,UINT32 Data) DeliverInterrupt			
 	
## -remarks

## -see-also