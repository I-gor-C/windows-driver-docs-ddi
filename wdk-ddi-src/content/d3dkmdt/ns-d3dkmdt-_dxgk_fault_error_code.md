---
UID: NS:d3dkmdt._DXGK_FAULT_ERROR_CODE
title: "_DXGK_FAULT_ERROR_CODE"
author: windows-driver-content
description: The DXGK_FAULT_ERROR_CODE structure provides a status code for the graphics processing unit (GPU) error reported via a page fault interrupt.
old-location: display\dxgk_fault_error_code.htm
old-project: display
ms.assetid: 753FC177-D430-40E5-98CD-B3BDFD47ACEF
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_FAULT_ERROR_CODE, DXGK_FAULT_ERROR_CODE structure [Display Devices], _DXGK_FAULT_ERROR_CODE, d3dkmdt/DXGK_FAULT_ERROR_CODE, display.dxgk_fault_error_code
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	D3dkmdt.h
api_name:
-	DXGK_FAULT_ERROR_CODE
product: Windows
targetos: Windows
req.typenames: DXGK_FAULT_ERROR_CODE
---

# _DXGK_FAULT_ERROR_CODE structure
The <b>DXGK_FAULT_ERROR_CODE</b> structure provides a status code for the graphics processing unit (GPU) error reported via a page fault interrupt.

## Syntax
```
typedef struct _DXGK_FAULT_ERROR_CODE {
  union {
    struct {
      UINT  : 1                     IsDeviceSpecificCode;
      DXGK_GENERAL_ERROR_CODE  : 31 GeneralErrorCode;
    };
    struct {
      UINT  : 1  IsDeviceSpecificCodeReservedBit;
      UINT  : 31 DeviceSpecificCode;
    };
  };
} DXGK_FAULT_ERROR_CODE;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmdt.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn906347">DXGK_GENERAL_ERROR_CODE</a>