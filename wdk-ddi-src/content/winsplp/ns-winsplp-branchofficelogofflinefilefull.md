---
UID : NS:winsplp.BranchOfficeLogOfflineFileFull
title : BranchOfficeLogOfflineFileFull
author : windows-driver-content
description : Contains the necessary data for logging that the offline log archive on the current client overflowed at some point.
old-location : print\branchofficelogofflinefilefull.htm
old-project : print
ms.assetid : 41190CE8-8779-477C-BFB0-6410DF096EFD
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.branchofficelogofflinefilefull, winsplp/PBranchOfficeLogOfflineFileFull, winsplp/BranchOfficeLogOfflineFileFull, BranchOfficeLogOfflineFileFull, *PBranchOfficeLogOfflineFileFull, PBranchOfficeLogOfflineFileFull, BranchOfficeLogOfflineFileFull structure [Print Devices], PBranchOfficeLogOfflineFileFull structure pointer [Print Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : winsplp.h
req.include-header : 
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
req.typenames : BranchOfficeLogOfflineFileFull, *PBranchOfficeLogOfflineFileFull
req.product : Windows 10 or later.
---

# BranchOfficeLogOfflineFileFull structure
Contains the necessary data for logging that the offline log archive on the current client overflowed at some point.

## Syntax
````
typedef struct {
  LPWSTR pMachineName;
} BranchOfficeLogOfflineFileFull, *PBranchOfficeLogOfflineFileFull;
````

## Members


`pMachineName`

Specifies the name of the print client.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | winsplp.h |