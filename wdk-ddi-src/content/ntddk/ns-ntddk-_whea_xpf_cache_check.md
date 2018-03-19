---
UID: NS:ntddk._WHEA_XPF_CACHE_CHECK
title: "_WHEA_XPF_CACHE_CHECK"
author: windows-driver-content
description: The WHEA_XPF_CACHE_CHECK union describes cache error information for an x86 or x64 processor.
old-location: whea\whea_xpf_cache_check.htm
old-project: whea
ms.assetid: 61dd30b9-5290-4c72-b053-586066c58108
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_XPF_CACHE_CHECK, PWHEA_XPF_CACHE_CHECK, PWHEA_XPF_CACHE_CHECK union pointer [WHEA Drivers and Applications], WHEA_XPF_CACHE_CHECK, WHEA_XPF_CACHE_CHECK union [WHEA Drivers and Applications], _WHEA_XPF_CACHE_CHECK, ntddk/PWHEA_XPF_CACHE_CHECK, ntddk/WHEA_XPF_CACHE_CHECK, whea.whea_xpf_cache_check, whearef_354fb32d-8724-4d6e-acc4-6d1a4cfd77a0.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
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
-	ntddk.h
api_name:
-	WHEA_XPF_CACHE_CHECK
product: Windows
targetos: Windows
req.typenames: WHEA_XPF_CACHE_CHECK, *PWHEA_XPF_CACHE_CHECK
---

# _WHEA_XPF_CACHE_CHECK structure
The WHEA_XPF_CACHE_CHECK union describes cache error information for an x86 or x64 processor.

## Syntax
````
typedef union _WHEA_XPF_CACHE_CHECK {
  struct {
    ULONGLONG TransactionTypeValid  :1;
    ULONGLONG OperationValid  :1;
    ULONGLONG LevelValid  :1;
    ULONGLONG ProcessorContextCorruptValid  :1;
    ULONGLONG UncorrectedValid  :1;
    ULONGLONG PreciseIPValid  :1;
    ULONGLONG RestartableIPValid  :1;
    ULONGLONG OverflowValid  :1;
    ULONGLONG ReservedValid  :8;
    ULONGLONG TransactionType  :2;
    ULONGLONG Operation  :4;
    ULONGLONG Level  :3;
    ULONGLONG ProcessorContextCorrupt  :1;
    ULONGLONG Uncorrected  :1;
    ULONGLONG PreciseIP  :1;
    ULONGLONG RestartableIP  :1;
    ULONGLONG Overflow  :1;
    ULONGLONG Reserved  :34;
  };
  ULONGLONG XpfCacheCheck;
} WHEA_XPF_CACHE_CHECK, *PWHEA_XPF_CACHE_CHECK;
````

## Members


`DUMMYSTRUCTNAME`



`XpfCacheCheck`

A ULONGLONG representation of the contents of the WHEA_XPF_CACHE_CHECK union.

## Remarks
If the <b>CheckInfoId</b> member of a <a href="..\ntddk\ns-ntddk-_whea_xpf_procinfo.md">WHEA_XPF_PROCINFO</a> structure contains WHEA_CACHECHECK_GUID, the <b>CheckInfo</b> member of the WHEA_XPF_PROCINFO structure contains a WHEA_XPF_CACHE_CHECK union.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="..\ntddk\ns-ntddk-_whea_xpf_procinfo.md">WHEA_XPF_PROCINFO</a>