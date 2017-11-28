---
UID: NS.61883._CIP_FRAME~r1
title: CIP_FRAME
author: windows-driver-content
description: The CIP_FRAME structure describes a frame to be attached to an input or output plug.
old-location: ieee\cip_frame.htm
old-project: IEEE
ms.assetid: ac9efa58-fd38-43f2-85e6-577d58735847
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: CIP_FRAME,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 61883.h
req.include-header: 61883.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CIP_FRAME
req.alt-loc: 61883.h
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
---

# CIP_FRAME structure



## -description
<p>The CIP_FRAME structure describes a frame to be attached to an input or output plug.  </p>


## -syntax

````
typedef struct _CIP_FRAME {
  union {
    PVOID Reserved;
    PVOID pNext;
  };
  ULONG                 Flags;
  PCIP_VALIDATE_ROUTINE pfnValidate;
  PVOID                 ValidateContext;
  PCIP_NOTIFY_ROUTINE   pfnNotify;
  PVOID                 NotifyContext;
  CYCLE_TIME            Timestamp;
  ULONG                 Status;
  PUCHAR                Packet;
  ULONG                 CompletedBytes;
} CIP_FRAME, *PCIP_FRAME;
````


## -struct-fields
<dl>

### -field <b>Reserved</b>

<dd></dd>

### -field <b>pNext</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies options associated with this frame. </p>
<p>For packets to be received, <b>Flags</b> can be one of the following:</p>
<p></p>
<dl>

### -field <a id="CIP_VALIDATE_FIRST_SOURCE"></a><a id="cip_validate_first_source"></a>CIP_VALIDATE_FIRST_SOURCE

<dd>
<p>Instructs the IEC-61883 protocol driver to call the client-driver-supplied function at <b>pfnValidate</b> to validate only the first source packet.</p>
</dd>

### -field <a id="CIP_VALIDATE_ALL_SOURCE"></a><a id="cip_validate_all_source"></a>CIP_VALIDATE_ALL_SOURCE

<dd>
<p>Instructs the IEC-61883 protocol driver to call the client-driver-supplied function at <b>pfnValidate</b> to validate all source packets.</p>
</dd>
</dl>
<p>For packets to be received, CIP_VALIDATE_XXX can be combined with either or both of the following:</p>
<p></p>
<dl>

### -field <a id="CIP_STRIP_SOURCE_HEADER"></a><a id="cip_strip_source_header"></a>CIP_STRIP_SOURCE_HEADER

<dd>
<p>Instructs the protocol driver to strip the source header packet within a source packet.</p>
</dd>

### -field <a id="CIP_USE_SOURCE_HEADER_TIMESTAMP"></a><a id="cip_use_source_header_timestamp"></a>CIP_USE_SOURCE_HEADER_TIMESTAMP

<dd>
<p>Instructs the protocol driver to timestamp the frame with the timestamp found within the source header packet.</p>
</dd>
</dl>
<p>For packets to be transmitted, <b>Flags</b> can be one of the following:</p>
<p></p>
<dl>

### -field <a id="CIP_DV_STYLE_SYT"></a><a id="cip_dv_style_syt"></a>CIP_DV_STYLE_SYT

<dd>
<p>The value at <b>TimeStamp</b> is formatted for data transmission to digital video devices (SD-DVCR, HD-DVCR, or SDL-DVCR).</p>
</dd>

### -field <a id="CIP_AUDIO_STYLE_SYT"></a><a id="cip_audio_style_syt"></a>CIP_AUDIO_STYLE_SYT

<dd>
<p>The value at <b>TimeStamp</b> is formatted for audio and music data transmission to audio devices.</p>
</dd>
</dl>
<p>For packets to be transmitted or received, <b>Flags</b> can also be set with the following:</p>
<p></p>
<dl>

### -field <a id="CIP_RESET_FRAME_ON_DISCONTINUITY"></a><a id="cip_reset_frame_on_discontinuity"></a>CIP_RESET_FRAME_ON_DISCONTINUITY

<dd>
<p>Instructs the protocol driver to resume a stopped stream at the beginning of the frame instead of the next source packet. </p>
</dd>
</dl>
</dd>

### -field <b>pfnValidate</b>

<dd>
<p>Points to a caller-supplied function to validate a source packet. This function uses the following prototype: The parameter <b>ValidateInfo</b> must point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537048">CIP_VALIDATE_INFO</a> structure that contains information about the frame. </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>ULONG 
  (*PCIP_VALIDATE_ROUTINE) ( 
    IN PCIP_VALIDATE_INFO ValidateInfo
   );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ValidateContext</b>

<dd>
<p>Points to an optional caller-defined context for the function at <b>pfnValidate</b>. If the function does not require a context, <b>ValidateContext</b> can be <b>NULL</b>.</p>
</dd>

### -field <b>pfnNotify</b>

<dd>
<p>Points to a caller-supplied function to be called by the protocol driver when the requested frame is completed. The protocol driver calls this function at IRQL = DISPATCH_LEVEL.</p>
<p>This function uses the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>ULONG 
  (*PCIP_NOTIFY_ROUTINE) ( 
     IN PCIP_NOTIFY_INFO NotifyInfo 
 );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="The_NotifyInfo_parameter_points_to_a_CIP_NOTIFY_INFO_structure_that_contains_information_about_the_frame._"></a><a id="the_notifyinfo_parameter_points_to_a_cip_notify_info_structure_that_contains_information_about_the_frame._"></a><a id="THE_NOTIFYINFO_PARAMETER_POINTS_TO_A_CIP_NOTIFY_INFO_STRUCTURE_THAT_CONTAINS_INFORMATION_ABOUT_THE_FRAME._"></a>The <i>NotifyInfo</i> parameter points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537046">CIP_NOTIFY_INFO</a> structure that contains information about the frame. 

<dd></dd>
</dl>
</dd>

### -field <b>NotifyContext</b>

<dd>
<p>Points to an optional caller-defined context for the caller-supplied function at <b>pfnNotify</b>. If the function does not require a context, <b>NotifyContext</b> can be <b>NULL</b>.</p>
</dd>

### -field <b>Timestamp</b>

<dd>
<p>The time associated with completion of the frame. </p>
<p>For packets to be received, the protocol driver sets this member to the time when transmission of the frame was completed, unless CIP_USE_SOURCE_HEADER_TIMESTAMP is set in <b>Flags</b>. </p>
<p>For packets to be transmitted, CIP-DV_STYLE_SYT or CIP_AUDIO_STYLE_SYT in <b>Flags</b> indicates the format of the timestamp.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>The status of the frame. Can be one of the following:</p>
<p>CIP_STATUS_SUCCESS</p>
<p>CIP_STATUS_CORRUPT_FRAME</p>
<p>CIP_STATUS_FIRST_FRAME</p>
</dd>

### -field <b>Packet</b>

<dd>
<p>Points to the beginning of a caller-allocated data buffer to be transmitted or received with this frame. The frame length specified in the associated <a href="https://msdn.microsoft.com/library/windows/hardware/ff536950">Av61883_AttachFrame</a> request indicates the size of the buffer.</p>
</dd>

### -field <b>CompletedBytes</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>61883.h (include 61883.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536950">Av61883_AttachFrame</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536956">Av61883_CancelFrame</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20CIP_FRAME structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
