---
UID: NS:ntddk._WHEA_ERROR_PACKET_FLAGS
title: "_WHEA_ERROR_PACKET_FLAGS"
author: windows-driver-content
description: The WHEA_ERROR_PACKET_FLAGS union defines the error condition reported through a WHEA_ERROR_PACKET structure.
old-location: whea\whea_error_packet_flags.htm
old-project: whea
ms.assetid: e1dae7df-7d81-42cc-9a01-44345f53ba4e
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_ERROR_PACKET_FLAGS, PWHEA_ERROR_PACKET_FLAGS, PWHEA_ERROR_PACKET_FLAGS union pointer [WHEA Drivers and Applications], WHEA_ERROR_PACKET_FLAGS, WHEA_ERROR_PACKET_FLAGS union [WHEA Drivers and Applications], _WHEA_ERROR_PACKET_FLAGS, ntddk/PWHEA_ERROR_PACKET_FLAGS, ntddk/WHEA_ERROR_PACKET_FLAGS, whea.whea_error_packet_flags, whearef_c193e4e7-f233-4de0-93ac-5e7b841a6c6e.xml"
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
-	WHEA_ERROR_PACKET_FLAGS
product: Windows
targetos: Windows
req.typenames: WHEA_ERROR_PACKET_FLAGS, *PWHEA_ERROR_PACKET_FLAGS
---

# _WHEA_ERROR_PACKET_FLAGS structure
The WHEA_ERROR_PACKET_FLAGS union defines the error condition reported through a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure.

## Syntax
```
typedef struct _WHEA_ERROR_PACKET_FLAGS {
  struct {
    ULONG  : 1  HypervisorError;
    ULONG  : 1  PlatformDirectedOffline;
    ULONG  : 1  PlatformPfaControl;
    ULONG  : 1  PreviousError;
    ULONG  : 1  Reserved1;
    ULONG  : 26 Reserved2;
    ULONG  : 1  Simulated;
  } DUMMYSTRUCTNAME;
  ULONG  AsULONG;
} WHEA_ERROR_PACKET_FLAGS, *PWHEA_ERROR_PACKET_FLAGS;
```

## Members


`DUMMYSTRUCTNAME`



`AsULONG`

A ULONG representation of the contents of the WHEA_ERROR_PACKET_FLAGS union.

## Remarks
The WHEA_ERROR_PACKET_FLAGS union describes the error condition reported by using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/d2ded330-edcc-4bdd-9b52-73c1961d8ef2">Predictive Failure Analysis (PFA)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a>