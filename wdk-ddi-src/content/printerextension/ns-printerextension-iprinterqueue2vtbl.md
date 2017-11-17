---
UID: NS.printerextension.IPrinterQueue2Vtbl
title: IPrinterQueue2Vtbl
author: windows-driver-content
description: 
ms.assetid: 11fbbf01-145b-46d5-b05c-94132b286d37
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterQueue2Vtbl, IPrinterQueue2Vtbl
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

# IPrinterQueue2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterQueue2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterQueue2 *This) AddRef			
 	
### -field ULONG(* )(IPrinterQueue2 *This) Release			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,HANDLE *phPrinter) get_Handle			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,BSTR bstrBidiQuery) SendBidiQuery			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,IPrinterPropertyBag **ppPropertyBag) GetProperties			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,BSTR bstrBidiRequest,IPrinterBidiSetRequestCallback *pCallback,IPrinterExtensionAsyncOperation **ppAsyncOperation) SendBidiSetRequestAsync			
 	
### -field HRESULT(* )(IPrinterQueue2 *This,ULONG ulViewOffset,ULONG ulViewSize,IPrinterQueueView **ppJobView) GetPrinterQueueView			
 	
## -remarks

## -see-also