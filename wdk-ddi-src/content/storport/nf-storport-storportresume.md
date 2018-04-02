---
UID: NF:storport.StorPortResume
title: StorPortResume function
author: windows-driver-content
description: The StorPortResume routine resumes a paused adapter.
old-location: storage\storportresume.htm
old-project: storage
ms.assetid: 2a1e380b-ddad-495b-a921-ebd85525d1a6
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortResume, StorPortResume routine [Storage Devices], storage.storportresume, storport/StorPortResume, storprt_3970ca06-96f5-4d0a-84b0-781145133788.xml
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
-	StorPortResume
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortResume function
The <b>StorPortResume</b> routine resumes a paused adapter.

## Syntax

```
STORPORT_API BOOLEAN StorPortResume(
  PVOID HwDeviceExtension
);
```

## Parameters

`HwDeviceExtension`

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff567108">StorPortInitialize</a>. The port driver frees this memory when it removes the device.


## Return Value

<b>StorPortResume</b> returns <b>TRUE</b> if the miniport driver succeeded in resuming the paused adapter, <b>FALSE</b> if not.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567459">StorPortPause</a>