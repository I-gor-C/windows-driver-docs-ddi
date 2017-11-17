---
UID: NS.printerextension.IPrinterScriptablePropertyBagVtbl
title: IPrinterScriptablePropertyBagVtbl
author: windows-driver-content
description: 
ms.assetid: d4988799-7003-48ef-8f7b-5bc88d88bdfd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterScriptablePropertyBagVtbl, IPrinterScriptablePropertyBagVtbl
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

# IPrinterScriptablePropertyBagVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterScriptablePropertyBag *This) AddRef			
 	
### -field ULONG(* )(IPrinterScriptablePropertyBag *This) Release			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,BOOL *pbValue) GetBool			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,BOOL bValue) SetBool			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,LONG *pnValue) GetInt32			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,LONG nValue) SetInt32			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,BSTR *pbstrValue) GetString			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,BSTR bstrValue) SetString			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,IDispatch **ppArray) GetBytes			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,IDispatch *pArray) SetBytes			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,IPrinterScriptableStream **ppStream) GetReadStream			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag *This,BSTR bstrName,IPrinterScriptableStream **ppStream) GetWriteStream			
 	
## -remarks

## -see-also