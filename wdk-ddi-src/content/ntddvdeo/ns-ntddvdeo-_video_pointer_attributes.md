---
UID : NS:ntddvdeo._VIDEO_POINTER_ATTRIBUTES
title : _VIDEO_POINTER_ATTRIBUTES
author : windows-driver-content
description : The VIDEO_POINTER_ATTRIBUTES structure contains attributes of the screen pointer.
old-location : display\video_pointer_attributes.htm
old-project : display
ms.assetid : aa897435-443b-4145-b6ca-7bafdb36b9c1
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _VIDEO_POINTER_ATTRIBUTES, *PVIDEO_POINTER_ATTRIBUTES, VIDEO_POINTER_ATTRIBUTES
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
req.alt-api : VIDEO_POINTER_ATTRIBUTES
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
req.typenames : "*PVIDEO_POINTER_ATTRIBUTES, VIDEO_POINTER_ATTRIBUTES"
---

# _VIDEO_POINTER_ATTRIBUTES structure
The VIDEO_POINTER_ATTRIBUTES structure contains attributes of the screen pointer.

## Syntax
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

## Members

        
            `Column`

            Horizontal coordinate of the pointer's hot spot.
        
            `Enable`

            Specifies whether the pointer is visible. A nonzero value specifies that the pointer is visible. A value of zero specifies that the pointer is not visible.
        
            `Flags`

            A set of flags that specify certain attributes of the pointer. <b>Flags</b> can be a combination of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Height`

            Specifies the height of the pointer in pixels.
        
            `Pixels`

            The pointer data, in device-compatible DIB format. Mask data is always in 1-bpp DIB format.
        
            `Row`

            Vertical coordinate of the pointer's hot spot.
        
            `Width`

            Specifies the width of the pointer in pixels.
        
            `WidthInBytes`

            Specifies the width of the pointer in bytes.


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
<a href="..\ntddvdeo\ni-ntddvdeo-ioctl_video_query_pointer_attr.md">IOCTL_VIDEO_QUERY_POINTER_ATTR</a>
</dt>
<dt>
<a href="..\ntddvdeo\ni-ntddvdeo-ioctl_video_set_pointer_attr.md">IOCTL_VIDEO_SET_POINTER_ATTR</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_POINTER_ATTRIBUTES structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>