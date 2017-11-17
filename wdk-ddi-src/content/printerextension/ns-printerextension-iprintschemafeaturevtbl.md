---
UID: NS.printerextension.IPrintSchemaFeatureVtbl
title: IPrintSchemaFeatureVtbl
author: windows-driver-content
description: 
ms.assetid: 2dfe9baa-fe1b-4ff0-a614-437d12da4209
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaFeatureVtbl, IPrintSchemaFeatureVtbl
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

# IPrintSchemaFeatureVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaFeature *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaFeature *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaFeature *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,BSTR *pbstrDisplayName) get_DisplayName			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,IPrintSchemaOption **ppOption) get_SelectedOption			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,IPrintSchemaOption *pOption) put_SelectedOption			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,PrintSchemaSelectionType *pSelectionType) get_SelectionType			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,BSTR bstrName,BSTR bstrNamespaceUri,IPrintSchemaOption **ppOption) GetOption			
 	
### -field HRESULT(* )(IPrintSchemaFeature *This,BOOL *pbShow) get_DisplayUI			
 	
## -remarks

## -see-also