---
UID: NS.wdfdevice._WDF_DEVICE_POWER_CAPABILITIES
title: WDF_DEVICE_POWER_CAPABILITIES
author: windows-driver-content
description: The WDF_DEVICE_POWER_CAPABILITIES structure describes a device's power capabilities.
old-location: wdf\wdf_device_power_capabilities.htm
ms.assetid: 56bb271f-d69c-4523-87cb-4922b405f808
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
req.alt-api: WDF_DEVICE_POWER_CAPABILITIES
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
ms.keywords: WDF_DEVICE_POWER_CAPABILITIES, WDF_DEVICE_POWER_CAPABILITIES, *PWDF_DEVICE_POWER_CAPABILITIES
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_POWER_CAPABILITIES structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The WDF_DEVICE_POWER_CAPABILITIES structure describes a device's power capabilities.</p>


## -syntax

````
typedef struct _WDF_DEVICE_POWER_CAPABILITIES {
  ULONG              Size;
  WDF_TRI_STATE      DeviceD1;
  WDF_TRI_STATE      DeviceD2;
  WDF_TRI_STATE      WakeFromD0;
  WDF_TRI_STATE      WakeFromD1;
  WDF_TRI_STATE      WakeFromD2;
  WDF_TRI_STATE      WakeFromD3;
  DEVICE_POWER_STATE DeviceState[PowerSystemMaximum];
  DEVICE_POWER_STATE DeviceWake;
  SYSTEM_POWER_STATE SystemWake;
  ULONG              D1Latency;
  ULONG              D2Latency;
  ULONG              D3Latency;
  DEVICE_POWER_STATE IdealDxStateForSx;
} WDF_DEVICE_POWER_CAPABILITIES, *PWDF_DEVICE_POWER_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>DeviceD1</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that indicates, if set to <b>WdfTrue</b>, that the device supports device sleeping state D1. For more information about the <b>WDF_TRI_STATE</b> value, see the following Remarks section.</p>
</dd>

### -field <b>DeviceD2</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that indicates, if set to <b>WdfTrue</b>, that the device supports device sleeping state D2. </p>
</dd>

### -field <b>WakeFromD0</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that indicates, if set to <b>WdfTrue</b>, that the device can respond to a wake signal while in its D0 state. </p>
</dd>

### -field <b>WakeFromD1</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that indicates, if set to <b>WdfTrue</b>, that the device can respond to a wake signal while in its D1 state. </p>
</dd>

### -field <b>WakeFromD2</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that indicates, if set to <b>WdfTrue</b>, that the device can respond to a wake signal while in its D2 state. </p>
</dd>

### -field <b>WakeFromD3</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that indicates, if set to <b>WdfTrue</b>, that the device can respond to a wake signal while in its D3 state. </p>
</dd>

### -field <b>DeviceState</b>

<dd>
<p>An array of DEVICE_POWER_STATE-typed values that indicates the most-powered device state that the device supports for each system power state. This array uses the SYSTEM_POWER_STATE enumeration as index values. If an array element's value is <b>PowerDeviceMaximum</b>, the framework uses whatever value that the operating system has stored for that element. The DEVICE_POWER_STATE and SYSTEM_POWER_STATE enumerations are defined in <i>wdm.h</i>. For more information about the <b>DeviceState</b> member, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543087">DeviceState</a>.</p>
</dd>

### -field <b>DeviceWake</b>

<dd>
<p>A DEVICE_POWER_STATE-typed value that indicates the lowest device power state from which the device can send a wake signal to the system. If this value is <b>PowerDeviceMaximum</b>, the framework uses whatever value is currently stored in the system for this member. </p>
</dd>

### -field <b>SystemWake</b>

<dd>
<p>A SYSTEM_POWER_STATE-typed value that indicates the lowest system power state from which the device can send a wake signal to the system. If this value is <b>PowerSystemMaximum</b>, the framework uses whatever value is currently stored in the system for this member. SYSTEM_POWER_STATE values are defined in <i>wdm.h</i>.</p>
</dd>

### -field <b>D1Latency</b>

<dd>
<p>The approximate time, in 100-nanosecond units, that the device requires to return to its D0 state from its D1 state. If this value is -1, the framework uses whatever value is currently stored in the system for this member. </p>
</dd>

### -field <b>D2Latency</b>

<dd>
<p>The approximate time, in 100-nanosecond units, that the device requires to return to its D0 state from its D2 state. If this value is -1, the framework uses whatever value is currently stored in the system for this member. </p>
</dd>

### -field <b>D3Latency</b>

<dd>
<p>The approximate time, in 100-nanosecond units, that the device requires to return to its D0 state from its D3 state. If this value is -1, the framework uses whatever value is currently stored in the system for this member. </p>
</dd>

### -field <b>IdealDxStateForSx</b>

<dd>
<p>A DEVICE_POWER_STATE-typed value that indicates the <a href="https://msdn.microsoft.com/f594a63f-10ce-439d-abe3-d342555d98f0">device sleeping state</a> that the device should enter when the system enters any <a href="https://msdn.microsoft.com/2fd883b5-4e89-4ce9-b75a-b821348ac860">system sleeping state</a> and the device is not enabled to wake the system. If this value is zero, the framework uses <b>PowerDeviceD3</b>. This value cannot be <b>PowerDeviceD0</b>.</p>
<p>If a driver specifies an <b>IdealDxStateForSx</b> value that represents a higher-powered device sleeping state than the device's stack has specified in the device's <a href="https://msdn.microsoft.com/library/windows/hardware/ff543087">DeviceState</a> array, the framework uses the lower-powered state that is in the array. For example, if the driver specifies an <b>IdealDxStateForSx</b> value of D1 and the device's <b>DeviceState</b> array specifies D2, the framework uses D2. </p>
</dd>
</dl>

## -remarks
<p>The WDF_DEVICE_POWER_CAPABILITIES structure is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546901">WdfDeviceSetPowerCapabilities</a>.</p>

<p>Several members use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a> type. For these members, the following rules apply:</p>

<p>A value of <b>WdfTrue</b> indicates that the device supports the capability and a value of <b>WdfFalse</b> indicates it does not. </p>

<p>Function drivers and filter drivers can specify <b>WdfTrue</b> or <b>WdfFalse</b>, or a value of <b>WdfUseDefault</b> to indicate that the framework should use the value that was provided by a lower driver in the stack. For example, if a bus driver specifies <b>WdfTrue</b> for <b>DeviceD1</b> and the device's function driver specifies <b>WdfUseDefault</b>, the framework uses <b>WdfTrue</b> for the capability.</p>

<p>When a bus driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546901">WdfDeviceSetPowerCapabilities</a> after it <a href="wdf.creating_device_objects_in_a_bus_driver">creates a device object</a> for a child device, it should specify <b>WdfTrue</b> or <b>WdfFalse</b>. A bus driver can specify <b>WdfUseDefault</b> for a child device, but in this case <b>WdfUseDefault</b> is the same as <b>WdfFalse</b>.</p>

<p>To initialize a WDF_DEVICE_POWER_CAPABILITIES structure, a driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551265">WDF_DEVICE_POWER_CAPABILITIES_INIT</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551257">WDF_DEVICE_PNP_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_POWER_CAPABILITIES structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
