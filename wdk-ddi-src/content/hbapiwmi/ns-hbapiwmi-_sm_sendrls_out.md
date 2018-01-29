---
UID : NS:hbapiwmi._SM_SendRLS_OUT
title : _SM_SendRLS_OUT
author : windows-driver-content
description : The SM_SendRLS_OUT structure is used to receive output parameters from the SM_SendRLS method.
old-location : storage\sm_sendrls_out.htm
old-project : storage
ms.assetid : 28c08a30-b6c6-4f1b-a3a9-0581da0159b9
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : SM_SendRLS_OUT, hbapiwmi/SM_SendRLS_OUT, storage.sm_sendrls_out, PSM_SendRLS_OUT structure pointer [Storage Devices], structs-Fibre_8244cf34-aaf9-4c88-aeb7-4adf77d40269.xml, _SM_SendRLS_OUT, *PSM_SendRLS_OUT, SM_SendRLS_OUT structure [Storage Devices], PSM_SendRLS_OUT, hbapiwmi/PSM_SendRLS_OUT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : hbapiwmi.h
req.include-header : Hbapiwmi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PSM_SendRLS_OUT, SM_SendRLS_OUT"
---

# _SM_SendRLS_OUT structure
The SM_SendRLS_OUT structure is used to receive output parameters from the SM_SendRLS method.

## Syntax
````
typedef struct _SM_SendRLS_OUT {
  ULONG HBAStatus;
  ULONG TotalRespBufferSize;
  ULONG OutRespBufferSize;
  UCHAR RespBuffer[1];
} SM_SendRLS_OUT, *PSM_SendRLS_OUT;
````

## Members


`HBAStatus`

The status of the operation. For a list of allowed values and their descriptions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>.

`OutRespBufferSize`

The size, in bytes, of the data that was actually retrieved.

`RespBuffer`

The results of the common transport command.

`TotalRespBufferSize`

The size, in bytes, of the results common transport (CT) command.

## Remarks
The WMI tool suite generates a declaration of the SM_SendRNID_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_FabricAndDomainManagementMethod WMI class.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | hbapiwmi.h (include Hbapiwmi.h) |