---
UID: NS.winsplp.PBranchOfficeJobDataPipelineFailed
title: PBranchOfficeJobDataPipelineFailed
author: windows-driver-content
description: Contains the necessary data for logging a branch office job Pipeline Rendering Failed event on a remote server. This is based on standard job-related data available to the spooler.
old-location: print\branchofficejobdatapipelinefailed.htm
old-project: print
ms.assetid: 3F5DB2F5-40B6-4A8D-983C-065D17E62AE6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PBranchOfficeJobDataPipelineFailed, BranchOfficeJobDataPipelineFailed, *PBranchOfficeJobDataPipelineFailed
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
req.alt-api: BranchOfficeJobDataPipelineFailed
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
req.iface: 
req.product: Windows 10 or later.
---

# PBranchOfficeJobDataPipelineFailed structure



## -description
<p>Contains the necessary data for logging a branch office job Pipeline Rendering Failed event on a remote server. This is based on standard job-related data available to the spooler.</p>


## -syntax

````
typedef struct {
  LPWSTR pDocumentName;
  LPWSTR pPrinterName;
  LPWSTR pExtraErrorInfo;
} BranchOfficeJobDataPipelineFailed, *PBranchOfficeJobDataPipelineFailed;
````


## -struct-fields
<dl>

### -field <b>pDocumentName</b>

<dd>
<p>Specifies the name of the print document.</p>
</dd>

### -field <b>pPrinterName</b>

<dd>
<p>Specifies the print connection.</p>
</dd>

### -field <b>pExtraErrorInfo</b>

<dd>
<p>Specifies the name of the client machine printing the job.</p>
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