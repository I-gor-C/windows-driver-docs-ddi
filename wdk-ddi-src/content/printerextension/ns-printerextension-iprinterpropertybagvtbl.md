---
UID: NS.printerextension.IPrinterPropertyBagVtbl
title: IPrinterPropertyBagVtbl
author: windows-driver-content
description: 
ms.assetid: fc7f89a8-7174-4114-aca3-a46bc6d188ba
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterPropertyBagVtbl, IPrinterPropertyBagVtbl
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

# IPrinterPropertyBagVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterPropertyBag *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterPropertyBag *This) AddRef			
 	
### -field ULONG(* )(IPrinterPropertyBag *This) Release			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,BOOL *pbValue) GetBool			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,BOOL bValue) SetBool			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,LONG *pnValue) GetInt32			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,LONG nValue) SetInt32			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,BSTR *pbstrValue) GetString			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,BSTR bstrValue) SetString			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,DWORD *pcbValue,BYTE **ppValue) GetBytes			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,DWORD cbValue,BYTE *pValue) SetBytes			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,IStream **ppValue) GetReadStream			
 	
### -field HRESULT(* )(IPrinterPropertyBag *This,BSTR bstrName,IStream **ppValue) GetWriteStream			
 	
## -remarks

## -see-also