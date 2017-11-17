---
UID: NS.filterpipeline.IInterFilterCommunicatorVtbl
title: IInterFilterCommunicatorVtbl
author: windows-driver-content
description: 
ms.assetid: ffbf3e82-68f1-40e8-95bd-1452aab1cfca
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IInterFilterCommunicatorVtbl, IInterFilterCommunicatorVtbl
req.header: filterpipeline.h
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

# IInterFilterCommunicatorVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IInterFilterCommunicator *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IInterFilterCommunicator *This) AddRef			
 	
### -field ULONG(* )(IInterFilterCommunicator *This) Release			
 	
### -field HRESULT(* )(IInterFilterCommunicator *This, void **ppIReader) RequestReader			
 	
### -field HRESULT(* )(IInterFilterCommunicator *This, void **ppIWriter) RequestWriter			
 	
## -remarks

## -see-also