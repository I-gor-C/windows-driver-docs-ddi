---
UID: NS.usbcamdi._pipe_config_descriptor
title: pipe_config_descriptor
author: windows-driver-content
description: The USBCAMD_Pipe_Config_Descriptor structure describes the association between pipes and streams.
old-location: stream\usbcamd_pipe_config_descriptor.htm
old-project: stream
ms.assetid: 8554a5d1-07ea-4ad5-83a4-f0c15386b3d1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: pipe_config_descriptor, USBCAMD_Pipe_Config_Descriptor, *PUSBCAMD_Pipe_Config_Descriptor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBCAMD_Pipe_Config_Descriptor
req.alt-loc: usbcamdi.h
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

# pipe_config_descriptor structure



## -description
<p>The <b>USBCAMD_Pipe_Config_Descriptor</b> structure describes the association between pipes and streams.</p>


## -syntax

````
typedef struct _pipe_config_descriptor {
  CHAR  StreamAssociation;
  UCHAR PipeConfigFlags;
} USBCAMD_Pipe_Config_Descriptor, *PUSBCAMD_Pipe_Config_Descriptor;
````


## -struct-fields
<dl>

### -field StreamAssociation

<dd>
<p>Specifies the type of stream. This should be set to one of the following values:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>USBCAMD_VIDEO_STREAM</p>
</td>
<td>
<p>Indicates that the stream contains video data.</p>
</td>
</tr>
<tr>
<td>
<p>USBCAMD_STILL_STREAM</p>
</td>
<td>
<p>Indicates that the stream contains still data.</p>
</td>
</tr>
<tr>
<td>
<p>USBCAMD_VIDEO_STILL_STREAM</p>
</td>
<td>
<p>Indicates that the stream contains both video and still data.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field PipeConfigFlags

<dd>
<p>Specifies the pipe characteristics. This should be set to one of the following values:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>USBCAMD_DATA_PIPE</p>
</td>
<td>
<p>Indicates a video or still data pipe.</p>
</td>
</tr>
<tr>
<td>
<p>USBCAMD_MULTIPLEX_PIPE</p>
</td>
<td>
<p>Indicates a video and still data pipe.</p>
</td>
</tr>
<tr>
<td>
<p>USBCAMD_SYNC_PIPE</p>
</td>
<td>
<p>Indicates an out-of-band signaling pipe.</p>
</td>
</tr>
<tr>
<td>
<p>USBCAMD_DONT_CARE_PIPE</p>
</td>
<td>
<p>Indicates a pipe that is not to be used for video or still streaming.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>The camera minidriver indicates pipe stream associations by identifying all streams associated with a particular pipe. If there is more than one stream association, USBCAMD creates a virtual still pin. The still stream pin always follows the video stream pin (that is, the video stream pin is the first stream pin). </p>

<p>The <a href="stream.camconfigureex">CamConfigureEx</a> routine uses the <b>USBCAMD_Pipe_Config_Descriptor</b> structure to establish a connection between pipes and streams. An array of USBCAMD_Pipe_Config_Descriptor structures is passed into <b>CamConfigureEx</b>, along with the array size, which is equal to the number of pipes found.</p>

<p>The camera minidriver must set the <b>PipeConfigFlags</b> member to the value USBCAMD_DONT_CARE_PIPE if a particular pipe should not be used by USBCAMD. For example, when using an audio and video isochronous pipe, and a camera device that supports stills and video, the <b>PipeConfigFlags</b> member in the first structure should be set to USBCAMD_DONT_CARE_PIPE. The second <b>USBCAMD_Pipe_Config_Descriptor</b> structure should have its <b>StreamAssociation</b> member value set to USBCAMD_VIDEO_STILL_STREAM and its <b>PipeConfigFlags</b> member value set to USBCAMD_MULTIPLEX_PIPE.</p>

<p>The USBCAMD library requires that the camera must have a single configuration description, and all alternate settings within the USB video streaming interface must have the same number and type of pipes.</p>

<p><b>USBCAMD_Pipe_Config_Descriptor</b> is not supported in the original USBCAMD.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.camconfigureex">CamConfigureEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_Pipe_Config_Descriptor structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
