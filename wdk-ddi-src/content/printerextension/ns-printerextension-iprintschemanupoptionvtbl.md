---
UID: NS.printerextension.IPrintSchemaNUpOptionVtbl
title: IPrintSchemaNUpOptionVtbl
author: windows-driver-content
description: 
ms.assetid: 08ef59fc-d710-4214-a72e-99f6eac25e6b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaNUpOptionVtbl, IPrintSchemaNUpOptionVtbl
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

# IPrintSchemaNUpOptionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaNUpOption *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaNUpOption *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaNUpOption *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,BSTR *pbstrDisplayName) get_DisplayName			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,BOOL *pbIsSelected) get_Selected			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,PrintSchemaConstrainedSetting *pSetting) get_Constrained			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,BSTR bstrName,BSTR bstrNamespaceUri,IUnknown **ppXmlValueNode) GetPropertyValue			
 	
### -field HRESULT(* )(IPrintSchemaNUpOption *This,ULONG *pulPagesPerSheet) get_PagesPerSheet			
 	
## -remarks

## -see-also