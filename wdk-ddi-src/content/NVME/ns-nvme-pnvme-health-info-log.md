---
UID: NS.nvme.PNVME_HEALTH_INFO_LOG
title: PNVME_HEALTH_INFO_LOG
author: windows-driver-content
description: 
ms.assetid: ff4cc537-4d5d-487d-b7db-7ffe2db115d9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PNVME_HEALTH_INFO_LOG, NVME_HEALTH_INFO_LOG, *PNVME_HEALTH_INFO_LOG
req.header: nvme.h
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

# PNVME_HEALTH_INFO_LOG structure

## -description



## -struct-fields

### -field union CriticalWarning			
 	
### -field __unnamed_union_0b31_145 __unnamed_union_0b31_145			
 	
### -field UCHAR [2] Temperature			
 	
### -field UCHAR AvailableSpare			
 	
### -field UCHAR AvailableSpareThreshold			
 	
### -field UCHAR PercentageUsed			
 	
### -field UCHAR [26] Reserved0			
 	
### -field UCHAR [16] DataUnitRead			
 	
### -field UCHAR [16] DataUnitWritten			
 	
### -field UCHAR [16] HostReadCommands			
 	
### -field UCHAR [16] HostWrittenCommands			
 	
### -field UCHAR [16] ControllerBusyTime			
 	
### -field UCHAR [16] PowerCycle			
 	
### -field UCHAR [16] PowerOnHours			
 	
### -field UCHAR [16] UnsafeShutdowns			
 	
### -field UCHAR [16] MediaErrors			
 	
### -field UCHAR [16] ErrorInfoLogEntryCount			
 	
### -field ULONG WarningCompositeTemperatureTime			
 	
### -field ULONG CriticalCompositeTemperatureTime			
 	
### -field USHORT TemperatureSensor1			
 	
### -field USHORT TemperatureSensor2			
 	
### -field USHORT TemperatureSensor3			
 	
### -field USHORT TemperatureSensor4			
 	
### -field USHORT TemperatureSensor5			
 	
### -field USHORT TemperatureSensor6			
 	
### -field USHORT TemperatureSensor7			
 	
### -field USHORT TemperatureSensor8			
 	
### -field UCHAR [296] Reserved1			
 	
### -field UCHAR  : 1 AvailableSpaceLow			
 	
### -field UCHAR  : 1 TemperatureThreshold			
 	
### -field UCHAR  : 1 ReliabilityDegraded			
 	
### -field UCHAR  : 1 ReadOnly			
 	
### -field UCHAR  : 1 VolatileMemoryBackupDeviceFailed			
 	
### -field UCHAR  : 3 Reserved			
 	
### -field UCHAR AsUchar			
 	
## -remarks

## -see-also