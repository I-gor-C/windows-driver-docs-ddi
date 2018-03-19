---
UID: NF:hbaapi.HBA_SendScsiInquiry
title: HBA_SendScsiInquiry function
author: windows-driver-content
description: The HBA_SendScsiInquiry routine sends a SCSI inquiry command to the indicated remote port.
old-location: storage\hba_sendscsiinquiry.htm
old-project: storage
ms.assetid: 6239f9b5-99e9-4ed7-b2a8-863c1784692b
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: HBA_SendScsiInquiry, HBA_SendScsiInquiry routine [Storage Devices], fibreHBA_rtns_7a60c4a4-d9d4-408f-b5c9-6cb593f510fb.xml, hbaapi/HBA_SendScsiInquiry, storage.hba_sendscsiinquiry
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
-	HBA_SendScsiInquiry
product: Windows
targetos: Windows
req.typenames: HBA_WWNTYPE
---


# HBA_SendScsiInquiry function
The <b>HBA_SendScsiInquiry</b> routine sends a SCSI inquiry command to the indicated remote port.

## Syntax

````
HBA_STATUS HBA_API HBA_SendScsiInquiry(
  _In_  HBA_HANDLE handle,
  _In_  HBA_WWN    portWWN,
  _In_  HBA_UINT64 fcLUN,
  _In_  HBA_UINT8  EVPD,
  _In_  HBA_UINT32 PageCode,
  _Out_ void       *pRspBuffer,
  _In_  HBA_UINT32 pRespBufferSize,
  _Out_ void       *pSenseBuffer,
  _In_  HBA_UINT32 SenseBufferSize
);
````

## Parameters

`Handle`

TBD

`PortWWN`

TBD

`FcLUN`

TBD

`EVPD`

Indicates, when 0, that the inquiry command retrieves the standard SCSI inquiry data. When this member is set to 1, it indicates the inquiry command retrieves the vital product data (VPD) specified by <i>PageCode</i>.

`PageCode`

Indicates the VPD page code to retrieve when <i>EVPD</i> is set to 1. If <i>EVPD </i>is not set to 1, <i>PageCode </i>is ignored.

`pRspBuffer`

Pointer to a buffer that receives the output data of the SCSI inquiry command.

`RspBufferSize`

TBD

`pSenseBuffer`

Pointer to a buffer that receives the SCSI sense data.

`SenseBufferSize`

On input, indicates the size, in bytes, of the buffer at <i>pSenseBuffer</i>. On output, this member indicates the number of bytes of sense data returned.


## Return Value

The <b>HBA_SendScsiInquiry</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_SendScsiInquiry</b> returns one of the following values.

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
Returned if the complete payload of a reply to the SCSI inquiry command was successfully retrieved. 

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
Returned if the SCSI inquiry command could not be delivered without causing a SCSI overlapped command condition.

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
Returned if an unspecified error occurred that prevented the execution of the SCSI inquiry command. 

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

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>



<a href="..\hbaapi\nf-hbaapi-hba_openadapter.md">HBA_OpenAdapter</a>