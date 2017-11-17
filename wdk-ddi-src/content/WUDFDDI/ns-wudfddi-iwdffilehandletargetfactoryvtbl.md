---
UID: NS.wudfddi.IWDFFileHandleTargetFactoryVtbl
title: IWDFFileHandleTargetFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: 7bf07e33-9390-4b9e-aa66-a524dedd733b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFFileHandleTargetFactoryVtbl, IWDFFileHandleTargetFactoryVtbl
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

# IWDFFileHandleTargetFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFFileHandleTargetFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFFileHandleTargetFactory *This) AddRef			
 	
### -field ULONG(* )(IWDFFileHandleTargetFactory *This) Release			
 	
### -field HRESULT(* )(IWDFFileHandleTargetFactory *This,HANDLE hTarget,IWDFIoTarget **ppTarget) CreateFileHandleTarget			
 	
## -remarks

## -see-also