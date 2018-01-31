---
UID : NF:ucxcontroller.UcxControllerSetIdStrings
title : UcxControllerSetIdStrings function
author : windows-driver-content
description : Updates the identifier strings of a controller after the controller has been initialized.
old-location : buses\ucxcontrollersetidstrings.htm
old-project : usbref
ms.assetid : FC0F6C02-C53A-4F7E-B718-70788FA807F3
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.ucxcontrollersetidstrings, UcxControllerSetIdStrings function [Buses], ucxcontroller/UcxControllerSetIdStrings, UcxControllerSetIdStrings
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ucxcontroller.h
req.include-header : Ucxclass.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 1.0
req.umdf-ver : 2.0
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ucxstubs.lib
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : UCX_CONTROLLER_STATE
req.product : Windows 10 or later.
---


# UcxControllerSetIdStrings function
Updates the identifier strings
    of a controller after the controller has been initialized.

## Syntax

````
NTSTATUS UcxControllerSetIdStrings(
  _In_ UCXCONTROLLER   UcxController,
  _In_ PUNICODE_STRING ManufacturerNameString,
  _In_ PUNICODE_STRING ModelNameString,
  _In_ PUNICODE_STRING ModelNumberString
);
````

## Parameters

`Controller`

TBD

`ManufacturerNameString`

A string that contains the name of controller manufacturer.

`ModelNameString`

A string that contains the name of device model.

`ModelNumberString`

A string that contains the revision number of the device model.


## Return Value

The function returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxcontroller.h (include Ucxclass.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |