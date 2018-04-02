---
UID: NE:ntddndis._NDIS_REQUEST_TYPE
title: "_NDIS_REQUEST_TYPE"
author: windows-driver-content
description: The NDIS_REQUEST_TYPE enumeration identifies the request type in an OID request.
old-location: netvista\ndis_request_type.htm
old-project: netvista
ms.assetid: c4352eab-8bbd-429e-93ad-190372d29f2c
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_REQUEST_TYPE, NDIS_REQUEST_TYPE, NDIS_REQUEST_TYPE enumeration [Network Drivers Starting with Windows Vista], NdisRequestClose, NdisRequestGeneric1, NdisRequestGeneric2, NdisRequestGeneric3, NdisRequestGeneric4, NdisRequestMethod, NdisRequestOpen, NdisRequestQueryInformation, NdisRequestQueryStatistics, NdisRequestReset, NdisRequestSend, NdisRequestSetInformation, NdisRequestTransferData, PNDIS_REQUEST_TYPE, PNDIS_REQUEST_TYPE enumeration pointer [Network Drivers Starting with Windows Vista], _NDIS_REQUEST_TYPE, ndis_request_ref_78880aa3-bab2-49bd-9232-117accb98ce3.xml, netvista.ndis_request_type, ntddndis/NDIS_REQUEST_TYPE, ntddndis/NdisRequestClose, ntddndis/NdisRequestGeneric1, ntddndis/NdisRequestGeneric2, ntddndis/NdisRequestGeneric3, ntddndis/NdisRequestGeneric4, ntddndis/NdisRequestMethod, ntddndis/NdisRequestOpen, ntddndis/NdisRequestQueryInformation, ntddndis/NdisRequestQueryStatistics, ntddndis/NdisRequestReset, ntddndis/NdisRequestSend, ntddndis/NdisRequestSetInformation, ntddndis/NdisRequestTransferData, ntddndis/PNDIS_REQUEST_TYPE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
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
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddndis.h
api_name:
-	NDIS_REQUEST_TYPE
product:
- Windows
targetos: Windows
req.typenames: NDIS_REQUEST_TYPE, *PNDIS_REQUEST_TYPE
---

# _NDIS_REQUEST_TYPE Enumeration
The NDIS_REQUEST_TYPE enumeration identifies the request type in an OID request.

## Syntax
```
typedef enum _NDIS_REQUEST_TYPE {
  NdisRequestQueryInformation  ,
  NdisRequestSetInformation    ,
  NdisRequestQueryStatistics   ,
  NdisRequestOpen              ,
  NdisRequestClose             ,
  NdisRequestSend              ,
  NdisRequestTransferData      ,
  NdisRequestReset             ,
  NdisRequestGeneric1          ,
  NdisRequestGeneric2          ,
  NdisRequestGeneric3          ,
  NdisRequestGeneric4          ,
  NdisRequestMethod
} NDIS_REQUEST_TYPE, *PNDIS_REQUEST_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>NdisRequestQueryInformation</td>
                    <td>A query-information request. For certain requests, NDIS satisfies the request. Otherwise,
     NDIS forwards such requests to the underlying driver's 
     <i>MiniportOidRequest</i> function. This type of request can originate in a user-mode application, filter module, or protocol driver.

<div class="alert"><b>Note</b>  Drivers should treat <b>NdisRequestQueryInformation</b> and <b>NdisRequestQueryStatistics</b> queries identically.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>NdisRequestSetInformation</td>
                    <td>A set-information request. NDIS forwards such a request to the underlying driver's 
     <i>MiniportOidRequest</i> function.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestQueryStatistics</td>
                    <td>A query-statistics request. For certain requests, NDIS satisfies the request. Otherwise,
     NDIS forwards such requests to the underlying driver's 
     <i>MiniportOidRequest</i> function. This type of request can originate in a user-mode application, filter module, or protocol driver.

<div class="alert"><b>Note</b>  Drivers should treat <b>NdisRequestQueryInformation</b> and <b>NdisRequestQueryStatistics</b> queries identically.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>NdisRequestOpen</td>
                    <td>This type is obsolete.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestClose</td>
                    <td>This type is obsolete.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestSend</td>
                    <td>This type is obsolete.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestTransferData</td>
                    <td>This type is obsolete.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestReset</td>
                    <td>This type is obsolete.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestGeneric1</td>
                    <td>A request that is specific to the type of the miniport driver.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestGeneric2</td>
                    <td>A request that is specific to the type of the miniport driver.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestGeneric3</td>
                    <td>A request that is specific to the type of the miniport driver.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestGeneric4</td>
                    <td>A request that is specific to the type of the miniport driver.</td>
                </tr>
            
                <tr>
                    <td>NdisRequestMethod</td>
                    <td>A method request. NDIS forwards such a request to the underlying driver's 
     <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function.</td>
                </tr>
</table>

## Remarks

The NDIS_REQUEST_TYPE enumeration is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure.

<div class="alert"><b>Note</b>  For any NDIS_REQUEST_TYPE value, the OID_<i>Xxx</i> that is specified in the 
    <b>Oid</b> member of the NDIS_OID_REQUEST structure must be compatible with the type of operation
    requested.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.0 and later. Supported in NDIS 6.0 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>