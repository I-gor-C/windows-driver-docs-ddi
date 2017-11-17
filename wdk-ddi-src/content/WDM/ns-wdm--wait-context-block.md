---
UID: NS.wdm._WAIT_CONTEXT_BLOCK
title: WAIT_CONTEXT_BLOCK
author: windows-driver-content
description: 
ms.assetid: 420ecd28-726e-4232-ae70-02fac0f9d251
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WAIT_CONTEXT_BLOCK, WAIT_CONTEXT_BLOCK, *PWAIT_CONTEXT_BLOCK
req.header: wdm.h
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

# WAIT_CONTEXT_BLOCK structure

## -description



## -struct-fields

### -field union __unnamed_union_0cb3_104			
 	
### -field PDRIVER_CONTROL DeviceRoutine			
 	
### -field PVOID DeviceContext			
 	
### -field ULONG NumberOfMapRegisters			
 	
### -field PVOID DeviceObject			
 	
### -field PVOID CurrentIrp			
 	
### -field PKDPC BufferChainingDpc			
 	
### -field LIST_ENTRY DmaWaitEntry			
 	
### -field ULONG NumberOfChannels			
 	
### -field ULONG  : 1 SyncCallback			
 	
### -field ULONG  : 1 DmaContext			
 	
### -field ULONG  : 1 ZeroMapRegisters			
 	
### -field ULONG  : 29 Reserved			
 	
### -field KDEVICE_QUEUE_ENTRY WaitQueueEntry			
 	
## -remarks

## -see-also