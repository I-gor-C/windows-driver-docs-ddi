---
UID: NI.bthxddi.IOCTL_BTHX_SET_VERSION
title: IOCTL_BTHX_SET_VERSION
author: windows-driver-content
description: IOCTL_BTHX_SET_VERSION is used to inform the transport driver of the version of the extensibility interface being used.
old-location: bltooth\ioctl_bthx_set_version.htm
old-project: bltooth
ms.assetid: FE572606-8F47-4C40-BF74-24D5F667D2EC
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: BTHDDI_SDP_PARSE_INTERFACE, BTHDDI_SDP_PARSE_INTERFACE, *PBTHDDI_SDP_PARSE_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: bthxddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_BTHX_SET_VERSION
req.alt-loc: BthXDDI.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: 
---

# IOCTL_BTHX_SET_VERSION IOCTL



## -description
<p>
<p>IOCTL_BTHX_SET_VERSION is used to inform the transport driver of the version of the extensibility interface being used.</p>
</p>
<p>IOCTL_BTHX_SET_VERSION is used to inform the transport driver of the version of the extensibility interface being used.</p>


## -ioctlparameters

### -input-buffer
<p>Profile drivers should use KMDF and its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550015">WdfRequestRetrieveInputMemory</a> method to retrieve input parameters.  For example, to get the input buffer:</p>

<p><code>Status = WdfRequestRetrieveInputMemory(_Request, &amp;ReqInMemory);</code></p>

<p>The buffer describes a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450838">BTHX_VERSION</a> structure. </p>

<p>Refer to the WDK Bluetooth samples for more information.</p>

### -input-buffer-length
<p>The length of the buffer is the size of the <b>BTHX_VERSION</b> structure.</p>

<p>The length of the buffer is the size of the <b>BTHX_VERSION</b> structure.</p>

### -output-buffer
<p>None.</p>

<p>None.</p>

<p>None.</p>

### -output-buffer-length
<p>None.</p>

<p>None.</p>

<p>None.</p>

<p>None.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to zero because the Bluetooth driver
      stack returns no data with this IOCTL.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to zero because the Bluetooth driver
      stack returns no data with this IOCTL.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to zero because the Bluetooth driver
      stack returns no data with this IOCTL.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to zero because the Bluetooth driver
      stack returns no data with this IOCTL.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to zero because the Bluetooth driver
      stack returns no data with this IOCTL.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

## -remarks
<p>IOCTL_BTHX_SET_VERSION is a synchronous operation.</p>

<p>Only one version will be selected and set.</p>

<p>IOCTL_BTHX_SET_VERSION is a synchronous operation.</p>

<p>Only one version will be selected and set.</p>

<p>IOCTL_BTHX_SET_VERSION is a synchronous operation.</p>

<p>Only one version will be selected and set.</p>

<p>IOCTL_BTHX_SET_VERSION is a synchronous operation.</p>

<p>Only one version will be selected and set.</p>

<p>IOCTL_BTHX_SET_VERSION is a synchronous operation.</p>

<p>Only one version will be selected and set.</p>

<p>IOCTL_BTHX_SET_VERSION is a synchronous operation.</p>

<p>Only one version will be selected and set.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>BthXDDI.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= PASSIVE_LEVEL</p>
</td>
</tr>
</table>