---
UID: NS.printerextension.IPrinterScriptablePropertyBag2Vtbl
title: IPrinterScriptablePropertyBag2Vtbl
author: windows-driver-content
description: 
ms.assetid: dea25818-f1c6-496f-ad6d-413daddc1e89
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterScriptablePropertyBag2Vtbl, IPrinterScriptablePropertyBag2Vtbl
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

# IPrinterScriptablePropertyBag2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterScriptablePropertyBag2 *This) AddRef			
 	
### -field ULONG(* )(IPrinterScriptablePropertyBag2 *This) Release			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,BOOL *pbValue) GetBool			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,BOOL bValue) SetBool			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,LONG *pnValue) GetInt32			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,LONG nValue) SetInt32			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,BSTR *pbstrValue) GetString			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,BSTR bstrValue) SetString			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,IDispatch **ppArray) GetBytes			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,IDispatch *pArray) SetBytes			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,IPrinterScriptableStream **ppStream) GetReadStream			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,IPrinterScriptableStream **ppStream) GetWriteStream			
 	
### -field HRESULT(* )(IPrinterScriptablePropertyBag2 *This,BSTR bstrName,IUnknown **ppXmlNode) GetReadStreamAsXML			
 	
## -remarks

## -see-also