---
UID: NI.bthxddi.IOCTL_BTHX_WRITE_HCI
title: IOCTL_BTHX_WRITE_HCI
author: windows-driver-content
description: IOCTL_BTHX_WRITE_HCI is used to write Bluetooth ACL Data and Commands to the transport layer.
old-location: bltooth\ioctl_bthx_hci_write.htm
ms.assetid: 77BBF6AC-F5FA-4795-8898-6DC02983F573
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
req.alt-api: IOCTL_BTHX_WRITE_HCI
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

# IOCTL_BTHX_WRITE_HCI IOCTL



## -description
<p>
<p>IOCTL_BTHX_WRITE_HCI is used to write Bluetooth ACL Data and Commands to the transport layer.</p>
</p>
<p>IOCTL_BTHX_WRITE_HCI is used to write Bluetooth ACL Data and Commands to the transport layer.</p>


## -ioctlparameters

### -input-buffer
<p>Profile drivers should use KMDF and its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550015">WdfRequestRetrieveInputMemory</a> method to retrieve input parameters.  For example, to get the input buffer:</p>

<p><code>Status = WdfRequestRetrieveInputMemory(_Request, &amp;ReqInMemory);</code></p>

<p>The buffer describes a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450835">BTHX_HCI_READ_WRITE_CONTEXT</a> structure that specifies the type of write and the data associated with the write. </p>

<p>Refer to the WDK Bluetooth samples for more information.</p>

### -input-buffer-length
<p>The length of the buffer is the size of the <b>BTHX_HCI_READ_WRITE_CONTEXT</b> structure.</p>

<p>The length of the buffer is the size of the <b>BTHX_HCI_READ_WRITE_CONTEXT</b> structure.</p>

### -output-buffer
<p>Profile drivers should use KMDF and its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550019">WdfRequestRetrieveOutputMemory</a> method to retrieve input parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>The buffer describes a ULONG of the number of bytes written for the input data specified in the <b>BTHX_HCI_READ_WRITE_CONTEXT</b> structure. </p>

<p>Refer to the WDK Bluetooth samples for more information.</p>

<p>Profile drivers should use KMDF and its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550019">WdfRequestRetrieveOutputMemory</a> method to retrieve input parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>The buffer describes a ULONG of the number of bytes written for the input data specified in the <b>BTHX_HCI_READ_WRITE_CONTEXT</b> structure. </p>

<p>Refer to the WDK Bluetooth samples for more information.</p>

<p>Profile drivers should use KMDF and its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550019">WdfRequestRetrieveOutputMemory</a> method to retrieve input parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>The buffer describes a ULONG of the number of bytes written for the input data specified in the <b>BTHX_HCI_READ_WRITE_CONTEXT</b> structure. </p>

<p>Refer to the WDK Bluetooth samples for more information.</p>

### -output-buffer-length
<p>The length of the buffer is the size of a ULONG.</p>

<p>The length of the buffer is the size of a ULONG.</p>

<p>The length of the buffer is the size of a ULONG.</p>

<p>The length of the buffer is the size of a ULONG.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If the request is successful the 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the number of bytes in the Output Parameter.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>If the request is successful the 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the number of bytes in the Output Parameter.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>If the request is successful the 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the number of bytes in the Output Parameter.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>If the request is successful the 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the number of bytes in the Output Parameter.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

<p>If the request is successful the 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the number of bytes in the Output Parameter.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p> </p>

## -remarks
<p>The Bluetooth stack sends IOCTL_BTHX_WRITE_HCI to write HCI ACL data and HCI command to the controller.</p>

<p>The input buffer points to a BTHX_HCI_READ_WRITE_CONTEXT structure whose <b>DataLen</b> member specifies the number of bytes in the <b>Data</b> member. The <b>Type</b> member is set based on whether the packet is a command packet or an ACL data packet.</p>

<p>The Bluetooth stack sends IOCTL_BTHX_WRITE_HCI to write HCI ACL data and HCI command to the controller.</p>

<p>The input buffer points to a BTHX_HCI_READ_WRITE_CONTEXT structure whose <b>DataLen</b> member specifies the number of bytes in the <b>Data</b> member. The <b>Type</b> member is set based on whether the packet is a command packet or an ACL data packet.</p>

<p>The Bluetooth stack sends IOCTL_BTHX_WRITE_HCI to write HCI ACL data and HCI command to the controller.</p>

<p>The input buffer points to a BTHX_HCI_READ_WRITE_CONTEXT structure whose <b>DataLen</b> member specifies the number of bytes in the <b>Data</b> member. The <b>Type</b> member is set based on whether the packet is a command packet or an ACL data packet.</p>

<p>The Bluetooth stack sends IOCTL_BTHX_WRITE_HCI to write HCI ACL data and HCI command to the controller.</p>

<p>The input buffer points to a BTHX_HCI_READ_WRITE_CONTEXT structure whose <b>DataLen</b> member specifies the number of bytes in the <b>Data</b> member. The <b>Type</b> member is set based on whether the packet is a command packet or an ACL data packet.</p>

<p>The Bluetooth stack sends IOCTL_BTHX_WRITE_HCI to write HCI ACL data and HCI command to the controller.</p>

<p>The input buffer points to a BTHX_HCI_READ_WRITE_CONTEXT structure whose <b>DataLen</b> member specifies the number of bytes in the <b>Data</b> member. The <b>Type</b> member is set based on whether the packet is a command packet or an ACL data packet.</p>

<p>The Bluetooth stack sends IOCTL_BTHX_WRITE_HCI to write HCI ACL data and HCI command to the controller.</p>

<p>The input buffer points to a BTHX_HCI_READ_WRITE_CONTEXT structure whose <b>DataLen</b> member specifies the number of bytes in the <b>Data</b> member. The <b>Type</b> member is set based on whether the packet is a command packet or an ACL data packet.</p>

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