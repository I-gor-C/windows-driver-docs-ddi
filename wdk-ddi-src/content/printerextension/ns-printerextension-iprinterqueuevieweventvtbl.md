---
UID: NS.printerextension.IPrinterQueueViewEventVtbl
title: IPrinterQueueViewEventVtbl
author: windows-driver-content
description: 
ms.assetid: 31bba1dc-0b92-4029-8789-8b8f78643d0b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterQueueViewEventVtbl, IPrinterQueueViewEventVtbl
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

# IPrinterQueueViewEventVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterQueueViewEvent *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterQueueViewEvent *This) AddRef			
 	
### -field ULONG(* )(IPrinterQueueViewEvent *This) Release			
 	
### -field HRESULT(* )(IPrinterQueueViewEvent *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterQueueViewEvent *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterQueueViewEvent *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterQueueViewEvent *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterQueueViewEvent *This,IPrintJobCollection *pCollection,ULONG ulViewOffset,ULONG ulViewSize,ULONG ulCountJobsInPrintQueue) OnChanged			
 	
## -remarks

## -see-also