---
UID: NF:hbaapi.HBA_SendRPL
title: HBA_SendRPL function
author: windows-driver-content
description: The HBA_SendRPL routine sends a read port list (RPL) request to the indicated port or domain controller.
old-location: storage\hba_sendrpl.htm
old-project: storage
ms.assetid: 2c8cb6bb-eb6b-4a2f-8d00-efb309273536
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: HBA_SendRPL, HBA_SendRPL routine [Storage Devices], fibreHBA_rtns_1b67cd99-3e8b-4667-a795-a3391b73e62c.xml, hbaapi/HBA_SendRPL, storage.hba_sendrpl
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
-	HBA_SendRPL
product:
- Windows
targetos: Windows
req.typenames: HBA_WWNTYPE
---


# HBA_SendRPL function
The <b>HBA_SendRPL</b> routine sends a read port list (RPL) request to the indicated port or domain controller.

## Syntax

```
HBA_STATUS HBA_API HBA_SendRPL(
  IN HBA_HANDLE     Handle,
  IN HBA_WWN        HbaPortWWN,
  IN HBA_WWN        Agent_wwn,
  IN HBA_UINT32     Agent_domain,
  IN HBA_UINT32     PortIndex,
  OUT void          *pRspBuffer,
  IN OUT HBA_UINT32 *pRspBufferSize
);
```

## Parameters

`Handle`

Contains a value returned by the routine <a href="https://msdn.microsoft.com/library/windows/hardware/ff557097">HBA_OpenAdapter</a> that identifies the local HBA through which the request is sent.

`HbaPortWWN`

Contains a 64-bit worldwide name (WWN) that uniquely identifies the local port through which the read port list (RPL) command is sent. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.

`Agent_wwn`

TBD

`Agent_domain`

TBD

`PortIndex`

Contains the port index of the first port in the retrieved list of ports of type FC_Port.

`pRspBuffer`

Pointer to a buffer that receives the results of the read port list (RPL) request, if the request succeeds. If the destination port or domain controller rejects the request, this buffer holds the link service reject (LS_RJT) payload data. If the amount of returned data exceeds the buffer size specified in <i>RspBufferSize</i>, the data is truncated to the buffer size<i>. </i>The payload data is in big-endian format (higher order bytes are in lower addresses).

`pRspBufferSize`

TBD


## Return Value

The <b>HBA_SendRPL</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_SendRPL</b> returns one of the following values.

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
Returned if the complete payload of a reply to the RPL request was successfully retrieved. 

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
<dt><b>HBA_STATUS_ERROR_ELS_REJECT</b></dt>
</dl>
</td>
<td width="60%">
Returned if the destination port referenced by <i>AgentWwn, </i>or the domain controller referenced by <i>AgentDomain, </i>rejected the request node identification information data (RNID) that identifies the source HBA. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl>
</td>
<td width="60%">
Returned if an unspecified error occurred that prevented the execution of the RPL request. 

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