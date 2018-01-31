---
UID : NF:wdfdpc.WdfDpcGetParentObject
title : WdfDpcGetParentObject function
author : windows-driver-content
description : The WdfDpcGetParentObject method returns the parent object of a specified DPC object.
old-location : wdf\wdfdpcgetparentobject.htm
old-project : wdf
ms.assetid : 77ebca0f-3056-4f11-9d59-fbd166967ed3
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdfdpc/WdfDpcGetParentObject, wdf.wdfdpcgetparentobject, DFDpcObjectRef_28be5a7f-4f65-4b9e-b9f4-80b754cc8ca3.xml, WdfDpcGetParentObject method, WdfDpcGetParentObject, PFN_WDFDPCGETPARENTOBJECT, kmdf.wdfdpcgetparentobject
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfdpc.h
req.include-header : Wdf.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 
req.ddi-compliance : DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Wdf01000.sys (see Framework Library Versioning.)
req.dll : 
req.irql : Any level
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PWDF_DMA_SYSTEM_PROFILE_CONFIG, WDF_DMA_SYSTEM_PROFILE_CONFIG"
req.product : Windows 10 or later.
---


# WdfDpcGetParentObject function
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDpcGetParentObject</b> method returns the parent object of a specified DPC object.

## Syntax

````
WDFOBJECT WdfDpcGetParentObject(
  _In_ WDFDPC Dpc
);
````

## Parameters

`Dpc`

A handle to a framework DPC object.


## Return Value

<b>WdfDpcGetParentObject</b> returns a handle to the parent object of a specified DPC object.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

A driver might call <b>WdfDpcGetParentObject</b> from within its <a href="https://msdn.microsoft.com/b934a0da-0709-4427-bbf2-8d53f9511cf1">EvtDpcFunc</a> callback function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** |  |
| **Header** | wdfdpc.h (include Wdf.h) |
| **Library** |  |
| **IRQL** | Any level |
| **DDI compliance rules** | DriverCreate, KmdfIrql, KmdfIrql2 |

## See Also

<a href="https://msdn.microsoft.com/b934a0da-0709-4427-bbf2-8d53f9511cf1">EvtDpcFunc</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDpcGetParentObject method%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>