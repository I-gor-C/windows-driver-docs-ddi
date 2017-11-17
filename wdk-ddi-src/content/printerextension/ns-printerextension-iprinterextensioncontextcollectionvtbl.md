---
UID: NS.printerextension.IPrinterExtensionContextCollectionVtbl
title: IPrinterExtensionContextCollectionVtbl
author: windows-driver-content
description: 
ms.assetid: 30f0147c-0b3f-4a52-a72a-065977eabae5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterExtensionContextCollectionVtbl, IPrinterExtensionContextCollectionVtbl
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

# IPrinterExtensionContextCollectionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterExtensionContextCollection *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterExtensionContextCollection *This) AddRef			
 	
### -field ULONG(* )(IPrinterExtensionContextCollection *This) Release			
 	
### -field HRESULT(* )(IPrinterExtensionContextCollection *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterExtensionContextCollection *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterExtensionContextCollection *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterExtensionContextCollection *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterExtensionContextCollection *This,ULONG *pulCount) get_Count			
 	
### -field HRESULT(* )(IPrinterExtensionContextCollection *This,ULONG ulIndex,IPrinterExtensionContext **ppContext) GetAt			
 	
### -field HRESULT(* )(IPrinterExtensionContextCollection *This,IUnknown **ppUnk) get__NewEnum			
 	
## -remarks

## -see-also