---
UID: NS:ntddk._WHEA_XPF_TLB_CHECK
title: "_WHEA_XPF_TLB_CHECK"
author: windows-driver-content
description: The WHEA_XPF_TLB_CHECK union describes translation lookaside buffer (TLB) error information for an x86 or x64 processor.
old-location: whea\whea_xpf_tlb_check.htm
old-project: whea
ms.assetid: 3943c854-3bb9-4fc9-9af9-735c3f4ee94e
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_XPF_TLB_CHECK, PWHEA_XPF_TLB_CHECK, PWHEA_XPF_TLB_CHECK union pointer [WHEA Drivers and Applications], WHEA_XPF_TLB_CHECK, WHEA_XPF_TLB_CHECK union [WHEA Drivers and Applications], _WHEA_XPF_TLB_CHECK, ntddk/PWHEA_XPF_TLB_CHECK, ntddk/WHEA_XPF_TLB_CHECK, whea.whea_xpf_tlb_check, whearef_20ed4273-105d-467b-a71f-46e50078543e.xml"
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
-	WHEA_XPF_TLB_CHECK
product:
- Windows
targetos: Windows
req.typenames: WHEA_XPF_TLB_CHECK, *PWHEA_XPF_TLB_CHECK
---

# _WHEA_XPF_TLB_CHECK structure
The WHEA_XPF_TLB_CHECK union describes translation lookaside buffer (TLB) error information for an x86 or x64 processor.

## Syntax
```
typedef struct _WHEA_XPF_TLB_CHECK {
  struct {
    ULONGLONG  : 3  Level;
    ULONGLONG  : 1  LevelValid;
    ULONGLONG  : 4  Operation;
    ULONGLONG  : 1  OperationValid;
    ULONGLONG  : 1  Overflow;
    ULONGLONG  : 1  OverflowValid;
    ULONGLONG  : 1  PreciseIP;
    ULONGLONG  : 1  PreciseIPValid;
    ULONGLONG  : 1  ProcessorContextCorrupt;
    ULONGLONG  : 1  ProcessorContextCorruptValid;
    ULONGLONG  : 34 Reserved;
    ULONGLONG  : 8  ReservedValid;
    ULONGLONG  : 1  RestartableIP;
    ULONGLONG  : 1  RestartableIPValid;
    ULONGLONG  : 2  TransactionType;
    ULONGLONG  : 1  TransactionTypeValid;
    ULONGLONG  : 1  Uncorrected;
    ULONGLONG  : 1  UncorrectedValid;
  } DUMMYSTRUCTNAME;
  ULONGLONG XpfTLBCheck;
} WHEA_XPF_TLB_CHECK, *PWHEA_XPF_TLB_CHECK;
```

## Members


`DUMMYSTRUCTNAME`



`XpfTLBCheck`

A ULONGLONG representation of the contents of the WHEA_XPF_TLB_CHECK union.

## Remarks
If the <b>CheckInfoId</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a> structure contains WHEA_TLBCHECK_GUID, the <b>CheckInfo</b> member of the WHEA_XPF_PROCINFO structure contains a WHEA_XPF_TLB_CHECK union.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a>