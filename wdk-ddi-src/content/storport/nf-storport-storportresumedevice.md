---
UID: NF:storport.StorPortResumeDevice
title: StorPortResumeDevice function
author: windows-driver-content
description: The StorPortResumeDevice routine resumes a previously paused logical unit.
old-location: storage\storportresumedevice.htm
old-project: storage
ms.assetid: 81b979a8-87bb-48f3-b44a-bac9286648fa
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortResumeDevice, StorPortResumeDevice routine [Storage Devices], storage.storportresumedevice, storport/StorPortResumeDevice, storprt_62696d8f-cfb1-43fd-8b23-b14f1ac0d429.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
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
req.lib: Storport.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Storport.lib
-	Storport.dll
api_name:
-	StorPortResumeDevice
product:
- Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortResumeDevice function
The <b>StorPortResumeDevice</b> routine resumes a previously paused logical unit.

## Syntax

```
STORPORT_API BOOLEAN StorPortResumeDevice(
  PVOID HwDeviceExtension,
  UCHAR PathId,
  UCHAR TargetId,
  UCHAR Lun
);
```

## Parameters

`HwDeviceExtension`

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff567108">StorPortInitialize</a>. The port driver frees this memory when it removes the device.

`PathId`

Identifies the SCSI bus.

`TargetId`

Identifies the target controller or device on the bus.

`Lun`

Identifies the logical unit number of the target device.


## Return Value

<b>StorPortResumeDevice</b> returns <b>TRUE</b> if the miniport driver succeeded in resuming the paused device, <b>FALSE</b> if not.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567461">StorPortPauseDevice</a>