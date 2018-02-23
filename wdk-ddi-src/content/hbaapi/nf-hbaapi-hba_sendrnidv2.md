---
UID: NF:hbaapi.HBA_SendRNIDV2
title: HBA_SendRNIDV2 function
author: windows-driver-content
description: The HBA_SendRNIDV2 routine sends a request for node identification data (RNID) to the indicated HBA, which in turn routes the request through the indicated port or node to the appropriate fabric configuration server.
old-location: storage\hba_sendrnidv2.htm
old-project: storage
ms.assetid: c46aee6e-f31d-4b8d-8244-3c364aa79ae4
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: fibreHBA_rtns_8e5796fe-6cfa-42e8-9855-9ab89752bfec.xml, hbaapi/HBA_SendRNIDV2, HBA_SendRNIDV2 routine [Storage Devices], storage.hba_sendrnidv2, HBA_SendRNIDV2
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	DllExport
apilocation:
-	Hbaapi.dll
apiname:
-	HBA_SendRNIDV2
product: Windows
targetos: Windows
req.typenames: HBA_WWNTYPE
---


# HBA_SendRNIDV2 function
The <b>HBA_SendRNIDV2</b> routine sends a request for node identification data (RNID) to the indicated HBA, which in turn routes the request through the indicated port or node to the appropriate fabric configuration server.

## Syntax

````
HBA_STATUS HBA_API HBA_SendRNIDV2(
  _In_    HBA_HANDLE handle,
  _In_    HBA_WWN    hbaPortWWN,
  _In_    HBA_WWN    destWWN,
  _In_    HBA_UINT32 destFCID,
  _In_    HBA_UINT32 NodeIdDataFormat,
  _Out_   void       *pRspBuffer,
  _Inout_ HBA_UINT32 *RspBufferSize
);
````

## Parameters

`Handle`

TBD

`HbaPortWWN`

TBD

`DestWWN`

TBD

`DestFCID`

TBD

`NodeIdDataFormat`

Contains a number that indicates the node identification format. For a complete description of the allowed formats and the numbers that identify each format, see the <i>Fibre Channel Generic Services - 4 (FC-GS-4)</i> specification published by the ANSI committee.

`pRspBuffer`

Pointer to a buffer that contains the payload data, in big-endian (wire) format, from the reply to the node identification request.

`pRspBufferSize`

TBD


## Return Value

The <b>HBA_SendRNIDV2</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA.

## Remarks

The node identification data request is a common transport (CT) command that queries a fabric configuration server for node identification data. For a complete description of this command, see the sections dealing with node identification requests in the <i>Fibre Channel Generic Services - 4 (FC-GS-4)</i> specification published by the ANSI committee.

The <b>HBA_SendRNIDV2</b> library routine serves a purpose very similar to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565459">SendRNID</a> WMI method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | hbaapi.h (include Hbaapi.h) |
| **Library** | Hbaapi.lib |
| **DLL** | Hbaapi.dll |

## See Also

<a href="..\hbaapi\nf-hbaapi-hba_openadapter.md">HBA_OpenAdapter</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff565459">SendRNID</a>



<a href="..\hbaapi\nf-hbaapi-hba_sendrnid.md">HBA_SendRNID</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_SendRNIDV2 routine%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>