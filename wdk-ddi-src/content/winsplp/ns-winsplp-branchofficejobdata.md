---
UID : NS:winsplp.BranchOfficeJobData
title : BranchOfficeJobData
author : windows-driver-content
description : This structure contains the type of event to log (eEventType), the job ID, and the data required by the event.
old-location : print\branchofficejobdata.htm
old-project : print
ms.assetid : B49FEED5-C90A-4E4F-9B73-E06E56FB4311
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : BranchOfficeJobData, BranchOfficeJobData structure [Print Devices], PBranchOfficeJobData, print.branchofficejobdata, PBranchOfficeJobData structure pointer [Print Devices], winsplp/BranchOfficeJobData, *PBranchOfficeJobData, winsplp/PBranchOfficeJobData
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
req.typenames : "*PBranchOfficeJobData, BranchOfficeJobData"
req.product : Windows 10 or later.
---

# BranchOfficeJobData structure
This structure contains the type of event to log (eEventType), the job ID, and the data required by the event.

## Syntax
````
typedef struct {
  EBranchOfficeJobEventType eEventType;
  DWORD                     JobId;
  union {
    BranchOfficeJobDataPrinted        LogJobPrinted;
    BranchOfficeJobDataRendered       LogJobRendered;
    BranchOfficeJobDataError          LogJobError;
    BranchOfficeJobDataPipelineFailed LogPipelineFailed;
    BranchOfficeLogOfflineFileFull    LogOfflineFileFull;
  } JobInfo;
} BranchOfficeJobData, *PBranchOfficeJobData;
````

## Members


`eEventType`

Specifies the type of event to be logged.

`JobId`

Specifies the ID of the job on the client.

`JobInfo`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | winsplp.h |