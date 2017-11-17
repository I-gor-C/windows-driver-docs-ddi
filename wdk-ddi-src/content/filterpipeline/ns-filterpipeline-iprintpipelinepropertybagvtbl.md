---
UID: NS.filterpipeline.IPrintPipelinePropertyBagVtbl
title: IPrintPipelinePropertyBagVtbl
author: windows-driver-content
description: 
ms.assetid: 56368178-37b0-45ab-aaf9-3c7ab2ebf5d1
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintPipelinePropertyBagVtbl, IPrintPipelinePropertyBagVtbl
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

# IPrintPipelinePropertyBagVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintPipelinePropertyBag *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintPipelinePropertyBag *This) AddRef			
 	
### -field ULONG(* )(IPrintPipelinePropertyBag *This) Release			
 	
### -field HRESULT(* )(IPrintPipelinePropertyBag *This, const wchar_t *pszName, const VARIANT *pVar) AddProperty			
 	
### -field HRESULT(* )(IPrintPipelinePropertyBag *This, const wchar_t *pszName,VARIANT *pVar) GetProperty			
 	
### -field BOOL(* )(IPrintPipelinePropertyBag *This, const wchar_t *pszName) DeleteProperty			
 	
## -remarks

## -see-also