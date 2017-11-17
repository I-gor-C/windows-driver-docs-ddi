---
UID: NS.printerextension.IPrintSchemaTicketVtbl
title: IPrintSchemaTicketVtbl
author: windows-driver-content
description: 
ms.assetid: d87e96c4-e3cb-4e4c-9a94-1a178589fadd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaTicketVtbl, IPrintSchemaTicketVtbl
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

# IPrintSchemaTicketVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaTicket *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaTicket *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaTicket *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,BSTR bstrKeyName,IPrintSchemaFeature **ppFeature) GetFeatureByKeyName			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,BSTR bstrName,BSTR bstrNamespaceUri,IPrintSchemaFeature **ppFeature) GetFeature			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,IPrintSchemaAsyncOperation **ppAsyncOperation) ValidateAsync			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,IPrintSchemaTicket *pPrintTicketCommit,IPrintSchemaAsyncOperation **ppAsyncOperation) CommitAsync			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This) NotifyXmlChanged			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,IPrintSchemaCapabilities **ppCapabilities) GetCapabilities			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,ULONG *pulJobCopiesAllDocuments) get_JobCopiesAllDocuments			
 	
### -field HRESULT(* )(IPrintSchemaTicket *This,ULONG ulJobCopiesAllDocuments) put_JobCopiesAllDocuments			
 	
## -remarks

## -see-also