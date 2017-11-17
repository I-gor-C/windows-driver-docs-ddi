---
UID: NS.pcivirt._SRIOV_DEVICE_INTERFACE_STANDARD_2
title: SRIOV_DEVICE_INTERFACE_STANDARD_2
author: windows-driver-content
description: Stores function pointers to callback functions implemented by the physical function (PF) driver in the device stack for the of the SR-IOV device. This is an extended version of SRIOV_DEVICE_INTERFACE_STANDARD.
old-location: pci\sriov_device_interface_standard_2.htm
ms.assetid: 46c9fa94-283c-481e-9fb1-2ed63df00386
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: PCI
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRIOV_DEVICE_INTERFACE_STANDARD_2
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
ms.keywords: SRIOV_DEVICE_INTERFACE_STANDARD_2, SRIOV_DEVICE_INTERFACE_STANDARD_2, *PSRIOV_DEVICE_INTERFACE_STANDARD_2
req.iface: 
---

# SRIOV_DEVICE_INTERFACE_STANDARD_2 structure



## -description
<p>Stores function pointers to callback functions implemented by the physical function (PF) driver  in the device stack for the of the SR-IOV device. This is an extended version of <a href="buses._sriov_device_interface_standard">SRIOV_DEVICE_INTERFACE_STANDARD</a>. </p>


## -syntax

````
typedef struct _SRIOV_DEVICE_INTERFACE_STANDARD_2 {
  USHORT                           Size;
  USHORT                           Version;
  PVOID                            Context;
  PINTERFACE_REFERENCE             InterfaceReference;
  PINTERFACE_REFERENCE             InterfaceDereference;
  PSRIOV_READ_CONFIG               ReadVfConfig;
  PSRIOV_WRITE_CONFIG              WriteVfConfig;
  PSRIOV_READ_BLOCK                ReadVfConfigBlock;
  PSRIOV_WRITE_BLOCK               WriteVfConfigBlock;
  PSRIOV_QUERY_PROBED_BARS         QueryProbedBars;
  PSRIOV_GET_VENDOR_AND_DEVICE_IDS GetVendorAndDevice;
  PSRIOV_GET_DEVICE_LOCATION       GetDeviceLocation;
  PSRIOV_RESET_FUNCTION            ResetVf;
  PSRIOV_SET_POWER_STATE           SetVfPowerState;
  PSRIOV_GET_RESOURCE_FOR_BAR      GetResourceForBar;
  PSRIOV_QUERY_LUID                QueryLuid;
  PSRIOV_QUERY_PROBED_BARS_2       QueryProbedBars_2;
  PSRIOV_QUERY_VF_LUID             QueryVfLuid;
  PSRIOV_QUERY_LUID_VF             QueryLuidVf;
} SRIOV_DEVICE_INTERFACE_STANDARD_2, SRIOV_DEVICE_INTERFACE_STANDARD_2;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version of this structure</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Driver-defined context passed by the driver.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>Pointer to a routine that increments the number of references to this interface. For more information about this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547833">InterfaceReference</a>. </p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>Pointer to a routine that decrements the number of references to this interface. For more information about this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547829">InterfaceDereference</a>. </p>
</dd>

### -field <b>ReadVfConfig</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/0fef9d53-b8af-4c9b-9914-982bcfc26517">SRIOV_READ_CONFIG</a> callback function that serves as a handler for reading the VF’s configurations space from the non-privileged VM.</p>
</dd>

### -field <b>WriteVfConfig</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/323c8150-ef58-42a4-8c8b-77081ecb64b3">SRIOV_WRITE_CONFIG</a> callback function that serves as a handler for writing the VF’s configuration space from the non-privileged VM.</p>
</dd>

### -field <b>ReadVfConfigBlock</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/af0d3465-2854-47d9-a6a4-06f510229a59">SRIOV_READ_BLOCK</a> callback function that serves as a handler for reading blocks of configuration data from the non-privileged VM.</p>
</dd>

### -field <b>WriteVfConfigBlock</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/da47d601-2fab-49bb-b669-909a2e5c95c0">SRIOV_WRITE_BLOCK</a> callback function that serves as a handler for writing blocks of configuration data from the non-privileged VM..</p>
</dd>

### -field <b>QueryProbedBars</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/422a9212-7227-4508-8f06-0056349fa835">SRIOV_QUERY_PROBED_BARS</a> callback function that allows a non-privileged VM to determine the value of the VF’s Base Address Registers if the value of -1 previously is written.</p>
</dd>

### -field <b>GetVendorAndDevice</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/d08bbaea-6f2b-49ef-bb8b-c1fe357e1c90">SRIOV_GET_VENDOR_AND_DEVICE_IDS</a> callback function that supplies the values from which the Plug and Play IDs for device is derived.</p>
</dd>

### -field <b>GetDeviceLocation</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/705b52e3-f695-4c58-9ae2-5a806f1e2140">SRIOV_GET_DEVICE_LOCATION</a> callback function that allows the a non-privileged VM to determine the bus to which the device is attached.</p>
</dd>

### -field <b>ResetVf</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/30c01528-8254-431f-aaba-79c05f66fc00">SRIOV_RESET_FUNCTION</a> callback function that causes the VF to be reset.</p>
</dd>

### -field <b>SetVfPowerState</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/d43a21cb-5cee-4e72-8f0c-7aa8b2453507">SRIOV_SET_POWER_STATE</a> callback function that serves as a handle for changing the device’s power state from the non-privileged VM.</p>
</dd>

### -field <b>GetResourceForBar</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/b52bafee-d541-4396-be0a-06956d07fb2b">SRIOV_GET_RESOURCE_FOR_BAR</a> callback function that gets the translated resource for a specific BAR.</p>
</dd>

### -field <b>QueryLuid</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/9bb8e54f-b42a-4f61-a3f5-6972141c8f28">SRIOV_QUERY_LUID</a> callback function that gets the unique identifier of the VF.</p>
</dd>

### -field <b>QueryProbedBars_2</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/e0c079aa-8adf-42c9-a4ac-bfc623471964">SRIOV_QUERY_PROBED_BARS_2</a> callback function.</p>
</dd>

### -field <b>QueryVfLuid</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/17fe6e28-59ce-4678-8268-b49cef09a3db">SRIOV_QUERY_VF_LUID</a> callback function that gets the unique identifier of the VF.</p>
</dd>

### -field <b>QueryLuidVf</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/00dddc92-08d1-4eaa-b3de-5e96c7a6d3e0">SRIOV_QUERY_LUID_VF</a> callback function that gets VF index for the specified unique identifier.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>