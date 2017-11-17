---
UID: NS.printerextension.IPrintSchemaCapabilities2Vtbl
title: IPrintSchemaCapabilities2Vtbl
author: windows-driver-content
description: 
ms.assetid: f7643f90-aed4-40aa-81ac-6e398e7f4743
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaCapabilities2Vtbl, IPrintSchemaCapabilities2Vtbl
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

# IPrintSchemaCapabilities2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaCapabilities2 *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaCapabilities2 *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,BSTR bstrKeyName,IPrintSchemaFeature **ppFeature) GetFeatureByKeyName			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,BSTR bstrName,BSTR bstrNamespaceUri,IPrintSchemaFeature **ppFeature) GetFeature			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,IPrintSchemaPageImageableSize **ppPageImageableSize) get_PageImageableSize			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,ULONG *pulJobCopiesAllDocumentsMinValue) get_JobCopiesAllDocumentsMinValue			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,ULONG *pulJobCopiesAllDocumentsMaxValue) get_JobCopiesAllDocumentsMaxValue			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,IPrintSchemaFeature *pFeature,IPrintSchemaOption **ppOption) GetSelectedOptionInPrintTicket			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,IPrintSchemaFeature *pFeature,IPrintSchemaOptionCollection **ppOptionCollection) GetOptions			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities2 *This,BSTR bstrName,BSTR bstrNamespaceUri,IPrintSchemaParameterDefinition **ppParameterDefinition) GetParameterDefinition			
 	
## -remarks

## -see-also