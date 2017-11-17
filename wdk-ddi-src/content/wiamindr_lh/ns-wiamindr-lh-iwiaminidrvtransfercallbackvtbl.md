---
UID: NS.wiamindr_lh.IWiaMiniDrvTransferCallbackVtbl
title: IWiaMiniDrvTransferCallbackVtbl
author: windows-driver-content
description: 
ms.assetid: 4e82de06-8841-493f-b17f-ae7f75d0f61a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWiaMiniDrvTransferCallbackVtbl, IWiaMiniDrvTransferCallbackVtbl
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

# IWiaMiniDrvTransferCallbackVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWiaMiniDrvTransferCallback *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWiaMiniDrvTransferCallback *This) AddRef			
 	
### -field ULONG(* )(IWiaMiniDrvTransferCallback *This) Release			
 	
### -field HRESULT(* )(IWiaMiniDrvTransferCallback *This,LONG lFlags,BSTR bstrItemName,BSTR bstrFullItemName,IStream **ppIStream) GetNextStream			
 	
### -field HRESULT(* )(IWiaMiniDrvTransferCallback *This,LONG lFlags,WiaTransferParams *pWiaTransferParams) SendMessage			
 	
## -remarks

## -see-also