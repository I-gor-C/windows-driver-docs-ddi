---
UID: NI.bthioctl.IOCTL_BTH_SDP_DISCONNECT
title: IOCTL_BTH_SDP_DISCONNECT
author: windows-driver-content
description: The IOCTL_BTH_SDP_DISCONNECT request closes a connection to a remote SDP server.
old-location: bltooth\ioctl_bth_sdp_disconnect.htm
old-project: bltooth
ms.assetid: 1d45465c-21ee-423c-967a-4462b61c2f0e
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: _HFP_BYPASS_CODEC_ID_V1, *PHFP_BYPASS_CODEC_ID_V1, HFP_BYPASS_CODEC_ID_V1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: bthioctl.h
req.include-header: Bthioctl.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_BTH_SDP_DISCONNECT
req.alt-loc: Bthioctl.h
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
---

# IOCTL_BTH_SDP_DISCONNECT IOCTL



## -description

The IOCTL_BTH_SDP_DISCONNECT request closes a connection to a remote SDP server.



The IOCTL_BTH_SDP_DISCONNECT request closes a connection to a remote SDP server.



## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member contains an 
      <a href="bltooth.bth_sdp_disconnect">BTH_SDP_DISCONNECT</a> structure that
      specifies the connection handle to the remote SDP connection to terminate.</p>The 
      <b>AssociatedIrp.SystemBuffer</b>AssociatedIrp.SystemBuffer member contains an 
      <a href="bltooth.bth_sdp_disconnect">BTH_SDP_DISCONNECT</a><b>BTH_SDP_DISCONNECT</b>BTH_SDP_DISCONNECT structure that
      specifies the connection handle to the remote SDP connection to terminate.


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
None</p>None


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to zero.</p>The 
      <b>Information</b>Information member of the STATUS_BLOCK structure is set to zero.
The 
      <b>Status</b> member is set to one of the values in the following table.</p>The 
      <b>Status</b>Status member is set to one of the values in the following table.
<table>
<tr>
<th>Status value</th>
<th>Description</th>
</tr>
<tr>
<td>
STATUS_SUCCESS

</td>
<td>
The IOCTL completed successfully.

</td>
</tr>
<tr>
<td>
STATUS_DEVICE_NOT_CONNECTED

</td>
<td>
The specified SDP server has already been disconnected.

</td>
</tr>
<tr>
<td>
STATUS_INVALID_PARAMETER

</td>
<td>
The connection handle passed in the input buffer is invalid.

</td>
</tr>
</table>
<tr>
<th>Status value</th>
<th>Description</th>
</tr>
<th>Status value</th>Status value
<th>Description</th>Description

<tr>
<td>
STATUS_SUCCESS

</td>
<td>
The IOCTL completed successfully.

</td>
</tr>
<td>
STATUS_SUCCESS

</td>
STATUS_SUCCESS</p>STATUS_SUCCESS

<td>
The IOCTL completed successfully.

</td>
The IOCTL completed successfully.</p>The IOCTL completed successfully.


<tr>
<td>
STATUS_DEVICE_NOT_CONNECTED

</td>
<td>
The specified SDP server has already been disconnected.

</td>
</tr>
<td>
STATUS_DEVICE_NOT_CONNECTED

</td>
STATUS_DEVICE_NOT_CONNECTED</p>STATUS_DEVICE_NOT_CONNECTED

<td>
The specified SDP server has already been disconnected.

</td>
The specified SDP server has already been disconnected.</p>The specified SDP server has already been disconnected.


<tr>
<td>
STATUS_INVALID_PARAMETER

</td>
<td>
The connection handle passed in the input buffer is invalid.

</td>
</tr>
<td>
STATUS_INVALID_PARAMETER

</td>
STATUS_INVALID_PARAMETER</p>STATUS_INVALID_PARAMETER

<td>
The connection handle passed in the input buffer is invalid.

</td>
The connection handle passed in the input buffer is invalid.</p>The connection handle passed in the input buffer is invalid.



 </p> 


## -remarks
Callers of 
    <a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_connect.md">IOCTL_BTH_SDP_CONNECT</a> must issue an
    IOCTL_BTH_SDP_DISCONNECT IOCTL when the SDP connection is no longer needed. After
    IOCTL_BTH_SDP_DISCONNECT is called, the specified SDP handle is no longer valid.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Versions: Supported in Windows Vista, and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Bthioctl.h (include Bthioctl.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="bltooth.bth_sdp_disconnect">BTH_SDP_DISCONNECT</a>
</dt>
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_connect.md">IOCTL_BTH_SDP_CONNECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20IOCTL_BTH_SDP_DISCONNECT control code%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

