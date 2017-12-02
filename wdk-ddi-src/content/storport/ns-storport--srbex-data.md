---
UID: NS.storport._SRBEX_DATA
title: SRBEX_DATA
author: windows-driver-content
description: The SRBEX_DATA structure is the generalized format for containing extended SRB data.
old-location: storage\srbex_data.htm
old-project: storage
ms.assetid: 15FB9877-6339-484B-83D5-6AD44EEE1D6E
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SRBEX_DATA, SRBEX_DATA, *PSRBEX_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h, Srb.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRBEX_DATA
req.alt-loc: Storport.h
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
req.product: Windows 10 or later.
---

# SRBEX_DATA structure



## -description
<p>The <b>SRBEX_DATA</b> structure is the generalized format for containing extended SRB data.</p>


## -syntax

````
typedef struct _SRBEX_DATA {
  SRBEXDATATYPE Type;
  ULONG         Length;
  UCHAR         Data[ANYSIZE_ARRAY];
} SRBEX_DATA, *PSRBEX_DATA;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>Data type indicator for the extended SRB data structure. The possible values for <b>Type</b> are one of the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypeUnknown"></a><a id="srbexdatatypeunknown"></a><a id="SRBEXDATATYPEUNKNOWN"></a><dl>

### -field SrbExDataTypeUnknown

</dl>
</td>
<td width="60%">
<p>The SRB extended data type is unknown.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypeBidirectional"></a><a id="srbexdatatypebidirectional"></a><a id="SRBEXDATATYPEBIDIRECTIONAL"></a><dl>

### -field SrbExDataTypeBidirectional

</dl>
</td>
<td width="60%">
<p>The SRB extended data is formatted as an <a href="..\storport\ns-storport--srbex-data-bidirectional.md">SRBEX_DATA_BIDIRECTIONAL</a> structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypeScsiCdb16"></a><a id="srbexdatatypescsicdb16"></a><a id="SRBEXDATATYPESCSICDB16"></a><dl>

### -field SrbExDataTypeScsiCdb16

</dl>
</td>
<td width="60%">
<p>The SRB extended data is formatted as an <a href="..\storport\ns-storport--srbex-data-scsi-cdb16.md">SRBEX_DATA_SCSI_CDB16</a> structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypeScsiCdb32"></a><a id="srbexdatatypescsicdb32"></a><a id="SRBEXDATATYPESCSICDB32"></a><dl>

### -field SrbExDataTypeScsiCdb32

</dl>
</td>
<td width="60%">
<p>The SRB extended data is formatted as an <a href="..\storport\ns-storport--srbex-data-scsi-cdb32.md">SRBEX_DATA_SCSI_CDB32</a> structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypeScsiCdbVar"></a><a id="srbexdatatypescsicdbvar"></a><a id="SRBEXDATATYPESCSICDBVAR"></a><dl>

### -field SrbExDataTypeScsiCdbVar

</dl>
</td>
<td width="60%">
<p>The SRB extended data is formatted as an <a href="..\storport\ns-storport--srbex-data-scsi-cdb-var.md">SRBEX_DATA_SCSI_CDB_VAR</a> structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypeWmi"></a><a id="srbexdatatypewmi"></a><a id="SRBEXDATATYPEWMI"></a><dl>

### -field SrbExDataTypeWmi

</dl>
</td>
<td width="60%">
<p>The SRB extended data is formatted as an <a href="..\storport\ns-storport--srbex-data-wmi.md">SRBEX_DATA_WMI</a> structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypePower"></a><a id="srbexdatatypepower"></a><a id="SRBEXDATATYPEPOWER"></a><dl>

### -field SrbExDataTypePower

</dl>
</td>
<td width="60%">
<p>The SRB extended data is formatted as an <a href="..\storport\ns-storport--srbex-data-power.md">SRBEX_DATA_POWER</a> structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypePnp"></a><a id="srbexdatatypepnp"></a><a id="SRBEXDATATYPEPNP"></a><dl>

### -field SrbExDataTypePnp

</dl>
</td>
<td width="60%">
<p>The SRB extended data is formatted as an <a href="..\storport\ns-storport--srbex-data-pnp.md">SRBEX_DATA_PNP</a> structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SrbExDataTypeIoInfo"></a><a id="srbexdatatypeioinfo"></a><a id="SRBEXDATATYPEIOINFO"></a><dl>

### -field SrbExDataTypeIoInfo

</dl>
</td>
<td width="60%">
<p>The SRB extended data is formatted as an <a href="..\storport\ns-storport--srbex-data-io-info.md">SRBEX_DATA_IO_INFO</a> structure.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Length

<dd>
<p>Length of the SRB data, in bytes, present  in the <b>Data</b> member.</p>
</dd>

### -field Data

<dd>
<p>The extended SRB data block contents.</p>
</dd>
</dl>

## -remarks
<p>The SRB extended data is present when the <b>SrbExDataOffset</b> array in the <a href="..\storport\ns-storport--storage-request-block.md">STORAGE_REQUEST_BLOCK</a> structure contains valid offset locations.  A storage driver initially references a memory offset location contained in <b>SrbExDataOffset</b> as an <b>SRBEX_DATA</b> structure. A pointer to the data block is then cast to the appropriate structure type based on the data type value in the <b>Type</b> member.</p>

<p>The following example code fragment shows how to access the extended data for the an SRB function of SRB_FUNCTION_PNP.</p>

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
<dt>Storport.h (include Storport.h or Srb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\storport\ns-storport--srbex-data-bidirectional.md">SRBEX_DATA_BIDIRECTIONAL</a>
</dt>
<dt>
<a href="..\storport\ns-storport--srbex-data-io-info.md">SRBEX_DATA_IO_INFO</a>
</dt>
<dt>
<a href="..\storport\ns-storport--srbex-data-pnp.md">SRBEX_DATA_PNP</a>
</dt>
<dt>
<a href="..\storport\ns-storport--srbex-data-power.md">SRBEX_DATA_POWER</a>
</dt>
<dt>
<a href="..\storport\ns-storport--srbex-data-scsi-cdb16.md">SRBEX_DATA_SCSI_CDB16</a>
</dt>
<dt>
<a href="..\storport\ns-storport--srbex-data-scsi-cdb32.md">SRBEX_DATA_SCSI_CDB32</a>
</dt>
<dt>
<a href="..\storport\ns-storport--srbex-data-scsi-cdb-var.md">SRBEX_DATA_SCSI_CDB_VAR</a>
</dt>
<dt>
<a href="..\storport\ns-storport--srbex-data-wmi.md">SRBEX_DATA_WMI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SRBEX_DATA structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
