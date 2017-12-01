---
UID: NS.ucxcontroller._UCX_CONTROLLER_PCI_INFORMATION
title: UCX_CONTROLLER_PCI_INFORMATION
author: windows-driver-content
description: This structure provides information about a PCI USB controller.
old-location: buses\_ucx_controller_pci_information.htm
old-project: usbref
ms.assetid: 178C9423-D7C9-43FD-BC80-A675383BDE9B
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_CONTROLLER_PCI_INFORMATION, UCX_CONTROLLER_PCI_INFORMATION, *PUCX_CONTROLLER_PCI_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_CONTROLLER_PCI_INFORMATION
req.alt-loc: Ucxcontroller.h
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

# UCX_CONTROLLER_PCI_INFORMATION structure



## -description
<p>This structure provides information about a PCI USB controller.</p>


## -syntax

````
typedef struct _UCX_CONTROLLER_PCI_INFORMATION {
  ULONG  VendorId;
  ULONG  DeviceId;
  USHORT RevisionId;
  ULONG  BusNumber;
  ULONG  DeviceNumber;
  ULONG  FunctionNumber;
} UCX_CONTROLLER_PCI_INFORMATION, *P_UCX_CONTROLLER_PCI_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>VendorId</b>

<dd>
<p>The vendor ID for the PCI USB controller.</p>
</dd>

### -field <b>DeviceId</b>

<dd>
<p>The device ID for the PCI USB controller.</p>
</dd>

### -field <b>RevisionId</b>

<dd>
<p>The revision ID for the PCI USB controller.</p>
</dd>

### -field <b>BusNumber</b>

<dd>
<p>Specifies the bus number that identifies the bus instance that a device instance is attached to.</p>
</dd>

### -field <b>DeviceNumber</b>

<dd>
<p>Specifies the device number that is assigned to the logical PCI slot. </p>
</dd>

### -field <b>FunctionNumber</b>

<dd>
<p>Specifies the specific function on the device that is located in the logical PCI slot. </p>
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
<dt>Ucxcontroller.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._ucx_controller_config">UCX_CONTROLLER_CONFIG</a>
</dt>
<dt>
<a href="buses.ucx_controller_parent_bus_type">UCX_CONTROLLER_PARENT_BUS_TYPE</a>
</dt>
<dt>
<a href="buses._ucx_controller_config_set_pci_info">UCX_CONTROLLER_CONFIG_SET_PCI_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_CONTROLLER_PCI_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
