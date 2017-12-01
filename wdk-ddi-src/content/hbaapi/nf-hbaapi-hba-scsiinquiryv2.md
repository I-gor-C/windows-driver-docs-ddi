---
UID: NF.hbaapi.HBA_ScsiInquiryV2
title: HBA_ScsiInquiryV2
author: windows-driver-content
description: The HBA_ScsiInquiryV2 routine sends a SCSI inquiry command to the specified remote port.
old-location: storage\hba_scsiinquiryv2.htm
old-project: storage
ms.assetid: ba82c6f1-f310-4258-8867-8309845320cc
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_ScsiInquiryV2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_ScsiInquiryV2
req.alt-loc: Hbaapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
req.iface: 
---

# HBA_ScsiInquiryV2 function



## -description
<p>The <b>HBA_ScsiInquiryV2</b> routine sends a SCSI inquiry command to the specified remote port.</p>


## -syntax

````
HBA_STATUS HBA_API HBA_ScsiInquiryV2(
  _In_    HBA_HANDLE HbaHandle,
  _In_    HBA_WWN    HbaPortWWN,
  _In_    HBA_WWN    discoveredPortWWN,
  _In_    HBA_UINT64 fcLUN,
  _In_    HBA_UINT8  CDB_Byte1,
  _In_    HBA_UINT8  CDB_Byte2,
  _Out_   void       *pRespBuffer,
  _Inout_ HBA_UINT32 *pRespBufferSize,
  _Out_   HBA_UINT8  *pScsiStatus,
  _Out_   void       *pSenseBuffer,
  _Inout_ HBA_UINT32 *pSenseBufferSize
);
````


## -parameters
<dl>

### -param <i>HbaHandle</i> [in]

<dd>
<p>Contains a value returned by the routine <a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a> that identifies the HBA through which the SCSI inquiry command is sent.</p>
</dd>

### -param <i>HbaPortWWN</i> [in]

<dd>
<p>Contains a 64-bit worldwide name (WWN) that uniquely identifies the local HBA port from which the SCSI inquiry command is sent. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification. </p>
</dd>

### -param <i>discoveredPortWWN</i> [in]

<dd>
<p>Contains a 64-bit worldwide name (WWN) that uniquely identifies the remote HBA port to which the SCSI inquiry command is sent. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification. </p>
</dd>

### -param <i>fcLUN</i> [in]

<dd>
<p>Indicates the fibre channel logical unit number of the logical unit to which the SCSI inquiry command is sent. </p>
</dd>

### -param <i>CDB_Byte1</i> [in]

<dd>
<p>Contains the value to insert in the first byte of the command descriptor block (CDB) of the SCSI inquiry command. This member must have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>Indicates that the SCSI inquiry command should request the standard SCSI INQUIRY data. </p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Indicates that the SCSI inquiry command should request the vital product data specified by <i>CDB_Byte2</i>. </p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Indicates that the SCSI inquiry command should request command support data (CmdDt) specified in <i>CDB_Byte2</i>. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>CDB_Byte2</i> [in]

<dd>
<p>Contains the value to insert in the third byte of the command descriptor block (CDB) of the SCSI inquiry command. This member must have one of the following values:</p>
<table>
<tr>
<th>Value in <i>CDB_Byte1</i></th>
<th>Meaning of the value in <i>CDB_Byte2</i></th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Indicates that <i>CDB_Byte2 </i>contains the page number of the vital product data to retrieve. </p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Indicates that <i>CDB_Byte2 </i>contains the operation code of the command support data to retrieve. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pRespBuffer</i> [out]

<dd>
<p>Pointer to a buffer that receives the output data of the SCSI inquiry command.</p>
</dd>

### -param <i>pRespBufferSize</i> [in, out]

<dd>
<p>Indicates the size, in bytes, of the buffer at <i>pRespBuffer</i>.</p>
</dd>

### -param <i>pScsiStatus</i> [out]

<dd>
<p>Pointer to a buffer that receives the SCSI status data. </p>
</dd>

### -param <i>pSenseBuffer</i> [out]

<dd>
<p>Pointer to a buffer that receives the SCSI sense data.</p>
</dd>

### -param <i>pSenseBufferSize</i> [in, out]

<dd>
<p>On input, indicates the size, in bytes, of the buffer at <i>pSenseBuffer</i>. On output, this member indicates the number of bytes of sense data returned.</p>
</dd>
</dl>

## -returns
<p>The <b>HBA_ScsiInquiryV2</b> routine returns a value of type <a href="storage.hba_status">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_ScsiInquiryV2</b> returns one of the following values.</p><dl>
<dt><b>HBA_STATUS_OK</b></dt>
</dl><p>Returned if the complete payload of a reply to the SCSI inquiry command was successfully retrieved. </p><dl>
<dt><b>HBA_STATUS_ERROR_ILLEGAL_WWN</b></dt>
</dl><p>Returned if the HBA referenced by <i>handle</i> does not contain a port with a name that matches <i>HbaPortWWN</i>. </p><dl>
<dt><b>HBA_STATUS_ERROR_NOT_A_TARGET</b></dt>
</dl><p>Returned if the specified remote port referenced by <i>discoveredPortWWN </i>does not have SCSI target functionality.</p><dl>
<dt><b>HBA_STATUS_ERROR_TARGET_BUSY</b></dt>
</dl><p>Returned if the SCSI inquiry command could not be delivered without causing a SCSI overlapped command condition.</p><dl>
<dt><b>HBA_STATUS_SCSI_CHECK_CONDITION</b></dt>
</dl><p>Returned if a SCSI check condition occurred and SCSI send data is provided in the buffer at <i>pSenseBuffer</i>.</p><dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl><p>Returned if an unspecified error occurred that prevented the execution of the SCSI inquiry command. </p>

<p> </p>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a>
</dt>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_ScsiInquiryV2 routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
