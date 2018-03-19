---
UID: NC:ks.PFNKSDEVICESETPOWER
title: PFNKSDEVICESETPOWER
author: windows-driver-content
description: AVStream calls a minidriver's AVStrMiniDeviceSetPower routine when it receives an IRP_MN_SET_POWER.
old-location: stream\avstrminidevicesetpower.htm
old-project: stream
ms.assetid: 40d5eb14-b7bd-42b6-a3f5-fe9e8c5c806e
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: AVStrMiniDeviceSetPower, AVStrMiniDeviceSetPower routine [Streaming Media Devices], PFNKSDEVICESETPOWER, avstclbk_8b833d83-a199-44a9-97b8-c4afc624d6d5.xml, ks/AVStrMiniDeviceSetPower, stream.avstrminidevicesetpower
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ks.h
api_name:
-	AVStrMiniDeviceSetPower
product: Windows
targetos: Windows
req.typenames: SOUNDDETECTOR_PATTERNHEADER
---


# PFNKSDEVICESETPOWER callback function
AVStream calls a minidriver's <i>AVStrMiniDeviceSetPower</i> routine when it receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>.

## Syntax

```
PFNKSDEVICESETPOWER Pfnksdevicesetpower;

void Pfnksdevicesetpower(
  PKSDEVICE Device,
  PIRP Irp,
  DEVICE_POWER_STATE To,
  DEVICE_POWER_STATE From
)
{...}
```

## Parameters

`Device`

Pointer to the <a href="..\ks\ns-ks-_ksdevice.md">KSDEVICE</a> structure that received the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>.

`Irp`

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> issued by <i>Device</i>.

`To`

The target device power state.

`From`

The current device power state.


## Return Value

None

## Remarks

If a driver has registered its device for idle detection, the power manager sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> to change the power state of an idle device.

The minidriver specifies this routine's address in the <b>SetPower</b> member of its <a href="..\ks\ns-ks-_ksdevice_dispatch.md">KSDEVICE_DISPATCH</a> structure.

This routine is optional.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.  |
| **Target Platform** | Desktop |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\ns-ks-_ksdevice_dispatch.md">KSDEVICE_DISPATCH</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>