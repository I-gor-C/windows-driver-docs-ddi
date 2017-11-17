---
UID: NS.mfidl.IMFSensorActivityReportVtbl
title: IMFSensorActivityReportVtbl
author: windows-driver-content
description: 
ms.assetid: b982f6bd-bd32-4eae-b867-54aa7a55d246
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSensorActivityReportVtbl, IMFSensorActivityReportVtbl
req.header: mfidl.h
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

# IMFSensorActivityReportVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSensorActivityReport *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSensorActivityReport *This) AddRef			
 	
### -field ULONG(* )(IMFSensorActivityReport *This) Release			
 	
### -field HRESULT(* )(IMFSensorActivityReport *This,LPWSTR FriendlyName,ULONG cchFriendlyName,ULONG *pcchWritten) GetFriendlyName			
 	
### -field HRESULT(* )(IMFSensorActivityReport *This,LPWSTR SymbolicLink,ULONG cchSymbolicLink,ULONG *pcchWritten) GetSymbolicLink			
 	
### -field HRESULT(* )(IMFSensorActivityReport *This,ULONG *pcCount) GetProcessCount			
 	
### -field HRESULT(* )(IMFSensorActivityReport *This,ULONG Index,IMFSensorProcessActivity **ppProcessActivity) GetProcessActivity			
 	
## -remarks

## -see-also