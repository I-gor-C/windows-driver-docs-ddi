---
UID: NS.ntddscsi._DUMP_POINTERS
title: DUMP_POINTERS
author: windows-driver-content
description: 
ms.assetid: 88596f08-ef26-4fb1-8fac-559a0105f519
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DUMP_POINTERS, DUMP_POINTERS, *PDUMP_POINTERS
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

# DUMP_POINTERS structure

## -description



## -struct-fields

### -field struct _ADAPTER_OBJECT			
 	
### -field _ADAPTER_OBJECT * AdapterObject			
 	
### -field PVOID MappedRegisterBase			
 	
### -field PVOID DumpData			
 	
### -field PVOID CommonBufferVa			
 	
### -field LARGE_INTEGER CommonBufferPa			
 	
### -field ULONG CommonBufferSize			
 	
### -field BOOLEAN AllocateCommonBuffers			
 	
### -field UCHAR [3] Spare1			
 	
### -field BOOLEAN UseDiskDump			
 	
### -field UCHAR [2] Spare1			
 	
### -field PVOID DeviceObject			
 	
## -remarks

## -see-also