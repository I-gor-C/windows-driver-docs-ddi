---
UID: NF.wdfdevice.WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT
title: WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT
author: windows-driver-content
description: The WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT function initializes a driver's WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS structure.
old-location: wdf\wdf_device_power_policy_wake_settings_init.htm
old-project: wdf
ms.assetid: bb712c92-c926-4a7a-a126-db4db3bc728f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT
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
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT</b> function initializes a driver's <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-wake-settings.md">WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS</a> structure.</p>


## -syntax

````
VOID WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT(
  _Out_ PWDF_DEVICE_POWER_POLICY_WAKE_SETTINGS Settings
);
````


## -parameters
<dl>

### -param Settings [out]

<dd>
<p>A pointer to a driver-allocated <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-wake-settings.md">WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT</b> function zeros the specified <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-wake-settings.md">WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS</a> structure and sets the structure's <b>Size</b> member. Then the function sets the structure's <b>Enabled</b> member to <b>WdfUseDefault</b>, sets the <b>DxState</b> member to <b>PowerDeviceMaximum</b>, and sets the <b>UserControlOfWakeSettings</b> member to <b>WakeAllowUserControl</b>.</p>

<p>For a code example that uses <b>WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT</b>, see <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceassignsxwakesettings.md">WdfDeviceAssignSxWakeSettings</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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