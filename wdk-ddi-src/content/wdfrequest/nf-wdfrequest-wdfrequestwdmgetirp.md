---
UID : NF:wdfrequest.WdfRequestWdmGetIrp
title : WdfRequestWdmGetIrp function
author : windows-driver-content
description : The WdfRequestWdmGetIrp method returns the WDM IRP structure that is associated with a specified framework request object.
old-location : wdf\wdfrequestwdmgetirp.htm
old-project : wdf
ms.assetid : 414950c6-b082-4ea9-bba4-f3d12b4d2a9e
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : PFN_WDFREQUESTWDMGETIRP, wdf.wdfrequestwdmgetirp, WdfRequestWdmGetIrp method, DFRequestObjectRef_2f8bba17-817e-4edb-98f2-bd56eb3e34ac.xml, kmdf.wdfrequestwdmgetirp, WdfRequestWdmGetIrp, wdfrequest/WdfRequestWdmGetIrp
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfrequest.h
req.include-header : Wdf.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 
req.ddi-compliance : DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Wdf01000.sys (see Framework Library Versioning.)
req.dll : 
req.irql : <=DISPATCH_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_REQUEST_TYPE
req.product : Windows 10 or later.
---


# WdfRequestWdmGetIrp function
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfRequestWdmGetIrp</b> method returns the WDM <a href="..\wdm\ns-wdm-_irp.md">IRP</a> structure that is associated with a specified framework request object.

## Syntax

````
PIRP WdfRequestWdmGetIrp(
  _In_ WDFREQUEST Request
);
````

## Parameters

`Request`

A handle to a framework request object.


## Return Value

<b>WdfRequestWdmGetIrp</b> returns a pointer to an <a href="..\wdm\ns-wdm-_irp.md">IRP</a> structure.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

The driver must not access a request's IRP structure after <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/completing-i-o-requests">completing the I/O request</a>.

For more information about <b>WdfRequestWdmGetIrp</b>, see <a href="https://msdn.microsoft.com/a686ea00-6987-480a-a4ce-892e1efbed87">Obtaining Information About an I/O Request</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** |  |
| **Header** | wdfrequest.h (include Wdf.h) |
| **Library** |  |
| **IRQL** | <=DISPATCH_LEVEL |
| **DDI compliance rules** | DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2 |

## See Also

<a href="..\wdfrequest\nf-wdfrequest-wdfrequestgetparameters.md">WdfRequestGetParameters</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestWdmGetIrp method%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>