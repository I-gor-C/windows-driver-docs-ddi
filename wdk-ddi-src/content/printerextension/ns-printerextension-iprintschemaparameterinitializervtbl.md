---
UID: NS.printerextension.IPrintSchemaParameterInitializerVtbl
title: IPrintSchemaParameterInitializerVtbl
author: windows-driver-content
description: 
ms.assetid: 04a03d21-7321-4ed5-89d5-d9aa4c72ce71
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaParameterInitializerVtbl, IPrintSchemaParameterInitializerVtbl
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

# IPrintSchemaParameterInitializerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaParameterInitializer *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaParameterInitializer *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,VARIANT *pVar) get_Value			
 	
### -field HRESULT(* )(IPrintSchemaParameterInitializer *This,VARIANT *pVar) put_Value			
 	
## -remarks

## -see-also