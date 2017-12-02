---
UID: NC.wdm.GET_VIRTUAL_FUNCTION_PROBED_BARS
title: GET_VIRTUAL_FUNCTION_PROBED_BARS
author: windows-driver-content
description: The GetVirtualFunctionProbedBars routine returns the values of the PCI Express (PCIe) Base Address Registers (BARs) of a device that supports the single root I/O virtualization (SR-IOV) interface.
old-location: kernel\getvirtualfunctionprobedbars.htm
old-project: kernel
ms.assetid: 02A86A3E-D543-4F0F-9985-7D42F381F8F1
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
req.alt-api: GetVirtualFunctionProbedBars
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# GET_VIRTUAL_FUNCTION_PROBED_BARS callback



## -description
<p>The <i>GetVirtualFunctionProbedBars</i> routine returns the values of the PCI Express (PCIe) Base Address Registers (BARs) of a device that supports the single root I/O virtualization (SR-IOV) interface. </p>
<p><i>GetVirtualFunctionProbedBars</i> returns the BAR values that were reported by the device after a query that was performed by the PCI bus driver. This query determines the memory or I/O address space that is required by the device.</p>


## -prototype

````
GET_VIRTUAL_FUNCTION_PROBED_BARS GetVirtualFunctionProbedBars;

NTSTATUS GetVirtualFunctionProbedBars(
  _Inout_ PVOID  Context,
  _Out_   PULONG BaseRegisterValues
)
{ ... }
````


## -parameters
<dl>

### -param Context [in, out]

<dd>
<p>A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="..\wdm\ns-wdm--pci-virtualization-interface.md">PCI_VIRTUALIZATION_INTERFACE</a> structure for the interface.</p>
</dd>

### -param BaseRegisterValues [out]

<dd>
<p>A pointer to an array of ULONG values. The <i>GetVirtualFunctionProbedBars</i> routine returns a value for each BAR of the device.</p>
<div class="alert"><b>Note</b>  <i>GetVirtualFunctionProbedBars</i> returns a maximum of <b>PCI_TYPE0_ADDRESSES</b> values within this array.
</div>
<div> </div>
</dd>
</dl>

## -returns
<p>The <i>GetVirtualFunctionProbedBars</i> routine returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The device does not support the SR-IOV interface.</p>

<p> </p>

## -remarks
<p>The PCI bus driver. which runs in the management operating system  of the Hyper-V parent partition, queries the memory or I/O address space requirements of each  BAR of the device. The PCI bus driver performs this query when the it first detects the adapter on the bus. </p>

<p>Through this BAR query, the PCI bus driver determines the following:</p>

<p>Whether a BAR is supported by the device.</p>

<p>If a BAR is supported, how much memory or I/O
address space is required for the BAR.</p>

<p>The PCI driver performs this BAR query as follows:</p>

<p>The PCI bus driver writes 0xFFFFFFFF to a BAR.</p>

<p>The PCI bus driver reads the BAR to determine the memory or address space that the device requires. A value of zero indicates that the device does not support the BAR.</p>

<p>The <i>GetVirtualFunctionProbedBars</i> routine is provided by the <a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface.</p>

<p>The following notes apply to the <i>GetVirtualFunctionProbedBars</i> routine:</p>

<p>The SR-IOV interface does not require that the BARs of a PCIe VF comply with the protocol for determining the size of the memory block or I/O address space of a BAR. Therefore, the virtual PCI (VPCI) driver, which runs in the guest operating system, determines the size by using the equivalent size from the BARs on the physical device. The VPCI driver obtains this information by calling the <i>GetVirtualFunctionProbedBars</i> routine.
</p>

<p>	The VPCI driver requires the size of the memory or I/O
address space for each BAR after the physical device has started. At that point, the PCI driver cannot perform a BAR query  on the device without altering the current value of the BAR. Therefore, when the <i>GetVirtualFunctionProbedBars</i> routine is called by the VPCI driver, the PCI driver returns the BAR information that it obtained during the BAR query. The PCI driver performed this query when the device was first detected on the bus.</p>

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
<p>PASSIVE_LEVEL</p>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20GET_VIRTUAL_FUNCTION_PROBED_BARS routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
