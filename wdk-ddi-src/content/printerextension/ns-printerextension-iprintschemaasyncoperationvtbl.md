---
UID: NS.printerextension.IPrintSchemaAsyncOperationVtbl
title: IPrintSchemaAsyncOperationVtbl
author: windows-driver-content
description: 
ms.assetid: b6f00bd2-cd94-4962-9332-7160ab908141
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaAsyncOperationVtbl, IPrintSchemaAsyncOperationVtbl
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

# IPrintSchemaAsyncOperationVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaAsyncOperation *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaAsyncOperation *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaAsyncOperation *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperation *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperation *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperation *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperation *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperation *This) Start			
 	
### -field HRESULT(* )(IPrintSchemaAsyncOperation *This) Cancel			
 	
## -remarks

## -see-also