---
UID: NS.wudfddi.IPnpCallbackHardwareVtbl
title: IPnpCallbackHardwareVtbl
author: windows-driver-content
description: 
ms.assetid: 80cd0eb0-c93e-4b5c-ab4b-cb585680bbf8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPnpCallbackHardwareVtbl, IPnpCallbackHardwareVtbl
req.header: wudfddi.h
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

# IPnpCallbackHardwareVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPnpCallbackHardware *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPnpCallbackHardware *This) AddRef			
 	
### -field ULONG(* )(IPnpCallbackHardware *This) Release			
 	
### -field HRESULT(* )(IPnpCallbackHardware *This,IWDFDevice *pWdfDevice) OnPrepareHardware			
 	
### -field HRESULT(* )(IPnpCallbackHardware *This,IWDFDevice *pWdfDevice) OnReleaseHardware			
 	
## -remarks

## -see-also