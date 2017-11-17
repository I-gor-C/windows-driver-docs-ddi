---
UID: NI.bthxddi.IOCTL_BTHX_QUERY_CAPABILITIES
title: IOCTL_BTHX_QUERY_CAPABILITIES
author: windows-driver-content
description: IOCTL_BTHX_QUERY_CAPABILITIES is used to query the capabilities of the transport driver.
old-location: bltooth\ioctl_bthx_query_capabilities.htm
ms.assetid: 199C93EC-AB91-47F1-914A-F44BFF1796A6
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: bltooth
req.header: bthxddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_BTHX_QUERY_CAPABILITIES
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: BTHDDI_SDP_PARSE_INTERFACE, BTHDDI_SDP_PARSE_INTERFACE, *PBTHDDI_SDP_PARSE_INTERFACE
req.iface: 
---

# IOCTL_BTHX_QUERY_CAPABILITIES IOCTL



## -description
<p>
<p>IOCTL_BTHX_QUERY_CAPABILITIES is used to query the capabilities of the transport driver.</p>
</p>
<p>IOCTL_BTHX_QUERY_CAPABILITIES is used to query the capabilities of the transport driver.</p>


## -ioctlparameters

### -input-buffer
<p>None.</p>

### -input-buffer-length
<p>None.</p>

<p>None.</p>

### -output-buffer
<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that holds a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450833">BTHX_CAPABILITIES</a> structure. </p>

<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that holds a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450833">BTHX_CAPABILITIES</a> structure. </p>

<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that holds a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450833">BTHX_CAPABILITIES</a> structure. </p>

### -output-buffer-length
<p>The length of the buffer is the size of the <b>BTHX_CAPABILITIES</b> structure.</p>

<p>The length of the buffer is the size of the <b>BTHX_CAPABILITIES</b> structure.</p>

<p>The length of the buffer is the size of the <b>BTHX_CAPABILITIES</b> structure.</p>

<p>The length of the buffer is the size of the <b>BTHX_CAPABILITIES</b> structure.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size of the structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size of the structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size of the structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size of the structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size of the structure.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

## -remarks
<p>During startup, the Bluetooth stack sends IOCTL_BTHX_QUERY_CAPABILITIES to query the capabilities of the transport driver.</p>

<p>This is a synchrononous call and failure of this IOCTL prevents Windows from loading the Bluetooth stack.</p>

<p>The output buffer of this IOCTL is defined by the BTHX_CAPABILITIES structure.</p>

<p>The <b>MaxScoChannels</b> member must be set to 1. The <b>ScoSupport</b> member must be set to <b>ScoSupportHCIBypass</b>. Failure to do so prevents the stack from being loaded.</p>

<p>During startup, the Bluetooth stack sends IOCTL_BTHX_QUERY_CAPABILITIES to query the capabilities of the transport driver.</p>

<p>This is a synchrononous call and failure of this IOCTL prevents Windows from loading the Bluetooth stack.</p>

<p>The output buffer of this IOCTL is defined by the BTHX_CAPABILITIES structure.</p>

<p>The <b>MaxScoChannels</b> member must be set to 1. The <b>ScoSupport</b> member must be set to <b>ScoSupportHCIBypass</b>. Failure to do so prevents the stack from being loaded.</p>

<p>During startup, the Bluetooth stack sends IOCTL_BTHX_QUERY_CAPABILITIES to query the capabilities of the transport driver.</p>

<p>This is a synchrononous call and failure of this IOCTL prevents Windows from loading the Bluetooth stack.</p>

<p>The output buffer of this IOCTL is defined by the BTHX_CAPABILITIES structure.</p>

<p>The <b>MaxScoChannels</b> member must be set to 1. The <b>ScoSupport</b> member must be set to <b>ScoSupportHCIBypass</b>. Failure to do so prevents the stack from being loaded.</p>

<p>During startup, the Bluetooth stack sends IOCTL_BTHX_QUERY_CAPABILITIES to query the capabilities of the transport driver.</p>

<p>This is a synchrononous call and failure of this IOCTL prevents Windows from loading the Bluetooth stack.</p>

<p>The output buffer of this IOCTL is defined by the BTHX_CAPABILITIES structure.</p>

<p>The <b>MaxScoChannels</b> member must be set to 1. The <b>ScoSupport</b> member must be set to <b>ScoSupportHCIBypass</b>. Failure to do so prevents the stack from being loaded.</p>

<p>During startup, the Bluetooth stack sends IOCTL_BTHX_QUERY_CAPABILITIES to query the capabilities of the transport driver.</p>

<p>This is a synchrononous call and failure of this IOCTL prevents Windows from loading the Bluetooth stack.</p>

<p>The output buffer of this IOCTL is defined by the BTHX_CAPABILITIES structure.</p>

<p>The <b>MaxScoChannels</b> member must be set to 1. The <b>ScoSupport</b> member must be set to <b>ScoSupportHCIBypass</b>. Failure to do so prevents the stack from being loaded.</p>

<p>During startup, the Bluetooth stack sends IOCTL_BTHX_QUERY_CAPABILITIES to query the capabilities of the transport driver.</p>

<p>This is a synchrononous call and failure of this IOCTL prevents Windows from loading the Bluetooth stack.</p>

<p>The output buffer of this IOCTL is defined by the BTHX_CAPABILITIES structure.</p>

<p>The <b>MaxScoChannels</b> member must be set to 1. The <b>ScoSupport</b> member must be set to <b>ScoSupportHCIBypass</b>. Failure to do so prevents the stack from being loaded.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>