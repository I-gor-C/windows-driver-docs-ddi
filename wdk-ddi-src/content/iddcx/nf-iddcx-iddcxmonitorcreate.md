---
UID : NF:iddcx.IddCxMonitorCreate
title : IddCxMonitorCreate function
author : windows-driver-content
description : An OS callback function the driver calls to create a monitor object that can later be used for arrival.
old-location : display\iddcxmonitorcreate.htm
old-project : display
ms.assetid : 2e089827-dd50-43cb-9e1a-34c439780831
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : IddCxMonitorCreate, IddCxMonitorCreate method [Display Devices], iddcx/IddCxMonitorCreate, display.iddcxmonitorcreate
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : iddcx.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
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
req.typenames : 
---


# IddCxMonitorCreate function
An OS callback function the driver calls to create a monitor object that can later be used for arrival.

## Syntax

````
NTSTATUS IddCxMonitorCreate(
  _In_        IDDCX_ADAPTER            AdapterObject,
  _In_  const IDARG_IN_MONITORCREATE*  pInArgs,
  _Out_       IDARG_OUT_MONITORCREATE* pOutArgs
);
````

## Parameters

`AdapterObject`

The adapter object that is hosting the newly arrived monitor

`pInArgs`

Input arguments to the function

`pOutArgs`

Output arguments to the function


## Return Value

(NTSTATUS) The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | iddcx.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |