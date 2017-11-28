---
UID: NC.pcivirt.SRIOV_SET_POWER_STATE
title: SRIOV_SET_POWER_STATE
author: windows-driver-content
description: Sets the power state of the specified PCI Express SR-IOV Virtual Function (VF).
old-location: pci\sriov_set_power_state.htm
old-project: PCI
ms.assetid: d43a21cb-5cee-4e72-8f0c-7aa8b2453507
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRIOV_SET_POWER_STATE
req.alt-loc: Pcivirt.h
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
req.iface: 
---

# SRIOV_SET_POWER_STATE callback



## -description
<p>Sets the power state of the specified PCI Express SR-IOV Virtual Function (VF).</p>


## -prototype

````
NTSTATUS  SRIOV_SET_POWER_STATE(
  _In_ PVOID              Context,
  _In_ USHORT             VfIndex,
  _In_ DEVICE_POWER_STATE PowerState,
  _In_ BOOLEAN            Wake
);
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to a driver-defined context.
                    
                </p>
</dd>

### -param <i>VfIndex</i> [in]

<dd>
<p>A zero-based index of the VF to which this power state set operation applies.</p>
</dd>

### -param <i>PowerState</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a>-type value that indicates the <b>Dx</b> power state to set.</p>
</dd>

### -param <i>Wake</i> [in]

<dd>
<p>A boolean value that indicates whether to arm the device for a wake signal (PME for PCI Express devices), as it goes into the low power state. TRUE  indicates the device is armed; FALSE otherwise. This value must be FALSE if <i>PowerState</i> is <b>PowerDeviceD0</b>.</p>
</dd>
</dl>

## -returns
<p>Set to STATUS_SUCCESS if the request is successful. Otherwise, return appropriate a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code to indicate the error condition. </p>

## -remarks
<p>This callback function is implemented by the physical function (PF) driver. The callback is invoked when the system wants to change the power state of a virtual function. </p>

<p>The PF driver registers its implementation by setting the <b>SetVfPowerState</b> member of the SRIOV_DEVICE_INTERFACE_STANDARD, configuring a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552439">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>.</p>

<p>Here is an example implementation of this callback function.</p>

<p>This callback function is implemented by the physical function (PF) driver. The callback is invoked when the system wants to change the power state of a virtual function. </p>

<p>The PF driver registers its implementation by setting the <b>SetVfPowerState</b> member of the SRIOV_DEVICE_INTERFACE_STANDARD, configuring a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552439">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>.</p>

<p>Here is an example implementation of this callback function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
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
<dt>Pcivirt.h</dt>
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