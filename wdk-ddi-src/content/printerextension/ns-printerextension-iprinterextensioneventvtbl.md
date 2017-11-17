---
UID: NS.printerextension.IPrinterExtensionEventVtbl
title: IPrinterExtensionEventVtbl
author: windows-driver-content
description: 
ms.assetid: 8e447afe-7b02-47c2-9c02-2db5ad898ed9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterExtensionEventVtbl, IPrinterExtensionEventVtbl
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

# IPrinterExtensionEventVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterExtensionEvent *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterExtensionEvent *This) AddRef			
 	
### -field ULONG(* )(IPrinterExtensionEvent *This) Release			
 	
### -field HRESULT(* )(IPrinterExtensionEvent *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterExtensionEvent *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterExtensionEvent *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterExtensionEvent *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterExtensionEvent *This,IPrinterExtensionEventArgs *pEventArgs) OnDriverEvent			
 	
### -field HRESULT(* )(IPrinterExtensionEvent *This,IPrinterExtensionContextCollection *pContextCollection) OnPrinterQueuesEnumerated			
 	
## -remarks

## -see-also