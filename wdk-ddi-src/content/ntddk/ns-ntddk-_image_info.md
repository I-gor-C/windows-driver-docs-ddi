---
UID: NS:ntddk._IMAGE_INFO
title: "_IMAGE_INFO"
author: windows-driver-content
description: Used by driver's load-image routine (PLOAD_IMAGE_NOTIFY_ROUTINE) to specify image information.
old-location: kernel\image_info.htm
old-project: kernel
ms.assetid: D2CD2457-8DDF-4449-9DC1-F1E7472C87CA
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PIMAGE_INFO, IMAGE_INFO, IMAGE_INFO structure [Kernel-Mode Driver Architecture], PIMAGE_INFO, PIMAGE_INFO structure pointer [Kernel-Mode Driver Architecture], _IMAGE_INFO, kernel.image_info, ntddk/IMAGE_INFO, ntddk/PIMAGE_INFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddk.h
api_name:
-	IMAGE_INFO
product:
- Windows
targetos: Windows
req.typenames: IMAGE_INFO, *PIMAGE_INFO
---

# _IMAGE_INFO structure
Used by driver's load-image routine (<a href="https://msdn.microsoft.com/library/windows/hardware/mt764088">PLOAD_IMAGE_NOTIFY_ROUTINE</a>) to specify image information.

## Syntax
```
typedef struct _IMAGE_INFO {
  union {
    ULONG Properties;
    struct {
      ULONG  : 8  ImageAddressingMode;
      ULONG  : 1  SystemModeImage;
      ULONG  : 1  ImageMappedToAllPids;
      ULONG  : 1  ExtendedInfoPresent;
      ULONG  : 1  MachineTypeMismatch;
      ULONG  : 4  ImageSignatureLevel;
      ULONG  : 3  ImageSignatureType;
      ULONG  : 1  ImagePartialMap;
      ULONG  : 12 Reserved;
    };
  };
  PVOID  ImageBase;
  ULONG  ImageSelector;
  SIZE_T ImageSize;
  ULONG  ImageSectionNumber;
} IMAGE_INFO, *PIMAGE_INFO;
```

## Members


`ImageBase`

Set to the virtual base address of the image.

`ImageSelector`

Always set to zero.

`ImageSize`

Set to the virtual size, in bytes, of the image.

`ImageSectionNumber`

Always set to zero.

## Remarks
If the <b>ExtendedInfoPresent</b> flag is set, the <b>IMAGE_INFO</b> structure is part of a larger, extended version of the image information structure, <a href="https://msdn.microsoft.com/library/windows/hardware/mt764084">IMAGE_INFO_EX</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt764084">IMAGE_INFO_EX</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt764088">PLOAD_IMAGE_NOTIFY_ROUTINE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559957">PsSetLoadImageNotifyRoutine</a>