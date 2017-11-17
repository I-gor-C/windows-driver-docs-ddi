---
UID: NS.printerextension.IPrinterScriptContextVtbl
title: IPrinterScriptContextVtbl
author: windows-driver-content
description: 
ms.assetid: 7ce8801f-5d95-41d9-a2c7-d76f78085582
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterScriptContextVtbl, IPrinterScriptContextVtbl
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

# IPrinterScriptContextVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterScriptContext *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterScriptContext *This) AddRef			
 	
### -field ULONG(* )(IPrinterScriptContext *This) Release			
 	
### -field HRESULT(* )(IPrinterScriptContext *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterScriptContext *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterScriptContext *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterScriptContext *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterScriptContext *This,IPrinterScriptablePropertyBag **ppPropertyBag) get_DriverProperties			
 	
### -field HRESULT(* )(IPrinterScriptContext *This,IPrinterScriptablePropertyBag **ppPropertyBag) get_QueueProperties			
 	
### -field HRESULT(* )(IPrinterScriptContext *This,IPrinterScriptablePropertyBag **ppPropertyBag) get_UserProperties			
 	
## -remarks

## -see-also