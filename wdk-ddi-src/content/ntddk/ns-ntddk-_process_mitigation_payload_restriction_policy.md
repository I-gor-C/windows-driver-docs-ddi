---
UID: NS:ntddk._PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
title: "_PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY"
author: windows-driver-content
description: Stores information about process mitigation policy.
old-location: kernel\process_mitigation_payload_restriction_policy.htm
old-project: kernel
ms.assetid: f55a47b2-c95c-4b6c-aeff-aed99dd9e43b
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY structure [Kernel-Mode Driver Architecture], _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, kernel.process_mitigation_payload_restriction_policy, ntddk/PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddk.h
api_name:
-	PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
product:
- Windows
targetos: Windows
req.typenames: PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, *PPROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
---

# _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY structure
Stores information about process mitigation policy.

## Syntax
```
typedef struct _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY {
  union {
    ULONG Flags;
    struct {
      ULONG  : 1  EnableExportAddressFilter;
      ULONG  : 1  AuditExportAddressFilter;
      ULONG  : 1  EnableExportAddressFilterPlus;
      ULONG  : 1  AuditExportAddressFilterPlus;
      ULONG  : 1  EnableImportAddressFilter;
      ULONG  : 1  AuditImportAddressFilter;
      ULONG  : 1  EnableRopStackPivot;
      ULONG  : 1  AuditRopStackPivot;
      ULONG  : 1  EnableRopCallerCheck;
      ULONG  : 1  AuditRopCallerCheck;
      ULONG  : 1  EnableRopSimExec;
      ULONG  : 1  AuditRopSimExec;
      ULONG  : 20 ReservedFlags;
    } DUMMYSTRUCTNAME;
  } DUMMYUNIONNAME;
} *PPROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY;
```

## Members


`DUMMYUNIONNAME`

#### Flags

Bitwise of flags in this structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Header** | ntddk.h |