---
UID: NF:hbaapi.HBA_SendSRL
title: HBA_SendSRL function
author: windows-driver-content
description: The HBA_SendSRL routine issues a scan remote loop (SRL) request through the specified HBA to a specified domain controller.
old-location: storage\hba_sendsrl.htm
old-project: storage
ms.assetid: 455ff9c9-89d5-4c79-8b01-f0d731ac8d5a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: HBA_SendSRL, HBA_SendSRL routine [Storage Devices], fibreHBA_rtns_30102c46-c07f-4d22-a0c7-83bea708c4b8.xml, hbaapi/HBA_SendSRL, storage.hba_sendsrl
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
-	HBA_SendSRL
product: Windows
targetos: Windows
req.typenames: HBA_WWNTYPE
---


# HBA_SendSRL function
The <b>HBA_SendSRL</b> routine issues a scan remote loop (SRL) request through the specified HBA to a specified domain controller.

## Syntax

````
HBA_STATUS HBA_API HBA_SendSRL(
  _In_    HBA_HANDLE handle,
  _In_    HBA_WWN    hbaPortWWN,
  _In_    HBA_WWN    wwn,
  _In_    HBA_UINT32 domain,
  _Out_   void       *pRspBuffer,
  _Inout_ HBA_UINT32 *pRspBufferSize
);
````

## Parameters

`Handle`

TBD

`HbaPortWWN`

TBD

`Wwn`

TBD

`Domain`

TBD

`pRspBuffer`

Pointer to a buffer that receives the output data of the SRL request.

`pRspBufferSize`

On input, indicates the size, in bytes, of the buffer at <i>pRspBuffer</i>. On output, this member contains the number of bytes of data retrieved in <i>pRspBuffer</i>. If the buffer is not large enough to receive all of the response data, the data is truncated to the size of the buffer. Eight bytes is sufficient buffer space for any response.


## Return Value

The <b>HBA_SendSRL</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_SendSRL</b> returns one of the following values.

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
Returned if the complete payload of a reply to the SRL request was successfully retrieved. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR_ILLEGAL_WWN</b></dt>
</dl>
</td>
<td width="60%">
Returned if the HBA referenced by <i>handle</i> does not contain a port with a name that matches <i>hbaPortWWN</i>. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR_ELS_REJECT</b></dt>
</dl>
</td>
<td width="60%">
Returned if the destination port referenced by <i>wwn, </i>or the domain controller referenced by <i>domain, </i>rejected the request node identification information data (RNID) that identifies the source HBA.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl>
</td>
<td width="60%">
Returned if an unspecified error occurred that prevented the execution of the SRL request. 

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