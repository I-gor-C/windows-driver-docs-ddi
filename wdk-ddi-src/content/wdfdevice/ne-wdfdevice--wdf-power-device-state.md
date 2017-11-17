---
UID: NE.wdfdevice._WDF_POWER_DEVICE_STATE
title: WDF_POWER_DEVICE_STATE
author: windows-driver-content
description: The WDF_POWER_DEVICE_STATE enumeration identifies the device power states that a device might support.
old-location: wdf\wdf_power_device_state.htm
ms.assetid: 66ff00fd-43b0-4fe1-a010-4b5ef65fa811
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_POWER_DEVICE_STATE
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
req.irql: PASSIVE_LEVEL
ms.keywords: WDF_REL_TIMEOUT_IN_US
req.iface: 
req.product: Windows 10 or later.
---

# WDF_POWER_DEVICE_STATE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_POWER_DEVICE_STATE</b> enumeration identifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543162">device power states</a> that a device might support.</p>


## -syntax

````
typedef enum _WDF_POWER_DEVICE_STATE { 
  WdfPowerDeviceInvalid                = 0,
  WdfPowerDeviceD0                     = 1,
  WdfPowerDeviceD1                     = 2,
  WdfPowerDeviceD2                     = 3,
  WdfPowerDeviceD3                     = 4,
  WdfPowerDeviceD3Final                = 5,
  WdfPowerDevicePrepareForHibernation  = 6,
  WdfPowerDeviceMaximum                = 7
} WDF_POWER_DEVICE_STATE, *PWDF_POWER_DEVICE_STATE;
````


## -enum-fields
<dl>

### -field <a id="WdfPowerDeviceInvalid"></a><a id="wdfpowerdeviceinvalid"></a><a id="WDFPOWERDEVICEINVALID"></a><b>WdfPowerDeviceInvalid</b>

<dd>
<p>The device power state is invalid or unknown.</p>
</dd>

### -field <a id="WdfPowerDeviceD0"></a><a id="wdfpowerdeviced0"></a><a id="WDFPOWERDEVICED0"></a><b>WdfPowerDeviceD0</b>

<dd>
<p>The D0 device power state.</p>
</dd>

### -field <a id="WdfPowerDeviceD1"></a><a id="wdfpowerdeviced1"></a><a id="WDFPOWERDEVICED1"></a><b>WdfPowerDeviceD1</b>

<dd>
<p>The D1 device power state.</p>
</dd>

### -field <a id="WdfPowerDeviceD2"></a><a id="wdfpowerdeviced2"></a><a id="WDFPOWERDEVICED2"></a><b>WdfPowerDeviceD2</b>

<dd>
<p>The D2 device power state.</p>
</dd>

### -field <a id="WdfPowerDeviceD3"></a><a id="wdfpowerdeviced3"></a><a id="WDFPOWERDEVICED3"></a><b>WdfPowerDeviceD3</b>

<dd>
<p>The D3 device power state.</p>
</dd>

### -field <a id="WdfPowerDeviceD3Final"></a><a id="wdfpowerdeviced3final"></a><a id="WDFPOWERDEVICED3FINAL"></a><b>WdfPowerDeviceD3Final</b>

<dd>
<p>Represents the final time that the device enters the D3 device power state. Typically, this enumerator means that the system is being turned off, the device is about to be removed, or a <a href="wdf.the_pnp_manager_redistributes_system_resources">resource rebalance</a> is in progress. The device might have been already removed.</p>
</dd>

### -field <a id="WdfPowerDevicePrepareForHibernation"></a><a id="wdfpowerdeviceprepareforhibernation"></a><a id="WDFPOWERDEVICEPREPAREFORHIBERNATION"></a><b>WdfPowerDevicePrepareForHibernation</b>

<dd>
<p>The device supports hibernation files, and the system is ready to hibernate by entering <a href="https://msdn.microsoft.com/2fd883b5-4e89-4ce9-b75a-b821348ac860">system state S4</a>. The driver must not turn off the device. For more information, see <a href="wdf.supporting_special_files">Supporting Special Files</a>.</p>
</dd>

### -field <a id="WdfPowerDeviceMaximum"></a><a id="wdfpowerdevicemaximum"></a><a id="WDFPOWERDEVICEMAXIMUM"></a><b>WdfPowerDeviceMaximum</b>

<dd>
<p>The maximum enumerator value for this enumeration.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/0cfabb0f-2d5e-4445-8683-d2916de5b549">EvtDeviceD0Entry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/bc3af732-f9ab-43a4-bc6f-7fa0b4c05a66">EvtDeviceD0Exit</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_POWER_DEVICE_STATE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
