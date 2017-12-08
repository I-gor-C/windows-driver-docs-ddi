---
UID: NS.ntddvdeo._VIDEO_MODE_INFORMATION
title: VIDEO_MODE_INFORMATION
author: windows-driver-content
description: The VIDEO_MODE_INFORMATION structure contains all of the information about one mode of a video adapter.
old-location: display\video_mode_information.htm
old-project: display
ms.assetid: aac658d9-b90a-4724-9dc4-af3a561f64bd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_MODE_INFORMATION, VIDEO_MODE_INFORMATION, *PVIDEO_MODE_INFORMATION
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
req.alt-api: VIDEO_MODE_INFORMATION
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

# VIDEO_MODE_INFORMATION structure



## -description
<p>The VIDEO_MODE_INFORMATION structure contains all of the information about one mode of a video adapter.</p>


## -syntax

````
typedef struct _VIDEO_MODE_INFORMATION {
  ULONG Length;
  ULONG ModeIndex;
  ULONG VisScreenWidth;
  ULONG VisScreenHeight;
  ULONG ScreenStride;
  ULONG NumberOfPlanes;
  ULONG BitsPerPlane;
  ULONG Frequency;
  ULONG XMillimeter;
  ULONG YMillimeter;
  ULONG NumberRedBits;
  ULONG NumberGreenBits;
  ULONG NumberBlueBits;
  ULONG RedMask;
  ULONG GreenMask;
  ULONG BlueMask;
  ULONG AttributeFlags;
  ULONG VideoMemoryBitmapWidth;
  ULONG VideoMemoryBitmapHeight;
  ULONG DriverSpecificAttributeFlags;
} VIDEO_MODE_INFORMATION, *PVIDEO_MODE_INFORMATION;
````


## -struct-fields
<dl>

### -field Length

<dd>
<p>Specifies the length, in bytes, of this structure. A miniport driver can use this value to determine the version of this structure. </p>
</dd>

### -field ModeIndex

<dd>
<p>Specifies the index of the particular mode to be used in a call to the miniport driver.</p>
</dd>

### -field VisScreenWidth

<dd>
<p>Specifies the number of visible pixels on one horizontal scan line.</p>
</dd>

### -field VisScreenHeight

<dd>
<p>Specifies the number of visible lines (or scan lines) on the screen.</p>
</dd>

### -field ScreenStride

<dd>
<p>Specifies the number of bytes between the start of one scan line and the next.</p>
</dd>

### -field NumberOfPlanes

<dd>
<p>Specifies the number of separate planes combined by the device.</p>
</dd>

### -field BitsPerPlane

<dd>
<p>Specifies the number of bits per pixel per plane.</p>
</dd>

### -field Frequency

<dd>
<p>Specifies the screen refresh rate, in Hertz.</p>
</dd>

### -field XMillimeter

<dd>
<p>Specifies the width, in millimeters, of the active region on the output device.</p>
</dd>

### -field YMillimeter

<dd>
<p>Specifies the height, in millimeters, of the active region on the output device.</p>
</dd>

### -field NumberRedBits

<dd>
<p>Specifies the number of bits in the red DAC.</p>
</dd>

### -field NumberGreenBits

<dd>
<p>Specifies the number of bits in the green DAC.</p>
</dd>

### -field NumberBlueBits

<dd>
<p>Specifies the number of bits in the blue DAC.</p>
</dd>

### -field RedMask

<dd>
<p>Is the red color mask for a device with direct color modes. For example, to indicate that bits 0 through 4 are to be used for red, use the value 0x001F.</p>
</dd>

### -field GreenMask

<dd>
<p>Is the green color mask for a device with direct color modes. For example, to indicate that bits 5 through 9 are to be used for green, use the value 0x03E0.</p>
</dd>

### -field BlueMask

<dd>
<p>Is the blue color mask for a device with direct color modes. For example, to indicate that bits 10 through 14 are to be used for blue, use the value 0x7C00.</p>
</dd>

### -field AttributeFlags

<dd>
<p>Is a set of flags indicating certain behavior for the device. The flags and their meanings are shown in the following table.</p>
<table>
<tr>
<th>Flag Name</th>
<th>Flag Value</th>
<th>Bit Number</th>
<th>Bit Value and Meaning</th>
</tr>
<tr>
<td>
<p>VIDEO_MODE_COLOR</p>
</td>
<td>
<p>0x0001</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>
<dl>

### -field 0 = Mono-compatible


### -field 1 = Color

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_GRAPHICS</p>
</td>
<td>
<p>0x0002</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>
<dl>

### -field 0 = Text mode


### -field 1 = Graphics

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_PALETTE_DRIVEN</p>
</td>
<td>
<p>0x0004</p>
</td>
<td>
<p>2</p>
</td>
<td>
<p>
<dl>

### -field 0 = Colors are direct


### -field 1 = Colors are indexed to a palette

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_MANAGED_PALETTE</p>
</td>
<td>
<p>0x0008</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p>
<dl>

### -field 0 = Palette is fixed (must be queried from miniport driver)


### -field 1 = Palette is settable

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_INTERLACED</p>
</td>
<td>
<p>0x0010</p>
</td>
<td>
<p>4</p>
</td>
<td>
<p>
<dl>

### -field 0 = Non-interlaced mode


### -field 1 = Interlaced mode

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_NO_OFF_SCREEN</p>
</td>
<td>
<p>0x0020</p>
</td>
<td>
<p>5</p>
</td>
<td>
<p>
<dl>

### -field 0 = Offscreen memory is available


### -field 1 = Offscreen memory cannot be used to store information

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_NO_64_BIT_ACCESS</p>
</td>
<td>
<p>0x0040</p>
</td>
<td>
<p>6</p>
</td>
<td>
<p>
<dl>

### -field 0 = 64-bit memory writes to frame buffer are handled properly


### -field 1 = 64-bit memory writes to frame buffer are not handled

</dl>
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field VideoMemoryBitmapWidth

<dd>
<p>Specifies the width, in pixels, of the video memory bitmap. </p>
</dd>

### -field VideoMemoryBitmapHeight

<dd>
<p>Specifies the height, in pixels, of the video memory bitmap.</p>
</dd>

### -field DriverSpecificAttributeFlags

<dd>
<p>Is a set of flags indicating certain behavior for the device. These private flags are defined in the miniport driver, and are for the use by the miniport and display drivers only.</p>
</dd>
</dl>

## -remarks
<p>The video miniport driver returns an array of VIDEO_MODE_INFORMATION structures in response to an <a href="..\ntddvdeo\ni-ntddvdeo-ioctl-video-query-avail-modes.md">IOCTL_VIDEO_QUERY_AVAIL_MODES</a> request, with each structure containing information about one mode of the adapter. The miniport driver returns one VIDEO_MODE_INFORMATION structure that contains information about the adapter's current mode in response to an <a href="..\ntddvdeo\ni-ntddvdeo-ioctl-video-query-current-mode.md">IOCTL_VIDEO_QUERY_CURRENT_MODE</a> request.</p>

<p>
<dl>
<dt>Three members of VIDEO_MODE_INFORMATION, <b>VisScreenWidth</b>, <b>VideoMemoryBitmapWidth</b>, and <b>ScreenStride</b>, are associated with horizontal screen width. For displays that use one or more bytes per pixel, these members satisfy the inequality </dt>
<dt><b>VisScreenWidth</b> &lt;= <b>VideoMemoryBitmapWidth</b> &lt;= <b>ScreenStride</b>.</dt>
</dl>
</p>

<p>
<dl>
<dt>In a similar relationship for vertical screen height, <b>VisScreenHeight</b> and <b>VideoMemoryBitmapHeight</b> satisfy the inequality</dt>
<dt><b>VisScreenHeight</b> &lt;= <b>VideoMemoryBitmapHeight</b>.</dt>
</dl>
</p>

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
<a href="..\ntddvdeo\ns-ntddvdeo--video-memory-information.md">VIDEO_MEMORY_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddvdeo\ni-ntddvdeo-ioctl-video-query-avail-modes.md">IOCTL_VIDEO_QUERY_AVAIL_MODES</a>
</dt>
<dt>
<a href="..\ntddvdeo\ni-ntddvdeo-ioctl-video-query-current-mode.md">IOCTL_VIDEO_QUERY_CURRENT_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_MODE_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
