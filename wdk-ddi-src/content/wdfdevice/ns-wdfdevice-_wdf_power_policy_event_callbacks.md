---
UID: NS:wdfdevice._WDF_POWER_POLICY_EVENT_CALLBACKS
title: "_WDF_POWER_POLICY_EVENT_CALLBACKS"
author: windows-driver-content
description: The WDF_POWER_POLICY_EVENT_CALLBACKS structure contains pointers to a driver's power policy event callback functions.
old-location: wdf\wdf_power_policy_event_callbacks.htm
old-project: wdf
ms.assetid: 6932c938-e477-4a18-9ada-bb3864c6a6f1
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWDF_POWER_POLICY_EVENT_CALLBACKS, DFDeviceObjectGeneralRef_d4970639-86cb-4b83-8ac8-a7662ebca017.xml, PWDF_POWER_POLICY_EVENT_CALLBACKS, PWDF_POWER_POLICY_EVENT_CALLBACKS structure pointer, WDF_POWER_POLICY_EVENT_CALLBACKS, WDF_POWER_POLICY_EVENT_CALLBACKS structure, _WDF_POWER_POLICY_EVENT_CALLBACKS, kmdf.wdf_power_policy_event_callbacks, wdf.wdf_power_policy_event_callbacks, wdfdevice/PWDF_POWER_POLICY_EVENT_CALLBACKS, wdfdevice/WDF_POWER_POLICY_EVENT_CALLBACKS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
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
-	wdfdevice.h
api_name:
-	WDF_POWER_POLICY_EVENT_CALLBACKS
product: Windows
targetos: Windows
req.typenames: WDF_POWER_POLICY_EVENT_CALLBACKS, *PWDF_POWER_POLICY_EVENT_CALLBACKS
req.product: Windows 10 or later.
---

# _WDF_POWER_POLICY_EVENT_CALLBACKS structure
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_POWER_POLICY_EVENT_CALLBACKS</b> structure contains pointers to a driver's power policy event callback functions.

## Syntax
```
typedef struct _WDF_POWER_POLICY_EVENT_CALLBACKS {
  ULONG                                       Size;
  PFN_WDF_DEVICE_ARM_WAKE_FROM_S0             EvtDeviceArmWakeFromS0;
  PFN_WDF_DEVICE_DISARM_WAKE_FROM_S0          EvtDeviceDisarmWakeFromS0;
  PFN_WDF_DEVICE_WAKE_FROM_S0_TRIGGERED       EvtDeviceWakeFromS0Triggered;
  PFN_WDF_DEVICE_ARM_WAKE_FROM_SX             EvtDeviceArmWakeFromSx;
  PFN_WDF_DEVICE_DISARM_WAKE_FROM_SX          EvtDeviceDisarmWakeFromSx;
  PFN_WDF_DEVICE_WAKE_FROM_SX_TRIGGERED       EvtDeviceWakeFromSxTriggered;
  PFN_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON EvtDeviceArmWakeFromSxWithReason;
} WDF_POWER_POLICY_EVENT_CALLBACKS, *PWDF_POWER_POLICY_EVENT_CALLBACKS;
```

## Members


`Size`

The size, in bytes, of this structure.

`EvtDeviceArmWakeFromS0`

A pointer to the driver's <a href="https://msdn.microsoft.com/a3579239-517f-4df0-a632-31e1176c6552">EvtDeviceArmWakeFromS0</a> event callback function, or <b>NULL</b>.

`EvtDeviceDisarmWakeFromS0`

A pointer to the driver's <a href="https://msdn.microsoft.com/e944c299-d0b4-4ee3-8f46-0458807e4cee">EvtDeviceDisarmWakeFromS0</a> event callback function, or <b>NULL</b>.

`EvtDeviceWakeFromS0Triggered`

A pointer to the driver's <a href="https://msdn.microsoft.com/4395b1c1-ae67-42fc-b6c7-b1bdbf090c5b">EvtDeviceWakeFromS0Triggered</a> event callback function, or <b>NULL</b>.

`EvtDeviceArmWakeFromSx`

A pointer to the driver's <a href="https://msdn.microsoft.com/4954a278-8470-402c-a8ba-5e46ca56ddf7">EvtDeviceArmWakeFromSx</a> event callback function, or <b>NULL</b>.

`EvtDeviceDisarmWakeFromSx`

A pointer to the driver's <a href="https://msdn.microsoft.com/79bf7a42-5053-428a-a78b-dd8bdff93a69">EvtDeviceDisarmWakeFromSx</a> event callback function, or <b>NULL</b>.

`EvtDeviceWakeFromSxTriggered`

A pointer to the driver's <a href="https://msdn.microsoft.com/a1899d90-4906-458d-b7e3-122655f4d926">EvtDeviceWakeFromSxTriggered</a> event callback function, or <b>NULL</b>.

`EvtDeviceArmWakeFromSxWithReason`

A pointer to the driver's <a href="https://msdn.microsoft.com/8966ea8f-9760-4a09-b9d3-8fd1ac278b12">EvtDeviceArmWakeFromSxWithReason</a> event callback function, or <b>NULL</b>.

## Remarks
The <b>WDF_POWER_POLICY_EVENT_CALLBACKS</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546774">WdfDeviceInitSetPowerPolicyEventCallbacks</a> method.

Your driver should initialize its <b>WDF_POWER_POLICY_EVENT_CALLBACKS</b> structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552426">WDF_POWER_POLICY_EVENT_CALLBACKS_INIT</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfdevice.h (include Wdf.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552416">WDF_PNPPOWER_EVENT_CALLBACKS</a>