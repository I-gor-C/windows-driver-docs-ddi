---
UID: NS.ntddscsi._DUMP_POINTERS_EX
title: DUMP_POINTERS_EX
author: windows-driver-content
description: 
ms.assetid: a3627643-ee36-4275-985d-2ff1fafaad49
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DUMP_POINTERS_EX, DUMP_POINTERS_EX, *PDUMP_POINTERS_EX
req.header: ntddscsi.h
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

# DUMP_POINTERS_EX structure

## -description



## -struct-fields

### -field DUMP_POINTERS_VERSION Header			
 	
### -field PVOID DumpData			
 	
### -field PVOID CommonBufferVa			
 	
### -field ULONG CommonBufferSize			
 	
### -field BOOLEAN AllocateCommonBuffers			
 	
### -field PVOID DeviceObject			
 	
### -field PVOID DriverList			
 	
### -field ULONG dwPortFlags			
 	
### -field ULONG MaxDeviceDumpSectionSize			
 	
### -field ULONG MaxDeviceDumpLevel			
 	
### -field ULONG MaxTransferSize			
 	
### -field PVOID AdapterObject			
 	
### -field PVOID MappedRegisterBase			
 	
### -field PBOOLEAN DeviceReady			
 	
### -field PDUMP_DEVICE_POWERON_ROUTINE DumpDevicePowerOn			
 	
### -field PVOID DumpDevicePowerOnContext			
 	
## -remarks

## -see-also