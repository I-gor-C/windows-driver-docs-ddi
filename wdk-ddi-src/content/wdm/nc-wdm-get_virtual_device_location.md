---
UID: NC.wdm.GET_VIRTUAL_DEVICE_LOCATION
title: GET_VIRTUAL_DEVICE_LOCATION
author: windows-driver-content
description: The GetLocation routine returns the device location of a PCI Express (PCIe) virtual function (VF) on a PCI bus. A device that supports the single root I/O virtualization (SR-IOV) interface can expose one or more VFs on the PCI bus.
old-location: kernel\getlocation.htm
old-project: kernel
ms.assetid: A08294EC-7A1B-4A2D-A425-D19ABDCB9DCA
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in Windows Server 2012 and later versions of Windows Server.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetLocation
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
req.product: Windows 10 or later.
---

# GET_VIRTUAL_DEVICE_LOCATION callback



## -description
The <i>GetLocation</i> routine returns the device location of a PCI Express (PCIe) virtual function (VF) on a PCI bus. A device that supports the single root I/O virtualization (SR-IOV) interface can expose one or more VFs on the PCI bus.


## -prototype

````
GET_VIRTUAL_DEVICE_LOCATION GetLocation;

NTSTATUS GetLocation(
  _Inout_ PVOID   Context,
  _In_    USHORT  VirtualFunction,
  _Out_   PUINT16 SegmentNumber,
  _Out_   PUINT8  BusNumber,
  _Out_   PUINT8  FunctionNumber
)
{ ... }
````


## -parameters

### -param Context [in, out]

A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="kernel.pci_virtualization_interface">PCI_VIRTUALIZATION_INTERFACE</a> structure for the interface.

### -param VirtualFunction [in]

A zero-based value that specifies the VF on the device for  which the device location is returned

### -param SegmentNumber [out]

A pointer to a caller-supplied variable in which this routine returns a UINT16 value for the current PCI segment number. This value specifies the group of PCI buses on which the device is attached.



### -param BusNumber [out]

A pointer to a caller-supplied variable in which this routine returns a UINT8 value. This value specifies the current PCI bus number on which the device is attached.



### -param FunctionNumber [out]

A pointer to a caller-supplied variable in which this routine returns a UINT8 value.  This value contains the function number for the specified VF on the PCI bus.

## -returns
The <i>GetLocation</i> routine returns one of the following NTSTATUS values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The operation completed successfully.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>The <i>VirtualFunction</i> parameter is larger than the value of the <b>TotalVFs</b> member of the SR-IOV Extended Capability structure for the device.

 

## -remarks
The <i>GetLocation</i> routine returns the current device location of a VF  in the PCIe hierarchy. This information is necessary for a virtualization system that is using an I/O memory management unit (IOMMU) to route traffic to or from the device.

Upon a successful return from a call to the <i>GetLocation</i> routine, the <i>FunctionNumber</i> parameter contains a value that represents the function number for the specified VF on the PCI bus. This value is based on the Alternative Routing Interpretation (ARI) option of the PCI Express 3.0 specification.  ARI treats a PCIe bus as a single device with an 8-bit function space, which allows for 256 functions on the bus.

The <i>GetLocation</i> routine is provided by the <a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported in Windows Server 2012 and later versions of Windows Server.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
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
<a href="kernel.pci_virtualization_interface">PCI_VIRTUALIZATION_INTERFACE</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20GET_VIRTUAL_DEVICE_LOCATION routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>