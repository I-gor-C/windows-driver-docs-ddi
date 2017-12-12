---
UID: NI.bthioctl.IOCTL_BTH_SDP_ATTRIBUTE_SEARCH
title: IOCTL_BTH_SDP_ATTRIBUTE_SEARCH
author: windows-driver-content
description: The IOCTL_BTH_SDP_ATTRIBUTE_SEARCH request obtains attributes for the specified SDP record.
old-location: bltooth\ioctl_bth_sdp_attribute_search.htm
old-project: bltooth
ms.assetid: 30daf70e-34d1-45f7-a69b-503e275b83af
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
req.alt-api: IOCTL_BTH_SDP_ATTRIBUTE_SEARCH
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

# IOCTL_BTH_SDP_ATTRIBUTE_SEARCH IOCTL



## -description

The IOCTL_BTH_SDP_ATTRIBUTE_SEARCH request obtains attributes for the specified SDP record.



The IOCTL_BTH_SDP_ATTRIBUTE_SEARCH request obtains attributes for the specified SDP record.



## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member contains a 
      <a href="bltooth.bth_sdp_attribute_search_request">
      BTH_SDP_ATTRIBUTE_SEARCH_REQUEST</a> structure that specifies the remote computer range of attributes
      to search plus other key members.</p>The 
      <b>AssociatedIrp.SystemBuffer</b>AssociatedIrp.SystemBuffer member contains a 
      <a href="bltooth.bth_sdp_attribute_search_request">
      BTH_SDP_ATTRIBUTE_SEARCH_REQUEST</a><b>
      BTH_SDP_ATTRIBUTE_SEARCH_REQUEST</b>
      BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure that specifies the remote computer range of attributes
      to search plus other key members.


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that contains a 
      <a href="bltooth.bth_sdp_stream_response">BTH_SDP_STREAM_RESPONSE</a> structure
      that is followed by a variable-length raw SDP stream.</p>The 
      <b>AssociatedIrp.SystemBuffer</b>AssociatedIrp.SystemBuffer member points to a buffer that contains a 
      <a href="bltooth.bth_sdp_stream_response">BTH_SDP_STREAM_RESPONSE</a><b>BTH_SDP_STREAM_RESPONSE</b>BTH_SDP_STREAM_RESPONSE structure
      that is followed by a variable-length raw SDP stream.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
If the request is successful, the 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size, in bytes, of the 
      <a href="bltooth.bth_sdp_stream_response">BTH_SDP_STREAM_RESPONSE</a> or the size
      of the output buffer, whichever is smaller. Otherwise, the 
      <b>Information</b> member is set to zero.</p>If the request is successful, the 
      <b>Information</b>Information member of the STATUS_BLOCK structure is set to the size, in bytes, of the 
      <a href="bltooth.bth_sdp_stream_response">BTH_SDP_STREAM_RESPONSE</a><b>BTH_SDP_STREAM_RESPONSE</b>BTH_SDP_STREAM_RESPONSE or the size
      of the output buffer, whichever is smaller. Otherwise, the 
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
STATUS_DEVICE_NOT_CONNECTED

</td>
<td>
The device on which the SDP service resides was not connected.

</td>
</tr>
<tr>
<td>
STATUS_INSUFFICIENT_RESOURCES

</td>
<td>
There was not enough memory to complete this operation.

</td>
</tr>
<tr>
<td>
STATUS_INVALID_BUFFER_SIZE

</td>
<td>
The output buffer was sized incorrectly.

</td>
</tr>
<tr>
<td>
STATUS_INVALID_PARAMETER

</td>
<td>
One of the values in the input buffer was not valid.

</td>
</tr>
<tr>
<td>
STATUS_REQUEST_NOT_ACCEPTED

</td>
<td>
The SDP service rejected the request.

</td>
</tr>
<tr>
<td>
STATUS_TOO_MANY_GUIDS_REQUESTED

</td>
<td>
The SDP service could not process the number of GUIDs passed in the input buffer.

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
The device on which the SDP service resides was not connected.

</td>
</tr>
<td>
STATUS_DEVICE_NOT_CONNECTED

</td>
STATUS_DEVICE_NOT_CONNECTED</p>STATUS_DEVICE_NOT_CONNECTED

<td>
The device on which the SDP service resides was not connected.

</td>
The device on which the SDP service resides was not connected.</p>The device on which the SDP service resides was not connected.


<tr>
<td>
STATUS_INSUFFICIENT_RESOURCES

</td>
<td>
There was not enough memory to complete this operation.

</td>
</tr>
<td>
STATUS_INSUFFICIENT_RESOURCES

</td>
STATUS_INSUFFICIENT_RESOURCES</p>STATUS_INSUFFICIENT_RESOURCES

<td>
There was not enough memory to complete this operation.

</td>
There was not enough memory to complete this operation.</p>There was not enough memory to complete this operation.


<tr>
<td>
STATUS_INVALID_BUFFER_SIZE

</td>
<td>
The output buffer was sized incorrectly.

</td>
</tr>
<td>
STATUS_INVALID_BUFFER_SIZE

</td>
STATUS_INVALID_BUFFER_SIZE</p>STATUS_INVALID_BUFFER_SIZE

<td>
The output buffer was sized incorrectly.

</td>
The output buffer was sized incorrectly.</p>The output buffer was sized incorrectly.


<tr>
<td>
STATUS_INVALID_PARAMETER

</td>
<td>
One of the values in the input buffer was not valid.

</td>
</tr>
<td>
STATUS_INVALID_PARAMETER

</td>
STATUS_INVALID_PARAMETER</p>STATUS_INVALID_PARAMETER

<td>
One of the values in the input buffer was not valid.

</td>
One of the values in the input buffer was not valid.</p>One of the values in the input buffer was not valid.


<tr>
<td>
STATUS_REQUEST_NOT_ACCEPTED

</td>
<td>
The SDP service rejected the request.

</td>
</tr>
<td>
STATUS_REQUEST_NOT_ACCEPTED

</td>
STATUS_REQUEST_NOT_ACCEPTED</p>STATUS_REQUEST_NOT_ACCEPTED

<td>
The SDP service rejected the request.

</td>
The SDP service rejected the request.</p>The SDP service rejected the request.


<tr>
<td>
STATUS_TOO_MANY_GUIDS_REQUESTED

</td>
<td>
The SDP service could not process the number of GUIDs passed in the input buffer.

</td>
</tr>
<td>
STATUS_TOO_MANY_GUIDS_REQUESTED

</td>
STATUS_TOO_MANY_GUIDS_REQUESTED</p>STATUS_TOO_MANY_GUIDS_REQUESTED

<td>
The SDP service could not process the number of GUIDs passed in the input buffer.

</td>
The SDP service could not process the number of GUIDs passed in the input buffer.</p>The SDP service could not process the number of GUIDs passed in the input buffer.



 </p> 


## -remarks
In most circumstances, profile drivers can combine SDP service and attribute searches by calling the 
    <a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_service_attribute_search.md">
    IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH</a> IOCTL. If a profile driver must reduce the amount of SDP
    traffic that is transmitted over the Bluetooth link, or extract information from the SDP server by using
    a small number of message transfer units (MTUs), the profile driver should call the 
    <a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_service_search.md">
    IOCTL_BTH_SDP_SERVICE_SEARCH</a> IOCTL to perform a service search. The profile driver should then call
    the IOCTL_BTH_SDP_ATTRIBUTE_SEARCH IOCTL to perform an attribute search.

The BTH_SDP_STREAM_RESPONSE structure returned in the output buffer contains information about the
    size of the entire SDP record, the size, in bytes, of the raw SDP record stream that follows the
    BTH_SDP_STREAM_RESPONSE structure, and the first byte of that stream. The variable-length stream is the
    SDP record attributes returned by the search.


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
<a href="bltooth.bth_sdp_attribute_search_request">
   BTH_SDP_ATTRIBUTE_SEARCH_REQUEST</a>
</dt>
<dt>
<a href="bltooth.bth_sdp_stream_response">BTH_SDP_STREAM_RESPONSE</a>
</dt>
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_service_attribute_search.md">
   IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH</a>
</dt>
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_service_search.md">IOCTL_BTH_SDP_SERVICE_SEARCH</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20IOCTL_BTH_SDP_ATTRIBUTE_SEARCH control code%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

