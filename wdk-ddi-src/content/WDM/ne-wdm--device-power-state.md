---
UID: NE.wdm._DEVICE_POWER_STATE
title: DEVICE_POWER_STATE
author: windows-driver-content
description: The DEVICE_POWER_STATE enumeration type indicates a device power state.
old-location: kernel\device_power_state.htm
ms.assetid: d3166685-2aec-4874-a5a9-8cc293a96a2c
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_POWER_STATE
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
req.iface: 
req.product: Windows 10 or later.
---

# DEVICE_POWER_STATE enumeration



## -description
<p>The <b>DEVICE_POWER_STATE</b> enumeration type indicates a <a href="https://msdn.microsoft.com/2229f34c-9b88-4e3e-802e-f7be2c7ef168">device power state</a>. </p>


## -syntax

````
typedef enum _DEVICE_POWER_STATE { 
  PowerDeviceUnspecified  = 0,
  PowerDeviceD0           = 1,
  PowerDeviceD1           = 2,
  PowerDeviceD2           = 3,
  PowerDeviceD3           = 4,
  PowerDeviceMaximum      = 5
} DEVICE_POWER_STATE, *PDEVICE_POWER_STATE;
````


## -enum-fields
<dl>

### -field <a id="PowerDeviceUnspecified"></a><a id="powerdeviceunspecified"></a><a id="POWERDEVICEUNSPECIFIED"></a><b>PowerDeviceUnspecified</b>

<dd>
<p>Indicates an unspecified device power state. </p>
</dd>

### -field <a id="PowerDeviceD0"></a><a id="powerdeviced0"></a><a id="POWERDEVICED0"></a><b>PowerDeviceD0</b>

<dd>
<p>Indicates a maximum device power state, which corresponds to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543210">device working state D0</a>. </p>
</dd>

### -field <a id="PowerDeviceD1"></a><a id="powerdeviced1"></a><a id="POWERDEVICED1"></a><b>PowerDeviceD1</b>

<dd>
<p>Indicates a <a href="https://msdn.microsoft.com/f594a63f-10ce-439d-abe3-d342555d98f0">device sleeping state</a> less than <b>PowerDeviceD0</b> and greater than <b>PowerDeviceD2</b>, which corresponds to device power state D1.</p>
</dd>

### -field <a id="PowerDeviceD2"></a><a id="powerdeviced2"></a><a id="POWERDEVICED2"></a><b>PowerDeviceD2</b>

<dd>
<p>Indicates a device sleeping state less than <b>PowerDeviceD1</b> and greater than <b>PowerDeviceD3</b>, which corresponds to device power state D2. </p>
</dd>

### -field <a id="PowerDeviceD3"></a><a id="powerdeviced3"></a><a id="POWERDEVICED3"></a><b>PowerDeviceD3</b>

<dd>
<p>Indicates the lowest-powered device sleeping state, which corresponds to device power state D3.</p>
</dd>

### -field <a id="PowerDeviceMaximum"></a><a id="powerdevicemaximum"></a><a id="POWERDEVICEMAXIMUM"></a><b>PowerDeviceMaximum</b>

<dd>
<p>The number of device power state values for this enumeration type that represent actual power states. The value of the other device power states is less than this value. </p>
</dd>
</dl>

## -remarks
<p>A power state indicates the level of power consumption—and thus the extent of computing activity—by the system or by a single device. The power manager sets the power state of the system as a whole, where the system power state is indicated by one of the values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564565">SYSTEM_POWER_STATE</a> enumeration type. Device drivers set the power state of their individual devices, where the device power state is indicated by one of the values of the <b>DEVICE_POWER_STATE</b> enumeration type.</p>

<p>For more information about system power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546941">Handling System Power State Requests</a>. For more information about device power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554397">Managing Power for Individual Devices</a>. For more information about power management in general, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548108">Introduction to Power Management</a>. </p>

<p>A power state indicates the level of power consumption—and thus the extent of computing activity—by the system or by a single device. The power manager sets the power state of the system as a whole, where the system power state is indicated by one of the values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564565">SYSTEM_POWER_STATE</a> enumeration type. Device drivers set the power state of their individual devices, where the device power state is indicated by one of the values of the <b>DEVICE_POWER_STATE</b> enumeration type.</p>

<p>For more information about system power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546941">Handling System Power State Requests</a>. For more information about device power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554397">Managing Power for Individual Devices</a>. For more information about power management in general, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548108">Introduction to Power Management</a>. </p>

<p>A power state indicates the level of power consumption—and thus the extent of computing activity—by the system or by a single device. The power manager sets the power state of the system as a whole, where the system power state is indicated by one of the values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564565">SYSTEM_POWER_STATE</a> enumeration type. Device drivers set the power state of their individual devices, where the device power state is indicated by one of the values of the <b>DEVICE_POWER_STATE</b> enumeration type.</p>

<p>For more information about system power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546941">Handling System Power State Requests</a>. For more information about device power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554397">Managing Power for Individual Devices</a>. For more information about power management in general, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548108">Introduction to Power Management</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564565">SYSTEM_POWER_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DEVICE_POWER_STATE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
