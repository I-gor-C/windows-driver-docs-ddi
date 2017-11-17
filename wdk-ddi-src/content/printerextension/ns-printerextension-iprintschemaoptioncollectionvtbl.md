---
UID: NS.printerextension.IPrintSchemaOptionCollectionVtbl
title: IPrintSchemaOptionCollectionVtbl
author: windows-driver-content
description: 
ms.assetid: 3198d352-eeb9-4853-85a3-7bd3e12a6d85
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaOptionCollectionVtbl, IPrintSchemaOptionCollectionVtbl
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

# IPrintSchemaOptionCollectionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaOptionCollection *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaOptionCollection *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaOptionCollection *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaOptionCollection *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaOptionCollection *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaOptionCollection *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaOptionCollection *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaOptionCollection *This,ULONG *pulCount) get_Count			
 	
### -field HRESULT(* )(IPrintSchemaOptionCollection *This,ULONG ulIndex,IPrintSchemaOption **ppOption) GetAt			
 	
### -field HRESULT(* )(IPrintSchemaOptionCollection *This,IUnknown **ppUnk) get__NewEnum			
 	
## -remarks

## -see-also