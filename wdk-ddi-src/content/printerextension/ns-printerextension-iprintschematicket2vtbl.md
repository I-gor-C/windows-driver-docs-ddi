---
UID: NS.printerextension.IPrintSchemaTicket2Vtbl
title: IPrintSchemaTicket2Vtbl
author: windows-driver-content
description: 
ms.assetid: 3c01e2cf-ec97-44a0-b2d7-4cd7d2874873
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaTicket2Vtbl, IPrintSchemaTicket2Vtbl
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

# IPrintSchemaTicket2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaTicket2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaTicket2 *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaTicket2 *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,BSTR bstrKeyName,IPrintSchemaFeature **ppFeature) GetFeatureByKeyName			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,BSTR bstrName,BSTR bstrNamespaceUri,IPrintSchemaFeature **ppFeature) GetFeature			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,IPrintSchemaAsyncOperation **ppAsyncOperation) ValidateAsync			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,IPrintSchemaTicket *pPrintTicketCommit,IPrintSchemaAsyncOperation **ppAsyncOperation) CommitAsync			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This) NotifyXmlChanged			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,IPrintSchemaCapabilities **ppCapabilities) GetCapabilities			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,ULONG *pulJobCopiesAllDocuments) get_JobCopiesAllDocuments			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,ULONG ulJobCopiesAllDocuments) put_JobCopiesAllDocuments			
 	
### -field HRESULT(* )(IPrintSchemaTicket2 *This,BSTR bstrName,BSTR bstrNamespaceUri,IPrintSchemaParameterInitializer **ppParameterInitializer) GetParameterInitializer			
 	
## -remarks

## -see-also