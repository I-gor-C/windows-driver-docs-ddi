---
UID: NF.video.VideoPortCheckForDeviceExistence
title: VideoPortCheckForDeviceExistence
author: windows-driver-content
description: The VideoPortCheckForDeviceExistence function determines whether the specified PCI device exists in the system.
old-location: display\videoportcheckfordeviceexistence.htm
old-project: display
ms.assetid: 2e0480a5-39d3-4977-9c0f-508bcf6c29a8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortCheckForDeviceExistence
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortCheckForDeviceExistence
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

# VideoPortCheckForDeviceExistence function



## -description
<p>The <b>VideoPortCheckForDeviceExistence</b> function determines whether the specified PCI device exists in the system.</p>


## -syntax

````
BOOLEAN VideoPortCheckForDeviceExistence(
  _In_ PVOID  HwDeviceExtension,
  _In_ USHORT VendorId,
  _In_ USHORT DeviceId,
  _In_ UCHAR  RevisionId,
  _In_ USHORT SubVendorId,
  _In_ USHORT SubSystemId,
  _In_ ULONG  Flags
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>VendorId</i> [in]

<dd>
<p>Specifies the vendor ID.</p>
</dd>

### -param <i>DeviceId</i> [in]

<dd>
<p>Specifies the device ID.</p>
</dd>

### -param <i>RevisionId</i> [in]

<dd>
<p>Specifies the revision ID.</p>
</dd>

### -param <i>SubVendorId</i> [in]

<dd>
<p>Specifies the subvendor ID.</p>
</dd>

### -param <i>SubSystemId</i> [in]

<dd>
<p>Specifies the subsystem ID.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Is a set of flags that determine whether the <i>RevisionID</i> and <i>SubSystemID</i> parameters should be used in checking for the new device. This parameter can be the logical OR of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>CDE_USE_REVISION</p>
</td>
<td>
<p>Use the value in the <i>RevisionID</i> parameter in checking for the new device.</p>
</td>
</tr>
<tr>
<td>
<p>CDE_USE_SUBSYSTEM_IDS</p>
</td>
<td>
<p>Use the value in the <i>SubSystemID</i> parameter in checking for the new device.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>VideoPortCheckForDeviceExistence</b> returns <b>TRUE</b> if the device exists in the system, and <b>FALSE</b> otherwise.</p>

## -remarks
<p>For more information about PCI identifiers, see <a href="NULL">Identifiers for PCI Devices</a>. </p>

<p>For more information about PCI identifiers, see <a href="NULL">Identifiers for PCI Devices</a>. </p>

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
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
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