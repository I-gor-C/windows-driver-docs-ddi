---
UID: NS.printerextension.IPrintSchemaParameterDefinitionVtbl
title: IPrintSchemaParameterDefinitionVtbl
author: windows-driver-content
description: 
ms.assetid: 7a56ddf4-8335-4a68-b375-1f70be70205c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaParameterDefinitionVtbl, IPrintSchemaParameterDefinitionVtbl
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

# IPrintSchemaParameterDefinitionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaParameterDefinition *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaParameterDefinition *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,BSTR *pbstrDisplayName) get_DisplayName			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,BOOL *pbIsRequired) get_UserInputRequired			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,BSTR *pbstrUnitType) get_UnitType			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,PrintSchemaParameterDataType *pDataType) get_DataType			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,INT *pRangeMin) get_RangeMin			
 	
### -field HRESULT(* )(IPrintSchemaParameterDefinition *This,INT *pRangeMax) get_RangeMax			
 	
## -remarks

## -see-also