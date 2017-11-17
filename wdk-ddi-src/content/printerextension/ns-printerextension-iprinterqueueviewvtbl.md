---
UID: NS.printerextension.IPrinterQueueViewVtbl
title: IPrinterQueueViewVtbl
author: windows-driver-content
description: 
ms.assetid: b9556992-b2d9-4581-912f-44d01314a52f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterQueueViewVtbl, IPrinterQueueViewVtbl
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

# IPrinterQueueViewVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterQueueView *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterQueueView *This) AddRef			
 	
### -field ULONG(* )(IPrinterQueueView *This) Release			
 	
### -field HRESULT(* )(IPrinterQueueView *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterQueueView *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterQueueView *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterQueueView *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterQueueView *This,ULONG ulViewOffset,ULONG ulViewSize) SetViewRange			
 	
## -remarks

## -see-also