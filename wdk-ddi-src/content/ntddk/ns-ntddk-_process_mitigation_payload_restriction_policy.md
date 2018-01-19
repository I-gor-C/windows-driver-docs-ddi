---
UID : NS:ntddk._PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
title : _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
author : windows-driver-content
description : Stores information about process mitigation policy.
old-location : kernel\process_mitigation_payload_restriction_policy.htm
old-project : kernel
ms.assetid : f55a47b2-c95c-4b6c-aeff-aed99dd9e43b
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, *PPROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
req.alt-loc : Ntddk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PPROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY"
---

# _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY structure
Stores information about process mitigation policy.

## Syntax
````
typedef struct _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY {
  union {
    ULONG Flags;
    struct {
      ULONG EnableExportAddressFilter  :1;
      ULONG AuditExportAddressFilter  :1;
      ULONG EnableExportAddressFilterPlus  :1;
      ULONG AuditExportAddressFilterPlus  :1;
      ULONG EnableImportAddressFilter  :1;
      ULONG AuditImportAddressFilter  :1;
      ULONG EnableRopStackPivot  :1;
      ULONG AuditRopStackPivot  :1;
      ULONG EnableRopCallerCheck  :1;
      ULONG AuditRopCallerCheck  :1;
      ULONG EnableRopSimExec  :1;
      ULONG AuditRopSimExec  :1;
      ULONG ReservedFlags  :20;
    } DUMMYSTRUCTNAME;
  } DUMMYUNIONNAME;
} PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY;
````

## Members

        
            `DUMMYUNIONNAME`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h |