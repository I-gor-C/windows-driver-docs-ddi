---
UID: NS:video._VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE
title: "_VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE"
author: windows-driver-content
description: The VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure describes the Write Combined video memory protection service routines implemented by the video port driver. The protected video memory cannot be accessed by the CPU.
old-location: display\video_port_wcmemoryprotection_interface.htm
old-project: display
ms.assetid: ac62a738-bde1-49e7-9c18-519471ec1092
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PVIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, PVIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, PVIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure pointer [Display Devices], VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure [Display Devices], Video_Structs_15076908-e598-4025-8884-a9ed60b1668c.xml, _VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, display.video_port_wcmemoryprotection_interface, video/PVIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, video/VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: video.h
req.include-header: Video.h
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
req.irql: See Remarks section.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	video.h
api_name:
-	VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, *PVIDEO_PORT_WCMEMORYPROTECTION_INTERFACE
req.product: Windows 10 or later.
---

# _VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure
The VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure describes the Write Combined video memory protection service routines implemented by the video port driver. The protected video memory cannot be accessed by the CPU.

## Syntax
```
typedef struct _VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE {
  IN USHORT                  Size;
  IN USHORT                  Version;
  OUT PVOID                  Context;
  OUT PINTERFACE_REFERENCE   InterfaceReference;
  OUT PINTERFACE_DEREFERENCE InterfaceDereference;
  OUT PROTECT_WC_MEMORY      VideoPortProtectWCMemory;
  OUT RESTORE_WC_MEMORY      VideoPortRestoreWCMemory;
} VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, *PVIDEO_PORT_WCMEMORYPROTECTION_INTERFACE;
```

## Members


`Size`

Specifies the size in bytes of this structure.

`Version`

Specifies the version of the interface to be returned by the miniport driver. The current interface version is defined in <i>video.h</i>, and has the form VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE_VERSION_<i>N</i>.

`Context`

Pointer to a miniport driver-defined context for the interface.

`InterfaceReference`

Pointer to the video port driver-implemented reference routine for this interface.

`InterfaceDereference`

Pointer to the video port driver-implemented dereference routine for this interface.

`VideoPortProtectWCMemory`

Pointer to the video port driver's <a href="https://msdn.microsoft.com/0cee4f4d-4d9c-44be-94ad-459000f2adb1">VideoPortProtectWCMemory</a> callback routine.

`VideoPortRestoreWCMemory`

Pointer to the video port driver's <a href="https://msdn.microsoft.com/8fa0be0c-04ce-41ab-93dd-6dc9e8daa356">VideoPortRestoreWCMemory</a> callback routine.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | video.h (include Video.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a>



<a href="https://msdn.microsoft.com/0cee4f4d-4d9c-44be-94ad-459000f2adb1">VideoPortProtectWCMemory</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570337">VideoPortQueryServices</a>



<a href="https://msdn.microsoft.com/8fa0be0c-04ce-41ab-93dd-6dc9e8daa356">VideoPortRestoreWCMemory</a>