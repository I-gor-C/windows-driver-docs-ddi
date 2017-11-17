---
UID: NS.printerextension.IPrinterExtensionContextVtbl
title: IPrinterExtensionContextVtbl
author: windows-driver-content
description: 
ms.assetid: f74fae7f-6924-4168-8f6e-45c2953508b8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterExtensionContextVtbl, IPrinterExtensionContextVtbl
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

# IPrinterExtensionContextVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterExtensionContext *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterExtensionContext *This) AddRef			
 	
### -field ULONG(* )(IPrinterExtensionContext *This) Release			
 	
### -field HRESULT(* )(IPrinterExtensionContext *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterExtensionContext *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterExtensionContext *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterExtensionContext *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterExtensionContext *This,IPrinterQueue **ppQueue) get_PrinterQueue			
 	
### -field HRESULT(* )(IPrinterExtensionContext *This,IPrintSchemaTicket **ppTicket) get_PrintSchemaTicket			
 	
### -field HRESULT(* )(IPrinterExtensionContext *This,IPrinterPropertyBag **ppPropertyBag) get_DriverProperties			
 	
### -field HRESULT(* )(IPrinterExtensionContext *This,IPrinterPropertyBag **ppPropertyBag) get_UserProperties			
 	
## -remarks

## -see-also