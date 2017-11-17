---
UID: NS.printerextension.IPrinterScriptableSequentialStreamVtbl
title: IPrinterScriptableSequentialStreamVtbl
author: windows-driver-content
description: 
ms.assetid: 2b615c15-0fa3-406c-9c25-7418465a79a0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterScriptableSequentialStreamVtbl, IPrinterScriptableSequentialStreamVtbl
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

# IPrinterScriptableSequentialStreamVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterScriptableSequentialStream *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterScriptableSequentialStream *This) AddRef			
 	
### -field ULONG(* )(IPrinterScriptableSequentialStream *This) Release			
 	
### -field HRESULT(* )(IPrinterScriptableSequentialStream *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterScriptableSequentialStream *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterScriptableSequentialStream *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterScriptableSequentialStream *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterScriptableSequentialStream *This,LONG cbRead,IDispatch **ppArray) Read			
 	
### -field HRESULT(* )(IPrinterScriptableSequentialStream *This,IDispatch *pArray,LONG *pcbWritten) Write			
 	
## -remarks

## -see-also