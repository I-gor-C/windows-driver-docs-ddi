---
UID: NS.printerextension.IPrintSchemaElementVtbl
title: IPrintSchemaElementVtbl
author: windows-driver-content
description: 
ms.assetid: fe3b42c1-8914-4528-a911-f8944e99cc2e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaElementVtbl, IPrintSchemaElementVtbl
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

# IPrintSchemaElementVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaElement *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaElement *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaElement *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaElement *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaElement *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaElement *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaElement *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaElement *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaElement *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaElement *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
## -remarks

## -see-also