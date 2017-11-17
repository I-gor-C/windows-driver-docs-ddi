---
UID: NS.printerextension.IPrintJobVtbl
title: IPrintJobVtbl
author: windows-driver-content
description: 
ms.assetid: efdfd8b2-cb2f-4bf2-91ed-267178b0ef2d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintJobVtbl, IPrintJobVtbl
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

# IPrintJobVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintJob *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintJob *This) AddRef			
 	
### -field ULONG(* )(IPrintJob *This) Release			
 	
### -field HRESULT(* )(IPrintJob *This,BSTR *pbstrName) get_Name			
 	
### -field HRESULT(* )(IPrintJob *This,ULONG *pulID) get_Id			
 	
### -field HRESULT(* )(IPrintJob *This,ULONG *pulPages) get_PrintedPages			
 	
### -field HRESULT(* )(IPrintJob *This,ULONG *pulPages) get_TotalPages			
 	
### -field HRESULT(* )(IPrintJob *This,PrintJobStatus *pStatus) get_Status			
 	
### -field HRESULT(* )(IPrintJob *This,DATE *pSubmissionTime) get_SubmissionTime			
 	
### -field HRESULT(* )(IPrintJob *This) RequestCancel			
 	
## -remarks

## -see-also