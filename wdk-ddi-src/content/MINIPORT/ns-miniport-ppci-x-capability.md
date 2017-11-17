---
UID: NS.miniport.PPCI_X_CAPABILITY
title: PPCI_X_CAPABILITY
author: windows-driver-content
description: 
ms.assetid: e7fd6cc0-7122-468a-b98d-4c2e3003c6ac
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PPCI_X_CAPABILITY, PCI_X_CAPABILITY, *PPCI_X_CAPABILITY
req.header: miniport.h
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

# PPCI_X_CAPABILITY structure

## -description



## -struct-fields

### -field union Command			
 	
### -field __unnamed_union_0c02_21 __unnamed_union_0c02_21			
 	
### -field union Status			
 	
### -field __unnamed_union_0c02_23 __unnamed_union_0c02_23			
 	
### -field PCI_CAPABILITIES_HEADER Header			
 	
### -field USHORT  : 1 DataParityErrorRecoveryEnable			
 	
### -field USHORT  : 1 EnableRelaxedOrdering			
 	
### -field USHORT  : 2 MaxMemoryReadByteCount			
 	
### -field USHORT  : 3 MaxOutstandingSplitTransactions			
 	
### -field USHORT  : 9 Reserved			
 	
### -field USHORT AsUSHORT			
 	
### -field ULONG  : 3 FunctionNumber			
 	
### -field ULONG  : 5 DeviceNumber			
 	
### -field ULONG  : 8 BusNumber			
 	
### -field ULONG  : 1 Device64Bit			
 	
### -field ULONG  : 1 Capable133MHz			
 	
### -field ULONG  : 1 SplitCompletionDiscarded			
 	
### -field ULONG  : 1 UnexpectedSplitCompletion			
 	
### -field ULONG  : 1 DeviceComplexity			
 	
### -field ULONG  : 2 DesignedMaxMemoryReadByteCount			
 	
### -field ULONG  : 3 DesignedMaxOutstandingSplitTransactions			
 	
### -field ULONG  : 3 DesignedMaxCumulativeReadSize			
 	
### -field ULONG  : 1 ReceivedSplitCompletionErrorMessage			
 	
### -field ULONG  : 1 CapablePCIX266			
 	
### -field ULONG  : 1 CapablePCIX533			
 	
### -field ULONG AsULONG			
 	
## -remarks

## -see-also