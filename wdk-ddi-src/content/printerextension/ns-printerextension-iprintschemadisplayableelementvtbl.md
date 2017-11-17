---
UID: NS.printerextension.IPrintSchemaDisplayableElementVtbl
title: IPrintSchemaDisplayableElementVtbl
author: windows-driver-content
description: 
ms.assetid: 501cec82-d6e0-47d8-aab9-f2812d2a1ab8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaDisplayableElementVtbl, IPrintSchemaDisplayableElementVtbl
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

# IPrintSchemaDisplayableElementVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaDisplayableElement *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaDisplayableElement *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaDisplayableElement *This,BSTR *pbstrDisplayName) get_DisplayName			
 	
## -remarks

## -see-also