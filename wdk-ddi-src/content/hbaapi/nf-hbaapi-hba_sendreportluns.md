---
UID: NF:hbaapi.HBA_SendReportLUNs
title: HBA_SendReportLUNs function
author: windows-driver-content
description: The HBA_SendReportLUNs routine sends a SCSI report LUNs command to the indicated remote port.
old-location: storage\hba_sendreportluns.htm
old-project: storage
ms.assetid: 0df38de0-bc05-45a3-8efa-9d7a0fc2a08e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: HBA_SendReportLUNs, HBA_SendReportLUNs routine [Storage Devices], fibreHBA_rtns_aeda6b0e-e4bf-4679-ab57-dbe562864726.xml, hbaapi/HBA_SendReportLUNs, storage.hba_sendreportluns
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Hbaapi.dll
api_name:
-	HBA_SendReportLUNs
product: Windows
targetos: Windows
req.typenames: HBA_WWNTYPE
---


# HBA_SendReportLUNs function
The <b>HBA_SendReportLUNs</b> routine sends a SCSI report LUNs command to the indicated remote port.

## Syntax

```
HBA_STATUS HBA_API HBA_SendReportLUNs(
  IN HBA_HANDLE Handle,
  IN HBA_WWN    PortWWN,
  OUT void      *pRspBuffer,
  IN HBA_UINT32 RspBufferSize,
  OUT void      *pSenseBuffer,
  IN HBA_UINT32 SenseBufferSize
);
```

## Parameters

`Handle`

TBD

`PortWWN`

TBD

`pRspBuffer`

Pointer to a buffer that receives the output data of the SCSI report LUNs command.

`RspBufferSize`

Indicates the size, in bytes, of the buffer at <i>pRspBuffer</i>.

`pSenseBuffer`

Pointer to a buffer that receives the SCSI sense data.

`SenseBufferSize`

On input, indicates the size, in bytes, of the buffer at <i>pSenseBuffer</i>. On output, this member indicates the number of bytes of sense data returned.


## Return Value

The <b>HBA_ScsiReportLUNs</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_ScsiReportLUNs</b> returns one of the following values.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_OK</b></dt>
</dl>
</td>
<td width="60%">
Returned if the complete payload of a reply to the SCSI report LUNs command was successfully retrieved. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR_ILLEGAL_WWN</b></dt>
</dl>
</td>
<td width="60%">
Returned if the HBA referenced by <i>handle</i> does not contain a port with a name that matches <i>portWWN</i>. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR_NOT_A_TARGET</b></dt>
</dl>
</td>
<td width="60%">
Returned if the specified remote port specified by <i>portWWN </i>does not have SCSI target functionality.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR_TARGET_BUSY</b></dt>
</dl>
</td>
<td width="60%">
Returned if the SCSI report LUNs command could not be delivered without causing a SCSI overlapped command condition.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_SCSI_CHECK_CONDITION</b></dt>
</dl>
</td>
<td width="60%">
Returned if a SCSI check condition occurred and SCSI send data is provided in the buffer at <i>pSenseBuffer</i>.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl>
</td>
<td width="60%">
Returned if an unspecified error occurred that prevented the execution of the SCSI report LUNs command. 

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | hbaapi.h (include Hbaapi.h) |
| **Library** | Hbaapi.lib |
| **DLL** | Hbaapi.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557097">HBA_OpenAdapter</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>