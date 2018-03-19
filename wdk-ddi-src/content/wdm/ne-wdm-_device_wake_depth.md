---
UID: NE:wdm._DEVICE_WAKE_DEPTH
title: "_DEVICE_WAKE_DEPTH"
author: windows-driver-content
description: The DEVICE_WAKE_DEPTH enumeration specifies the deepest device power state from which a device can trigger a wake signal.
old-location: kernel\device_wake_depth.htm
old-project: kernel
ms.assetid: C8829785-1EB7-4F29-9279-F2FC2A3C0ABD
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PDEVICE_WAKE_DEPTH, DEVICE_WAKE_DEPTH, DEVICE_WAKE_DEPTH enumeration [Kernel-Mode Driver Architecture], DeviceWakeDepthD0, DeviceWakeDepthD1, DeviceWakeDepthD2, DeviceWakeDepthD3cold, DeviceWakeDepthD3hot, DeviceWakeDepthMaximum, DeviceWakeDepthNotWakeable, _DEVICE_WAKE_DEPTH, kernel.device_wake_depth, wdm/DEVICE_WAKE_DEPTH, wdm/DeviceWakeDepthD0, wdm/DeviceWakeDepthD1, wdm/DeviceWakeDepthD2, wdm/DeviceWakeDepthD3cold, wdm/DeviceWakeDepthD3hot, wdm/DeviceWakeDepthMaximum, wdm/DeviceWakeDepthNotWakeable"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	DEVICE_WAKE_DEPTH
product: Windows
targetos: Windows
req.typenames: DEVICE_WAKE_DEPTH, *PDEVICE_WAKE_DEPTH
req.product: Windows 10 or later.
---

# _DEVICE_WAKE_DEPTH Enumeration
The <b>DEVICE_WAKE_DEPTH</b> enumeration specifies the deepest device power state from which a device can trigger a wake signal.

## Syntax
````
typedef enum _DEVICE_WAKE_DEPTH { 
  DeviceWakeDepthNotWakeable  = 0,
  DeviceWakeDepthD0,
  DeviceWakeDepthD1,
  DeviceWakeDepthD2,
  DeviceWakeDepthD3hot,
  DeviceWakeDepthD3cold,
  DeviceWakeDepthMaximum
} DEVICE_WAKE_DEPTH;
````

## Constants

<table>
            
                <tr>
                    <td>DeviceWakeDepthNotWakeable</td>
                    <td>There is no device power state that can trigger a wake signal.</td>
                </tr>
            
                <tr>
                    <td>DeviceWakeDepthD0</td>
                    <td>D0 is the deepest device power state from which the device can trigger a wake signal. For more information, see Remarks.</td>
                </tr>
            
                <tr>
                    <td>DeviceWakeDepthD1</td>
                    <td>D1 is the deepest low-power device power state from which the device can trigger a wake signal.</td>
                </tr>
            
                <tr>
                    <td>DeviceWakeDepthD2</td>
                    <td>D2 is the deepest low-power device power state from which the device can trigger a wake signal.</td>
                </tr>
            
                <tr>
                    <td>DeviceWakeDepthD3hot</td>
                    <td>D3hot is the deepest low-power device power state from which the device can trigger a wake signal.</td>
                </tr>
            
                <tr>
                    <td>DeviceWakeDepthD3cold</td>
                    <td>D3cold is the deepest low-power device power state from which the device can trigger a wake signal.</td>
                </tr>
            
                <tr>
                    <td>DeviceWakeDepthMaximum</td>
                    <td>Reserved for use by the operating system.</td>
                </tr>
</table>

## Remarks

The <i>DeepestWakeableDstate</i> parameter of the <a href="..\wdm\nc-wdm-get_idle_wake_info.md">GetIdleWakeInfo</a> routine is a pointer to a variable of type <b>DEVICE_WAKE_DEPTH</b>.

The drivers for most devices have no reason to arm a wake signal when the device is in D0. These drivers can treat the <b>DeviceWakeDepthD0</b> output value as equivalent to a call to the <i>GetIdleWakeInfo</i> routine that fails and returns an error status.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h) |

## See Also

<a href="..\wdm\nc-wdm-get_idle_wake_info.md">GetIdleWakeInfo</a>