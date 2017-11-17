---
UID: NS.printerextension.IPrintJobCollectionVtbl
title: IPrintJobCollectionVtbl
author: windows-driver-content
description: 
ms.assetid: 02d38deb-2460-4d24-b9be-d268a9dd2229
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintJobCollectionVtbl, IPrintJobCollectionVtbl
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

# IPrintJobCollectionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintJobCollection *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintJobCollection *This) AddRef			
 	
### -field ULONG(* )(IPrintJobCollection *This) Release			
 	
### -field HRESULT(* )(IPrintJobCollection *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintJobCollection *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintJobCollection *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintJobCollection *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintJobCollection *This,ULONG *pulCount) get_Count			
 	
### -field HRESULT(* )(IPrintJobCollection *This,ULONG ulIndex,IPrintJob **ppJob) GetAt			
 	
### -field HRESULT(* )(IPrintJobCollection *This,IUnknown **ppUnk) get__NewEnum			
 	
## -remarks

## -see-also