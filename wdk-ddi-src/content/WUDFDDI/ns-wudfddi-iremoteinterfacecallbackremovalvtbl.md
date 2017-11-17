---
UID: NS.wudfddi.IRemoteInterfaceCallbackRemovalVtbl
title: IRemoteInterfaceCallbackRemovalVtbl
author: windows-driver-content
description: 
ms.assetid: e266f529-9203-44e9-980c-44d27bff1be3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IRemoteInterfaceCallbackRemovalVtbl, IRemoteInterfaceCallbackRemovalVtbl
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

# IRemoteInterfaceCallbackRemovalVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IRemoteInterfaceCallbackRemoval *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IRemoteInterfaceCallbackRemoval *This) AddRef			
 	
### -field ULONG(* )(IRemoteInterfaceCallbackRemoval *This) Release			
 	
### -field void(* )(IRemoteInterfaceCallbackRemoval *This,IWDFRemoteInterface *pWdfRemoteInterface) OnRemoteInterfaceRemoval			
 	
## -remarks

## -see-also