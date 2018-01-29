---
UID : NF:printoem.OEMQueryDeviceSupport
title : OEMQueryDeviceSupport function
author : windows-driver-content
description : The OEMQueryDeviceSupport function returns requested device-specific information.
old-location : print\oemquerydevicesupport.htm
old-project : print
ms.assetid : 38e1bb07-be98-494b-a9c9-a83edef367e0
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : OEMQueryDeviceSupport function [Print Devices], print.oemquerydevicesupport, printoem/OEMQueryDeviceSupport, OEMQueryDeviceSupport, print_unidrv-pscript_rendering_9bfec781-8785-4ff6-8abf-6e14233827dc.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : printoem.h
req.include-header : Printoem.h
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
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : STDVARIABLEINDEX
req.product : Windows 10 or later.
---


# OEMQueryDeviceSupport function
The <code>OEMQueryDeviceSupport</code> function returns requested device-specific information.

## Syntax

````
BOOL APIENTRY OEMQueryDeviceSupport(
        SURFOBJ                     *pso,
        XLATEOBJ                    *pxlo,
        XFORMOBJ                    *pxo,
        ULONG                       iType,
        ULONG                       cjIn,
  _In_  _reads_bytes_(cjIn) PVOID   pvIn,
        ULONG                       cjOut,
  _Out_ _writes_bytes_(cjOut) PVOID pvOut
);
````

## Parameters

`pso`



`pxlo`



`pxo`



`iType`



`cjIn`



`pvIn`



`cjOut`



`pvOut`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | printoem.h (include Printoem.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |