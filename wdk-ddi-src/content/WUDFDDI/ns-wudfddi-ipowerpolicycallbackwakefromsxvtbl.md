---
UID: NS.wudfddi.IPowerPolicyCallbackWakeFromSxVtbl
title: IPowerPolicyCallbackWakeFromSxVtbl
author: windows-driver-content
description: 
ms.assetid: 4a597681-b2d0-481e-a401-dc15bbdbda8f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPowerPolicyCallbackWakeFromSxVtbl, IPowerPolicyCallbackWakeFromSxVtbl
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

# IPowerPolicyCallbackWakeFromSxVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPowerPolicyCallbackWakeFromSx *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPowerPolicyCallbackWakeFromSx *This) AddRef			
 	
### -field ULONG(* )(IPowerPolicyCallbackWakeFromSx *This) Release			
 	
### -field HRESULT(* )(IPowerPolicyCallbackWakeFromSx *This,IWDFDevice *pWdfDevice) OnArmWakeFromSx			
 	
### -field void(* )(IPowerPolicyCallbackWakeFromSx *This,IWDFDevice *pWdfDevice) OnDisarmWakeFromSx			
 	
### -field void(* )(IPowerPolicyCallbackWakeFromSx *This,IWDFDevice *pWdfDevice) OnWakeFromSxTriggered			
 	
## -remarks

## -see-also