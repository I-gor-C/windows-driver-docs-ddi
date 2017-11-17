---
UID: NF.wdm.PoFxSetTargetDripsDevicePowerState
title: PoFxSetTargetDripsDevicePowerState
author: windows-driver-content
description: This routine is called to notify the power manager of the device's target device power state for DRIPS. The driver can override the DRIPS constraint provided by the PEP.
old-location: kernel\pofxsettargetdripsdevicepowerstate.htm
ms.assetid: 435c0731-101c-498b-9041-904001be3f2c
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxSetTargetDripsDevicePowerState
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode)
req.irql: PASSIVE_LEVEL
ms.keywords: PoFxSetTargetDripsDevicePowerState
req.iface: 
req.product: Windows 10 or later.
---

# PoFxSetTargetDripsDevicePowerState function



## -description
<p>    This routine is called to notify the power manager of the device's target
    device power state for DRIPS.  The driver can override the
    DRIPS constraint provided by the PEP.  </p>


## -syntax

````
NTSTATUS  PoFxSetTargetDripsDevicePowerState(
  _In_ POHANDLE           Handle,
  _In_ DEVICE_POWER_STATE TargetState
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>A handle that represents the registration of the device with PoFx. The device driver previously received this handle from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a> routine.</p>
</dd>

### -param <i>TargetState</i> [in]

<dd>
<p>Specifies the target DRIPS device power state. Possible values are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a> enumeration. This value must
    be lower than the existing device constraint.  A device power state
    of <b>PowerDeviceUnspecified</b> resets to the PEP provided constraint.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the target state was accepted.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe (kernel mode)</dt>
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