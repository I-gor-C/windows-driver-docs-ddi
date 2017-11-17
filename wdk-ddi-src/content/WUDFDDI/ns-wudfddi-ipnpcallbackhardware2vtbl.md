---
UID: NS.wudfddi.IPnpCallbackHardware2Vtbl
title: IPnpCallbackHardware2Vtbl
author: windows-driver-content
description: 
ms.assetid: b54b7c3b-2a39-4537-8ce9-120084991e9c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPnpCallbackHardware2Vtbl, IPnpCallbackHardware2Vtbl
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

# IPnpCallbackHardware2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPnpCallbackHardware2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPnpCallbackHardware2 *This) AddRef			
 	
### -field ULONG(* )(IPnpCallbackHardware2 *This) Release			
 	
### -field HRESULT(* )(IPnpCallbackHardware2 *This,IWDFDevice3 *pWdfDevice,IWDFCmResourceList *pWdfResourcesRaw,IWDFCmResourceList *pWdfResourcesTranslated) OnPrepareHardware			
 	
### -field HRESULT(* )(IPnpCallbackHardware2 *This,IWDFDevice3 *pWdfDevice,IWDFCmResourceList *pWdfResourcesTranslated) OnReleaseHardware			
 	
## -remarks

## -see-also