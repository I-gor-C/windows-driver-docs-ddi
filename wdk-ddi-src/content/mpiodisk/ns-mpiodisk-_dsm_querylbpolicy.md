---
UID : NS:mpiodisk._DSM_QueryLBPolicy
title : "_DSM_QueryLBPolicy"
author : windows-driver-content
description : The DSM_QueryLBPolicy structure is used to query a LUN's current load balance policy.
old-location : storage\dsm_querylbpolicy.htm
old-project : storage
ms.assetid : f2ac985a-8fcb-48ad-b100-4137b5b1a777
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : PDSM_QueryLBPolicy, *PDSM_QueryLBPolicy, PDSM_QueryLBPolicy structure pointer [Storage Devices], storage.dsm_querylbpolicy, _DSM_QueryLBPolicy, mpiodisk/PDSM_QueryLBPolicy, DSM_QueryLBPolicy, mpiodisk/DSM_QueryLBPolicy, DSM_QueryLBPolicy structure [Storage Devices], structs-scsibus_f1a0bedd-e5ba-474d-9a45-ae6a2863cfb3.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : mpiodisk.h
req.include-header : Mpiowmi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PDSM_QueryLBPolicy, DSM_QueryLBPolicy"
---

# _DSM_QueryLBPolicy structure
The DSM_QueryLBPolicy structure is used to query a LUN's current load balance policy.

## Syntax
````
typedef struct _DSM_QueryLBPolicy {
  DSM_Load_Balance_Policy LoadBalancePolicy;
} DSM_QueryLBPolicy, *PDSM_QueryLBPolicy;
````

## Members


`LoadBalancePolicy`

An instance of a DSM_Load_Balance_Policy structure that has information about the current load balance policy that is being applied by the DSM on the targeted pseudo-LUN.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | mpiodisk.h (include Mpiowmi.h) |