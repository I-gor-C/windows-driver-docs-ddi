---
UID: NS.printerextension.IPrintSchemaAsyncOperationEventVtbl
title: IPrintSchemaAsyncOperationEventVtbl
author: windows-driver-content
description: 
ms.assetid: 5969144b-a80c-4e94-a39c-1ce29af2963c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaAsyncOperationEventVtbl, IPrintSchemaAsyncOperationEventVtbl
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

# IPrintSchemaAsyncOperationEventVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaAsyncOperationEvent *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaAsyncOperationEvent *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaAsyncOperationEvent *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperationEvent *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperationEvent *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperationEvent *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperationEvent *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperationEvent *This,IPrintSchemaTicket *pTicket,HRESULT hrOperation) Completed			
 	
## -remarks

## -see-also