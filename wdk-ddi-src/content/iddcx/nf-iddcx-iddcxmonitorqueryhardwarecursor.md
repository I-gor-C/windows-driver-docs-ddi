---
UID : NF:iddcx.IddCxMonitorQueryHardwareCursor
title : IddCxMonitorQueryHardwareCursor function
author : windows-driver-content
description : An OS callback function the driver calls when it wants obtain the updated cursor information. The driver normally only calls this when the event that signals cursor update has triggered.
old-location : display\iddcxmonitorqueryhardwarecursor.htm
old-project : display
ms.assetid : e954b7e7-9e4a-47ae-9b0f-8c7e051cc00e
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : IddCxMonitorQueryHardwareCursor method [Display Devices], iddcx/IddCxMonitorQueryHardwareCursor, display.iddcxmonitorqueryhardwarecursor, IddCxMonitorQueryHardwareCursor
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
req.irql : "_Must_inspect_result_"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---


# IddCxMonitorQueryHardwareCursor function
An OS callback function the driver calls when it wants obtain the updated cursor information. The driver normally only calls this when the event that signals cursor update has triggered

## Syntax

````
NTSTATUS IddCxMonitorQueryHardwareCursor(
  _In_        IDDCX_MONITOR             MonitorObject,
  _In_  const IDARG_IN_QUERY_HWCURSOR*  pInArgs,
  _Out_       IDARG_OUT_QUERY_HWCURSOR* pOutArgs
);
````

## Parameters

`MonitorObject`

This is the OS context handle for this monitor returned by the <a href="..\iddcx\nf-iddcx-iddcxmonitorarrival.md">IddCxMonitorArrival</a> call

`pInArgs`

Input arguments of the function

`pOutArgs`

Output arguments of the function


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
| **IRQL** | "_Must_inspect_result_" |
| **DDI compliance rules** |  |