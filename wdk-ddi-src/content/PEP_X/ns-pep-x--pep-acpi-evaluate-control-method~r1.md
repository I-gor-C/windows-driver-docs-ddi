---
UID: NS.pep_x._PEP_ACPI_EVALUATE_CONTROL_METHOD~r1
title: PEP_ACPI_EVALUATE_CONTROL_METHOD
author: windows-driver-content
description: 
ms.assetid: 52a35b1e-83f5-44cf-9448-8e9733e38262
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PEP_ACPI_EVALUATE_CONTROL_METHOD, PEP_ACPI_EVALUATE_CONTROL_METHOD, *PPEP_ACPI_EVALUATE_CONTROL_METHOD
req.header: pep_x.h
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

# PEP_ACPI_EVALUATE_CONTROL_METHOD structure

## -description



## -struct-fields

### -field union __unnamed_union_0c3d_37			
 	
### -field PEPHANDLE DeviceHandle			
 	
### -field ULONG RequestFlags			
 	
### -field NTSTATUS MethodStatus			
 	
### -field PVOID CompletionContext			
 	
### -field ULONG InputArgumentCount			
 	
### -field SIZE_T InputArgumentSize			
 	
### -field PACPI_METHOD_ARGUMENT InputArguments			
 	
### -field ULONG OutputArgumentCount			
 	
### -field SIZE_T OutputArgumentSize			
 	
### -field PACPI_METHOD_ARGUMENT OutputArguments			
 	
### -field ULONG MethodName			
 	
### -field ANSI_STRING MethodNameString			
 	
## -remarks

## -see-also