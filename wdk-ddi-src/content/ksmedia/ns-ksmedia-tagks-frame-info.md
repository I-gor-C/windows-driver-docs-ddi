---
UID: NS.ksmedia.tagKS_FRAME_INFO
title: tagKS_FRAME_INFO
author: windows-driver-content
description: The KS_FRAME_INFO structure extends the KSSTREAM_HEADER structure for video streams.
old-location: stream\ks_frame_info.htm
old-project: stream
ms.assetid: 7c2ebe5d-ecb0-41d2-a1bb-7e131ea350a7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagKS_FRAME_INFO, KS_FRAME_INFO, *PKS_FRAME_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_FRAME_INFO
req.alt-loc: ksmedia.h
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
---

# tagKS_FRAME_INFO structure



## -description
<p>The <b>KS_FRAME_INFO</b> structure extends the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567138">KSSTREAM_HEADER</a> structure for video streams.</p>


## -syntax

````
typedef struct tagKS_FRAME_INFO {
  ULONG    ExtendedHeaderSize;
  DWORD    dwFrameFlags;
  LONGLONG PictureNumber;
  LONGLONG DropCount;
  HANDLE   hDirectDraw;
  HANDLE   hSurfaceHandle;
  RECT     DirectDrawRect;
  union {
    LONG  lSurfacePitch;
    DWORD Reserved1;
  };
  DWORD    Reserved2;
  union {
    struct {
      DWORD Reserved3;
      DWORD Reserved4;
    };
    ULONGLONG FrameCompletionNumber;
  };
} KS_FRAME_INFO, *PKS_FRAME_INFO;
````


## -struct-fields
<dl>

### -field <b>ExtendedHeaderSize</b>

<dd>
<p>Specifies the size of this structure, in bytes.</p>
</dd>

### -field <b>dwFrameFlags</b>

<dd>
<p>Specifies flags indicating additional information about the frame captured. During capture, the minidriver sets this member to one of the following values that are defined in <i>ksmedia.h</i>:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KS_VIDEO_FLAG_FRAME</p>
</td>
<td>
<p>Indicates a complete frame.</p>
</td>
</tr>
<tr>
<td>
<p>KS_VIDEO_FLAG_FIELD1</p>
</td>
<td>
<p>Indicates Field 1 of a two-field sequence.</p>
</td>
</tr>
<tr>
<td>
<p>KS_VIDEO_FLAG_FIELD2</p>
</td>
<td>
<p>Indicates Field 2 of a two-field sequence.</p>
</td>
</tr>
<tr>
<td>
<p>KS_VIDEO_FLAG_I_FRAME</p>
</td>
<td>
<p>Indicates that this frame can be completely decoded without reference to any other frames.</p>
</td>
</tr>
<tr>
<td>
<p>KS_VIDEO_FLAG_P_FRAME</p>
</td>
<td>
<p>Indicates that this is a predicted frame.</p>
</td>
</tr>
<tr>
<td>
<p>KS_VIDEO_FLAG_B_FRAME</p>
</td>
<td>
<p>Indicates that this is a bidirectional frame.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PictureNumber</b>

<dd>
<p>Specifies a count representing the current picture number. Initialize or update this value on transition into KSSTATE_ACQUIRE.</p>
</dd>

### -field <b>DropCount</b>

<dd>
<p>Specifies the number of pictures that were not captured. During capture, the minidriver sets this member. This counter should be incremented whenever a frame should have been captured but was not; this condition usually arises when no buffers were available during capture. Initialize or update this value on transition into KSSTATE_ACQUIRE.</p>
</dd>

### -field <b>hDirectDraw</b>

<dd>
<p>Specifies the user-mode handle to DirectDraw. This handle is only provided to the minidriver when capturing to a DirectDraw surface for preview or overlay purposes.</p>
</dd>

### -field <b>hSurfaceHandle</b>

<dd>
<p>Specifies the user-mode handle to the DirectDraw surface. This handle is only provided to the minidriver when capturing to a DirectDraw surface for preview or overlay purposes.</p>
</dd>

### -field <b>DirectDrawRect</b>

<dd>
<p>Specifies the portion of the DirectDraw surface that has been locked. This is normally the entire surface.</p>
</dd>

### -field <b>lSurfacePitch</b>

<dd>
<p>Contains surface pitch a.k.a stride</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved and should not be used by the minidriver.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved and should not be used by the minidriver.</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved and should not be used by the minidriver.</p>
</dd>

### -field <b>Reserved4</b>

<dd>
<p>Reserved and should not be used by the minidriver.</p>
</dd>

### -field <b>FrameCompletionNumber</b>

<dd>
<p>An identifying sequence number for the frame in the completed queue. This number is used to verify proper frame order. When this value is 0, the frame was cancelled.</p>
<p>This member is available starting with Windows 8.1.</p>
</dd>
</dl>

## -remarks
<p>The KS_FRAME_INFO structure provides a way to return information about the frame captured, as well as a way to pass Microsoft DirectDraw handles used when capturing to a DirectDraw surface.</p>

<p>The <b>PictureNumber</b> member count represents the count of the current picture, which is calculated in one of two ways depending on the device:</p>

<p>Measure the time since the stream was started and divide by the frame duration. This method is appropriate for devices that do not provide their own clock. For example: </p>

<p>Add together the count of frames captured and the count of frame dropped. This method is appropriate for devices that provide their own clock. For example: </p>

<p>When calculating <b>PictureNumber</b> and <b>DropCount</b>, it is important to use the frame duration specified when the stream was opened, which may not necessarily match the rate at which the device is actually producing images. For example, a USB camera may only produce images at 7.5 fps, but a client could open the stream at 8 fps. In this case, all calculations should use the 8 fps number. </p>

<p>For more information about updating <b>PictureNumber</b> and <b>DropCount</b> see <a href="NULL">Capturing Video</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567138">KSSTREAM_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_FRAME_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
