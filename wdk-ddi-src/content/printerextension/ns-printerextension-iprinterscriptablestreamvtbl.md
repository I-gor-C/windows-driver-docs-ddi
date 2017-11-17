---
UID: NS.printerextension.IPrinterScriptableStreamVtbl
title: IPrinterScriptableStreamVtbl
author: windows-driver-content
description: 
ms.assetid: 960c8c93-14a1-4f30-955e-5b4a22297984
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterScriptableStreamVtbl, IPrinterScriptableStreamVtbl
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

# IPrinterScriptableStreamVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterScriptableStream *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterScriptableStream *This) AddRef			
 	
### -field ULONG(* )(IPrinterScriptableStream *This) Release			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This,LONG cbRead,IDispatch **ppArray) Read			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This,IDispatch *pArray,LONG *pcbWritten) Write			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This) Commit			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This,LONG lOffset,STREAM_SEEK streamSeek,LONG *plPosition) Seek			
 	
### -field HRESULT(* )(IPrinterScriptableStream *This,LONG lSize) SetSize			
 	
## -remarks

## -see-also