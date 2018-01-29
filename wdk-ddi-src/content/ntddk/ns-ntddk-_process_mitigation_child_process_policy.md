---
UID : NS:ntddk._PROCESS_MITIGATION_CHILD_PROCESS_POLICY
title : _PROCESS_MITIGATION_CHILD_PROCESS_POLICY
author : windows-driver-content
description : Stores policy information about creating child processes.
old-location : kernel\process_mitigation_child_process_policy.htm
old-project : kernel
ms.assetid : 8f388c0e-41ee-40e4-b633-687eeff74a0a
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : "*PPROCESS_MITIGATION_CHILD_PROCESS_POLICY, PROCESS_MITIGATION_CHILD_PROCESS_POLICY, _PROCESS_MITIGATION_CHILD_PROCESS_POLICY, PROCESS_MITIGATION_CHILD_PROCESS_POLICY structure [Kernel-Mode Driver Architecture], kernel.process_mitigation_child_process_policy, ntddk/PROCESS_MITIGATION_CHILD_PROCESS_POLICY"
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PROCESS_MITIGATION_CHILD_PROCESS_POLICY, *PPROCESS_MITIGATION_CHILD_PROCESS_POLICY
---

# _PROCESS_MITIGATION_CHILD_PROCESS_POLICY structure
Stores policy information about creating child processes.

## Syntax
````
typedef struct _PROCESS_MITIGATION_CHILD_PROCESS_POLICY {
  union {
    struct {
      ULONG NoChildProcessCreation  :1;
      ULONG AuditNoChildProcessCreation  :1;
      ULONG AllowSecureProcessCreation  :1;
      ULONG ReservedFlags  :29;
    } DUMMYSTRUCTNAME;
  } DUMMYUNIONNAME;
} PROCESS_MITIGATION_CHILD_PROCESS_POLICY, PROCESS_MITIGATION_CHILD_PROCESS_POLICY;
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