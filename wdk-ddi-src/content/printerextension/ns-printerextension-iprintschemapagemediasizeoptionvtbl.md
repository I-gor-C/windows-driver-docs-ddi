---
UID: NS.printerextension.IPrintSchemaPageMediaSizeOptionVtbl
title: IPrintSchemaPageMediaSizeOptionVtbl
author: windows-driver-content
description: 
ms.assetid: 03fb546e-5ec4-4679-9e24-e48bc44619c8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaPageMediaSizeOptionVtbl, IPrintSchemaPageMediaSizeOptionVtbl
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

# IPrintSchemaPageMediaSizeOptionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaPageMediaSizeOption *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaPageMediaSizeOption *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,BSTR *pbstrDisplayName) get_DisplayName			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,BOOL *pbIsSelected) get_Selected			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,PrintSchemaConstrainedSetting *pSetting) get_Constrained			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,BSTR bstrName,BSTR bstrNamespaceUri,IUnknown **ppXmlValueNode) GetPropertyValue			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,ULONG *pulWidth) get_WidthInMicrons			
 	
### -field HRESULT(* )(IPrintSchemaPageMediaSizeOption *This,ULONG *pulHeight) get_HeightInMicrons			
 	
## -remarks

## -see-also