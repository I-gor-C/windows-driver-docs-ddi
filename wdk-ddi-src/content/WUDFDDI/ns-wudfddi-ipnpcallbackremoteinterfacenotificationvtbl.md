---
UID: NS.wudfddi.IPnpCallbackRemoteInterfaceNotificationVtbl
title: IPnpCallbackRemoteInterfaceNotificationVtbl
author: windows-driver-content
description: 
ms.assetid: 5c563f1b-dca1-4ebd-a03a-41dd690f025f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPnpCallbackRemoteInterfaceNotificationVtbl, IPnpCallbackRemoteInterfaceNotificationVtbl
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

# IPnpCallbackRemoteInterfaceNotificationVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPnpCallbackRemoteInterfaceNotification *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPnpCallbackRemoteInterfaceNotification *This) AddRef			
 	
### -field ULONG(* )(IPnpCallbackRemoteInterfaceNotification *This) Release			
 	
### -field void(* )(IPnpCallbackRemoteInterfaceNotification *This,IWDFRemoteInterfaceInitialize *pWdfRemoteInterfaceInit) OnRemoteInterfaceArrival			
 	
## -remarks

## -see-also