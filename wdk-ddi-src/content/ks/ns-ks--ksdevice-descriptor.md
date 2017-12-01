---
UID: NS.ks._KSDEVICE_DESCRIPTOR
title: KSDEVICE_DESCRIPTOR
author: windows-driver-content
description: The KSDEVICE_DESCRIPTOR structure describes the characteristics of a particular device.
old-location: stream\ksdevice_descriptor.htm
old-project: stream
ms.assetid: dc68f6d8-a2d5-4940-a708-fe761c3a8a0d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSDEVICE_DESCRIPTOR,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDEVICE_DESCRIPTOR
req.alt-loc: ks.h
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
---

# KSDEVICE_DESCRIPTOR structure



## -description
<p>The KSDEVICE_DESCRIPTOR structure describes the characteristics of a particular device.</p>


## -syntax

````
typedef struct _KSDEVICE_DESCRIPTOR {
  const KSDEVICE_DISPATCH   *Dispatch;
  ULONG                     FilterDescriptorsCount;
  const KSFILTER_DESCRIPTOR *FilterDescriptors;
  ULONG                     Version;
  ULONG                     Flags;
} KSDEVICE_DESCRIPTOR, *PKSDEVICE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Dispatch</b>

<dd>
<p>A pointer to the client dispatch table for this device. This dispatch table contains client dispatch functions for PNP messages such as <b>Add</b>, <b>Start</b>, <b>Stop</b>, <b>Remove</b>. Clients are not required to supply a dispatch table unless they want to receive callbacks for the PNP messages described in the dispatch table. Any member of the dispatch table can be <b>NULL</b> to indicate that the client does not want to receive notification for that particular message. For more information, see <a href="..\ks\ns-ks--ksdevice-dispatch.md">KSDEVICE_DISPATCH</a>.</p>
</dd>

### -field <b>FilterDescriptorsCount</b>

<dd>
<p>This member contains the number of filter descriptors for this device that will be provided in the <b>FilterDescriptors</b> member. Zero is a legal value for this member; clients can create filter factories dynamically with the <a href="..\ks\nf-ks-kscreatefilterfactory.md">KsCreateFilterFactory</a> function instead of statically describing them in the device descriptor.</p>
</dd>

### -field <b>FilterDescriptors</b>

<dd>
<p>A pointer to an array of filter descriptors that describe filters that can be created by this device. This member may be <b>NULL</b> if <b>FilterDescriptorsCount</b> is zero. For more information, see <a href="..\ks\ns-ks--ksfilter-descriptor.md">KSFILTER_DESCRIPTOR</a>.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>A value of type ULONG. This should be one and only one of the values in the following table, or set to zero if writing a pre-version 0x100 driver.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSDEVICE_DESCRIPTOR_VERSION</p>
</td>
<td>
<p>Indicates support of the <a href="stream.avstrminidevicequeryinterface">AVStrMiniDeviceQueryInterface</a> dispatch of <a href="..\ks\ns-ks--ksdevice-dispatch.md">KSDEVICE_DISPATCH</a>.</p>
</td>
</tr>
<tr>
<td>
<p>KSDEVICE_DESCRIPTOR_VERSION_2</p>
</td>
<td>
<p>Indicates support of the <b>Flags</b> member of KSDEVICE_DESCRIPTOR.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A value of type ULONG. There is only one flag currently defined.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSDEVICE_FLAG_ENABLE_REMOTE_WAKEUP</p>
</td>
<td>
<p>Indicates that the device supports remote wakeup.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>Most often, this structure is used in conjunction with <a href="..\ks\nf-ks-ksinitializedriver.md">KsInitializeDriver</a> in the client's <b>DriverEntry</b> function to initialize the device. This structure is also used to manually initialize or create devices with the <a href="..\ks\nf-ks-ksinitializedevice.md">KsInitializeDevice</a> and <a href="..\ks\nf-ks-kscreatedevice.md">KsCreateDevice</a> functions.</p>

<p>If you set <b>Version</b> to KSDEVICE_DESCRIPTOR_VERSION_2 and run your driver on an early version of AVStream that does not support <b>Flags</b>, all flags will be considered to be zero.</p>

<p>Similarly, using an earlier version descriptor on later versions of AVStream causes no flags to be specified.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--ksdevice-dispatch.md">KSDEVICE_DISPATCH</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksfilter-descriptor.md">KSFILTER_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksinitializedriver.md">KsInitializeDriver</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksinitializedevice.md">KsInitializeDevice</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kscreatedevice.md">KsCreateDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSDEVICE_DESCRIPTOR structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
