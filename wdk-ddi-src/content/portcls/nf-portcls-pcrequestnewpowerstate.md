---
UID: NF.portcls.PcRequestNewPowerState
title: PcRequestNewPowerState
author: windows-driver-content
description: The PcRequestNewPowerState function is used to request a new power state for the device. This function is typically not needed by adapter drivers but can occasionally be useful in working around some kinds of hardware problems.
old-location: audio\pcrequestnewpowerstate.htm
old-project: audio
ms.assetid: fbe2c665-a7e8-43e4-95e5-a7e87521e163
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcRequestNewPowerState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcRequestNewPowerState function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcRequestNewPowerState
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PcRequestNewPowerState function



## -description
<p>The <b>PcRequestNewPowerState</b> function is used to request a new power state for the device. This function is typically not needed by adapter drivers but can occasionally be useful in working around some kinds of hardware problems.</p>


## -syntax

````
NTSTATUS PcRequestNewPowerState(
  _In_ PDEVICE_OBJECT     pDeviceObject,
  _In_ DEVICE_POWER_STATE RequestedNewState
);
````


## -parameters
<dl>

### -param <i>pDeviceObject</i> [in]

<dd>
<p>Pointer to the adapter's <a href="wdkgloss.f#wdkgloss.functional_device_object__fdo_#wdkgloss.functional_device_object__fdo_"><i>functional device object (FDO)</i></a>. This parameter must point to a system structure of type <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>.</p>
</dd>

### -param <i>RequestedNewState</i> [in]

<dd>
<p>Specifies the device power state being requested. Set this parameter to one of the following DEVICE_POWER_STATE enumeration values: <b>PowerDeviceD0</b>, <b>PowerDeviceD1</b>, <b>PowerDeviceD2</b>, or <b>PowerDeviceD3</b>.</p>
</dd>
</dl>

## -returns
<p><b>PcRequestNewPowerState</b> returns STATUS_SUCCESS if the call was successful. Otherwise, returns an appropriate error message.</p>

## -remarks
<p>An adapter driver can call <b>PcRequestNewPowerState</b> to compensate for hardware design flaws. For example, if the functions in an audio adapter are not mutually independent and need to be shut down in a particular order, the adapter can call <b>PcRequestNewPowerState</b> to ensure that a particular subdevice is shut down first.</p>

<p>The <b>RequestedNewState</b> parameter can be set to one of the DEVICE_POWER_STATE enumeration values in the following table.</p>

<p><b>PowerDeviceD0</b></p>

<p>Full power state</p>

<p><b>PowerDeviceD1</b></p>

<p>The sleep state with the lowest power-up latency</p>

<p><b>PowerDeviceD2</b></p>

<p>A medium-latency sleep state</p>

<p><b>PowerDeviceD3</b></p>

<p>A full hibernation state and the sleep state with the longest power-up latency</p>

<p>The hardware can be accessed only in power state <b>PowerDeviceD0</b>. In any other state, the driver must cache any attempted hardware accesses and defer those accesses until the <b>PowerDeviceD0</b> state is restored.</p>

<p>For more information, see <a href="NULL">Power Management for Audio Devices</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>The PortCls system driver implements the PcRequestNewPowerState function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcRequestNewPowerState function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
