---
UID: NC.video.PVIDEO_HW_LEGACYRESOURCES
title: PVIDEO_HW_LEGACYRESOURCES
author: windows-driver-content
description: HwVidLegacyResources returns a list of resources that are not listed in a device's PCI configuration space but that are decoded by the device.
old-location: display\hwvidlegacyresources.htm
ms.assetid: 015086e9-70b4-4756-9945-c9da17829e90
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HwVidLegacyResources
req.alt-loc: video.h
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
ms.keywords: VHF_CONFIG, VHF_CONFIG, *PVHF_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# PVIDEO_HW_LEGACYRESOURCES callback



## -description
<p><i>HwVidLegacyResources </i>returns a list of resources that are not listed in a device's PCI configuration space but that are decoded by the device.</p>


## -prototype

````
PVIDEO_HW_LEGACYRESOURCES HwVidLegacyResources;

VOID HwVidLegacyResources(
  _In_    ULONG               VendorId,
  _In_    ULONG               DeviceId,
  _Inout_ PVIDEO_ACCESS_RANGE *LegacyResourceList,
  _Inout_ PULONG              LegacyResourceCount
)
{ ... }
````


## -parameters
<dl>

### -param <i>VendorId</i> [in]

<dd>
<p>Specifies a code that identifies the device's vendor. This is the vendor ID specified in the device's PCI configuration space. For more information, see <a href="NULL">Identifiers for PCI Devices</a>.</p>
</dd>

### -param <i>DeviceId</i> [in]

<dd>
<p>Specifies a code that identifies the particular device. This is the device ID specified in the device's PCI configuration space.</p>
</dd>

### -param <i>LegacyResourceList</i> [in, out]

<dd>
<p>Pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff570498">VIDEO_ACCESS_RANGE</a> structures. Each structure describes a device I/O port or memory range for the graphics adapter that is not listed in PCI configuration space. </p>
</dd>

### -param <i>LegacyResourceCount</i> [in, out]

<dd>
<p>Is the number of elements in the array to which <i>LegacyResourceList</i> points.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Legacy resources are those resources that are not listed in the device's PCI configuration space but that are decoded by the device. If the legacy resource list for the device is not known at compile time, a miniport driver should implement a <i>HwVidLegacyResources </i> function and initialize the <b>HwGetLegacyResources</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a> to point to this function. For example, a miniport driver that supports two devices with different sets of legacy resources would implement <i>HwVidLegacyResources </i> to report the legacy resources for a particular device at run time.</p>

<p>The resources returned by <i>HwVidLegacyResources </i> are added to the list of resources that PnP reserves for the device.</p>

<p><i>HwVidLegacyResources</i> should be made pageable.</p>

<p>Legacy resources are those resources that are not listed in the device's PCI configuration space but that are decoded by the device. If the legacy resource list for the device is not known at compile time, a miniport driver should implement a <i>HwVidLegacyResources </i> function and initialize the <b>HwGetLegacyResources</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a> to point to this function. For example, a miniport driver that supports two devices with different sets of legacy resources would implement <i>HwVidLegacyResources </i> to report the legacy resources for a particular device at run time.</p>

<p>The resources returned by <i>HwVidLegacyResources </i> are added to the list of resources that PnP reserves for the device.</p>

<p><i>HwVidLegacyResources</i> should be made pageable.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PVIDEO_HW_LEGACYRESOURCES callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
