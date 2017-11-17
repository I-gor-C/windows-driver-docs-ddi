---
UID: NS.wudfddi.IPnpCallbackVtbl
title: IPnpCallbackVtbl
author: windows-driver-content
description: 
ms.assetid: e8999b58-9afe-41f3-80dc-95f53fc268fd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPnpCallbackVtbl, IPnpCallbackVtbl
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

# IPnpCallbackVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPnpCallback *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPnpCallback *This) AddRef			
 	
### -field ULONG(* )(IPnpCallback *This) Release			
 	
### -field HRESULT(* )(IPnpCallback *This,IWDFDevice *pWdfDevice,WDF_POWER_DEVICE_STATE previousState) OnD0Entry			
 	
### -field HRESULT(* )(IPnpCallback *This,IWDFDevice *pWdfDevice,WDF_POWER_DEVICE_STATE newState) OnD0Exit			
 	
### -field void(* )(IPnpCallback *This,IWDFDevice *pWdfDevice) OnSurpriseRemoval			
 	
### -field HRESULT(* )(IPnpCallback *This,IWDFDevice *pWdfDevice) OnQueryRemove			
 	
### -field HRESULT(* )(IPnpCallback *This,IWDFDevice *pWdfDevice) OnQueryStop			
 	
## -remarks

## -see-also