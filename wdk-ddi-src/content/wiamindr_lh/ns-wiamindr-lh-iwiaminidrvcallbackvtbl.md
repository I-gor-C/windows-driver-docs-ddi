---
UID: NS.wiamindr_lh.IWiaMiniDrvCallBackVtbl
title: IWiaMiniDrvCallBackVtbl
author: windows-driver-content
description: 
ms.assetid: 0b94ba42-fb72-424f-b878-2dd4f7d59474
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWiaMiniDrvCallBackVtbl, IWiaMiniDrvCallBackVtbl
req.header: wiamindr_lh.h
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

# IWiaMiniDrvCallBackVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWiaMiniDrvCallBack *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWiaMiniDrvCallBack *This) AddRef			
 	
### -field ULONG(* )(IWiaMiniDrvCallBack *This) Release			
 	
### -field HRESULT(* )(IWiaMiniDrvCallBack *This,LONG lReason,LONG lStatus,LONG lPercentComplete,LONG lOffset,LONG lLength,PMINIDRV_TRANSFER_CONTEXT pTranCtx,LONG lReserved) MiniDrvCallback			
 	
## -remarks

## -see-also