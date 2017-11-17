---
UID: NS.wudfddi.IPowerPolicyCallbackWakeFromS0Vtbl
title: IPowerPolicyCallbackWakeFromS0Vtbl
author: windows-driver-content
description: 
ms.assetid: f0acfd75-2221-4f79-be76-5349d52fbcd6
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPowerPolicyCallbackWakeFromS0Vtbl, IPowerPolicyCallbackWakeFromS0Vtbl
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

# IPowerPolicyCallbackWakeFromS0Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPowerPolicyCallbackWakeFromS0 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPowerPolicyCallbackWakeFromS0 *This) AddRef			
 	
### -field ULONG(* )(IPowerPolicyCallbackWakeFromS0 *This) Release			
 	
### -field HRESULT(* )(IPowerPolicyCallbackWakeFromS0 *This,IWDFDevice *pWdfDevice) OnArmWakeFromS0			
 	
### -field void(* )(IPowerPolicyCallbackWakeFromS0 *This,IWDFDevice *pWdfDevice) OnDisarmWakeFromS0			
 	
### -field void(* )(IPowerPolicyCallbackWakeFromS0 *This,IWDFDevice *pWdfDevice) OnWakeFromS0Triggered			
 	
## -remarks

## -see-also