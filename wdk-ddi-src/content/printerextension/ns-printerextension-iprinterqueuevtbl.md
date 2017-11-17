---
UID: NS.printerextension.IPrinterQueueVtbl
title: IPrinterQueueVtbl
author: windows-driver-content
description: 
ms.assetid: 3b2bb200-c523-445c-ac4a-7e261d475680
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterQueueVtbl, IPrinterQueueVtbl
req.header: printerextension.h
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

# IPrinterQueueVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterQueue *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterQueue *This) AddRef			
 	
### -field ULONG(* )(IPrinterQueue *This) Release			
 	
### -field HRESULT(* )(IPrinterQueue *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterQueue *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterQueue *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterQueue *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterQueue *This,HANDLE *phPrinter) get_Handle			
 	
### -field HRESULT(* )(IPrinterQueue *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrinterQueue *This,BSTR bstrBidiQuery) SendBidiQuery			
 	
### -field HRESULT(* )(IPrinterQueue *This,IPrinterPropertyBag **ppPropertyBag) GetProperties			
 	
## -remarks

## -see-also