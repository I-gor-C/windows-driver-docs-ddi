---
UID: NS.wudfddi.IRemoteTargetCallbackRemovalVtbl
title: IRemoteTargetCallbackRemovalVtbl
author: windows-driver-content
description: 
ms.assetid: 1d68ee2e-b7c2-46fa-ab4c-766333baaa71
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IRemoteTargetCallbackRemovalVtbl, IRemoteTargetCallbackRemovalVtbl
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

# IRemoteTargetCallbackRemovalVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IRemoteTargetCallbackRemoval *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IRemoteTargetCallbackRemoval *This) AddRef			
 	
### -field ULONG(* )(IRemoteTargetCallbackRemoval *This) Release			
 	
### -field BOOL(* )(IRemoteTargetCallbackRemoval *This,IWDFRemoteTarget *pWdfRemoteTarget) OnRemoteTargetQueryRemove			
 	
### -field void(* )(IRemoteTargetCallbackRemoval *This,IWDFRemoteTarget *pWdfRemoteTarget) OnRemoteTargetRemoveCanceled			
 	
### -field void(* )(IRemoteTargetCallbackRemoval *This,IWDFRemoteTarget *pWdfRemoteTarget) OnRemoteTargetRemoveComplete			
 	
## -remarks

## -see-also