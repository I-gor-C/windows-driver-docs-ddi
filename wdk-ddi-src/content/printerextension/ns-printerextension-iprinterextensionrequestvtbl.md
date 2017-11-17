---
UID: NS.printerextension.IPrinterExtensionRequestVtbl
title: IPrinterExtensionRequestVtbl
author: windows-driver-content
description: 
ms.assetid: eca6d081-f7ce-43aa-8bfc-9350fd61dc36
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterExtensionRequestVtbl, IPrinterExtensionRequestVtbl
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

# IPrinterExtensionRequestVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterExtensionRequest *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterExtensionRequest *This) AddRef			
 	
### -field ULONG(* )(IPrinterExtensionRequest *This) Release			
 	
### -field HRESULT(* )(IPrinterExtensionRequest *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterExtensionRequest *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterExtensionRequest *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterExtensionRequest *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterExtensionRequest *This,HRESULT hrStatus,BSTR bstrLogMessage) Cancel			
 	
### -field HRESULT(* )(IPrinterExtensionRequest *This) Complete			
 	
## -remarks

## -see-also