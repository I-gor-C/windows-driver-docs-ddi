---
UID: NS.printerextension.IPrinterQueueEventVtbl
title: IPrinterQueueEventVtbl
author: windows-driver-content
description: 
ms.assetid: 72053a5b-6ed8-46e5-affa-f6ef8de769dd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterQueueEventVtbl, IPrinterQueueEventVtbl
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

# IPrinterQueueEventVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterQueueEvent *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterQueueEvent *This) AddRef			
 	
### -field ULONG(* )(IPrinterQueueEvent *This) Release			
 	
### -field HRESULT(* )(IPrinterQueueEvent *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterQueueEvent *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterQueueEvent *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterQueueEvent *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterQueueEvent *This,BSTR bstrResponse,HRESULT hrStatus) OnBidiResponseReceived			
 	
## -remarks

## -see-also