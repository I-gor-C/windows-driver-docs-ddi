---
UID: NS:d3dkmthk._D3DKMT_OUTPUTDUPLPRESENTFLAGS
title: "_D3DKMT_OUTPUTDUPLPRESENTFLAGS"
author: windows-driver-content
description: Describes options for a Desktop Duplication API swapchain present operation.
old-location: display\d3dkmt_outputduplpresentflags.htm
old-project: display
ms.assetid: d80bcf24-4d53-4ec9-897d-d3243c7fda25
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_OUTPUTDUPLPRESENTFLAGS, D3DKMT_OUTPUTDUPLPRESENTFLAGS structure [Display Devices], _D3DKMT_OUTPUTDUPLPRESENTFLAGS, d3dkmthk/D3DKMT_OUTPUTDUPLPRESENTFLAGS, display.d3dkmt_outputduplpresentflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3dkmthk.h
api_name:
-	D3DKMT_OUTPUTDUPLPRESENTFLAGS
product: Windows
targetos: Windows
req.typenames: D3DKMT_OUTPUTDUPLPRESENTFLAGS
---

# _D3DKMT_OUTPUTDUPLPRESENTFLAGS structure
Describes options for a <a href="https://msdn.microsoft.com/523FBFAD-5D78-4EE3-A3B7-8FD5BA39DC46">Desktop Duplication API</a> swapchain present operation.

## Syntax
```
typedef struct _D3DKMT_OUTPUTDUPLPRESENTFLAGS {
  union {
    struct {
      UINT  : 1  ProtectedContentBlankedOut;
      UINT  : 1  RemoteSession;
      UINT  : 1  FullScreenPresent;
      UINT  : 1  PresentIndirect;
      UINT  : 28 Reserved;
    };
    UINT Value;
  };
} D3DKMT_OUTPUTDUPLPRESENTFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |