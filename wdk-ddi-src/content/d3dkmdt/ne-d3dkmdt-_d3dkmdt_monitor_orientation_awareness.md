---
UID: NE:d3dkmdt._D3DKMDT_MONITOR_ORIENTATION_AWARENESS
title: "_D3DKMDT_MONITOR_ORIENTATION_AWARENESS"
author: windows-driver-content
description: The D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration is used to describe the ability of a video output device (on the display adapter) to detect changes in the orientation (rotation angle) of a connected external display device.
old-location: display\d3dkmdt_monitor_orientation_awareness.htm
old-project: display
ms.assetid: cea11e84-bff5-4189-9ed4-830049a44a4b
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: D3DKMDT_MOA_INTERRUPTIBLE, D3DKMDT_MOA_NONE, D3DKMDT_MOA_POLLED, D3DKMDT_MOA_UNINITIALIZED, D3DKMDT_MONITOR_ORIENTATION_AWARENESS, D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration [Display Devices], DmEnums_d2570bc0-98c7-4402-b167-a4167715cc90.xml, _D3DKMDT_MONITOR_ORIENTATION_AWARENESS, d3dkmdt/D3DKMDT_MOA_INTERRUPTIBLE, d3dkmdt/D3DKMDT_MOA_NONE, d3dkmdt/D3DKMDT_MOA_POLLED, d3dkmdt/D3DKMDT_MOA_UNINITIALIZED, d3dkmdt/D3DKMDT_MONITOR_ORIENTATION_AWARENESS, display.d3dkmdt_monitor_orientation_awareness
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmdt.h
api_name:
-	D3DKMDT_MONITOR_ORIENTATION_AWARENESS
product: Windows
targetos: Windows
req.typenames: D3DKMDT_MONITOR_ORIENTATION_AWARENESS
---

# _D3DKMDT_MONITOR_ORIENTATION_AWARENESS Enumeration
The D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration is used to describe the ability of a video output device (on the display adapter) to detect changes in the orientation (rotation angle) of a connected external display device.

## Syntax
````
typedef enum _D3DKMDT_MONITOR_ORIENTATION_AWARENESS { 
  D3DKMDT_MOA_UNINITIALIZED  = 0,
  D3DKMDT_MOA_NONE           = 1,
  D3DKMDT_MOA_POLLED         = 2,
  D3DKMDT_MOA_INTERRUPTIBLE  = 3
} D3DKMDT_MONITOR_ORIENTATION_AWARENESS;
````

## Constants

<table>
            
                <tr>
                    <td>D3DKMDT_MOA_INTERRUPTIBLE</td>
                    <td>Indicates that the video output device can generate an interrupt when the orientation of a connected external display device changes.</td>
                </tr>
            
                <tr>
                    <td>D3DKMDT_MOA_NONE</td>
                    <td>Indicates that the video output device is unable to determine the orientation of a connected external display device.</td>
                </tr>
            
                <tr>
                    <td>D3DKMDT_MOA_POLLED</td>
                    <td>Indicates that the video output device can determine the orientation of a connected external display device, and the display miniport driver can be aware of changes in orientation by polling the video output device.</td>
                </tr>
            
                <tr>
                    <td>D3DKMDT_MOA_UNINITIALIZED</td>
                    <td>Indicates that a variable of type D3DKMDT_MONITOR_ORIENTATION_AWARENESS has not yet been assigned a meaningful value.</td>
                </tr>
</table>

## Remarks

The <b>ChildCapabilities</b> member of a <a href="..\dispmprt\ns-dispmprt-_dxgk_child_descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structure is a <a href="..\dispmprt\ns-dispmprt-_dxgk_child_capabilities.md">DXGK_CHILD_CAPABILITIES</a> structure. The <b>Type.VideoOutput</b> member of a CHILD_CAPABILITIES structure is a <a href="..\dispmprt\ns-dispmprt-_dxgk_video_output_capabilities.md">DXGK_VIDEO_OUTPUT_CAPABILITIES</a> structure. The <b>MonitorOrientationAwareness</b> member of a VIDEO_OUTPUT_CAPABILITIES structure is a D3DKMDT_MONITOR_ORIENTATION_AWARENESS value.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="..\dispmprt\nc-dispmprt-dxgkddi_query_child_relations.md">DxgkDdiQueryChildRelations</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>