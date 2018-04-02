---
UID: NS:storport._MESSAGE_INTERRUPT_INFORMATION
title: "_MESSAGE_INTERRUPT_INFORMATION"
author: windows-driver-content
description: The MESSAGE_INTERRUPT_INFORMATION structure describes a message signaled interrupt (MSI).
old-location: storage\message_interrupt_information.htm
old-project: storage
ms.assetid: 469896b3-3ae0-4edd-9fb0-ee5869633872
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PMESSAGE_INTERRUPT_INFORMATION, MESSAGE_INTERRUPT_INFORMATION, MESSAGE_INTERRUPT_INFORMATION structure [Storage Devices], PMESSAGE_INTERRUPT_INFORMATION, PMESSAGE_INTERRUPT_INFORMATION structure pointer [Storage Devices], _MESSAGE_INTERRUPT_INFORMATION, storage.message_interrupt_information, storport/MESSAGE_INTERRUPT_INFORMATION, storport/PMESSAGE_INTERRUPT_INFORMATION, structs-storport_a918acbf-24eb-4112-8bab-bb2ee441064e.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	storport.h
api_name:
-	MESSAGE_INTERRUPT_INFORMATION
product:
- Windows
targetos: Windows
req.typenames: MESSAGE_INTERRUPT_INFORMATION, *PMESSAGE_INTERRUPT_INFORMATION
req.product: Windows 10 or later.
---

# _MESSAGE_INTERRUPT_INFORMATION structure
The <b>MESSAGE_INTERRUPT_INFORMATION</b> structure describes a message signaled interrupt (MSI).

## Syntax
```
typedef struct _MESSAGE_INTERRUPT_INFORMATION {
  ULONG                 MessageId;
  ULONG                 MessageData;
  STOR_PHYSICAL_ADDRESS MessageAddress;
  ULONG                 InterruptVector;
  ULONG                 InterruptLevel;
  KINTERRUPT_MODE       InterruptMode;
} MESSAGE_INTERRUPT_INFORMATION, *PMESSAGE_INTERRUPT_INFORMATION;
```

## Members


`MessageId`

An identifier identifies the MSI interrupt. A miniport driver can pass this value to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567023">StorPortAcquireMSISpinLock</a> in the <i>MessageId</i> parameter to obtain a spin lock for synchronization purposes.

`MessageData`

The data associated with the message.

`MessageAddress`

The physical address associated with the message.

`InterruptVector`

The interrupt vector associated with the message.

`InterruptLevel`

The interrupt level associated with the message.

`InterruptMode`

A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff554239">KINTERRUPT_MODE</a> that specifies the interrupt mode associated with the message.

## Remarks
Miniport drivers retrieve the MSI information in a <b>MESSAGE_INTERRUPT_INFORMATION</b> structure by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567090">StorPortGetMSIInfo</a> routine.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | storport.h (include Storport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567090">StorPortGetMSIInfo</a>