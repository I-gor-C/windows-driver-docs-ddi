---
UID: NS.winsplp.PBranchOfficeJobData
title: PBranchOfficeJobData
author: windows-driver-content
description: This structure contains the type of event to log (eEventType), the job ID, and the data required by the event.
old-location: print\branchofficejobdata.htm
ms.assetid: B49FEED5-C90A-4E4F-9B73-E06E56FB4311
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
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
ms.keywords: PBranchOfficeJobData, BranchOfficeJobData, *PBranchOfficeJobData
req.iface: 
req.product: Windows 10 or later.
---

# PBranchOfficeJobData structure



## -description
<p>This structure contains the type of event to log (eEventType), the job ID, and the data required by the event.</p>


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
<dl>

### -field <b>eEventType</b>

<dd>
<p>Specifies the type of event to be logged.</p>
</dd>

### -field <b>JobId</b>

<dd>
<p>Specifies the ID of the job on the client.</p>
</dd>

### -field <b>JobInfo</b>

<dd>
<dl>

### -field <b>LogJobPrinted</b>

<dd>
<p>Describes  the <b>BranchOfficeJobDataPrinted</b> type member <b>LogJobPrinted</b>.</p>
</dd>

### -field <b>LogJobRendered</b>

<dd>
<p>Describes the <b>BranchOfficeJobDataRendered</b> type member <b>LogJobRendered</b>.</p>
</dd>

### -field <b>LogJobError</b>

<dd>
<p>Describes the <b>BranchOfficeJobDataError</b> type member <b>LogJobError</b>.</p>
</dd>

### -field <b>LogPipelineFailed</b>

<dd>
<p>Describes the <b>BranchOfficeJobDataPipelineFailed</b> type member <b>LogPipelineFailed</b>.</p>
</dd>

### -field <b>LogOfflineFileFull</b>

<dd>
<p>Describes the <b>BranchOfficeLogOfflineFileFull</b> type member <b>LogOfflineFileFull</b>.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>