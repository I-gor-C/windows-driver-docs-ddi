---
UID: NI.bthioctl.IOCTL_BTH_SDP_CONNECT
title: IOCTL_BTH_SDP_CONNECT
author: windows-driver-content
description: The IOCTL_BTH_SDP_CONNECT request creates a connection to the SDP service on a remote Bluetooth device.
old-location: bltooth\ioctl_bth_sdp_connect.htm
old-project: bltooth
ms.assetid: 8bfe92c9-6049-4d68-80a9-3a8f8dda3bcc
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
req.alt-api: IOCTL_BTH_SDP_CONNECT
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

# IOCTL_BTH_SDP_CONNECT IOCTL



## -description

The IOCTL_BTH_SDP_CONNECT request creates a connection to the SDP service on a remote Bluetooth
     device.



The IOCTL_BTH_SDP_CONNECT request creates a connection to the SDP service on a remote Bluetooth
     device.



## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member contains a 
      <a href="bltooth.bth_sdp_connect">BTH_SDP_CONNECT</a> structure that specifies
      the address of the remote SDP server, the request's timeout setting, and other information specific to
      the connection.</p>The 
      <b>AssociatedIrp.SystemBuffer</b>AssociatedIrp.SystemBuffer member contains a 
      <a href="bltooth.bth_sdp_connect">BTH_SDP_CONNECT</a><b>BTH_SDP_CONNECT</b>BTH_SDP_CONNECT structure that specifies
      the address of the remote SDP server, the request's timeout setting, and other information specific to
      the connection.


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member contains a BTH_SDP_CONNECT structure that holds the SDP
      connection handle to the remote server.</p>The 
      <b>AssociatedIrp.SystemBuffer</b>AssociatedIrp.SystemBuffer member contains a BTH_SDP_CONNECT structure that holds the SDP
      connection handle to the remote server.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
If the request is successful, the 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size, in bytes, of the output
      buffer. Otherwise, the 
      <b>Information</b> member is set to zero.</p>If the request is successful, the 
      <b>Information</b>Information member of the STATUS_BLOCK structure is set to the size, in bytes, of the output
      buffer. Otherwise, the 
      <b>Information</b>Information member is set to zero.
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
STATUS_DEVICE_BUSY

</td>
<td>
The HCI layer is currently unable to accept requests.

</td>
</tr>
<tr>
<td>
STATUS_DEVICE_NOT_CONNECTED

</td>
<td>
If a cached connection was specified, there are no cached records available. Otherwise, the
         connection was canceled before it completed.

</td>
</tr>
<tr>
<td>
STATUS_INSUFFICIENT_RESOURCES

</td>
<td>
There was not enough memory available to process the request.

</td>
</tr>
<tr>
<td>
STATUS_INVALID_PARAMETER

</td>
<td>
A portion of the structure found in the input buffer was incorrect.

</td>
</tr>
<tr>
<td>
STATUS_PENDING

</td>
<td>
The system cannot currently respond, but will attempt to shortly.

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
STATUS_DEVICE_BUSY

</td>
<td>
The HCI layer is currently unable to accept requests.

</td>
</tr>
<td>
STATUS_DEVICE_BUSY

</td>
STATUS_DEVICE_BUSY</p>STATUS_DEVICE_BUSY

<td>
The HCI layer is currently unable to accept requests.

</td>
The HCI layer is currently unable to accept requests.</p>The HCI layer is currently unable to accept requests.


<tr>
<td>
STATUS_DEVICE_NOT_CONNECTED

</td>
<td>
If a cached connection was specified, there are no cached records available. Otherwise, the
         connection was canceled before it completed.

</td>
</tr>
<td>
STATUS_DEVICE_NOT_CONNECTED

</td>
STATUS_DEVICE_NOT_CONNECTED</p>STATUS_DEVICE_NOT_CONNECTED

<td>
If a cached connection was specified, there are no cached records available. Otherwise, the
         connection was canceled before it completed.

</td>
If a cached connection was specified, there are no cached records available. Otherwise, the
         connection was canceled before it completed.</p>If a cached connection was specified, there are no cached records available. Otherwise, the
         connection was canceled before it completed.


<tr>
<td>
STATUS_INSUFFICIENT_RESOURCES

</td>
<td>
There was not enough memory available to process the request.

</td>
</tr>
<td>
STATUS_INSUFFICIENT_RESOURCES

</td>
STATUS_INSUFFICIENT_RESOURCES</p>STATUS_INSUFFICIENT_RESOURCES

<td>
There was not enough memory available to process the request.

</td>
There was not enough memory available to process the request.</p>There was not enough memory available to process the request.


<tr>
<td>
STATUS_INVALID_PARAMETER

</td>
<td>
A portion of the structure found in the input buffer was incorrect.

</td>
</tr>
<td>
STATUS_INVALID_PARAMETER

</td>
STATUS_INVALID_PARAMETER</p>STATUS_INVALID_PARAMETER

<td>
A portion of the structure found in the input buffer was incorrect.

</td>
A portion of the structure found in the input buffer was incorrect.</p>A portion of the structure found in the input buffer was incorrect.


<tr>
<td>
STATUS_PENDING

</td>
<td>
The system cannot currently respond, but will attempt to shortly.

</td>
</tr>
<td>
STATUS_PENDING

</td>
STATUS_PENDING</p>STATUS_PENDING

<td>
The system cannot currently respond, but will attempt to shortly.

</td>
The system cannot currently respond, but will attempt to shortly.</p>The system cannot currently respond, but will attempt to shortly.



 </p> 


## -remarks
The IOCTL_BTH_SDP_CONNECT request allows a profile driver to obtain an SDP connection handle to a
    remote device. After the SDP connection handle is obtained, the profile driver can pass it to other SDP
    IOCTL interfaces to gather information about the remote device's SDP server. When the SDP queries are
    completed, the profile driver must close the SDP connection with 
    <a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_disconnect.md">IOCTL_BTH_SDP_DISCONNECT</a>.


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
<a href="bltooth.bth_sdp_connect">BTH_SDP_CONNECT</a>
</dt>
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_disconnect.md">IOCTL_BTH_SDP_DISCONNECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20IOCTL_BTH_SDP_CONNECT control code%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

