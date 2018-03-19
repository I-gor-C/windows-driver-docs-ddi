---
UID: NS:d3dkmthk._D3DKMT_CREATEKEYEDMUTEX2_FLAGS
title: "_D3DKMT_CREATEKEYEDMUTEX2_FLAGS"
author: windows-driver-content
description: Indicates how a handle to a keyed mutex is specified.
old-location: display\d3dkmt_createkeyedmutex2_flags.htm
old-project: display
ms.assetid: 21c2d262-bf8c-48a3-9801-5c2bd73f0282
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DKMT_CREATEKEYEDMUTEX2_FLAGS, D3DKMT_CREATEKEYEDMUTEX2_FLAGS structure [Display Devices], _D3DKMT_CREATEKEYEDMUTEX2_FLAGS, d3dkmthk/D3DKMT_CREATEKEYEDMUTEX2_FLAGS, display.d3dkmt_createkeyedmutex2_flags
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
-	D3DKMT_CREATEKEYEDMUTEX2_FLAGS
product: Windows
targetos: Windows
req.typenames: D3DKMT_CREATEKEYEDMUTEX2_FLAGS
---

# _D3DKMT_CREATEKEYEDMUTEX2_FLAGS structure
Indicates how a handle to a keyed mutex is specified.

## Syntax
````
typedef struct _D3DKMT_CREATEKEYEDMUTEX2_FLAGS {
  union {
    struct {
      UINT NtSecuritySharing  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} D3DKMT_CREATEKEYEDMUTEX2_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_createkeyedmutex2.md">D3DKMT_CREATEKEYEDMUTEX2</a>



<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtshareobjects.md">D3DKMTShareObjects</a>



<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatekeyedmutex2.md">D3DKMTCreateKeyedMutex2</a>