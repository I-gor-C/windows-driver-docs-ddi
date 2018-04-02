---
UID: NS:d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT
title: "_D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT"
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure is used to indicate the types of scaling (and centering) that are supported by a particular VidPN present path.
old-location: display\d3dkmdt_vidpn_present_path_scaling_support.htm
old-project: display
ms.assetid: 44b7f841-40e5-4d7d-adca-b70b4a8ef55c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT, D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure [Display Devices], DmStructs_8a17e0fc-7c6c-4c95-bbdb-471beef9e830.xml, _D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT, d3dkmdt/D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT, display.d3dkmdt_vidpn_present_path_scaling_support
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmdt.h
api_name:
-	D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT
product:
- Windows
targetos: Windows
req.typenames: D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT
---

# _D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure
The D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure is used to indicate the types of scaling (and centering) that are supported by a particular VidPN present path.

## Syntax
```
typedef struct _D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT {
  UINT  : 1 Identity;
  UINT  : 1 Centered;
  UINT  : 1 Stretched;
  UINT  : 1 AspectRatioCenteredMax;
  UINT  : 1 Custom;
} D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT;
```

## Members


`Identity`

The path is capable of displaying content with no transformation.

`Centered`

The path is capable of displaying centered content.

`Stretched`

The path is capable of displaying scaled content.

`AspectRatioCenteredMax`

The path is capable of scaling source content to fit the target while preserving the aspect ratio of the source.

This member is available beginning with Windows 7.

`Custom`

The path is capable of displaying one or more scaling modes that are not described by other members of this structure.

## Remarks
The <b>ScalingSupport</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a> structure is a D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546706">D3DKMDT_VIDPN_PRESENT_PATH_SCALING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a>