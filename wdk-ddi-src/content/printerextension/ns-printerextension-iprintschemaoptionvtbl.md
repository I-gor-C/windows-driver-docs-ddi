---
UID: NS.printerextension.IPrintSchemaOptionVtbl
title: IPrintSchemaOptionVtbl
author: windows-driver-content
description: 
ms.assetid: 7cdd7922-89ef-4b3b-91c6-9ccb5ed83a2a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaOptionVtbl, IPrintSchemaOptionVtbl
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

# IPrintSchemaOptionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaOption *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaOption *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaOption *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,BSTR *pbstrDisplayName) get_DisplayName			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,BOOL *pbIsSelected) get_Selected			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,PrintSchemaConstrainedSetting *pSetting) get_Constrained			
 	
### -field HRESULT(* )(IPrintSchemaOption *This,BSTR bstrName,BSTR bstrNamespaceUri,IUnknown **ppXmlValueNode) GetPropertyValue			
 	
## -remarks

## -see-also