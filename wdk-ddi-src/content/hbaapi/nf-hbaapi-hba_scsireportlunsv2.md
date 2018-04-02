---
UID: NF:hbaapi.HBA_ScsiReportLUNsV2
title: HBA_ScsiReportLUNsV2 function
author: windows-driver-content
description: The HBA_ScsiReportLUNsV2 routine sends a SCSI report LUNs command to the indicated remote port.
old-location: storage\hba_scsireportlunsv2.htm
old-project: storage
ms.assetid: 6a4dfb93-4044-4a7a-a993-38c91f84cae2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: HBA_ScsiReportLUNsV2, HBA_ScsiReportLUNsV2 routine [Storage Devices], fibreHBA_rtns_ca5de2ac-67e1-49e0-9397-c5e987854154.xml, hbaapi/HBA_ScsiReportLUNsV2, storage.hba_scsireportlunsv2
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
-	HBA_ScsiReportLUNsV2
product:
- Windows
targetos: Windows
req.typenames: HBA_WWNTYPE
---


# HBA_ScsiReportLUNsV2 function
The <b>HBA_ScsiReportLUNsV2</b> routine sends a SCSI report LUNs command to the indicated remote port.

## Syntax

```
HBA_STATUS HBA_API HBA_ScsiReportLUNsV2(
  IN HBA_HANDLE     Hbahandle,
  IN HBA_WWN        HbaPortWWN,
  IN HBA_WWN        DiscoveredPortWWN,
  OUT void          *pRespBuffer,
  IN OUT HBA_UINT32 *pRespBufferSize,
  OUT HBA_UINT8     *pScsiStatus,
  OUT void          *pSenseBuffer,
  IN OUT HBA_UINT32 *pSenseBufferSize
);
```

## Parameters

`Hbahandle`

TBD

`HbaPortWWN`

Contains a 64-bit worldwide name (WWN) that uniquely identifies the local HBA port from which the SCSI report LUNs command is sent. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.

`DiscoveredPortWWN`

TBD

`pRespBuffer`

Pointer to a buffer that receives the output data of the SCSI report LUNs command.

`pRespBufferSize`

Indicates the size, in bytes, of the buffer at <i>pRespBuffer</i>.

`pScsiStatus`

Pointer to a buffer that receives the SCSI status data.

`pSenseBuffer`

Pointer to a buffer that receives the SCSI sense data.

`pSenseBufferSize`

On input, indicates the size, in bytes, of the buffer at <i>pSenseBuffer</i>. On output, this member indicates the number of bytes of sense data returned.


## Return Value

The <b>HBA_ScsiReportLUNsV2</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_ScsiReportLUNsV2</b> returns one of the following values.

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
Returned if the HBA referenced by <i>handle</i> does not contain a port with a name that matches <i>HbaPortWWN</i>. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR_NOT_A_TARGET</b></dt>
</dl>
</td>
<td width="60%">
Returned if the specified remote port referenced by <i>discoveredPortWWN </i>does not have SCSI target functionality.

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