---
UID: NS.scsi.PRECEIVE_TOKEN_INFORMATION_HEADER
title: PRECEIVE_TOKEN_INFORMATION_HEADER
author: windows-driver-content
description: The RECEIVE_TOKEN_INFORMATION_HEADER structure contains information returned as status from an offload data transfer operation.
old-location: storage\receive_token_information_header.htm
old-project: storage
ms.assetid: 3D8BF059-2063-499E-B287-41EE184A2264
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PRECEIVE_TOKEN_INFORMATION_HEADER, RECEIVE_TOKEN_INFORMATION_HEADER, *PRECEIVE_TOKEN_INFORMATION_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: scsi.h
req.include-header: Scsi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RECEIVE_TOKEN_INFORMATION_HEADER
req.alt-loc: scsi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PRECEIVE_TOKEN_INFORMATION_HEADER structure



## -description
<p>The <b>RECEIVE_TOKEN_INFORMATION_HEADER</b> structure contains information returned as status from an offload data transfer operation.</p>


## -syntax

````
typedef struct _RECEIVE_TOKEN_INFORMATION_HEADER {
  UCHAR AvailableData[4];
  UCHAR ResponseToServiceAction  :5;
  UCHAR Reserved1  :3;
  UCHAR OperationStatus  :7;
  UCHAR Reserved2   :1;
  UCHAR OperationCounter[2];
  UCHAR EstimatedStatusUpdateDelay[4];
  UCHAR CompletionStatus;
  UCHAR SenseDataFieldLength;
  UCHAR SenseDataLength;
  UCHAR TransferCountUnits;
  UCHAR TransferCount[8];
  UCHAR SegmentsProcessed[2];
  UCHAR Reserved3[6];
  UCHAR SenseData[ANYSIZE_ARRAY];
} RECEIVE_TOKEN_INFORMATION_HEADER, *PRECEIVE_TOKEN_INFORMATION_HEADER;
````


## -struct-fields
<dl>

### -field AvailableData

<dd>
<p>The amount of data available in the <b>SenseData</b> array and any additional result information.</p>
</dd>

### -field ResponseToServiceAction

<dd>
<p>A response code indicating which command action the response is for. The service action codes are the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="SERVICE_ACTION_POPULATE_TOKEN"></a><a id="service_action_populate_token"></a><dl>

### -field SERVICE_ACTION_POPULATE_TOKEN

</dl>
</td>
<td width="60%">
<p>The response information is for a POPULATE TOKEN command.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SERVICE_ACTION_WRITE_USING_TOKEN"></a><a id="service_action_write_using_token"></a><dl>

### -field SERVICE_ACTION_WRITE_USING_TOKEN

</dl>
</td>
<td width="60%">
<p>The response information is for a WRITE USING TOKEN command.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>

### -field OperationStatus

<dd>
<p>The current status of the copy operation. The status can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x01

</dl>
</td>
<td width="60%">
<p>The operation completed successfully.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x02

</dl>
</td>
<td width="60%">
<p>The operation completed unsuccessfully.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x04

</dl>
</td>
<td width="60%">
<p>The operation completed successfully but the copy initiator should verify that all data was transferred.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x10

</dl>
</td>
<td width="60%">
<p>The operation is in progress. Foreground or background operation state is unknown.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x11

</dl>
</td>
<td width="60%">
<p>The operation is in progress in the foreground.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x12

</dl>
</td>
<td width="60%">
<p>The operation is in progress in the background.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x60

</dl>
</td>
<td width="60%">
<p>The operation was terminated. Possibly by an existing resource reservation.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Reserved2 

<dd>
<p>Reserved.</p>
</dd>

### -field OperationCounter

<dd>
<p>The number of commands processed for the current copy operation.</p>
</dd>

### -field EstimatedStatusUpdateDelay

<dd>
<p>The recommended time, in milliseconds, to wait before sending the next RECEIVE COPY STATUS command for updated information about the current copy operation.</p>
</dd>

### -field CompletionStatus

<dd>
<p>SCSI status code for the copy command operation.</p>
</dd>

### -field SenseDataFieldLength

<dd>
<p>The length, in bytes, of the entire data area available for sense data. This value is always &gt;=  <b>SenseDataLength</b>.</p>
</dd>

### -field SenseDataLength

<dd>
<p>The length, in bytes, of the data in <b>SenseData</b>.</p>
</dd>

### -field TransferCountUnits

<dd>
<p>The byte units applied to <i>TransferCount</i>. Each unit expansion is a exponent in base 2. The multiplier value of <b>TRANSFER_COUNT_UNITS_KIBIBYTES</b>, for example, is 1024 and not 1000. The defined units are the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="TRANSFER_COUNT_UNITS_BYTES"></a><a id="transfer_count_units_bytes"></a><dl>

### -field TRANSFER_COUNT_UNITS_BYTES

</dl>
</td>
<td width="60%">
<p>Transfer count is in bytes.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="TRANSFER_COUNT_UNITS_KIBIBYTES"></a><a id="transfer_count_units_kibibytes"></a><dl>

### -field TRANSFER_COUNT_UNITS_KIBIBYTES

</dl>
</td>
<td width="60%">
<p>Transfer count is in kilobytes.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="TRANSFER_COUNT_UNITS_MEBIBYTES"></a><a id="transfer_count_units_mebibytes"></a><dl>

### -field TRANSFER_COUNT_UNITS_MEBIBYTES

</dl>
</td>
<td width="60%">
<p>Transfer count is in megabytes.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="TRANSFER_COUNT_UNITS_GIBIBYTES"></a><a id="transfer_count_units_gibibytes"></a><dl>

### -field TRANSFER_COUNT_UNITS_GIBIBYTES

</dl>
</td>
<td width="60%">
<p>Transfer count is in gigabytes.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="TRANSFER_COUNT_UNITS_TEBIBYTES"></a><a id="transfer_count_units_tebibytes"></a><dl>

### -field TRANSFER_COUNT_UNITS_TEBIBYTES

</dl>
</td>
<td width="60%">
<p>Transfer count is in terabytes.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="TRANSFER_COUNT_UNITS_PEBIBYTES"></a><a id="transfer_count_units_pebibytes"></a><dl>

### -field TRANSFER_COUNT_UNITS_PEBIBYTES

</dl>
</td>
<td width="60%">
<p>Transfer count is in petabytes.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="TRANSFER_COUNT_UNITS_EXBIBYTES"></a><a id="transfer_count_units_exbibytes"></a><dl>

### -field TRANSFER_COUNT_UNITS_EXBIBYTES

</dl>
</td>
<td width="60%">
<p>Transfer count is in exabytes.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="TRANSFER_COUNT_UNITS_NUMBER_BLOCKS"></a><a id="transfer_count_units_number_blocks"></a><dl>

### -field TRANSFER_COUNT_UNITS_NUMBER_BLOCKS

</dl>
</td>
<td width="60%">
<p>Transfer count is not an exponent, but in units of logical block length.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field TransferCount

<dd>
<p>The length of data transferred in the operation. The unit type in <b>TransferCountUnits</b> is applied to this value to give the total byte count.</p>
</dd>

### -field SegmentsProcessed

<dd>
<p>The number of segments processed for the data transfer operation. Segments are copy length units used internally by a storage device's copy provider. On Windowssystems, this value is reserved and applications must ignore this member.</p>
</dd>

### -field Reserved3

<dd>
<p>Reserved.</p>
</dd>

### -field SenseData

<dd>
<p>Sense data returned for the copy operation.</p>
</dd>
</dl>

## -remarks
<p>If <b>RECEIVE_TOKEN_INFORMATION_HEADER</b> is for a POPULATE TOKEN command operation, and the command completed successfully, a <a href="storage.receive_token_information_response_header">RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER</a> structure will also be present after <b>SenseData</b> at an offset of <b>SenseDataFieldLength</b> from the beginning of the <b>SenseData</b> array. The <b>RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER</b> structure will contain the token created as a representation of data (ROD) for the range parameters sent with the command.</p>

<p>All multibyte values are in big endian format. Prior to evaluation, these values must be converted to match the endian format of the current platform.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsi.h (include Scsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.receive_token_information_response_header">RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20RECEIVE_TOKEN_INFORMATION_HEADER structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
