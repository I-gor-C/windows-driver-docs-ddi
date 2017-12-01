---
UID: NI.bthxddi.IOCTL_BTHX_READ_HCI
title: IOCTL_BTHX_READ_HCI
author: windows-driver-content
description: IOCTL_BTHX_READ_HCI is used to read Bluetooth ACL Data and Events from the transport layer.
old-location: bltooth\ioctl_bthx_hci_read.htm
old-project: bltooth
ms.assetid: 02CC3534-D319-40C1-A73C-DEFC1F5709F7
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
req.alt-api: IOCTL_BTHX_READ_HCI
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

# IOCTL_BTHX_READ_HCI IOCTL



## -description
<p>IOCTL_BTHX_READ_HCI is used to read Bluetooth ACL Data and Events from the transport layer.</p>


## -ioctlparameters

### -input-buffer
<p>Profile drivers should use KMDF and its <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveinputmemory.md">WdfRequestRetrieveInputMemory</a> method to retrieve input parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveInputMemory(_Request, &amp;ReqInMemory);</code></p>

<p>For more information, see the WDK Bluetooth samples.</p>

### -input-buffer-length
<p>The buffer describes a UCHAR that represents the type of read. The length of the buffer is the size of the UCHAR.</p>

<p>The buffer describes a UCHAR that represents the type of read. The length of the buffer is the size of the UCHAR.</p>

### -output-buffer
<p>Profile drivers should use KMDF and its <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputmemory.md">WdfRequestRetrieveOutputMemory</a> method to retrieve input parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>For more information, see the WDK Bluetooth samples.</p>

<p>Profile drivers should use KMDF and its <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputmemory.md">WdfRequestRetrieveOutputMemory</a> method to retrieve input parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>For more information, see the WDK Bluetooth samples.</p>

<p>Profile drivers should use KMDF and its <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputmemory.md">WdfRequestRetrieveOutputMemory</a> method to retrieve input parameters.  For example, to get the output buffer:</p>

<p><code>Status = WdfRequestRetrieveOutputMemory(_Request, &amp;ReqOutMemory);</code></p>

<p>For more information, see the WDK Bluetooth samples.</p>

### -output-buffer-length
<p>The 
       <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that holds a <a href="..\bthxddi\ns-bthxddi--bthx-hci-read-write-context.md">BTHX_HCI_READ_WRITE_CONTEXT</a> structure and additional data associated with the read. The  buffer must be large enough to hold the largest event or ACL Data packet, depending on its packet type.</p>

<p>For an event packet, it is FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) +257 where 257 is the sum of a 2-byte event header and 255-byte event data.</p>

<p>For an ACL Data packet, it is FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) + MaxAclTransferInSize where MaxAclTransferInSize is the value in BTHX_CAPABILITIES that is returned from the transport driver with IOCTL_BTHX_QUERY_CAPABILITIES.</p>

<p>The 
       <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that holds a <a href="..\bthxddi\ns-bthxddi--bthx-hci-read-write-context.md">BTHX_HCI_READ_WRITE_CONTEXT</a> structure and additional data associated with the read. The  buffer must be large enough to hold the largest event or ACL Data packet, depending on its packet type.</p>

<p>For an event packet, it is FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) +257 where 257 is the sum of a 2-byte event header and 255-byte event data.</p>

<p>For an ACL Data packet, it is FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) + MaxAclTransferInSize where MaxAclTransferInSize is the value in BTHX_CAPABILITIES that is returned from the transport driver with IOCTL_BTHX_QUERY_CAPABILITIES.</p>

<p>The 
       <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that holds a <a href="..\bthxddi\ns-bthxddi--bthx-hci-read-write-context.md">BTHX_HCI_READ_WRITE_CONTEXT</a> structure and additional data associated with the read. The  buffer must be large enough to hold the largest event or ACL Data packet, depending on its packet type.</p>

<p>For an event packet, it is FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) +257 where 257 is the sum of a 2-byte event header and 255-byte event data.</p>

<p>For an ACL Data packet, it is FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) + MaxAclTransferInSize where MaxAclTransferInSize is the value in BTHX_CAPABILITIES that is returned from the transport driver with IOCTL_BTHX_QUERY_CAPABILITIES.</p>

<p>The 
       <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that holds a <a href="..\bthxddi\ns-bthxddi--bthx-hci-read-write-context.md">BTHX_HCI_READ_WRITE_CONTEXT</a> structure and additional data associated with the read. The  buffer must be large enough to hold the largest event or ACL Data packet, depending on its packet type.</p>

<p>For an event packet, it is FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) +257 where 257 is the sum of a 2-byte event header and 255-byte event data.</p>

<p>For an ACL Data packet, it is FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) + MaxAclTransferInSize where MaxAclTransferInSize is the value in BTHX_CAPABILITIES that is returned from the transport driver with IOCTL_BTHX_QUERY_CAPABILITIES.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The 
       <b>Information</b>  member of the STATUS_BLOCK structure is set to the number of bytes of data returned.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p>STATUS_CANCELLED</p>

<p>The IOCTL has been canceled.</p>

<p> </p>

<p>The 
       <b>Information</b>  member of the STATUS_BLOCK structure is set to the number of bytes of data returned.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p>STATUS_CANCELLED</p>

<p>The IOCTL has been canceled.</p>

<p> </p>

<p>The 
       <b>Information</b>  member of the STATUS_BLOCK structure is set to the number of bytes of data returned.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p>STATUS_CANCELLED</p>

<p>The IOCTL has been canceled.</p>

<p> </p>

<p>The 
       <b>Information</b>  member of the STATUS_BLOCK structure is set to the number of bytes of data returned.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p>STATUS_CANCELLED</p>

<p>The IOCTL has been canceled.</p>

<p> </p>

<p>The 
       <b>Information</b>  member of the STATUS_BLOCK structure is set to the number of bytes of data returned.</p>

<p>The 
      <b>Status</b> member is set to one of the values in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The IOCTL completed successfully.</p>

<p>STATUS_CANCELLED</p>

<p>The IOCTL has been canceled.</p>

<p> </p>

## -remarks
<p>The input buffer points to the type of packet that is being read.</p>

<p>The output buffer points to a BTHX_HCI_READ_WRITE_CONTEXT structure whose <b>DataLen</b> member specifies the number of bytes in the <b>Data</b> member. The <b>Type</b> member must be set to the same as the Input packet type.</p>

<p>The <b>Information</b> member of the STATUS_BLOCK should be set to FIELD_OFFSET(BTHX_HCI_READ_WRITE_CONTEXT, Data) + <b>DataLen</b>.</p>

<p>The maximum size of the <b>Data</b> member for an ACL read is determined by <b>MaxAclTransferInSize</b>, specified in the BTHX_CAPABILITIES structure.  The maximum size of the <b>Data</b> member for an event is 255.</p>

<p>This IOCTL should return STATUS_SUCCESS only under normal operation. Transport-specific errors should not be returned.  The IOCTL should return STATUS_CANCELLED only if this IOCTL has been canceled.</p>

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