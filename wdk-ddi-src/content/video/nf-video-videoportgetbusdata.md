---
UID: NF.video.VideoPortGetBusData
title: VideoPortGetBusData function
author: windows-driver-content
description: The VideoPortGetBusData function returns bus-type-specific configuration information.
old-location: display\videoportgetbusdata.htm
old-project: display
ms.assetid: ebc5e74f-82ba-4c19-8dae-3ebe8c843fd2
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: VideoPortGetBusData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortGetBusData
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# VideoPortGetBusData function



## -description
The <b>VideoPortGetBusData</b> function returns bus-type-specific configuration information.


## -syntax

````
ULONG VideoPortGetBusData(
        PVOID         HwDeviceExtension,
        BUS_DATA_TYPE BusDataType,
        ULONG         SlotNumber,
  _Out_ PVOID         Buffer,
        ULONG         Offset,
        ULONG         Length
);
````


## -parameters

### -param HwDeviceExtension 

Pointer to the miniport driver's device extension.

### -param BusDataType 

Specifies the type of bus configuration data to return. The value of this parameter can be <b>Cmos</b>, <b>EisaConfiguration</b>, or <b>PCIConfiguration</b>. However, additional types of bus configuration might be supported in the future. The upper bound on the types supported is always <b>MaximumBusDataType</b>.

### -param SlotNumber 

Specifies the location of the device on the bus for a <b>Cmos </b><i>BusDataType</i>; zero for all other bus types.

### -param Buffer [out]

Pointer to a buffer into which <b>VideoPortGetBusData</b> returns the configuration information. The contents of the buffer depend on the <i>BusDataType</i>, as follows:
<ul>
<li>
If <b>Cmos</b> is specified, the buffer contains the contents of the CMOS (bus number equals zero) or ECMOS (bus number equals one) locations, starting with the location specified for <i>SlotNumber</i>. A miniport driver's <a href="..\video\nc-video-pvideo_hw_find_adapter.md">HwVidFindAdapter</a> function can determine the number of the bus from the <b>SystemIoBusNumber</b> member of the <a href="display.video_port_config_info">VIDEO_PORT_CONFIG_INFO</a> input structure.
</li>
<li>
If <b>EisaConfiguration</b> is specified, the buffer contains the <a href="kernel.cm_eisa_slot_information">CM_EISA_SLOT_INFORMATION</a> structure, followed by zero or more <a href="kernel.cm_eisa_function_information">CM_EISA_FUNCTION_INFORMATION</a> structures for the specified slot.
</li>
<li>
If <b>PCIConfiguration</b> is specified, the buffer contains the <a href="kernel.pci_common_config">PCI_COMMON_CONFIG</a> information for the specified slot.
</li>
</ul>

### -param Offset 

Specifies the offset, in bytes, into the PCI configuration space that should be retrieved If <i>BusDataType</i> is <b>PCIConfiguration</b>; otherwise zero. See <b>Remarks</b> for more information.

### -param Length 

Specifies the length, in bytes, of <i>Buffer</i>.

## -returns
<b>VideoPortGetBusData</b> returns the number of bytes of configuration information it has written in <i>Buffer</i>. If the given <i>BusDataType</i> is not valid for the current platform, this function generally returns zero.
<dl>
<dt><b>0</b></dt>
</dl>The PCI bus does not exist.
<dl>
<dt><b>2</b></dt>
</dl>The PCI bus exists, but <i>Buffer</i> contains the value PCI_INVALID_VENDOR_ID at the PCI_COMMON_CONFIG <b>VendorId</b> member.

 

## -remarks
To obtain only a part of the configuration information, the miniport driver should set <i>Offset</i> to the byte offset of the information needed, and set <i>Length</i> to the number of bytes of the information needed. For example, if only the command register is needed, set <i>Offset</i> to the offset of this register, and set <i>Length</i> to <b>sizeof</b>(USHORT).

The driver should call <a href="display.videoportgetaccessranges">VideoPortGetAccessRanges</a> rather than <b>VideoPortGetBusData</b> to retrieve its hardware resources. 

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
Available in Windows 2000 and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
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
<dt>
<a href="kernel.cm_eisa_function_information">CM_EISA_FUNCTION_INFORMATION</a>
</dt>
<dt>
<a href="kernel.cm_eisa_slot_information">CM_EISA_SLOT_INFORMATION</a>
</dt>
<dt>
<a href="..\video\nc-video-pminiport_query_device_routine.md">HwVidQueryDeviceCallback</a>
</dt>
<dt>
<a href="kernel.pci_common_config">PCI_COMMON_CONFIG</a>
</dt>
<dt>
<a href="kernel.pci_slot_number">PCI_SLOT_NUMBER</a>
</dt>
<dt>
<a href="display.video_port_config_info">VIDEO_PORT_CONFIG_INFO</a>
</dt>
<dt>
<a href="display.videoportgetaccessranges">VideoPortGetAccessRanges</a>
</dt>
<dt>
<a href="display.videoportgetdevicebase">VideoPortGetDeviceBase</a>
</dt>
<dt>
<a href="display.videoportgetdevicedata">VideoPortGetDeviceData</a>
</dt>
<dt>
<a href="display.videoportgetregistryparameters">VideoPortGetRegistryParameters</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortGetBusData function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
