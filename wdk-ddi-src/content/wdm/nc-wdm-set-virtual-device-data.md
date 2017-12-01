---
UID: NC.wdm.SET_VIRTUAL_DEVICE_DATA
title: SET_VIRTUAL_DEVICE_DATA
author: windows-driver-content
description: The SetVirtualFunctionData routine writes data to the PCI Express (PCIe) configuration space of a virtual function (VF) on a device that supports the single root I/O virtualization (SR-IOV) interface.
old-location: kernel\setvirtualfunctiondata.htm
old-project: kernel
ms.assetid: 12CC6973-E691-425E-A8E8-839F83116D29
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in Windows Server 2012 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetVirtualFunctionData
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# SET_VIRTUAL_DEVICE_DATA callback



## -description
<p>The  <i>SetVirtualFunctionData</i> routine writes data to the PCI Express (PCIe) configuration space of a virtual function (VF) on a device that supports the single root I/O virtualization (SR-IOV) interface.</p>


## -prototype

````
SET_VIRTUAL_DEVICE_DATA SetVirtualFunctionData;

ULONG SetVirtualFunctionData(
  _Inout_ PVOID  Context,
  _In_    USHORT VirtualFunction,
  _In_    PVOID  Buffer,
  _In_    ULONG  Offset,
  _In_    ULONG  Length
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in, out]

<dd>
<p>A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="..\wdm\ns-wdm--pci-virtualization-interface.md">PCI_VIRTUALIZATION_INTERFACE</a> structure for the interface.</p>
</dd>

### -param <i>VirtualFunction</i> [in]

<dd>
<p>A zero-based value that specifies the VF on the device from which data is to be written.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to the buffer that contains the configuration information to be written to the PCIe configuration space of the VF.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>The offset into the PCIe configuration space data of the VF. This member specifies where this write operation begins.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length, in bytes, of the data to be written. </p>
</dd>
</dl>

## -returns
<p>The 
      <i>SetVirtualFunctionData</i> routine returns the length, in bytes, of the PCIe configuration data that was written after a successful write operation. If the write operation is unsuccessful, the routine returns zero. </p>

## -remarks
<p>The <i>SetVirtualFunctionData</i> routine is similar to the <a href="..\wdm\nc-wdm-get-set-device-data.md">SetBusData</a> routine, except that it writes PCIe configuration data to a VF instead of to a device's physical function (PF).</p>

<p>The <i>SetVirtualFunctionData</i> routine is provided by the <a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface. The <a href="..\wdm\nc-wdm-get-set-device-data.md">SetBusData</a> routine is provided by the <a href="kernel.guid_bus_interface_standard">GUID_BUS_INTERFACE_STANDARD</a> interface.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2012 and later versions of Windows.</p>
</td>
</tr>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--pci-virtualization-interface.md">PCI_VIRTUALIZATION_INTERFACE</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-get-set-device-data.md">SetBusData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20SET_VIRTUAL_DEVICE_DATA routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
