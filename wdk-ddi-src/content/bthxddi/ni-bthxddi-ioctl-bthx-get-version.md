---
UID: NI.bthxddi.IOCTL_BTHX_GET_VERSION
title: IOCTL_BTHX_GET_VERSION
author: windows-driver-content
description: Profile drivers use IOCTL_BTHX_GET_VERSION to get the version supported by the transport driver.
old-location: bltooth\ioctl_bthx_get_version.htm
old-project: bltooth
ms.assetid: F4FD760B-551C-4738-A13D-444E08215D59
ms.author: windowsdriverdev
ms.date: 11/27/2017
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
req.alt-api: IOCTL_BTHX_GET_VERSION
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

# IOCTL_BTHX_GET_VERSION IOCTL



## -description
<p>
<p>Profile drivers use IOCTL_BTHX_GET_VERSION to get the version supported by the transport driver.</p>
</p>
<p>Profile drivers use IOCTL_BTHX_GET_VERSION to get the version supported by the transport driver.</p>


## -ioctlparameters

### -input-buffer
<p>None.</p>

### -input-buffer-length
<p>None.</p>

<p>None.</p>

### -output-buffer
<p>Profile drivers should use KMDF and its <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputmemory.md">WdfRequestRetrieveOutputMemory</a> method to retrieve output parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>The buffer describes a <a href="..\bthxddi\ns-bthxddi--bthx-version.md">BTHX_VERSION</a> structure. </p>

<p>Refer to the WDK Bluetooth samples for more information.</p>

<p>Profile drivers should use KMDF and its <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputmemory.md">WdfRequestRetrieveOutputMemory</a> method to retrieve output parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>The buffer describes a <a href="..\bthxddi\ns-bthxddi--bthx-version.md">BTHX_VERSION</a> structure. </p>

<p>Refer to the WDK Bluetooth samples for more information.</p>

<p>Profile drivers should use KMDF and its <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputmemory.md">WdfRequestRetrieveOutputMemory</a> method to retrieve output parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>The buffer describes a <a href="..\bthxddi\ns-bthxddi--bthx-version.md">BTHX_VERSION</a> structure. </p>

<p>Refer to the WDK Bluetooth samples for more information.</p>

### -output-buffer-length
<p>The length of the buffer is the size of the <b>BTHX_VERSION</b> structure.</p>

<p>The length of the buffer is the size of the <b>BTHX_VERSION</b> structure.</p>

<p>The length of the buffer is the size of the <b>BTHX_VERSION</b> structure.</p>

<p>The length of the buffer is the size of the <b>BTHX_VERSION</b> structure.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size, in bytes, of the buffer that holds the BTHX_VERSION structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size, in bytes, of the buffer that holds the BTHX_VERSION structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size, in bytes, of the buffer that holds the BTHX_VERSION structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size, in bytes, of the buffer that holds the BTHX_VERSION structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size, in bytes, of the buffer that holds the BTHX_VERSION structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>Any unsuccessful NT status code prevents the driver from loading.</p>

## -remarks
<p>IOCTL_BTHX_GET_VERSION is a synchronous operation.</p>

<p>A transport driver can return one or more versions that it supports in BTHX_VERSION structure.  If no version is set,  Windows unloads the Bluetooth stack.</p>

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