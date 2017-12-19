---
UID: NS.WINSPLP.BRANCHOFFICEJOBDATAPIPELINEFAILED
title: BranchOfficeJobDataPipelineFailed
author: windows-driver-content
description: Contains the necessary data for logging a branch office job Pipeline Rendering Failed event on a remote server. This is based on standard job-related data available to the spooler.
old-location: print\branchofficejobdatapipelinefailed.htm
old-project: print
ms.assetid: 3F5DB2F5-40B6-4A8D-983C-065D17E62AE6
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: BranchOfficeJobDataPipelineFailed, BranchOfficeJobDataPipelineFailed, PBranchOfficeJobDataPipelineFailed, *PBranchOfficeJobDataPipelineFailed
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
req.product: Windows 10 or later.
---

# BranchOfficeJobDataPipelineFailed structure



## -description
Contains the necessary data for logging a branch office job Pipeline Rendering Failed event on a remote server. This is based on standard job-related data available to the spooler.



## -syntax

````
typedef struct {
  LPWSTR pDocumentName;
  LPWSTR pPrinterName;
  LPWSTR pExtraErrorInfo;
} BranchOfficeJobDataPipelineFailed, *PBranchOfficeJobDataPipelineFailed;
````


## -struct-fields

### -field pDocumentName

Specifies the name of the print document.


### -field pPrinterName

Specifies the print connection.


### -field pExtraErrorInfo

Specifies the name of the client machine printing the job.


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