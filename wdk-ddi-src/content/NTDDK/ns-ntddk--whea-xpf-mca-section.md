---
UID: NS.ntddk._WHEA_XPF_MCA_SECTION
title: WHEA_XPF_MCA_SECTION
author: windows-driver-content
description: 
ms.assetid: a4460f54-4f17-4684-b38a-fe3c34a110b5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WHEA_XPF_MCA_SECTION, WHEA_XPF_MCA_SECTION, *PWHEA_XPF_MCA_SECTION
req.header: ntddk.h
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

# WHEA_XPF_MCA_SECTION structure

## -description



## -struct-fields

### -field ULONG VersionNumber			
 	
### -field WHEA_CPU_VENDOR CpuVendor			
 	
### -field LARGE_INTEGER Timestamp			
 	
### -field ULONG ProcessorNumber			
 	
### -field MCG_STATUS GlobalStatus			
 	
### -field ULONGLONG InstructionPointer			
 	
### -field ULONG BankNumber			
 	
### -field MCI_STATUS Status			
 	
### -field ULONGLONG Address			
 	
### -field ULONGLONG Misc			
 	
### -field ULONG ExtendedRegisterCount			
 	
### -field ULONG Reserved2			
 	
### -field ULONGLONG [WHEA_XPF_MCA_EXTREG_MAX_COUNT] ExtendedRegisters			
 	
## -remarks

## -see-also