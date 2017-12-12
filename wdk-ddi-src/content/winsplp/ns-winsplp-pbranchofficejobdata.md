---
UID: NS.WINSPLP.PBRANCHOFFICEJOBDATA
title: PBranchOfficeJobData
author: windows-driver-content
description: This structure contains the type of event to log (eEventType), the job ID, and the data required by the event.
old-location: print\branchofficejobdata.htm
old-project: print
ms.assetid: B49FEED5-C90A-4E4F-9B73-E06E56FB4311
ms.author: windowsdriverdev
ms.date: 12/9/2017
ms.keywords: PBranchOfficeJobData, BranchOfficeJobData, *PBranchOfficeJobData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BranchOfficeJobData
req.alt-loc: Winsplp.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# PBranchOfficeJobData structure



## -description
This structure contains the type of event to log (eEventType), the job ID, and the data required by the event.



## -syntax

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


## -struct-fields

### -field eEventType

Specifies the type of event to be logged.


### -field JobId

Specifies the ID of the job on the client.


### -field JobInfo


### -field LogJobPrinted

Describes  the <b>BranchOfficeJobDataPrinted</b> type member <b>LogJobPrinted</b>.


### -field LogJobRendered

Describes the <b>BranchOfficeJobDataRendered</b> type member <b>LogJobRendered</b>.


### -field LogJobError

Describes the <b>BranchOfficeJobDataError</b> type member <b>LogJobError</b>.


### -field LogPipelineFailed

Describes the <b>BranchOfficeJobDataPipelineFailed</b> type member <b>LogPipelineFailed</b>.


### -field LogOfflineFileFull

Describes the <b>BranchOfficeLogOfflineFileFull</b> type member <b>LogOfflineFileFull</b>.

</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>