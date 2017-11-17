---
UID: NS.wudfusb.IWDFUsbTargetFactoryVtbl
title: IWDFUsbTargetFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: da28dca9-7378-45a7-a684-f9aaa8661f78
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFUsbTargetFactoryVtbl, IWDFUsbTargetFactoryVtbl
req.header: wudfusb.h
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

# IWDFUsbTargetFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFUsbTargetFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFUsbTargetFactory *This) AddRef			
 	
### -field ULONG(* )(IWDFUsbTargetFactory *This) Release			
 	
### -field HRESULT(* )(IWDFUsbTargetFactory *This,IWDFUsbTargetDevice **ppDevice) CreateUsbTargetDevice			
 	
## -remarks

## -see-also