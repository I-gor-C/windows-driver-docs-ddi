---
UID: NF:ks.KsReleaseDevice
title: KsReleaseDevice function
author: windows-driver-content
description: The KsReleaseDevice function releases the device mutex and exits the critical region.
old-location: stream\ksreleasedevice.htm
old-project: stream
ms.assetid: 47692ac1-969a-4f6f-a2e1-008b82ac1429
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsReleaseDevice, KsReleaseDevice function [Streaming Media Devices], avfunc_47876dbc-0dea-459f-96f7-81790d245745.xml, ks/KsReleaseDevice, stream.ksreleasedevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
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
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Ks.lib
-	Ks.dll
api_name:
-	KsReleaseDevice
product: Windows
targetos: Windows
req.typenames: 
---


# KsReleaseDevice function
The<b> KsReleaseDevice</b> function releases the device mutex and exits the critical region.

## Syntax

```
void KsReleaseDevice(
  PKSDEVICE Device
);
```

## Parameters

`Device`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> structure representing the AVStream device for which to release synchronous control.


## Return Value

None

## Remarks

<b>KsReleaseDevice </b>is used by a client that has finished accessing the device in a synchronous manner following a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560911">KsAcquireDevice</a>.

For more information, see <a href="https://msdn.microsoft.com/011edaaa-7449-41c3-8cfb-0d319901af8b">Mutexes in AVStream</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.  |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560911">KsAcquireDevice</a>