---
UID: NS:ntddk._WHEA_XPF_BUS_CHECK
title: "_WHEA_XPF_BUS_CHECK"
author: windows-driver-content
description: The WHEA_XPF_BUS_CHECK union describes bus error information for an x86 or x64 processor.
old-location: whea\whea_xpf_bus_check.htm
old-project: whea
ms.assetid: 7886a796-2755-4367-bbbd-2017e7900bf4
ms.author: windowsdriverdev
ms.date: 2/8/2018
ms.keywords: ntddk/PWHEA_XPF_BUS_CHECK, whea.whea_xpf_bus_check, _WHEA_XPF_BUS_CHECK, whearef_fff50a8d-8ab0-4f25-adb3-b33e1ea80aed.xml, WHEA_XPF_BUS_CHECK union [WHEA Drivers and Applications], *PWHEA_XPF_BUS_CHECK, ntddk/WHEA_XPF_BUS_CHECK, PWHEA_XPF_BUS_CHECK union pointer [WHEA Drivers and Applications], PWHEA_XPF_BUS_CHECK, WHEA_XPF_BUS_CHECK
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddk.h
apiname:
-	WHEA_XPF_BUS_CHECK
product: Windows
targetos: Windows
req.typenames: WHEA_XPF_BUS_CHECK, *PWHEA_XPF_BUS_CHECK
---

# _WHEA_XPF_BUS_CHECK structure
The WHEA_XPF_BUS_CHECK union describes bus error information for an x86 or x64 processor.

## Syntax
````
typedef union _WHEA_XPF_BUS_CHECK {
  struct {
    ULONGLONG TransactionTypeValid  :1;
    ULONGLONG OperationValid  :1;
    ULONGLONG LevelValid  :1;
    ULONGLONG ProcessorContextCorruptValid  :1;
    ULONGLONG UncorrectedValid  :1;
    ULONGLONG PreciseIPValid  :1;
    ULONGLONG RestartableIPValid  :1;
    ULONGLONG OverflowValid  :1;
    ULONGLONG ParticipationValid  :1;
    ULONGLONG TimeoutValid  :1;
    ULONGLONG AddressSpaceValid  :1;
    ULONGLONG ReservedValid  :5;
    ULONGLONG TransactionType  :2;
    ULONGLONG Operation  :4;
    ULONGLONG Level  :3;
    ULONGLONG ProcessorContextCorrupt  :1;
    ULONGLONG Uncorrected  :1;
    ULONGLONG PreciseIP  :1;
    ULONGLONG RestartableIP  :1;
    ULONGLONG Overflow  :1;
    ULONGLONG Participation  :2;
    ULONGLONG Timeout  :1;
    ULONGLONG AddressSpace  :2;
    ULONGLONG Reserved  :29;
  };
  ULONGLONG XpfBusCheck;
} WHEA_XPF_BUS_CHECK, *PWHEA_XPF_BUS_CHECK;
````

## Members


`DUMMYSTRUCTNAME`



`XpfBusCheck`

A ULONGLONG representation of the contents of the WHEA_XPF_BUS_CHECK union.

## Remarks
If the <b>CheckInfoId</b> member of a <a href="..\ntddk\ns-ntddk-_whea_xpf_procinfo.md">WHEA_XPF_PROCINFO</a> structure contains WHEA_BUSCHECK_GUID, the <b>CheckInfo</b> member of the WHEA_XPF_PROCINFO structure contains a WHEA_XPF_BUS_CHECK union.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="..\ntddk\ns-ntddk-_whea_xpf_procinfo.md">WHEA_XPF_PROCINFO</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_XPF_BUS_CHECK union%20 RELEASE:%20(2/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>