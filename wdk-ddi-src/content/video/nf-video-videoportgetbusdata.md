---
UID: NF.video.VideoPortGetBusData
title: VideoPortGetBusData
author: windows-driver-content
description: The VideoPortGetBusData function returns bus-type-specific configuration information.
old-location: display\videoportgetbusdata.htm
old-project: display
ms.assetid: ebc5e74f-82ba-4c19-8dae-3ebe8c843fd2
ms.author: windowsdriverdev
ms.date: 11/14/2017
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
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortGetBusData function



## -description
<p>The <b>VideoPortGetBusData</b> function returns bus-type-specific configuration information.</p>


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
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>BusDataType</i> 

<dd>
<p>Specifies the type of bus configuration data to return. The value of this parameter can be <b>Cmos</b>, <b>EisaConfiguration</b>, or <b>PCIConfiguration</b>. However, additional types of bus configuration might be supported in the future. The upper bound on the types supported is always <b>MaximumBusDataType</b>.</p>
</dd>

### -param <i>SlotNumber</i> 

<dd>
<p>Specifies the location of the device on the bus for a <b>Cmos </b><i>BusDataType</i>; zero for all other bus types.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Pointer to a buffer into which <b>VideoPortGetBusData</b> returns the configuration information. The contents of the buffer depend on the <i>BusDataType</i>, as follows:</p>
<ul>
<li>
<p>If <b>Cmos</b> is specified, the buffer contains the contents of the CMOS (bus number equals zero) or ECMOS (bus number equals one) locations, starting with the location specified for <i>SlotNumber</i>. A miniport driver's <a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a> function can determine the number of the bus from the <b>SystemIoBusNumber</b> member of the <a href="..\video\ns-video--video-port-config-info.md">VIDEO_PORT_CONFIG_INFO</a> input structure.</p>
</li>
<li>
<p>If <b>EisaConfiguration</b> is specified, the buffer contains the <a href="..\wdm\ns-wdm--cm-eisa-slot-information.md">CM_EISA_SLOT_INFORMATION</a> structure, followed by zero or more <a href="..\wdm\ns-wdm--cm-eisa-function-information.md">CM_EISA_FUNCTION_INFORMATION</a> structures for the specified slot.</p>
</li>
<li>
<p>If <b>PCIConfiguration</b> is specified, the buffer contains the <a href="..\wdm\ns-wdm--pci-common-config.md">PCI_COMMON_CONFIG</a> information for the specified slot.</p>
</li>
</ul>
</dd>

### -param <i>Offset</i> 

<dd>
<p>Specifies the offset, in bytes, into the PCI configuration space that should be retrieved If <i>BusDataType</i> is <b>PCIConfiguration</b>; otherwise zero. See <b>Remarks</b> for more information.</p>
</dd>

### -param <i>Length</i> 

<dd>
<p>Specifies the length, in bytes, of <i>Buffer</i>.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortGetBusData</b> returns the number of bytes of configuration information it has written in <i>Buffer</i>. If the given <i>BusDataType</i> is not valid for the current platform, this function generally returns zero.</p><dl>
<dt><b>0</b></dt>
</dl><p>The PCI bus does not exist.</p><dl>
<dt><b>2</b></dt>
</dl><p>The PCI bus exists, but <i>Buffer</i> contains the value PCI_INVALID_VENDOR_ID at the PCI_COMMON_CONFIG <b>VendorId</b> member.</p>

<p> </p>

## -remarks
<p>To obtain only a part of the configuration information, the miniport driver should set <i>Offset</i> to the byte offset of the information needed, and set <i>Length</i> to the number of bytes of the information needed. For example, if only the command register is needed, set <i>Offset</i> to the offset of this register, and set <i>Length</i> to <b>sizeof</b>(USHORT).</p>

<p>The driver should call <a href="..\video\nf-video-videoportgetaccessranges.md">VideoPortGetAccessRanges</a> rather than <b>VideoPortGetBusData</b> to retrieve its hardware resources. </p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
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
<dt>
<a href="..\wdm\ns-wdm--cm-eisa-function-information.md">CM_EISA_FUNCTION_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--cm-eisa-slot-information.md">CM_EISA_SLOT_INFORMATION</a>
</dt>
<dt>
<a href="..\video\nc-video-pminiport-query-device-routine.md">HwVidQueryDeviceCallback</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--pci-common-config.md">PCI_COMMON_CONFIG</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--pci-slot-number.md">PCI_SLOT_NUMBER</a>
</dt>
<dt>
<a href="..\video\ns-video--video-port-config-info.md">VIDEO_PORT_CONFIG_INFO</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportgetaccessranges.md">VideoPortGetAccessRanges</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportgetdevicebase.md">VideoPortGetDeviceBase</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportgetdevicedata.md">VideoPortGetDeviceData</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportgetregistryparameters.md">VideoPortGetRegistryParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortGetBusData function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
