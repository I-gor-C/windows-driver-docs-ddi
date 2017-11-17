---
UID: NS.printerextension.IPrintSchemaCapabilitiesVtbl
title: IPrintSchemaCapabilitiesVtbl
author: windows-driver-content
description: 
ms.assetid: 33381ffd-6887-46f6-a6b8-d6331368c106
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaCapabilitiesVtbl, IPrintSchemaCapabilitiesVtbl
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

# IPrintSchemaCapabilitiesVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaCapabilities *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaCapabilities *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaCapabilities *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,BSTR bstrKeyName,IPrintSchemaFeature **ppFeature) GetFeatureByKeyName			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,BSTR bstrName,BSTR bstrNamespaceUri,IPrintSchemaFeature **ppFeature) GetFeature			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,IPrintSchemaPageImageableSize **ppPageImageableSize) get_PageImageableSize			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,ULONG *pulJobCopiesAllDocumentsMinValue) get_JobCopiesAllDocumentsMinValue			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,ULONG *pulJobCopiesAllDocumentsMaxValue) get_JobCopiesAllDocumentsMaxValue			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,IPrintSchemaFeature *pFeature,IPrintSchemaOption **ppOption) GetSelectedOptionInPrintTicket			
 	
### -field HRESULT(* )(IPrintSchemaCapabilities *This,IPrintSchemaFeature *pFeature,IPrintSchemaOptionCollection **ppOptionCollection) GetOptions			
 	
## -remarks

## -see-also