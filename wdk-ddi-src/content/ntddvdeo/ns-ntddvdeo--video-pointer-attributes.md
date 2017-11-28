---
UID: NS.ntddvdeo._VIDEO_POINTER_ATTRIBUTES
title: VIDEO_POINTER_ATTRIBUTES
author: windows-driver-content
description: The VIDEO_POINTER_ATTRIBUTES structure contains attributes of the screen pointer.
old-location: display\video_pointer_attributes.htm
old-project: display
ms.assetid: aa897435-443b-4145-b6ca-7bafdb36b9c1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_POINTER_ATTRIBUTES, VIDEO_POINTER_ATTRIBUTES, *PVIDEO_POINTER_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_POINTER_ATTRIBUTES
req.alt-loc: ntddvdeo.h
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

# VIDEO_POINTER_ATTRIBUTES structure



## -description
<p>The VIDEO_POINTER_ATTRIBUTES structure contains attributes of the screen pointer.</p>


## -syntax

````
typedef struct _VIDEO_POINTER_ATTRIBUTES {
  ULONG Flags;
  ULONG Width;
  ULONG Height;
  ULONG WidthInBytes;
  ULONG Enable;
  SHORT Column;
  SHORT Row;
  UCHAR Pixels[1];
} VIDEO_POINTER_ATTRIBUTES, *PVIDEO_POINTER_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>A set of flags that specify certain attributes of the pointer. <b>Flags</b> can be a combination of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="VIDEO_MODE_ASYNC_POINTER"></a><a id="video_mode_async_pointer"></a><dl>

### -field <b>VIDEO_MODE_ASYNC_POINTER</b>

</dl>
</td>
<td width="60%">
<p>The pointer can be updated asynchronously to drawing operations.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="VIDEO_MODE_MONO_POINTER"></a><a id="video_mode_mono_pointer"></a><dl>

### -field <b>VIDEO_MODE_MONO_POINTER</b>

</dl>
</td>
<td width="60%">
<p>A monochrome hardware pointer is supported.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="VIDEO_MODE_COLOR_POINTER"></a><a id="video_mode_color_pointer"></a><dl>

### -field <b>VIDEO_MODE_COLOR_POINTER</b>

</dl>
</td>
<td width="60%">
<p>A color hardware pointer is supported.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="VIDEO_MODE_ANIMATE_START"></a><a id="video_mode_animate_start"></a><dl>

### -field <b>VIDEO_MODE_ANIMATE_START</b>

</dl>
</td>
<td width="60%">
<p>The current pointer has the same hotspot as the previous pointer.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="VIDEO_MODE_ANIMATE_UPDATE"></a><a id="video_mode_animate_update"></a><dl>

### -field <b>VIDEO_MODE_ANIMATE_UPDATE</b>

</dl>
</td>
<td width="60%">
<p>The current pointer has the same hotspot as the previous pointer.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Width</b>

<dd>
<p>Specifies the width of the pointer in pixels.</p>
</dd>

### -field <b>Height</b>

<dd>
<p>Specifies the height of the pointer in pixels.</p>
</dd>

### -field <b>WidthInBytes</b>

<dd>
<p>Specifies the width of the pointer in bytes.</p>
</dd>

### -field <b>Enable</b>

<dd>
<p>Specifies whether the pointer is visible. A nonzero value specifies that the pointer is visible. A value of zero specifies that the pointer is not visible.</p>
</dd>

### -field <b>Column</b>

<dd>
<p>Horizontal coordinate of the pointer's hot spot.</p>
</dd>

### -field <b>Row</b>

<dd>
<p>Vertical coordinate of the pointer's hot spot.</p>
</dd>

### -field <b>Pixels</b>

<dd>
<p>The pointer data, in device-compatible DIB format. Mask data is always in 1-bpp DIB format.</p>
</dd>
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
<dt>Ntddvdeo.h (include Ntddvdeo.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567825">IOCTL_VIDEO_QUERY_POINTER_ATTR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568144">IOCTL_VIDEO_SET_POINTER_ATTR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_POINTER_ATTRIBUTES structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
