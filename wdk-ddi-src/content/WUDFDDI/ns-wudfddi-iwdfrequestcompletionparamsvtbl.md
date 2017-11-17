---
UID: NS.wudfddi.IWDFRequestCompletionParamsVtbl
title: IWDFRequestCompletionParamsVtbl
author: windows-driver-content
description: 
ms.assetid: 1f4f8199-3cbc-4640-b6b4-554ca43152bf
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFRequestCompletionParamsVtbl, IWDFRequestCompletionParamsVtbl
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

# IWDFRequestCompletionParamsVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFRequestCompletionParams *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFRequestCompletionParams *This) AddRef			
 	
### -field ULONG(* )(IWDFRequestCompletionParams *This) Release			
 	
### -field HRESULT(* )(IWDFRequestCompletionParams *This) GetCompletionStatus			
 	
### -field ULONG_PTR(* )(IWDFRequestCompletionParams *This) GetInformation			
 	
### -field WDF_REQUEST_TYPE(* )(IWDFRequestCompletionParams *This) GetCompletedRequestType			
 	
## -remarks

## -see-also