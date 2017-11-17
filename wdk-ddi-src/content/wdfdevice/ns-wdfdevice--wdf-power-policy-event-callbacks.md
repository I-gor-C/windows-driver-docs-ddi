---
UID: NS.wdfdevice._WDF_POWER_POLICY_EVENT_CALLBACKS
title: WDF_POWER_POLICY_EVENT_CALLBACKS
author: windows-driver-content
description: The WDF_POWER_POLICY_EVENT_CALLBACKS structure contains pointers to a driver's power policy event callback functions.
old-location: wdf\wdf_power_policy_event_callbacks.htm
ms.assetid: 6932c938-e477-4a18-9ada-bb3864c6a6f1
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_POWER_POLICY_EVENT_CALLBACKS
req.alt-loc: wdfdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_POWER_POLICY_EVENT_CALLBACKS, WDF_POWER_POLICY_EVENT_CALLBACKS, *PWDF_POWER_POLICY_EVENT_CALLBACKS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_POWER_POLICY_EVENT_CALLBACKS structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_POWER_POLICY_EVENT_CALLBACKS</b> structure contains pointers to a driver's power policy event callback functions. </p>


## -syntax

````
typedef struct _WDF_POWER_POLICY_EVENT_CALLBACKS {
  ULONG                                       Size;
  PFN_WDF_DEVICE_ARM_WAKE_FROM_S0             EvtDeviceArmWakeFromS0;
  PFN_WDF_DEVICE_DISARM_WAKE_FROM_S0          EvtDeviceDisarmWakeFromS0;
  PFN_WDF_DEVICE_WAKE_FROM_S0_TRIGGERED       EvtDeviceWakeFromS0Triggered;
  PFN_WDF_DEVICE_ARM_WAKE_FROM_SX             EvtDeviceArmWakeFromSx;
  PFN_WDF_DEVICE_DISARM_WAKE_FROM_SX          EvtDeviceDisarmWakeFromSx;
  PFN_WDF_DEVICE_WAKE_FROM_SX_TRIGGERED       EvtDeviceWakeFromSxTriggered;
  PFN_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON EvtDeviceArmWakeFromSxWithReason;
} WDF_POWER_POLICY_EVENT_CALLBACKS, *PWDF_POWER_POLICY_EVENT_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>EvtDeviceArmWakeFromS0</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/a3579239-517f-4df0-a632-31e1176c6552">EvtDeviceArmWakeFromS0</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceDisarmWakeFromS0</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/e944c299-d0b4-4ee3-8f46-0458807e4cee">EvtDeviceDisarmWakeFromS0</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceWakeFromS0Triggered</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/4395b1c1-ae67-42fc-b6c7-b1bdbf090c5b">EvtDeviceWakeFromS0Triggered</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceArmWakeFromSx</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/4954a278-8470-402c-a8ba-5e46ca56ddf7">EvtDeviceArmWakeFromSx</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceDisarmWakeFromSx</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/79bf7a42-5053-428a-a78b-dd8bdff93a69">EvtDeviceDisarmWakeFromSx</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceWakeFromSxTriggered</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/a1899d90-4906-458d-b7e3-122655f4d926">EvtDeviceWakeFromSxTriggered</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceArmWakeFromSxWithReason</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/8966ea8f-9760-4a09-b9d3-8fd1ac278b12">EvtDeviceArmWakeFromSxWithReason</a> event callback function, or <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_POWER_POLICY_EVENT_CALLBACKS</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546774">WdfDeviceInitSetPowerPolicyEventCallbacks</a> method.</p>

<p>Your driver should initialize its <b>WDF_POWER_POLICY_EVENT_CALLBACKS</b> structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552426">WDF_POWER_POLICY_EVENT_CALLBACKS_INIT</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552416">WDF_PNPPOWER_EVENT_CALLBACKS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_POWER_POLICY_EVENT_CALLBACKS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
