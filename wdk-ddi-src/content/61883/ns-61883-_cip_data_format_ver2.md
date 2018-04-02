---
UID: NS:61883._CIP_DATA_FORMAT_VER2
title: "_CIP_DATA_FORMAT_VER2"
author: windows-driver-content
description: This structure is a CIP data format which is used by CMP_CONNECT_VER2.
old-location: ieee\cip_data_format_ver2.htm
old-project: IEEE
ms.assetid: C78543F5-82CC-43CF-8769-1E721C17FF9C
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PCIP_DATA_FORMAT, *PCIP_DATA_FORMAT_VER2, 61883/CIP_DATA_FORMAT_VER2, 61883/PCIP_DATA_FORMAT_VER2, CIP_DATA_FORMAT, CIP_DATA_FORMAT_VER2, CIP_DATA_FORMAT_VER2 structure [Buses], IEEE.cip_data_format_ver2, PCIP_DATA_FORMAT_VER2, PCIP_DATA_FORMAT_VER2 structure pointer [Buses], _CIP_DATA_FORMAT_VER2"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 61883.h
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
-	61883.h
api_name:
-	CIP_DATA_FORMAT_VER2
product: Windows
targetos: Windows
req.typenames: CIP_DATA_FORMAT_VER2, *PCIP_DATA_FORMAT_VER2
---

# _CIP_DATA_FORMAT_VER2 structure
This structure is a CIP data format which is used by <a href="https://msdn.microsoft.com/2A2C1478-0512-4F84-90B9-B9C62B5D44DA">CMP_CONNECT_VER2</a>.

## Syntax
```
typedef struct _CIP_DATA_FORMAT_VER2 {
  UCHAR    FMT;
  UCHAR    FDF_hi;
  UCHAR    FDF_mid;
  UCHAR    FDF_lo;
  BOOLEAN  bHeader;
  UCHAR    Padding;
  UCHAR    BlockSize;
  UCHAR    Fraction;
  IN ULONG BlockPeriod;
} CIP_DATA_FORMAT_VER2, *PCIP_DATA_FORMAT_VER2;
```

## Members


`FMT`



`FDF_hi`



`FDF_mid`



`FDF_lo`



`bHeader`



`Padding`



`BlockSize`



`Fraction`



`BlockPeriod`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | 61883.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>