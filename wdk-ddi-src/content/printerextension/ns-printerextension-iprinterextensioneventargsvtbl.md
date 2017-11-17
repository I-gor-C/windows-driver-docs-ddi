---
UID: NS.printerextension.IPrinterExtensionEventArgsVtbl
title: IPrinterExtensionEventArgsVtbl
author: windows-driver-content
description: 
ms.assetid: 590562f5-54d4-4419-b223-57c9846c7619
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrinterExtensionEventArgsVtbl, IPrinterExtensionEventArgsVtbl
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

# IPrinterExtensionEventArgsVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrinterExtensionEventArgs *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrinterExtensionEventArgs *This) AddRef			
 	
### -field ULONG(* )(IPrinterExtensionEventArgs *This) Release			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,IPrinterQueue **ppQueue) get_PrinterQueue			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,IPrintSchemaTicket **ppTicket) get_PrintSchemaTicket			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,IPrinterPropertyBag **ppPropertyBag) get_DriverProperties			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,IPrinterPropertyBag **ppPropertyBag) get_UserProperties			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,BSTR *pbstrBidiNotification) get_BidiNotification			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,GUID *pReasonId) get_ReasonId			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,IPrinterExtensionRequest **ppRequest) get_Request			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,BSTR *pbstrApplication) get_SourceApplication			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,GUID *pDetailedReasonId) get_DetailedReasonId			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,BOOL *pbModal) get_WindowModal			
 	
### -field HRESULT(* )(IPrinterExtensionEventArgs *This,HANDLE *phwndParent) get_WindowParent			
 	
## -remarks

## -see-also