---
UID: NS.printerextension.IPrintSchemaPageImageableSizeVtbl
title: IPrintSchemaPageImageableSizeVtbl
author: windows-driver-content
description: 
ms.assetid: 96ad08d0-cc52-4a0d-8b31-ba6ce2c5c98d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintSchemaPageImageableSizeVtbl, IPrintSchemaPageImageableSizeVtbl
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

# IPrintSchemaPageImageableSizeVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintSchemaPageImageableSize *This) AddRef			
 	
### -field ULONG(* )(IPrintSchemaPageImageableSize *This) Release			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,UINT *pctinfo) GetTypeInfoCount			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,UINT iTInfo,LCID lcid,ITypeInfo **ppTInfo) GetTypeInfo			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,REFIID riid,LPOLESTR *rgszNames,UINT cNames,LCID lcid,DISPID *rgDispId) GetIDsOfNames			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,DISPID dispIdMember,REFIID riid,LCID lcid,WORD wFlags,DISPPARAMS *pDispParams,VARIANT *pVarResult,EXCEPINFO *pExcepInfo,UINT *puArgErr) Invoke			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,IUnknown **ppXmlNode) get_XmlNode			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,BSTR *pbstrNamespaceUri) get_NamespaceUri			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,ULONG *pulImageableSizeWidth) get_ImageableSizeWidthInMicrons			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,ULONG *pulImageableSizeHeight) get_ImageableSizeHeightInMicrons			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,ULONG *pulOriginWidth) get_OriginWidthInMicrons			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,ULONG *pulOriginHeight) get_OriginHeightInMicrons			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,ULONG *pulExtentWidth) get_ExtentWidthInMicrons			
 	
### -field HRESULT(* )(IPrintSchemaPageImageableSize *This,ULONG *pulExtentHeight) get_ExtentHeightInMicrons			
 	
## -remarks

## -see-also