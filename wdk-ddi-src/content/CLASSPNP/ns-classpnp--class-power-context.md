---
UID: NS.classpnp._CLASS_POWER_CONTEXT
title: CLASS_POWER_CONTEXT
author: windows-driver-content
description: 
ms.assetid: a3d3d908-4606-4d5b-a3ab-9be5577dafd6
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: CLASS_POWER_CONTEXT, CLASS_POWER_CONTEXT, *PCLASS_POWER_CONTEXT
req.header: classpnp.h
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

# CLASS_POWER_CONTEXT structure

## -description



## -struct-fields

### -field union PowerChangeState			
 	
### -field __unnamed_union_0b7c_9 __unnamed_union_0b7c_9			
 	
### -field CLASS_POWER_OPTIONS Options			
 	
### -field BOOLEAN InUse			
 	
### -field BOOLEAN QueueLocked			
 	
### -field NTSTATUS FinalStatus			
 	
### -field ULONG RetryCount			
 	
### -field ULONG RetryInterval			
 	
### -field PIO_COMPLETION_ROUTINE CompletionRoutine			
 	
### -field PDEVICE_OBJECT DeviceObject			
 	
### -field PIRP Irp			
 	
### -field SCSI_REQUEST_BLOCK Srb			
 	
### -field CLASS_POWER_DOWN_STATE PowerDown			
 	
### -field CLASS_POWER_DOWN_STATE2 PowerDown2			
 	
### -field CLASS_POWER_DOWN_STATE3 PowerDown3			
 	
### -field CLASS_POWER_UP_STATE PowerUp			
 	
## -remarks

## -see-also