---
UID: NS.pcivirt._MITIGABLE_DEVICE_INTERFACE
title: MITIGABLE_DEVICE_INTERFACE
author: windows-driver-content
description: Stores function pointers to callback functions implemented by the physical function (PF) driver for the mitigable device interface.
old-location: pci\mitigable_device_interface.htm
ms.assetid: 1fac7c03-2a48-4b29-951d-c777fbec7dd3
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
req.alt-api: MITIGABLE_DEVICE_INTERFACE
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
ms.keywords: MITIGABLE_DEVICE_INTERFACE, MITIGABLE_DEVICE_INTERFACE, *PMITIGABLE_DEVICE_INTERFACE
req.iface: 
---

# MITIGABLE_DEVICE_INTERFACE structure



## -description
<p>Stores function pointers to callback functions implemented by the physical function (PF) driver  for the mitigable device interface.</p>


## -syntax

````
typedef struct _MITIGABLE_DEVICE_INTERFACE {
  USHORT                         Size;
  USHORT                         Version;
  PVOID                          Context;
  PINTERFACE_REFERENCE           InterfaceReference;
  PINTERFACE_REFERENCE           InterfaceDereference;
  PREAD_WRITE_MITIGATED_REGISTER ReadWriteMitigatedRegister;
} MITIGABLE_DEVICE_INTERFACE, MITIGABLE_DEVICE_INTERFACE;
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

### -field <b>ReadWriteMitigatedRegister</b>

<dd>
<p>Pointer to the driver's implementation of the <a href="buses.read_write_mitigated_register">READ_WRITE_MITIGATED_REGISTER</a> callback function.</p>
</dd>
</dl>

## -remarks
<p>This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to reset a specific virtual function. </p>

<p>The PF driver registers its implementation by setting the <b>ReadVfConfig</b> member of the <a href="buses._sriov_device_interface_standard">SRIOV_DEVICE_INTERFACE_STANDARD</a>, configuring a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552439">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>.</p>

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