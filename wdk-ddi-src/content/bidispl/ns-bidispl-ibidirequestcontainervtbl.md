---
UID: NS.bidispl.IBidiRequestContainerVtbl
title: IBidiRequestContainerVtbl
author: windows-driver-content
description: 
ms.assetid: 2199621c-5b8d-4fe4-ae57-2827af981a96
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IBidiRequestContainerVtbl, IBidiRequestContainerVtbl
req.header: bidispl.h
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

# IBidiRequestContainerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IBidiRequestContainer *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IBidiRequestContainer *This) AddRef			
 	
### -field ULONG(* )(IBidiRequestContainer *This) Release			
 	
### -field HRESULT(* )(IBidiRequestContainer *This,IBidiRequest *pRequest) AddRequest			
 	
### -field HRESULT(* )(IBidiRequestContainer *This,ULONG *puCount) GetRequestCount			
 	
## -remarks

## -see-also