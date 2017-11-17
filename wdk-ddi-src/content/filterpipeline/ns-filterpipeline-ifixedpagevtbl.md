---
UID: NS.filterpipeline.IFixedPageVtbl
title: IFixedPageVtbl
author: windows-driver-content
description: 
ms.assetid: 1798c3d9-5198-48e6-91bd-55c34776b775
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IFixedPageVtbl, IFixedPageVtbl
req.header: filterpipeline.h
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

# IFixedPageVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IFixedPage *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IFixedPage *This) AddRef			
 	
### -field ULONG(* )(IFixedPage *This) Release			
 	
### -field HRESULT(* )(IFixedPage *This,BSTR *uri) GetUri			
 	
### -field HRESULT(* )(IFixedPage *This,IPrintReadStream **ppStream) GetStream			
 	
### -field HRESULT(* )(IFixedPage *This,EXpsCompressionOptions *pCompression) GetPartCompression			
 	
### -field HRESULT(* )(IFixedPage *This,EXpsCompressionOptions compression) SetPartCompression			
 	
### -field HRESULT(* )(IFixedPage *This,IPartPrintTicket **ppPrintTicket) GetPrintTicket			
 	
### -field HRESULT(* )(IFixedPage *This, const wchar_t *uri,IUnknown **ppUnk) GetPagePart			
 	
### -field HRESULT(* )(IFixedPage *This,IPrintWriteStream **ppWriteStream) GetWriteStream			
 	
### -field HRESULT(* )(IFixedPage *This,IPartPrintTicket *ppPrintTicket) SetPrintTicket			
 	
### -field HRESULT(* )(IFixedPage *This,IUnknown *pUnk) SetPagePart			
 	
### -field HRESULT(* )(IFixedPage *This, const wchar_t *uri) DeleteResource			
 	
### -field HRESULT(* )(IFixedPage *This,IXpsPartIterator **pXpsPartIt) GetXpsPartIterator			
 	
## -remarks

## -see-also