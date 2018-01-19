---
UID : NS:ntddvdeo._VIDEO_MODE_INFORMATION
title : _VIDEO_MODE_INFORMATION
author : windows-driver-content
description : The VIDEO_MODE_INFORMATION structure contains all of the information about one mode of a video adapter.
old-location : display\video_mode_information.htm
old-project : display
ms.assetid : aac658d9-b90a-4724-9dc4-af3a561f64bd
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _VIDEO_MODE_INFORMATION, VIDEO_MODE_INFORMATION, *PVIDEO_MODE_INFORMATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddvdeo.h
req.include-header : Ntddvdeo.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : VIDEO_MODE_INFORMATION
req.alt-loc : ntddvdeo.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : VIDEO_MODE_INFORMATION, *PVIDEO_MODE_INFORMATION
---

# _VIDEO_MODE_INFORMATION structure
The VIDEO_MODE_INFORMATION structure contains all of the information about one mode of a video adapter.

## Syntax
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

## Members

        
            `AttributeFlags`

            Is a set of flags indicating certain behavior for the device. The flags and their meanings are shown in the following table.

<table>
<tr>
<th>Flag Name</th>
<th>Flag Value</th>
<th>Bit Number</th>
<th>Bit Value and Meaning</th>
</tr>
<tr>
<td>
VIDEO_MODE_COLOR

</td>
<td>
0x0001

</td>
<td>
0

</td>
<td>
        
            `BitsPerPlane`

            Specifies the number of bits per pixel per plane.
        
            `BlueMask`

            Is the blue color mask for a device with direct color modes. For example, to indicate that bits 10 through 14 are to be used for blue, use the value 0x7C00.
        
            `DriverSpecificAttributeFlags`

            Is a set of flags indicating certain behavior for the device. These private flags are defined in the miniport driver, and are for the use by the miniport and display drivers only.
        
            `Frequency`

            Specifies the screen refresh rate, in Hertz.
        
            `GreenMask`

            Is the green color mask for a device with direct color modes. For example, to indicate that bits 5 through 9 are to be used for green, use the value 0x03E0.
        
            `Length`

            Specifies the length, in bytes, of this structure. A miniport driver can use this value to determine the version of this structure.
        
            `ModeIndex`

            Specifies the index of the particular mode to be used in a call to the miniport driver.
        
            `NumberBlueBits`

            Specifies the number of bits in the blue DAC.
        
            `NumberGreenBits`

            Specifies the number of bits in the green DAC.
        
            `NumberOfPlanes`

            Specifies the number of separate planes combined by the device.
        
            `NumberRedBits`

            Specifies the number of bits in the red DAC.
        
            `RedMask`

            Is the red color mask for a device with direct color modes. For example, to indicate that bits 0 through 4 are to be used for red, use the value 0x001F.
        
            `ScreenStride`

            Specifies the number of bytes between the start of one scan line and the next.
        
            `VideoMemoryBitmapHeight`

            Specifies the height, in pixels, of the video memory bitmap.
        
            `VideoMemoryBitmapWidth`

            Specifies the width, in pixels, of the video memory bitmap.
        
            `VisScreenHeight`

            Specifies the number of visible lines (or scan lines) on the screen.
        
            `VisScreenWidth`

            Specifies the number of visible pixels on one horizontal scan line.
        
            `XMillimeter`

            Specifies the width, in millimeters, of the active region on the output device.
        
            `YMillimeter`

            Specifies the height, in millimeters, of the active region on the output device.

    ## Remarks
        The video miniport driver returns an array of VIDEO_MODE_INFORMATION structures in response to an <a href="..\ntddvdeo\ni-ntddvdeo-ioctl_video_query_avail_modes.md">IOCTL_VIDEO_QUERY_AVAIL_MODES</a> request, with each structure containing information about one mode of the adapter. The miniport driver returns one VIDEO_MODE_INFORMATION structure that contains information about the adapter's current mode in response to an <a href="..\ntddvdeo\ni-ntddvdeo-ioctl_video_query_current_mode.md">IOCTL_VIDEO_QUERY_CURRENT_MODE</a> request.


<dl>
<dt>Three members of VIDEO_MODE_INFORMATION, <b>VisScreenWidth</b>, <b>VideoMemoryBitmapWidth</b>, and <b>ScreenStride</b>, are associated with horizontal screen width. For displays that use one or more bytes per pixel, these members satisfy the inequality </dt>
<dt><b>VisScreenWidth</b> &lt;= <b>VideoMemoryBitmapWidth</b> &lt;= <b>ScreenStride</b>.</dt>
</dl>



<dl>
<dt>In a similar relationship for vertical screen height, <b>VisScreenHeight</b> and <b>VideoMemoryBitmapHeight</b> satisfy the inequality</dt>
<dt><b>VisScreenHeight</b> &lt;= <b>VideoMemoryBitmapHeight</b>.</dt>
</dl>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddvdeo.h (include Ntddvdeo.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddvdeo\ns-ntddvdeo-_video_memory_information.md">VIDEO_MEMORY_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddvdeo\ni-ntddvdeo-ioctl_video_query_avail_modes.md">IOCTL_VIDEO_QUERY_AVAIL_MODES</a>
</dt>
<dt>
<a href="..\ntddvdeo\ni-ntddvdeo-ioctl_video_query_current_mode.md">IOCTL_VIDEO_QUERY_CURRENT_MODE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_MODE_INFORMATION structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>