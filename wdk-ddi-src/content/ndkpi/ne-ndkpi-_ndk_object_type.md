---
UID: NE:ndkpi._NDK_OBJECT_TYPE
title: "_NDK_OBJECT_TYPE"
author: windows-driver-content
description: The NDK_OBJECT_TYPE enumeration defines types of Network Direct Kernel (NDK) objects.
old-location: netvista\ndk_object_type.htm
old-project: netvista
ms.assetid: 8CB39DF6-00DA-4480-A44E-62CAF1DB35CE
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NDK_OBJECT_TYPE, NDK_OBJECT_TYPE enumeration [Network Drivers Starting with Windows Vista], NdkObjectTypeAdapter, NdkObjectTypeConnector, NdkObjectTypeCq, NdkObjectTypeListener, NdkObjectTypeMax, NdkObjectTypeMr, NdkObjectTypeMw, NdkObjectTypePd, NdkObjectTypeQp, NdkObjectTypeSharedEndpoint, NdkObjectTypeSrq, NdkObjectTypeUndefined, _NDK_OBJECT_TYPE, ndkpi/NDK_OBJECT_TYPE, ndkpi/NdkObjectTypeAdapter, ndkpi/NdkObjectTypeConnector, ndkpi/NdkObjectTypeCq, ndkpi/NdkObjectTypeListener, ndkpi/NdkObjectTypeMax, ndkpi/NdkObjectTypeMr, ndkpi/NdkObjectTypeMw, ndkpi/NdkObjectTypePd, ndkpi/NdkObjectTypeQp, ndkpi/NdkObjectTypeSharedEndpoint, ndkpi/NdkObjectTypeSrq, ndkpi/NdkObjectTypeUndefined, netvista.ndk_object_type
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
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
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ndkpi.h
api_name:
-	NDK_OBJECT_TYPE
product:
- Windows
targetos: Windows
req.typenames: NDK_OBJECT_TYPE
---

# _NDK_OBJECT_TYPE Enumeration
The <b>NDK_OBJECT_TYPE</b> enumeration defines  types of Network Direct Kernel (NDK) objects.

## Syntax
```
typedef enum _NDK_OBJECT_TYPE {
  NdkObjectTypeUndefined       ,
  NdkObjectTypeAdapter         ,
  NdkObjectTypeQp              ,
  NdkObjectTypeCq              ,
  NdkObjectTypeMr              ,
  NdkObjectTypeMw              ,
  NdkObjectTypePd              ,
  NdkObjectTypeSharedEndpoint  ,
  NdkObjectTypeConnector       ,
  NdkObjectTypeListener        ,
  NdkObjectTypeSrq             ,
  NdkObjectTypeMax
} NDK_OBJECT_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>NdkObjectTypeUndefined</td>
                    <td>Specifies  an undefined NDK  object.</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeAdapter</td>
                    <td>Specifies an NDK adapter object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeQp</td>
                    <td>Specifies an NDK queue pair (QP) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeCq</td>
                    <td>Specifies an NDK completion queue (CQ) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeMr</td>
                    <td>Specifies an NDK memory region (MR) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeMw</td>
                    <td>Specifies an NDK memory window (MW) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439926">NDK_MW</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypePd</td>
                    <td>Specifies an NDK protection domain (PD) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeSharedEndpoint</td>
                    <td>Specifies an NDK shared endpoint object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeConnector</td>
                    <td>Specifies an NDK connector object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeListener</td>
                    <td>Specifies an NDK listener object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeSrq</td>
                    <td>Specifies an NDK shared receive queue (SRQ) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439939">NDK_SRQ</a>).</td>
                </tr>
            
                <tr>
                    <td>NdkObjectTypeMax</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the header files and binaries.</td>
                </tr>
</table>

## Remarks

NDK objects include an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439928">NDK_OBJECT_HEADER</a> structure that packages the object type,  version, and other information.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. None supported,Supported in NDIS 6.30 and later. |
| **Header** | ndkpi.h (include Ndkpi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439926">NDK_MW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439928">NDK_OBJECT_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439939">NDK_SRQ</a>