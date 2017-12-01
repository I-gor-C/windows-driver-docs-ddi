---
UID: NE.wudfddi_types._WDF_POWER_POLICY_S0_IDLE_CAPABILITIES
title: WDF_POWER_POLICY_S0_IDLE_CAPABILITIES
author: windows-driver-content
description: The WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration identifies the capabilities that a device can support when it enters a low-power state while it is idling.
old-location: wdf\wdf_power_policy_s0_idle_capabilities.htm
old-project: wdf
ms.assetid: b4a3611d-5eb6-4fb2-a66a-e563569c4790
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WRITE_REGISTER_USHORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfddi_types.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 1.11
req.alt-api: WDF_POWER_POLICY_S0_IDLE_CAPABILITIES
req.alt-loc: wdfdevice.h,wudfddi_types.h
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
req.iface: 
req.product: Windows 10 or later.
---

# WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_POWER_POLICY_S0_IDLE_CAPABILITIES</b> enumeration identifies the capabilities that a device can support when it enters a low-power state while it is idling.</p>


## -syntax

````
typedef enum _WDF_POWER_POLICY_S0_IDLE_CAPABILITIES { 
  IdleCapsInvalid          = 0,
  IdleCannotWakeFromS0     = 1,
  IdleCanWakeFromS0        = 2,
  IdleUsbSelectiveSuspend  = 3
} WDF_POWER_POLICY_S0_IDLE_CAPABILITIES;
````


## -enum-fields
<dl>

### -field <a id="IdleCapsInvalid"></a><a id="idlecapsinvalid"></a><a id="IDLECAPSINVALID"></a><b>IdleCapsInvalid</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="IdleCannotWakeFromS0"></a><a id="idlecannotwakefroms0"></a><a id="IDLECANNOTWAKEFROMS0"></a><b>IdleCannotWakeFromS0</b>

<dd>
<p>The device cannot wake itself from a low-power state while the system is in its working (S0) state.</p>
</dd>

### -field <a id="IdleCanWakeFromS0"></a><a id="idlecanwakefroms0"></a><a id="IDLECANWAKEFROMS0"></a><b>IdleCanWakeFromS0</b>

<dd>
<p>The device can wake itself from a low-power state while the system is in its working (S0) state.</p>
</dd>

### -field <a id="IdleUsbSelectiveSuspend"></a><a id="idleusbselectivesuspend"></a><a id="IDLEUSBSELECTIVESUSPEND"></a><b>IdleUsbSelectiveSuspend</b>

<dd>
<p>The device is connected to a USB bus and supports <a href="buses.usb_selective_suspend">USB selective suspend</a>. Use this value if your USB-connected device supports both idling and waking itself while the computer is in its working state. If your USB device supports only idling, use <b>IdleCannotWakeFromS0</b>. (Drivers for USB devices must not specify <b>IdleCanWakeFromS0</b>.) See the code examples in the following Examples section.</p>
<p>For Windows XP, the framework supports USB selective suspend only if the device's <a href="..\usbspec\ns-usbspec--usb-configuration-descriptor.md">USB_CONFIGURATION_DESCRIPTOR</a> structure shows that the device supports <a href="buses.remote_wakeup_of_usb_devices">remote wakeup</a>. For Windows Vista and later versions of Windows, the framework supports USB selective suspend whether or not the device supports remote wakeup.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_POWER_POLICY_S0_IDLE_CAPABILITIES</b> enumeration is used in the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-idle-settings.md">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure. </p>

<p>The following code examples show how to enable idle support for a USB device. In each case, the STATUS_POWER_STATE_INVALID return value means the bus driver has reported that the device cannot wake itself.</p>

<p><b>KMDF Example</b></p>

<p><b>UMDF Example</b></p>

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
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h); </dt>
<dt>Wudfddi_types.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-idle-settings.md">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
