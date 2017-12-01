---
UID: NS.wdm.CM_Power_Data_s
title: CM_Power_Data_s
author: windows-driver-content
description: The CM_POWER_DATA structure contains information about a device's power management state and capabilities.
old-location: kernel\cm_power_data.htm
old-project: kernel
ms.assetid: 38fea22b-4d9a-4b03-bbb7-c22578f60def
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: CM_Power_Data_s, CM_POWER_DATA, *PCM_POWER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CM_POWER_DATA
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
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# CM_Power_Data_s structure



## -description
<p>The <b>CM_POWER_DATA</b> structure contains information about a device's power management state and capabilities.</p>


## -syntax

````
typedef struct CM_Power_Data_s {
  ULONG              PD_Size;
  DEVICE_POWER_STATE PD_MostRecentPowerState;
  ULONG              PD_Capabilities;
  ULONG              PD_D1Latency;
  ULONG              PD_D2Latency;
  ULONG              PD_D3Latency;
  DEVICE_POWER_STATE PD_PowerStateMapping[POWER_SYSTEM_MAXIMUM];
  SYSTEM_POWER_STATE PD_DeepestSystemWake;
} CM_POWER_DATA, *PCM_POWER_DATA;
````


## -struct-fields
<dl>

### -field <b>PD_Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>PD_MostRecentPowerState</b>

<dd>
<p>A <a href="..\wudfddi\ne-wudfddi--device-power-state.md">DEVICE_POWER_STATE</a> value representing the device's most recent power state.</p>
</dd>

### -field <b>PD_Capabilities</b>

<dd>
<p>The device's power capabilities, represented by a combination of the following bit flags:</p>
<p>PDCAP_D0_SUPPORTED</p>
<p>PDCAP_D1_SUPPORTED</p>
<p>PDCAP_D2_SUPPORTED</p>
<p>PDCAP_D3_SUPPORTED</p>
<p>PDCAP_WAKE_FROM_D0_SUPPORTED</p>
<p>PDCAP_WAKE_FROM_D1_SUPPORTED</p>
<p>PDCAP_WAKE_FROM_D2_SUPPORTED</p>
<p>PDCAP_WAKE_FROM_D3_SUPPORTED</p>
<p>PDCAP_WARM_EJECT_SUPPORTED</p>
</dd>

### -field <b>PD_D1Latency</b>

<dd>
<p>The device's latency when returning the D0 state from the D1 state. For more information, see the <b>D1Latency</b> member of <a href="..\wdm\ns-wdm--device-capabilities.md">DEVICE_CAPABILITIES</a>.</p>
</dd>

### -field <b>PD_D2Latency</b>

<dd>
<p>The device's latency when returning the D0 state from the D2 state. For more information, see the <b>D2Latency</b> member of <b>DEVICE_CAPABILITIES</b>.</p>
</dd>

### -field <b>PD_D3Latency</b>

<dd>
<p>The device's latency when returning the D0 state from the D3 state. For more information, see the <b>D3Latency</b> member of <b>DEVICE_CAPABILITIES</b>.</p>
</dd>

### -field <b>PD_PowerStateMapping</b>

<dd>
<p>An array of <b>DEVICE_POWER_STATE</b> values representing the maximum device power state achievable for each system power state. For more information, see the <b>DeviceState</b> member of <a href="..\wdm\ns-wdm--device-capabilities.md">DEVICE_CAPABILITIES</a>.</p>
</dd>

### -field <b>PD_DeepestSystemWake</b>

<dd>
<p>Specifies the least-powered system state from which the device can wake the system. <b>PD_DeepestSystemWake</b> typically indicates one of the system sleeping states, S1, S2, or S3 (as specified by <b>PowerSystemSleeping1</b>, <b>PowerSystemSleeping2</b>, and <b>PowerSystemSleeping3</b>, respectively). Note, however, that some devices might be able to wake the system from the system hibernate state, S4 (as specified by <b>PowerSystemHibernate</b>), or even from the system shutdown state, S5 (as specified by <b>PowerSystemShutdown</b>). </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--device-capabilities.md">DEVICE_CAPABILITIES</a>
</dt>
<dt>
<a href="..\wudfddi\ne-wudfddi--device-power-state.md">DEVICE_POWER_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551967">SetupDiGetDeviceRegistryProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CM_POWER_DATA structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
