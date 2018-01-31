---
UID : NF:wdfobject.WdfObjectGetTypedContextWorker
title : WdfObjectGetTypedContextWorker function
author : windows-driver-content
description : The WdfObjectGetTypedContextWorker method is reserved for internal use only. Use the WdfObjectGetTypedContext macro instead.
old-location : wdf\wdfobjectgettypedcontextworker.htm
old-project : wdf
ms.assetid : 1d95084b-16c4-468e-84af-47650292c5a1
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdfobject/WdfObjectGetTypedContextWorker, kmdf.wdfobjectgettypedcontextworker, wdf.wdfobjectgettypedcontextworker, WdfObjectGetTypedContextWorker, WdfObjectGetTypedContextWorker method, DFGenObjectRef_d932d163-5341-45b3-b896-bb3adb5831a6.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfobject.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : DriverCreate
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_SYNCHRONIZATION_SCOPE
req.product : Windows 10 or later.
---


# WdfObjectGetTypedContextWorker function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfObjectGetTypedContextWorker</b> method is reserved for internal use only. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548749">WdfObjectGetTypedContext</a> macro instead.

## Syntax

````
PVOID WdfObjectGetTypedContextWorker(
  _In_ WDFOBJECT                      Handle,
  _In_ PCWDF_OBJECT_CONTEXT_TYPE_INFO TypeInfo
);
````

## Parameters

`Handle`



`TypeInfo`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdfobject.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** | DriverCreate |