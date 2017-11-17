---
UID: NS.scsi._SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
title: SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
author: windows-driver-content
description: The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process.
old-location: storage\ses_download_microcode_control_diagnostic_page.htm
ms.assetid: 09c2746f-cfe4-41dc-82ce-0b7e0c348897
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: scsi.h
req.include-header: Minitape.h, Storport.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10, version 1709 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
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
ms.keywords: SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE, SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE, *PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
req.iface: 
req.product: Windows 10 or later.
---

# SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure



## -description
<p>The <b>SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE</b> structure contains a vendor specific microcode (i.e., firmware) image
for use by the enclosure services process. </p>


## -syntax

````
typedef struct _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE {
  UCHAR  PageCode;
  UCHAR  SubEnclosureId;
  UCHAR  PageLength[2];
  UCHAR  ExpectedGenerationCode[4];
  UCHAR  Mode;
  UCHAR  Reserved[2];
  UCHAR  BufferID;
  UCHAR  BufferOffset[4];
  UCHAR  ImageLength[4];
  UCHAR  DataLength[4];
  UCHAR  Data[ANYSIZE_ARRAY];
} SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE, *PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE;
````


## -struct-fields
<dl>

### -field <b>PageCode</b>

<dd>
<p>Specifies the diagnostic page being sent or requested based on the value. For a Microcode Control diagnostic page, the value should be 0x0E.</p>
</dd>

### -field <b>SubEnclosureId</b>

<dd>
<p>Specifies the sub enclosure to which the application client is
sending the microcode image. If the value does not match a valid SUBENCLOSURE_IDENTIFIER field value found in the <a href="https://msdn.microsoft.com/0FD748D6-F598-44D1-A8D3-E63764CB90C6">SES_CONFIGURATION_DIAGNOSTIC_PAGE</a>, then the enclosure services
process shall abort the download microcode operation with a status of 0x80.</p>
</dd>

### -field <b>PageLength</b>

<dd>
<p>Specifies the number of bytes that follow in the diagnostic page.</p>
</dd>

### -field <b>ExpectedGenerationCode</b>

<dd>
<p>Specifies the expected value of the generation code. If this parameter is not set to the current generation code, then the enclosure services
process shall abort the download microcode operation with a status of 0x80. </p>
</dd>

### -field <b>Mode</b>

<dd>
<p>Specifies which mode to download the microcode with. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="Download_microcode_with_offsets__save__and_activate"></a><a id="download_microcode_with_offsets__save__and_activate"></a><a id="DOWNLOAD_MICROCODE_WITH_OFFSETS__SAVE__AND_ACTIVATE"></a><dl>

### -field <b>Download
microcode
with
offsets,
save, and
activate</b>


### -field 0x07

</dl>
</td>
<td width="60%">
<p>After the last SEND DIAGNOSTIC command delivers a Download Microcode
Control diagnostic page to the subenclosure completes, the enclosure services
process shall verify the complete microcode image (e.g., perform a vendor
specific checksum) and save the new microcode image into nonvolatile storage.</p>
<p> If there are no errors in the microcode image or in the save operation, then the
enclosure services process shall perform one of the following actions:<ul>
<li>Set the <i>Status</i> field in <a href="storage._ses_download_microcode_status_descriptor">SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</a>  to 0x10, if
requested, and activate the new microcode image after either returning the Download Microcode Status diagnostic page, power on, or for standalone enclosure services processes, a hard reset.</li>
<li>Set the <i>Status</i> field in <a href="storage._ses_download_microcode_status_descriptor">SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</a>  to 0x11, if
requested,  and for standalone enclosure services processes only,
activate the new microcode image after either power on or hard reset.</li>
<li>Set the <i>Status</i> field in <a href="storage._ses_download_microcode_status_descriptor">SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</a>  to 0x12, if
requested,  and activate the new microcode image after power on.</li>
</ul>
</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Download_microcode_with_offsets__save__and_defer_activate"></a><a id="download_microcode_with_offsets__save__and_defer_activate"></a><a id="DOWNLOAD_MICROCODE_WITH_OFFSETS__SAVE__AND_DEFER_ACTIVATE"></a><dl>

### -field <b>Download
microcode
with
offsets,
save, and
defer
activate</b>


### -field 0x0E

</dl>
</td>
<td width="60%">
<p>After the last SEND DIAGNOSTIC command delivering a <b>SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE</b> to the subenclosure completes, the enclosure services
process shall verify the complete microcode image (e.g., perform a vendor
specific checksum), save the new microcode image into nonvolatile storage
(e.g., flash ROM), and defer activation of the new microcode.
</p>
<p>If there are no errors in the microcode image or in the save operation, then the
enclosure services process shall set the <i>Status</i> field in <a href="storage._ses_download_microcode_status_descriptor">SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</a>  to 0x13 in the <a href="storage._ses_download_microcode_status_diagnostic_page">SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE</a>, if
requested, and activate the new microcode after either:</p>
<ul>
<li>Processing this structure with the
<i>Mode</i> field set to 0x0F (i.e., Activate deferred
microcode)</li>
<li>A power on</li>
<li>A hard reset</li>
</ul>
</td>
</tr>
<tr>
<td width="40%"><a id="Activate_deferred_microcode"></a><a id="activate_deferred_microcode"></a><a id="ACTIVATE_DEFERRED_MICROCODE"></a><dl>

### -field <b>Activate
deferred
microcode</b>


### -field 0x0F

</dl>
</td>
<td width="60%">
<p>After the SEND DIAGNOSTIC command specifying this mode completes, the
enclosure services process shall activate the deferred microcode image, if any.
</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Reserved"></a><a id="reserved"></a><a id="RESERVED"></a><dl>

### -field <b>Reserved</b>


### -field All other values

</dl>
</td>
<td width="60%">
<p>Reserved for future use.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>BufferID</b>

<dd>
<p>Specifies a specific buffer within the enclosure services process to receive the microcode
image. The enclosure services process assigns vendor specific buffer ID codes to buffers (e.g., the main
firmware image may be stored in buffer 00h and a backup firmware image may be stored in buffer 01h). The
enclosure services process shall support a buffer ID value of 00h. If more than one buffer is supported, then
the enclosure services process shall assign additional buffer ID codes contiguously, beginning with 01h. If the
enclosure services process receives an unsupported buffer ID code, then it shall abort the download
microcode operation and set the <i>Status</i> field in <a href="storage._ses_download_microcode_status_descriptor">SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</a>  to 0x80 in the <a href="storage._ses_download_microcode_status_diagnostic_page">SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE</a> structure.</p>
</dd>

### -field <b>BufferOffset</b>

<dd>
<p>Specifies the offset in bytes within the buffer to which the microcode data is written in multiples of four. The enclosure services process may require that this  field be contiguously increasing in consecutive SEND DIAGNOSTIC commands. </p>
</dd>

### -field <b>ImageLength</b>

<dd>
<p>specifies the total number of bytes in the microcode image the application
intends to send to the specified <i>BufferID</i>.</p>
</dd>

### -field <b>DataLength</b>

<dd>
<p>Specifies the length of <i>Data</i>, in bytes.</p>
</dd>

### -field <b>Data</b>

<dd>
<p>Contains part of the vendor specific microcode image.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10, version 1709 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsi.h (include Minitape.h or Storport.h)</dt>
</dl>
</td>
</tr>
</table>