---
UID: NS.wudfddi.IPnpCallbackHardwareInterruptVtbl
title: IPnpCallbackHardwareInterruptVtbl
author: windows-driver-content
description: 
ms.assetid: 7594afda-af0e-4e64-8b85-f312c1b902a0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPnpCallbackHardwareInterruptVtbl, IPnpCallbackHardwareInterruptVtbl
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

# IPnpCallbackHardwareInterruptVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPnpCallbackHardwareInterrupt *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPnpCallbackHardwareInterrupt *This) AddRef			
 	
### -field ULONG(* )(IPnpCallbackHardwareInterrupt *This) Release			
 	
### -field HRESULT(* )(IPnpCallbackHardwareInterrupt *This,IWDFDevice3 *pDevice,WDF_POWER_DEVICE_STATE PreviousState) OnD0EntryPostInterruptsEnabled			
 	
### -field HRESULT(* )(IPnpCallbackHardwareInterrupt *This,IWDFDevice3 *pDevice,WDF_POWER_DEVICE_STATE TargetState) OnD0ExitPreInterruptsDisabled			
 	
## -remarks

## -see-also