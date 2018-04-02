---
UID: NS:d3dkmddi._DXGK_MONITORDESCRIPTORSET_INTERFACE
title: "_DXGK_MONITORDESCRIPTORSET_INTERFACE"
author: windows-driver-content
description: The DXGK_MONITORDESCRIPTORSET_INTERFACE structure contains pointers to functions that belong to the Monitor Descriptor Set Interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_monitordescriptorset_interface.htm
old-project: display
ms.assetid: ac492a44-f14e-4b66-9ec1-4f1b04806646
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_MONITORDESCRIPTORSET_INTERFACE, DXGK_MONITORDESCRIPTORSET_INTERFACE structure [Display Devices], DmStructs_da0cca60-6df0-480b-8e02-0affe5eb5cfd.xml, _DXGK_MONITORDESCRIPTORSET_INTERFACE, d3dkmddi/DXGK_MONITORDESCRIPTORSET_INTERFACE, display.dxgk_monitordescriptorset_interface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
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
-	d3dkmddi.h
api_name:
-	DXGK_MONITORDESCRIPTORSET_INTERFACE
product:
- Windows
targetos: Windows
req.typenames: DXGK_MONITORDESCRIPTORSET_INTERFACE
---

# _DXGK_MONITORDESCRIPTORSET_INTERFACE structure
The DXGK_MONITORDESCRIPTORSET_INTERFACE structure contains pointers to functions that belong to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568427">Monitor Descriptor Set Interface</a>, which is implemented by the video present network (VidPN) manager.

## Syntax
```
typedef struct _DXGK_MONITORDESCRIPTORSET_INTERFACE {
  DXGKDDI_MONITORDESCRIPTORSET_GETNUMDESCRIPTORS          pfnGetNumDescriptors;
  DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO pfnAcquireFirstDescriptorInfo;
  DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO  pfnAcquireNextDescriptorInfo;
  DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO      pfnReleaseDescriptorInfo;
} DXGK_MONITORDESCRIPTORSET_INTERFACE;
```

## Members


`pfnGetNumDescriptors`

A pointer to the <a href="https://msdn.microsoft.com/7bfcef0b-1371-4e3b-b5dc-c4c548625c8f">pfnGetNumDescriptors</a> function.

`pfnAcquireFirstDescriptorInfo`

A pointer to the <a href="https://msdn.microsoft.com/228f6947-a7e5-4b76-8224-fac6889fc77a">pfnAcquireFirstDescriptorInfo</a> function.

`pfnAcquireNextDescriptorInfo`

A pointer to the <a href="https://msdn.microsoft.com/34d048df-d4a1-4ef5-b917-791f35de9e3a">pfnAcquireNextDescriptorInfo</a> function.

`pfnReleaseDescriptorInfo`

A pointer to the <a href="https://msdn.microsoft.com/8debdd01-c4e4-4b7c-b4cd-c1143ea7ebaa">pfnReleaseDescriptorInfo</a> function.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/228f6947-a7e5-4b76-8224-fac6889fc77a">pfnAcquireFirstDescriptorInfo</a>



<a href="https://msdn.microsoft.com/34d048df-d4a1-4ef5-b917-791f35de9e3a">pfnAcquireNextDescriptorInfo</a>



<a href="https://msdn.microsoft.com/7bfcef0b-1371-4e3b-b5dc-c4c548625c8f">pfnGetNumDescriptors</a>



<a href="https://msdn.microsoft.com/8debdd01-c4e4-4b7c-b4cd-c1143ea7ebaa">pfnReleaseDescriptorInfo</a>