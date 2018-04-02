---
UID: NI:ntddvdeo.IOCTL_VIDEO_SET_CURRENT_MODE
title: IOCTL_VIDEO_SET_CURRENT_MODE
author: windows-driver-content
description: Sets the adapter to the specified operating mode.
old-location: display\ioctl_video_set_current_mode.htm
old-project: display
ms.assetid: 7dd77e55-01d7-4e10-8134-813fe0c1fc6c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IOCTL_VIDEO_SET_CURRENT_MODE, IOCTL_VIDEO_SET_CURRENT_MODE control code [Display Devices], Video_IOCTLs_df8e3e45-0a72-427b-b47f-49bc936d53a5.xml, display.ioctl_video_set_current_mode, ntddvdeo/IOCTL_VIDEO_SET_CURRENT_MODE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddvdeo.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddvdeo.h
api_name:
-	IOCTL_VIDEO_SET_CURRENT_MODE
product: Windows
targetos: Windows
req.typenames: TAPE_WRITE_MARKS, *PTAPE_WRITE_MARKS
---

# IOCTL_VIDEO_SET_CURRENT_MODE IOCTL
Sets the adapter to the specified operating mode. Miniport drivers are required to support this nonmodal request because it resets the current mode. The miniport driver must also consider the two high order flags which are used to additionally control the mode set operation. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff570520">VIDEO_MODE</a> for further information.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The VRP <b>InputBuffer</b> contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570520">VIDEO_MODE</a> structure specifying the mode to be set.

### Input Buffer Length
<text></text>

### Output Buffer
None

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The miniport driver does not set the <b>Information</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569732">STATUS_BLOCK</a> structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddvdeo.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff570520">VIDEO_MODE</a>